# setting up ubuntu server with qemu + custom bridge

## qemu section

```sh
# create image first
qemu-img create -f qcow2 ubuntu-server.img 10G

# run the iso
qemu-system-x86_64 \
      -enable-kvm \
      -boot order=d \
      -cdrom ubuntu-24.04.2-live-server-amd64.iso \
      -drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
      -drive if=pflash,format=raw,file=OVMF_VARS_ubuntu_server_gpt.4m.fd \
      -drive file=ubuntu-server.img,format=qcow2 \
      -m 4G \
      -smp 4 \
      -net user,hostfwd=tcp::20022-:22 \
      -net nic

# run iso
qemu-system-x86_64 \
	-enable-kvm \
	-boot order=d \
	-drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
	-drive if=pflash,format=raw,file=OVMF_VARS_ubuntu_server_gpt.4m.fd \
	-drive file=ubuntu-server.img,format=qcow2 \
	-m 4G \
	-smp 4 \
	-net user,hostfwd=tcp::20022-:22 \
	-net nic \
	-vga virtio
```