# bookmarks highly useful link

## this section is derived from my original channel [@xorriso](https://t.me/xorriso)

###  [https://xenbits.xen.org/docs/4.6-testing/misc/pvh.html](https://xenbits.xen.org/docs/4.6-testing/misc/pvh.html)

`
"PVH is to make use of the hardware virtualization extensions present in modern x86 CPUs in order to improve performance."
`

### [https://wiki.xenproject.org/wiki/Linux_PVH](https://wiki.xenproject.org/wiki/Linux_PVH)
`Where one will select Processor type and features ---> Linux guest support --->Support for running as a PVH guest`

### [https://github.com/Goldside543/goldspace](https://github.com/Goldside543/goldspace)

### [https://mongoc.org/libmongoc/current/mongoc_client_new.html](https://mongoc.org/libmongoc/current/mongoc_client_new.html)

```
kesimpulan: mongoc_client_new return null on error, but not even the string are correct
no connection checked.

jangan ngeharap mongoc_client_new ngeluarin null
```

### [https://faculty.cs.niu.edu/~hutchins/csci480/signals.htm](https://faculty.cs.niu.edu/~hutchins/csci480/signals.htm)
daftar exit code

### [https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/arch/x86/entry/syscalls/syscall_64.tbl](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/arch/x86/entry/syscalls/syscall_64.tbl)

`list syscall`

### [https://www.bitsinthewind.com/about-dac/publications/unix-systems-programming](https://www.bitsinthewind.com/about-dac/publications/unix-systems-programming)
`system programming`

### [https://lwn.net/Articles/205126/](https://lwn.net/Articles/205126/)
`In recent times, Al's work has resulted in a long series of patches merged into the mainline, almost all of which have been marked as "endianness annotations." These patches mostly change the declared types for various functions, variables, and structure members. The new types may be unfamiliar to many, since they are relatively new - though not that new; they were introduced in 2.6.9. These types are __le16, __le32, __le64, __be16, __be32, and __be64. `

### [https://github.com/AugustTan/documents/blob/master/UNIX%20Network%20Programming(Volume1%2C3rd).pdf](https://github.com/AugustTan/documents/blob/master/UNIX%20Network%20Programming(Volume1%2C3rd).pdf)

### [https://ics.uci.edu/~aburtsev/143A/2017fall/lectures/](https://ics.uci.edu/~aburtsev/143A/2017fall/lectures/)
`Gas kuliah online
tiada kata untuk tidak belajar, di topik ini Pak aburtsev membahas sistem operasi, sistem locknya, memory managemen, kernel, boot step nya, dll`

### [http://osblog.stephenmarz.com/index.html](http://osblog.stephenmarz.com/index.html)

### [https://c-ares.org/docs.html#examples](https://c-ares.org/docs.html#examples)
dokumentasi C-ares (async dns resolver)

### [https://github.com/torvalds/linux/blob/d683b96b072dc4680fc74964eca77e6a23d1fa6e/drivers/char/random.c#L55](https://github.com/torvalds/linux/blob/d683b96b072dc4680fc74964eca77e6a23d1fa6e/drivers/char/random.c#L55)
"Computers are very predictable devices.  Hence it is extremely hard to produce truly random numbers on a computer"

### [https://stackoverflow.com/questions/17898989/what-is-global-start-in-assembly-language](https://stackoverflow.com/questions/17898989/what-is-global-start-in-assembly-language)

If you want to use a different entry point name other than _start (which is the default), you can specify -e parameter to ld like

`ld -e my_entry_point -o output_filename object_filename`

### inline ASM GCC
- [https://gcc.gnu.org/onlinedocs/gcc/Extended-Asm.html](https://gcc.gnu.org/onlinedocs/gcc/Extended-Asm.html)
- [https://gcc.gnu.org/onlinedocs/gcc/Extended-Asm.html#AssemblerTemplate](https://gcc.gnu.org/onlinedocs/gcc/Extended-Asm.html#AssemblerTemplate)
- [https://splichal.eu/gccsphinx-final/html/gcc/extensions-to-the-c-language-family/how-to-use-inline-assembly-language-in-c-code.html#inputoperands](https://splichal.eu/gccsphinx-final/html/gcc/extensions-to-the-c-language-family/how-to-use-inline-assembly-language-in-c-code.html#inputoperands)

### [http://www.ucw.cz/~hubicka/papers/amd64/node1.html](http://www.ucw.cz/~hubicka/papers/amd64/node1.html)

movabs is ATT-syntax for mov al/ax/eax/rax, byte/[d|q]word ptr [<64-bit absolute address>] or mov byte/[d|q]word ptr[<64-bit absolute address>], al/ax/eax/rax

tambahan:
movabs is used for absolute data moves, to either load an arbitrary 64-bit constant into a register or to load data in a register from a 64-bit address.


### [https://electronicsreference.com/assembly-language/assembly-language-registers/](https://electronicsreference.com/assembly-language/assembly-language-registers/)

### bookmark movabs 
- http://www.ucw.cz/~hubicka/papers/amd64/node1.html
- https://gcc.gnu.org/bugzilla/show_bug.cgi?id=82339
- https://cs4157.github.io/www/2024-1/lect/13-x86-assembly.html


### memory layout linux
- [https://www.kernel.org/doc/html/v5.8/x86/x86_64/mm.html](https://www.kernel.org/doc/html/v5.8/x86/x86_64/mm.html)

## this section is pure form, created when I use mdbook

### getopt example
- [https://www.gnu.org/software/libc/manual/html_node/Example-of-Getopt.html](https://www.gnu.org/software/libc/manual/html_node/Example-of-Getopt.html)

### manage email using LEI
- [https://people.kernel.org/monsieuricon/lore-lei-part-1-getting-started](https://people.kernel.org/monsieuricon/lore-lei-part-1-getting-started)

- [https://docs.kernel.org/maintainer/feature-and-driver-maintainers.html](https://docs.kernel.org/maintainer/feature-and-driver-maintainers.html)

### intel SGX
[https://docs.kernel.org/arch/x86/sgx.html](https://docs.kernel.org/arch/x86/sgx.html)

### system V abi
- [https://refspecs.linuxfoundation.org/LSB_2.1.0/LSB-Core-generic/LSB-Core-generic/normativerefs.html#STD.ABIUPDATE](https://refspecs.linuxfoundation.org/LSB_2.1.0/LSB-Core-generic/LSB-Core-generic/normativerefs.html#STD.ABIUPDATE)

### ELF Structure types
- [https://refspecs.linuxfoundation.org/LSB_2.1.0/LSB-Core-generic/LSB-Core-generic/elftypes.html](https://refspecs.linuxfoundation.org/LSB_2.1.0/LSB-Core-generic/LSB-Core-generic/elftypes.html)

### ELF cheatsheet
- [https://gist.github.com/x0nu11byt3/bcb35c3de461e5fb66173071a2379779](https://gist.github.com/x0nu11byt3/bcb35c3de461e5fb66173071a2379779)
- [https://www.uclibc.org/docs/elf-64-gen.pdf](https://www.uclibc.org/docs/elf-64-gen.pdf)

### AMD & clang
- [https://rocm.docs.amd.com/projects/llvm-project/en/latest/LLVM/clang/html/ClangFormatStyleOptions.html](https://rocm.docs.amd.com/projects/llvm-project/en/latest/LLVM/clang/html/ClangFormatStyleOptions.html)