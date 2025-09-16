# qemu booting debian ARM64

this tutorial based on [https://blog.jitendrapatro.me/emulating-aarch64arm64-with-qemu-part-1/](https://blog.jitendrapatro.me/emulating-aarch64arm64-with-qemu-part-1/), big thanks!

I will replicate the steps

### create qcow2
```sh
qemu-img create -f qcow2 debian.qcow 16G
```

after it, in future in case the url is 404, please look at [this](http://ftp.debian.org/debian/dists/bookworm/main/installer-arm64/current/images/netboot/debian-installer/arm64/)

### download the init & kernel

```sh
wget http://ftp.debian.org/debian/dists/bookworm/main/installer-arm64/current/images/netboot/debian-installer/arm64/initrd.gz
wget http://ftp.debian.org/debian/dists/bookworm/main/installer-arm64/current/images/netboot/debian-installer/arm64/linux
```

### run the system
```sh
qemu-system-aarch64 -machine virt -smp 2 -cpu max -m 4G \
          -initrd initrd.gz \
          -kernel linux \
          -drive file=debian.qcow,if=virtio \
          -nic user,model=e1000
```

### ss
![image](../_images/312f90fae112c79aa2ef955cc044f1248ce24f04dc068773dbefb9170651d2d2fbd2f9d5f4abe8cf220a7f8762e04b775519f8f419f04d5fbf45aa28.png)
![image](../_images/8a2ab9814e5abec61dfba05a8cb731982f9824f326117b4066a198b2484976355ea5f2a4de2c4be6777ae164f31a58c8f0ab4419f4ee6769aaa20a67.png)