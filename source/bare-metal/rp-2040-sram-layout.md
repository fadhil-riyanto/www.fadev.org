# RP2040 sram layout

the static ram is contains 6 section of ram, which is two 4KB and four 64 KB ram

RAM start at address `0x20000000`

`0x20040000` and `0x20041000` is a start address of 4KB area wide

and, this is section about 64KB wide ram
`0x20000000` - `0x20010000` (64 kb)
`0x20010000` - `0x20020000` (64 kb)
`0x20020000` - `0x20030000` (64 kb)
`0x20030000` - `0x20040000` (64 kb)

this is MIRROR of 64 kb region (stripped)
0x21000000
0x21010000
0x21020000
0x21030000