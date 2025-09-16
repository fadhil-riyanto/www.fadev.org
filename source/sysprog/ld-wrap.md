# linker --wrap symbol

konsep wrap linker compiler ini sebenernya berguna ketika kita ingin menimpa suatu fungsi, ke fungsi yang kita map sendiri. contoh misal saya ada

```c
printf()
```

ketika saya compile dengan gcc, printf akan dipanggil sebagai

```c
__wrap_printf()
```

nah, dengan trick ini, kita bisa mengubah behavior dari printf nya itu sendiri, misal

- kirim ke uart
- kirim ke swdclk

# PoC

```c
#include <stdlib.h>
#include <stdio.h>

void* __real_malloc(size_t __size) {
        // return malloc(__size);
        printf("do?\n");
}

void* __wrap_malloc(size_t __size) {
        printf("wrap malloc called\n");
        return __real_malloc(__size);
}

int main() {
        char* x = malloc(1);

        // free(x);
}
```

lalu compile dengan `gcc -Wl,--wrap=malloc wrap_malloc.c -o p -g`

hasil hexdump main

```c
0000000000001180 <main>:
    1180:       55                      push   %rbp
    1181:       48 89 e5                mov    %rsp,%rbp
    1184:       48 83 ec 10             sub    $0x10,%rsp
    1188:       bf 01 00 00 00          mov    $0x1,%edi
    118d:       e8 c5 ff ff ff          call   1157 <__wrap_malloc>
    1192:       48 89 45 f8             mov    %rax,-0x8(%rbp)
    1196:       b8 00 00 00 00          mov    $0x0,%eax
    119b:       c9                      leave
    119c:       c3                      ret
```