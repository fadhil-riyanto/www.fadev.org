# ARM AArch32 ABI Convention

link: [https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst](https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst)

![image](../assets/c9f880c8e4778755426768441f6f31d9f9f6694a62c0a28dd8498d4f43783e2307c68fda111aa8b7c810553a96cd4eeb2eaba31080f4bc92b2e1413f.png)

Registers R0-3 are also, by convention, used to hold parameter values to be passed to a subroutine or function. Functions with more than four parameters typically use one or more of those parameter registers to hold addresses pointing to data structures in memory.