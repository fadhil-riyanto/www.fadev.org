# amd64 endianness

I'll show you, the little endian (that used in most x86-64 linux systems), let go deeper

I have very simple program, the program

```c
#include <stdio.h>

typedef unsigned char byte_ptr;

void show_bytes(byte_ptr *data, size_t n) {
        int i = 0;
        for(; i < n; i++) {
                printf("%p -> %.2x\n",  &data[i], data[i]);
        }

        printf("\n");
}

int main() {
        unsigned long da = 0x5894F93;
        show_bytes((unsigned char*)&da, 8);
}
```

as you can see, this is what we write

```
hexadecimal	: 0x05 0x89 0x4F 0x93
dummy addr  : 0    1    2    3
```
the result

```
0x7fff0fe80d10 -> 93
0x7fff0fe80d11 -> 4f
0x7fff0fe80d12 -> 89
0x7fff0fe80d13 -> 05
0x7fff0fe80d14 -> 00
0x7fff0fe80d15 -> 00
0x7fff0fe80d16 -> 00
0x7fff0fe80d17 -> 00
```

wow, it reversed!, because
```
hexcode      : 0x93 0x4f 0x89 0x05 0x00 0x00 0x00 0x00
dummy addr   : 0    1    2    3    4    5    6    7
               ^~~ MSB                            ^~~ LSB
```

(read it first from right, to left, as you read binary code)
WOW, its least endian first, so the machine is `little-endian`

you can also check out my lscpu result
![image](../_images/cb27cc742ecc2180a209e7c7e35460caf57e4d3354e8a1c1b0056a66365d64f1f9b419000ab32ea67b58ef467e860f098f4a239813be980dc17e7573.png)

![image](../_images/b482f061fbd71bb226383393d5343644a6bf830c9c43ac2ac45380889b93986d110b6c192b18208f71e9cfba970939fd8004466e719577e245116607.png)

![image](../_images/e70f7497ba5ae41b2a242bfa5bf80ee2706a328cb64e3b23e731cf475ad845b143274ef27879d63789c844812caf425c5c8d031360efd6a5b371284e.png)

## rust

result
![image](../_images/168766015cce02d62b18bb5339cd98f30dd83b729fbece7e291a97bcd758d1bfccc4a96c3d97f772b334d83b09a091c4a495abc30921582e8a95b291.png)

# big endian 

because most of machine is little-endian, even RP2040 ARM chip, I'll demontrate it (with some stuff)

first, I'll use miri

## miri

this unique tool can emulate big endian
![image](../_images/c33299af4f933e3251ee297c402e8474c8786599200d7b8675187d3d3b880b0ece7f37b8d3c5028c577f16e44d80cde36cba17ed83a776c41bd55492.png)