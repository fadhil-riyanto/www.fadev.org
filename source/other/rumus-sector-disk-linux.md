# Rumus sector disk Linux

rumus sector linux

\\( x \times 512 = (n \times 1024 \times 1024 \times 1024) \\)

dan untuk \\( n \\) sesuaikan dengan kebutuhan.

disk sector mulai dari 2048. maka misal, x adalah 3145728, command parted nya
parted /dev/sda --script mkpart P1 ext4 2048s 3145728s
misal ingin menambah sekitar 500 MB, maka offset terakhir ditambah 1, misal

```sh
parted /dev/sda --script mkpart P2 ext4 3145729s 4194304s
```

link referensi
- [https://wiki.archlinux.org/title/Parted#UEFI/GPT_examples](https://wiki.archlinux.org/title/Parted#UEFI/GPT_examples)
- [https://ioflood.com/blog/parted-linux-command/](https://ioflood.com/blog/parted-linux-command/)