# TLDR qemu

buat file namanya `setup-network.sh`, lalu isi dengan

```sh
sudo ip link add br0-lan type bridge
sudo ip tuntap add tap0 mode tap
sudo ip tuntap add tap1 mode tap
sudo ip tuntap add tap2 mode tap

sudo ip link set tap0 master br0-lan
sudo ip link set tap1 master br0-lan
sudo ip link set tap2 master br0-lan

sudo ip link set br0-lan up
sudo ip link set tap0 up
sudo ip link set tap1 up
sudo ip link set tap2 up

sudo ip a

```

lalu lakukan ini agar bisa di exec via terminal
- `sudo chmod 666 setup-network.sh`
- `sh ./setup-network.sh`

# running qemu

run routerOS

```sh
# download dahulu chr-7.19.1.img dari web resminya
qemu-img convert -f raw -O qcow2 chr-7.19.1.img chr7.qcow2

# run chr
# port yang dipakai
# - 8291: untuk winbox
# - 30022: untuk keperluan sftp, utak atik file hotspot nya
qemu-system-x86_64 \
	-enable-kvm \
	-smp 4 \
	-m 256M \
	-drive file=chr7.qcow2,format=qcow2 \
	-boot order=d \
	-net user,hostfwd=tcp::8291-:8291,hostfwd=tcp::30022-:22 \
	-net nic \
	-nographic \
	-netdev tap,id=net0,ifname=tap0,script=no,downscript=no \
	-device virtio-net-pci,netdev=net0,mac=02:11:2a:3b:ff:c3
```

# ubuntu server

buat image (HDD virtual untuk os kita nanti)
```sh
qemu-img create -f qcow2 ubuntu-server.img 15G
```

run iso (saat install)
```sh
qemu-system-x86_64 \
	-enable-kvm \
	-boot order=d \
	-cdrom GANTI_NAMA_ISO_UBUNTU.iso \
	-drive file=ubuntu-server.img,format=qcow2 \
	-m 4G \
	-smp 4 \
	-netdev user,id=net0,hostfwd=tcp::20022-:22,hostfwd=tcp::10000-:5432 \
	-device e1000,netdev=net0 \
	-netdev tap,id=net1,ifname=tap1,script=no,downscript=no \
	-device virtio-net-pci,netdev=net1,mac=02:11:2a:3b:aa:c4 \
	-vga virtio
```

lalu run hasil image (Default no graphic, jadi ntar kita ssh pakai `ssh -p 20022 root@127.0.0.1` biar bisa copas)

dan juga kita optimalisasi dengan cara pakai nographic, tanpa cdrom, map port yang dibutuhkan saja

port yg di forward:
- 20022: untuk remote
- 10302: untuk keperluan ngoding laravel
- 10000: untuk keperluan postgresql, siapa tahu mau di remote via adminer, pgadmin dari local, atau cuman psql dll

```sh
qemu-system-x86_64 \
	-enable-kvm \
	-boot order=d \
	-drive file=ubuntu-server.img,format=qcow2 \
	-m 4G \
	-smp 4 \
	-netdev user,id=net0,hostfwd=tcp::20022-:22,hostfwd=tcp::10302-:10302,hostfwd=tcp::10000-:5432 \
	-device e1000,netdev=net0 \
	-netdev tap,id=net1,ifname=tap1,script=no,downscript=no \
	-device virtio-net-pci,netdev=net1,mac=02:11:2a:3b:aa:c4 \
	-vga virtio \
	-nographic
```

VPS KVM siap jadi bahan ujicoba, langsung test saja ke `ssh -p 20022 root@127.0.0.1`

# experimental (jangan dipakai / do not use)
untuk catatan pribadi bahan experimental UEFI, KVM, sama custom machine q35 

# experimental 1 (safest)
```sh
qemu-system-x86_64 \
    -name guest=ubuntu22.04,debug-threads=on \
    -machine type=pc,accel=kvm \
    -cpu host \
    -enable-kvm \
    -boot order=d \
    -drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
    -drive if=pflash,format=raw,file=OVMF_VARS_ubuntu_server_gpt.4m.fd \
    -drive file=ubuntu-server.img,format=qcow2 \
    -m 4G \
    -smp 4 \
    -netdev user,id=net0,hostfwd=tcp::20022-:22,hostfwd=tcp::10000-:5432 \
    -device virtio-net-pci,netdev=net0 \
    -netdev tap,id=net1,ifname=tap1,script=no,downscript=no \
    -device virtio-net-pci,netdev=net1,mac=02:11:2a:3b:aa:c4

```

dgn iso

```sh
qemu-system-x86_64 \
	-name guest=ubuntu22.04,debug-threads=on \
	-machine type=pc,accel=kvm \
	-cpu host \
	-enable-kvm \
	-boot order=d \
	-cdrom a.iso \
	-drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
	-drive if=pflash,format=raw,file=OVMF_VARS_ubuntu_server_gpt.4m.fd \
	-drive file=ubuntu-server.img,format=qcow2 \
	-m 4G \
	-smp 4 \
	-netdev user,id=net0,hostfwd=tcp::20022-:22,hostfwd=tcp::10302-:10302,hostfwd=tcp::10000-:5432 \
	-device e1000,netdev=net0 \
	-netdev tap,id=net1,ifname=tap1,script=no,downscript=no \
	-device virtio-net-pci,netdev=net1,mac=02:11:2a:3b:aa:c4 \
	-vga virtio
```

custom machine chipset PC, KVM, UEFI headless

```sh
qemu-system-x86_64 \
	-name guest=ubuntu22.04,debug-threads=on \
	-machine type=pc,accel=kvm \
	-cpu host \
	-enable-kvm \
	-boot order=d \
	-drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
	-drive if=pflash,format=raw,file=OVMF_VARS_ubuntu_server_gpt.4m.fd \
	-drive file=ubuntu-server.img,format=qcow2 \
	-m 4G \
	-smp 4 \
	-netdev user,id=net0,hostfwd=tcp::20022-:22,hostfwd=tcp::10302-:10302,hostfwd=tcp::10000-:5432 \
	-device e1000,netdev=net0 \
	-netdev tap,id=net1,ifname=tap1,script=no,downscript=no \
	-device virtio-net-pci,netdev=net1,mac=02:11:2a:3b:aa:c4 \
	-vga virtio \
	-nographic
```

working (part 2)
```sh
qemu-system-x86_64 \
          -enable-kvm \
          -boot order=d \
          -drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
          -drive if=pflash,format=raw,file=OVMF_VARS_ubuntu_server_gpt.4m.fd \
          -drive file=ubuntu-server.img,format=qcow2 \
          -m 4G \
          -smp 4 \
          -netdev user,id=net0,hostfwd=tcp::20022-:22,hostfwd=tcp::10000-:5432 \
          -device e1000,netdev=net0 \
          -netdev tap,id=net1,ifname=tap1,script=no,downscript=no \
          -device virtio-net-pci,netdev=net1,mac=02:11:2a:3b:aa:c4 \
          -vga virtio
```

no iso (headless)
```sh
qemu-system-x86_64 \
	-name guest=ubuntu22.04,debug-threads=on \
	-machine type=q35,accel=kvm \
	-cpu host \
	-enable-kvm \
	-boot order=d \
	-drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
	-drive if=pflash,format=raw,file=OVMF_VARS_ubuntu_server_gpt.4m.fd \
	-drive file=ubuntu-server.img,format=qcow2 \
	-m 4G \
	-smp 4 \
	-netdev user,id=net0,hostfwd=tcp::20022-:22,hostfwd=tcp::10000-:5432 \
	-device e1000,netdev=net0 \
	-netdev tap,id=net1,ifname=tap1,script=no,downscript=no \
	-device virtio-net-pci,netdev=net1,mac=02:11:2a:3b:aa:c4
```