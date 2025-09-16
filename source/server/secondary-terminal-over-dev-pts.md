# secondary terminal over /dev/pts/

here my qemu

```sh
qemu-system-x86_64 \
	-name guest=ubuntu22.04 \
	-machine type=pc,accel=kvm \
	-cpu host -m 4G -smp 4 \
	-enable-kvm \
	-boot order=d \
	-drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
	-drive if=pflash,format=raw,file=./nvram/OVMF_VARS_ubuntu_server_gpt.4m.fd \
	-drive file=./images/ubuntu-server-btik-captive-portal.img,format=qcow2 \
	-netdev user,id=net0,hostfwd=tcp::20022-:22,hostfwd=tcp::10000-:5432,hostfwd=tcp::10302-:10302,hostfwd=tcp::8080-:8080,hostfwd=udp::1813-:1813,hostfwd=udp::1812-:1812 \
	-device virtio-net-pci,netdev=net0 \
	-nographic \
	-serial mon:stdio \
	-device virtio-serial \
	-chardev pty,id=char0 \
	-device virtconsole,chardev=char0
char device redirected to /dev/pts/14 (label char0)

```

then in picocom 

```sh
# run inside qemu
sudo systemctl start getty@hvc0.service

# un on host
sudo picocom /dev/pts/14
```

