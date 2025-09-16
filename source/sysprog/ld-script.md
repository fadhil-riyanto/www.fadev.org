# GNU linker scripts journey

first, we need to know about sections, lets take a look, nice stuff

- [https://mcyoung.xyz/2021/06/01/linker-script/#appendix](https://mcyoung.xyz/2021/06/01/linker-script/#appendix)
- [https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/4/html/red_hat_enterprise_linux_4_-_archived_documents/index#using_ld_the_gnu_linker](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/4/html/red_hat_enterprise_linux_4_-_archived_documents/index#using_ld_the_gnu_linker)

lets start with make very simple library

```c
// gcc -c libcall.c

extern int random_me;

/* this is .text section */
int lib_call(const char* str) {
        (void)str;

        /* this is .bss */
        static int im_counting;
        im_counting++;
}
```

then, run `nm libcall.o`
![image](../_images/7536e425e8a27c20b49228491904def3f58f23c9d9989eb537744c638817697c211122447ed8cbf5fed7e7f91648d019a4a19e6e8f35683fbfc0e5a0.png)

as we can see, b (lowercase) means the `bss` section is not exported, while T (uppercase) means `.text` is exported. then, lets call `lib_call` function from `run` function (in other file), say the file is `run.c` which has contents

```c
// gcc -c run.c
extern int  lib_call(const char* str);

void run(void) {
        /* this will be .data */
        static int data = 5;
        data = lib_call("im a .rodata");
}
```

again, we got this

![image](../_images/9d5ca7a30c57e872e52778eed34af90ddbfc56cbc1ec89b5bd73f75310a29996f4d23d9808827208f5fea5b8ed8662ee95b1c3a3637d63f816e3b146.png)

the U uppercase is means, the `lib_call` is undefined. now how we can resolve it?

first, lets link `run.o`
```sh
> gcc run.o
/usr/bin/ld: /usr/lib/gcc/x86_64-pc-linux-gnu/15.1.1/../../../../lib/Scrt1.o: in function `_start':
(.text+0x1b): undefined reference to `main'
/usr/bin/ld: run.o: in function `run':
run.c:(.text+0xf): undefined reference to `lib_call'
collect2: error: ld returned 1 exit status
```

[ads]
if you want automate it, use Makefile instead

```Makefile
CC = gcc

stage_1_libcall: libcall.c
	gcc -c libcall.c
	ar r libcall.a libcall.o


stage_2_run: run.c
	gcc -c run.c

stage_3: stage_1_libcall stage_2_run
	gcc run.o -L. -lcall -nostartfiles

clean:
	rm -f a.out
	rm -f libcall.a
	rm -f libcall.o
	rm -f run.o
```

back to linker, lets run `make stage_3`, and check for `nm a.out`. supraisingly, the `lib_call` is not undefined again. thanks for `ld`

![image](../_images/3d0ffb5e120f5d3030b8a5a715f0724c35c553ce1e7f3ce10e28c9200b1fef528e88be8384c81a129d10443ce9e1788295e86b5234b53df0c8aab4dc.png)

# objdump

![image](../_images/cd8d13d2935dc8fa5f9df1471b11c7cfec2585069abf1e84b70d84d253b97095a2b86e1052bd8f5ffcfb584997f8f968f3ee15b8ee34f548ffce1996.png)

# ld
now, our task. how to rearrange this order. lets create our `link.ld`

```c
ENTRY(run) 
SECTIONS {
    .text : {
        *(.text);
        *(.text.*)
    }

    .bss : {
        *(.bss);
        *(.bss.*)
    }

    .data : {
        *(.data);
        *(.data.*)
    }

    .rodata : {
        *(.rodata);
        *(.rodata.*)
    }
}
```

v2:
```c
ENTRY(run)

PHDRS {
    text PT_LOAD FLAGS(5); /* RX */
    data PT_LOAD FLAGS(6); /* RW */
}

SECTIONS {
    . = 0x10000;

    .text : {
        *(.text);
        *(.text.*)
    } :text

    .rodata : {
        *(.rodata);
        *(.rodata.*)
    } :text

    .data : {
        *(.data);
        *(.data.*)
    } :data

    .bss : {
        *(.bss);
        *(.bss.*)
        *(COMMON)
    } :data
}

```

