# resizing qemu image

lets add 10 GiB

```sh
qemu-img resize ubuntu-server.img +10G
```

then

![image](../_images/184aa9877fe42d187e0b75e010695b33809a7f5245f90e087adcfa877be2cd55c8bb193f90bd86b497e97884c6aa5d2b04423fb87d92e639ce121671.png)

nice work!

# fixing
if your ubuntu use LVM2, Use this command

![image](../_images/1845e6740dc67207974700ee9a9583d8cd4d4056d4be06a3fdacd31643a1c6585009adc6f696bd47113242084f2f30307415a32464b5f709122c2216.png)

then, run

```sh
sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
sudo e2fsck -f /dev/ubuntu-vg/ubuntu-lv
sudo resize2fs /dev/ubuntu-vg/ubuntu-lv
```