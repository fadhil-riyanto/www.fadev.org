# ELF64 text only

## ELF Types
There are three main types for ELF files.

-  An executable file contains code and data suitable for execution. It specifies the memory layout of the process. 
-  A relocatable file contains code and data suitable for linking with other relocatable and shared object files. 
-  A shared object file (a.k.a. shared library) contains code and data suitable for the link editor ld at link time and the dynamic linker at run time. The dynamic linker may be called ld.so.1, libc.so.1 or ld-linux.so.1, depending on the implementation. 

 The most useful part of ELF lies in its section structure. With the right tools and techniques, programmers can manipulate the execution of executables with great flexibility. 

source: [https://ftp.math.utah.edu/u/ma/hohn/linux/misc/elf/node2.html](https://ftp.math.utah.edu/u/ma/hohn/linux/misc/elf/node2.html)

big fat ELF docs: [https://docs.oracle.com/cd/E19683-01/816-1386/6m7qcoblh/index.html](https://docs.oracle.com/cd/E19683-01/816-1386/6m7qcoblh/index.html), big thanks to oracle!