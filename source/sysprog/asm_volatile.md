# asm volatile

ref: https://gcc.gnu.org/onlinedocs/gcc/Extended-Asm.html

formal syntax:

```txt
asm asm-qualifiers ( AssemblerTemplate 
                 : OutputOperands 
                 [ : InputOperands
                 [ : Clobbers ] ])

asm asm-qualifiers ( AssemblerTemplate 
                      : OutputOperands
                      : InputOperands
                      : Clobbers
                      : GotoLabels)
```