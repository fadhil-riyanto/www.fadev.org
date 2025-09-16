# ELF struct datatype

![image](../_images/226c75ba603c0f75c0e287cb7cf1502cd4e7857fd7ceba8ef1d60013d08fd225da41b2432866136e0dfbe0152981a49dc106553e664968dade76f92b.png)

recently, I had confusion about ELF datatype. let's look into elf.h

![image](../_images/6fd29d1b194c2d80f6924f6326b6876cb023450367b66064c6debcfaffb38c05a83aa30637373852cc25a630d962542c0f47021636c205cf965ad4e6.png)

see it?

```c
// 32 bit elf
typedef __u32	Elf32_Word;

// 64 bit elf
typedef __u32	Elf64_Word;
```

why word? even in assembly says

- 8 bit -> byte
- 16 bit -> word
- 32 bit -> dword
- 64 -> qword

why word (that is 16 bit), its uses u32 instead u16?

# answer
the key is portability. lets look at elf64 and elf32 

```c
typedef __u32	Elf32_Word;
typedef __u32	Elf64_Word;
```

keep in mind that word (in ELF) is 32 bit int. so we use this convention

- half -> unsigned 16 bit
- word -> unsigned 32 bit
- Xword -> unsigned 64 bit

also works for
- Shalf -> signed 16 bit
- Sword -> signed 32 bit
- Sxword -> signed 64 bit