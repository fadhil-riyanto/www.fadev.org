# types war

recently, I face a spesific issue in order choosing best types for my program. my goal is choose best need for my C datatype

there has some header exists

- `stdint.h`
- `sys/types.h`

difference from location presefective

- `/usr/lib/clang/20/include/stdint.h`
- `/usr/include/sys/types.h`

see? `stdint.h` is more compiler oriented, and `sys/types.h` is more system oriented, that right, `sys/types.h` is POSIX. It's fundamentally about defining types used by system calls and other OS-level interfaces.

# `sys/types.h`

Purpose: To define data types used in system-level programming. These types are often opaque and their actual size can vary between different systems (e.g., a 32-bit vs. a 64-bit system), but they provide a portable way to interface with the OS kernel.

Origin: System V and BSD systems, later standardized by POSIX.

Use sys/types.h when you are writing code that makes POSIX-compliant system calls (open, read, fork, stat, etc.).

<div class="warning">

Note

there is no format specifier header.
</div>

# `stdint.h`
This header is part of the ISO C99 standard and later. It is focused on providing programmers with explicit control over the size of integer data types.

Purpose: To define integer types of a specific, fixed width and to provide macros for printing and scanning these types with the printf and scanf family of functions.

<div class="warning">

Note

use `inttypes.h` for formatting, see spesific topic about it [here](inttypes.md)
</div>

# conlusion
Default to `<stdint.h>` for all your data definitions. Only use types from `<sys/types.h>` when you are calling an OS/POSIX function that requires them.

normal struct? use stdint.h

interacting with os APIs, such read(), return pid, etc. use `<sys/types.h>`

# another types wars

- `uint_least8_t` vs `uint8_t`, imagine, you on very old board, where 8 bit int is not available, this `uint_least8_t` will be taken as 16 bit int. meanwhile, `uint8_t` give you exactly 8 bit wide variable.