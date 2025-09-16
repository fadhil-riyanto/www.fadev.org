# bits data models

this section will talk about data models.

![image](../_images/49ca87fe9c4f571a24bb33cdb4e0345559bca935f4e3e6401897f8516f9f55a23b9f7517138bedb84c4354529e14ac2cc97471c67338f96512458472.png)

that footage, show us what `__ILP32__` is, also what is ILP32?

There has some nice websites
- [https://duetorun.com/blog/20211008/data-model/#concept](https://duetorun.com/blog/20211008/data-model/#concept)
- [https://gcc.gnu.org/onlinedocs/gccint/Effective-Target-Keywords.html#Data-type-sizes](https://gcc.gnu.org/onlinedocs/gccint/Effective-Target-Keywords.html#Data-type-sizes)

![image](../_images/dd5c48b5d5ce4dad3f26ac9d50a73238005154b08f1951a96eb6cb7e1256f4d63cc44d21f104adb9f47e8f553780f701248b6e183316a3277a3b65df.png)

for example, most linux system uses LP64, which long int, and pointer are 64 bit wide. the other example is ILP32, which used by `arm64ilp32`, but its deprecated [https://gcc.gnu.org/pipermail/gcc-patches/2025-January/673207.html](https://gcc.gnu.org/pipermail/gcc-patches/2025-January/673207.html)

LP64 and ILP32 refer to the data model used by the language. "I" is an abbreviation that represents int type, "L" represents long type, and "P" represents the pointer type. 64 and 32 refer to the size of the data types. When the ILP32 option is used, int, long and pointers are 32-bit in size. When LP64 is used, long and pointer are 64-bit in size; int remains 32-bit. The addressing mode used by LP64 is AMODE 64, and by ILP32 is AMODE 31. In the latter case, only 31 bits within the pointer are taken to form the address. For the sake of conciseness, the terms 31-bit mode and ILP32, will be used interchangeably in this document when there is no ambiguity. The same applies to 64-bit mode and LP64. [see here](https://www.ibm.com/docs/en/zos/2.4.0?topic=options-lp64-ilp32#d41843e90)

# Common data models
| Model      | `int`  | `long` | `pointer` | Common in                           |
| ---------- | ------ | ------ | --------- | ----------------------------------- |
| **ILP32**  | 32-bit | 32-bit | 32-bit    | x86 (32-bit), ARM32, MIPS32         |
| **LP64**   | 32-bit | 64-bit | 64-bit    | x86\_64 (Linux, macOS), AArch64     |
| **LLP64**  | 32-bit | 32-bit | 64-bit    | Windows x64 (MSVC), long long is 64 bit|
| **ILP64**  | 64-bit | 64-bit | 64-bit    | Rare: Cray supercomputers, some HPC |
| **SILP64** | 16-bit | 64-bit | 64-bit    | Very rare, some historic systems    |
| **LP32**   | 16-bit | 32-bit | 32-bit    | Some embedded systems               |

# check
```c
#include <stdio.h>

int main() {
    printf("sizeof(int): %zu\n", sizeof(int));
    printf("sizeof(long): %zu\n", sizeof(long));
    printf("sizeof(void *): %zu\n", sizeof(void *));
}
```

intresting topics
- https://www.ibm.com/docs/en/zos/2.4.0?topic=options-lp64-ilp32#d41843e90
- LP64 also predefined, see https://gcc.gnu.org/onlinedocs/cpp/Common-Predefined-Macros.html