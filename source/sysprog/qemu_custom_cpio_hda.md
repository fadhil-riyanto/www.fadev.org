# qemu custom cpio HDA

skrip init custom linux

```sh
qemu-system-x86_64 \-kernel ./vmlinux \
                                                 -nographic \
                                                 --append "console=tty0 console=ttyS0 panic=1 root=/dev/sda rootfstype=ext2" \
                                                 -hda root.img \
                                                 -m 1024 \
                                                 -vga none \
                                                 -display none \
                                                 -serial mon:stdio \
                                                 -no-reboot \
                                                 -initrd vfs/root.cpio.gz
```

generate cpio

```sh
find . | cpio -o -H newc | gzip > root.cpio.gz
``