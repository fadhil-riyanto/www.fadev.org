# all about ASan & debug symbol

## prerequisites

if you use clang infrastructure
- [llvm-symbolizer](https://man.archlinux.org/man/llvm-symbolizer.1.en): without this, asan offset at debug output will be binary offset, not actual source code. I will demonstrate it
- clang

if you use GCC
- addr2line (usually preinstalled)
- gcc

the tools
- gdb (optional)
- [address sanitizer](https://github.com/google/sanitizers.git)

## testing

very simple memory buggy program

```c
#include <stdlib.h>
#include <stdio.h>

int main() {
        char* data = malloc(1024);
        printf("%s", data);
        return 0;
}
```

`gcc ./leak.c -o leak -g -fsanitize=address`

here buggy result
![image](../_images/08c0c6679e504c218e3ea81a7a77b8113be47f6f1051d4ee8a309e861e279d04f7b62f86d5869c61686070f49d3b2721989b5ba0cd9fa4e97e797002.png)

lets compile it with clang
`clang ./leak.c -o leak -g -fsanitize=address`

![image](../_images/e7127c07db68b7f553bb1e16e9527a2acd0e61c8e53fd6adda3ea10ff960327a91028e0581ef0b02653e3b75d4e586818af5ae6b3a3c81fbd409adc8.png)

after llvm-symbolizer installed
![image](../_images/0a689ab3274a41163d066078f133ed63f1cc7316538b018e94490a106f7b3e8d8395616fb744109e4b91b9f072f9426a0a1e4a0f0a32055106216181.png)