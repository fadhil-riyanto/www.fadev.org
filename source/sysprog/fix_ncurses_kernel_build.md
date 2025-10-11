# fix ncurses kernel build


suppose

```text
*** Unable to find the ncurses libraries or the
 *** required header files.
 *** 'make menuconfig' requires the ncurses libraries.
 *** 
 *** Install ncurses (ncurses-devel) and try again.
 *** 
make[2]: *** [/home/fadhil_riyanto/linux-kernel/busybox-1.37.0/scripts/kconfig/lxdialog/Makefile:15: scripts/kconfig/lxdialog/dochecklxdialog] Error 1
make[1]: *** [/home/fadhil_riyanto/linux-kernel/busybox-1.37.0/scripts/kconfig/Makefile:14: menuconfig] Error 2
make: *** [Makefile:444: menuconfig] Error 2
```

maka solusi
`nano scripts/kconfig/lxdialog/Makefile`

ubah
```text
always         := $(hostprogs-y) dochecklxdialog
```