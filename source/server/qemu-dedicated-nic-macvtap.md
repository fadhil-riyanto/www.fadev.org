# qemu & dedicated nic + macvtap

docs ini memahas solusi agar bisa akses tap (dari vm) tetapi hw yang diakses adalah nic asli, diusahakan tanpa bridge dan NAT NAT

ADA 2 strategi
- add iface fisik ke bridge, lalu attach bridge tersebut ke vm.
- pakai macvtap, dengan cara meredirect packet yang datang, ke arah tap device menggunakan fd (file descriptor). kita akan (ab)use option `-net` tap di qemu

strategi lain (tidak direkomendasikan, diluar topik macvtap)
- membuat virtual eth pair, redirect pakai iptables
- pakai -netdev user (somewhat slow, need triage)

# normal
bagian ini tanpa macvtap ataupun hal hal lain dahulu, pure qemu bridging

configuration
- eth1: mostly WAN
- eth2: tap

```sh
qemu-system-x86_64 \
    -enable-kvm \
    -smp 4 -m 256M \
    -drive file=chr7.qcow2,format=qcow2 \
    -boot order=d \
    -net user,hostfwd=tcp::8291-:8291,hostfwd=tcp::10022-:22 \
    -net nic \
    -netdev tap,id=net0,ifname=tap0,script=no,downscript=no \
    -device virtio-net-pci,netdev=net0,mac=02:11:2a:3b:ff:c3 \
    -nographic
```
```sh
qemu-system-x86_64 \
	-name guest=ubuntu22.04 \
	-machine type=pc,accel=kvm \
	-cpu host -m 4G -smp 4 \
	-enable-kvm \
	-boot order=d \
	-drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
	-drive if=pflash,format=raw,file=OVMF_VARS_ubuntu_server_gpt.4m.fd \
	-drive file=ubuntu-server.img,format=qcow2 \
	-netdev user,id=net0,hostfwd=tcp::20022-:22,hostfwd=tcp::10000-:5432,hostfwd=tcp::10302-:10302 \
	-device virtio-net-pci,netdev=net0 \
	-netdev tap,id=net1,ifname=tap1,script=no,downscript=no \
	-device virtio-net-pci,netdev=net1,mac=02:11:2a:3b:aa:c4 \
	-nographic
```
network stack note:
- ens3: come from qemu bridge (for ssh purpose)
- ens4: come from tap1 (connected to bridge, internal lan)

netplan configuration
```yaml
network:
  version: 2
  ethernets:
    ens4:
      addresses:
        - 192.168.1.2/24
      routes:
        - to: default
          via: 192.168.1.1
    ens3:
      dhcp4: true
```

```sh
// ip a 

2: ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 52:54:00:12:34:56 brd ff:ff:ff:ff:ff:ff
    altname enp0s3
    inet 10.0.2.15/24 metric 100 brd 10.0.2.255 scope global dynamic ens3
       valid_lft 86314sec preferred_lft 86314sec
    inet6 fec0::5054:ff:fe12:3456/64 scope site dynamic mngtmpaddr noprefixroute 
       valid_lft 86317sec preferred_lft 14317sec
    inet6 fe80::5054:ff:fe12:3456/64 scope link 
       valid_lft forever preferred_lft forever
3: ens4: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 02:11:2a:3b:aa:c4 brd ff:ff:ff:ff:ff:ff
    altname enp0s4
    inet 192.168.1.2/24 brd 192.168.1.255 scope global ens4
       valid_lft forever preferred_lft forever
    inet6 fe80::11:2aff:fe3b:aac4/64 scope link 
       valid_lft forever preferred_lft forever

```