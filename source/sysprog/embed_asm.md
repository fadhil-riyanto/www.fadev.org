# General embedded ASM linked in C

this is program is succesfully compiled with `as`, but failed to run due to SIGSEGV.

this is will fail
```asm
.data
val:
    .byte 0xF6
    .byte 0xF6
    .byte 0xF6
    .byte 0xF6
    

.globl do_asm

do_asm:
    # movl 0x12345678, %eax
    # movl 0xAABBCCDD, %edx 

    # # move edx 8 bit high into al (eax)
    # movb %dh, %al

    
    movq $9, %rax
    ret

```

this is will compile
```asm
.data
val:
    .byte 0xF6
    .byte 0xF6
    .byte 0xF6
    .byte 0xF6
    

.globl do_asm

.text
do_asm:
    # movl 0x12345678, %eax
    # movl 0xAABBCCDD, %edx 

    # # move edx 8 bit high into al (eax)
    # movb %dh, %al

    
    movq $9, %rax
    ret

```

the difference only in `.text` section