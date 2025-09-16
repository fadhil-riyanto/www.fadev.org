# alpine install SSH + firefox lite qemu

## create image 
```sh
qemu-img create -f qcow2 alpine-client.qcow2 2G
```

## RUN
THIS is dry run

```sh
qemu-system-x86_64 \
	-enable-kvm \
	-m 1G -smp 4 -cpu host \
	-boot d \
	-drive file=alpine-client.qcow2,format=qcow2 \
	-cdrom ./iso/alpine-virt-3.21.3-x86_64.iso \
	-netdev user,id=net0,hostfwd=tcp::30022-:22 \
	-device virtio-net-pci,netdev=net0 \
	-vga virtio
```


