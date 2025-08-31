# difference between thumb-1 (T16) and normal ARM

hi, today I will show you what difference between thumb-1 and normal arm

## what is thumb-1
thumb-1 is lite version of full arm instruction, the instruction has 16 bit wide. and because if its "lite", the binary size is should be smaller compared than normal arm

normal arm has instruction wide 32 bit (idk about aarch64)

## start

tool:

- arm-none-eabi-gcc
- arm-none-eabi-objdump

first, lets compile this very simple program

```c
#define A       0xA

int _sbrk() {

}

int _write() {
        
}

int _read() {
        
}

int _lseek() {
        
}

int _close() {
        
}

int _exit() {
        
}

int main() {
        int a = 9;
        int b = 2;

        int c = a * b;
}

```

compile it for normal arm, the output binary I call it as `a.out`

```sh
arm-none-eabi-gcc test_asm.c
```

objdump it
```sh
arm-none-eabi-objdump -d a.out --disassemble=main
```

![image](../assets/c38e8c412d7bcbe693941611f86723b28fc4a786e84d164de0ca2f1d4ae5b764db556df0eb245afdad4f2d5db66cbfe540ce7a2e1a1e6d06c3780118.png)

# thumb-1
the instruction should be 16 bit wide

```sh
arm-none-eabi-gcc test_asm.c -mthumb -mcpu=cortex-m0plus -o a-thumb.out
arm-none-eabi-objdump -d a-thumb.out --disassemble=main
```

![image](../assets/b04a081419adbabb9ed3f9109f8fea8b1c20b14413955f208d256afbef6ad9ace8712dd8fc5b5b1168effabe0ee4b59a0218443982237179aead52b4.png)

see?