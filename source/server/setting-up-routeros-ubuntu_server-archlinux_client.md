# setting up routeros + ubuntu server (freeradius) + and archlinux client

## first, setup virtual lan
setup configurasi ip hingga seperti ini

```sh
51: br0-lan: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
    link/ether 8a:b9:27:b3:c7:a5 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::88b9:27ff:feb3:c7a5/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
53: tap0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel master br0-lan state DOWN group default qlen 1000
    link/ether c6:33:f3:fe:d3:ba brd ff:ff:ff:ff:ff:ff
    inet6 fe80::c433:f3ff:fefe:d3ba/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
54: tap1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel master br0-lan state DOWN group default qlen 1000
    link/ether a2:eb:ee:56:8a:90 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::a0eb:eeff:fe56:8a90/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
55: tap2: <BROADCAST,MULTICAST> mtu 1500 qdisc noop master br0-lan state DOWN group default qlen 1000
    link/ether c6:c7:1c:7c:67:8a brd ff:ff:ff:ff:ff:ff
```

untuk membuatnya, jalankan skrip command command ini:
- `sudo ip link add br0-lan type bridge` <- buat switch virtual
- `sudo ip tuntap add tap0 mode tap` <- buat colokan virtual
- `sudo ip tuntap add tap1 mode tap`
- `sudo ip tuntap add tap2 mode tap`
- `sudo ip link set tap0 master br0-lan` <- set semua colokan punya induk ke switch br0-lan, intinya harus satu switch
- `sudo ip link set tap1 master br0-lan`
- `sudo ip link set tap2 master br0-lan`
- `sudo ip link set br0-lan up` <- nyalakan semua interface nya
- `sudo ip link set tap0 up`
- `sudo ip link set tap1 up`
- `sudo ip link set tap2 up`

## alokasi interface
- `br0-lan` --> switch utama
- `tap0` --> interface untuk routerOS
- `tap1` --> interface untuk freeradius (running di ubuntu server)
- `tap2` --> interface test client (bisa alpineLinux, archlinux, bebas)

## run routeros

download links: https://download.mikrotik.com/routeros/6.49.18/chr-6.49.18.img.zip

```sh
# convert first
qemu-img convert -f raw -O qcow2 chr-6.49.18.img chr.qcow2

# then run
qemu-system-x86_64 \
      -enable-kvm \
      -smp 4 \
      -m 256M \
      -drive file=chr.qcow2,format=qcow2 \
      -boot order=d \
      -net user,hostfwd=tcp::8291-:8291 \
      -net nic \
      -nographic \
      -netdev tap,id=net0,ifname=tap0,script=no,downscript=no \
      -device virtio-net-pci,netdev=net0,mac=02:11:2a:3b:ff:c3
```

![image](../_images/5f64d4f9b4ff9ec75cdb5641d5ccc8e63e796e7e736d3b66f0523fdbb984f651e399a2fa28fd943cfc1272db3b1330dddf56b5ca9100e9316e8c31a5.png)
setidaknya, mac-addr nya sama. yaitu ether3

## run ubuntu server

command ini hanya dirun run sekali (ketika instalasi)

```sh
# copy firmware uefi vars
cp /usr/share/edk2/x64/OVMF_VARS.4m.fd .
mv OVMF_VARS.4m.fd OVMF_VARS_ubuntu_server_gpt.4m.fd

# run qemu
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
```

proses instalasi ubuntu server cari di internet xixi.

setelah installed, kita install beberapa base package dahulu. base package yg akan diinstall adalah 

```sh
sudo apt-get update && \
sudo apt-get upgrade && \
sudo apt-get install \
    openssh-server freeradius isc-dhcp-client
```

lalu setelah installed, kita tidak butuh iso lagi, kita bisa buang saja parameter `-cdrom ubuntu-24.04.2-live-server-amd64.iso` karna unused. dan untuk konfigurasi tambahan, saya buat pakai vga virtio (agar text nya smooth), dan juga netdev untuk colokan `tap1` yang nyambung ke bridge

```sh
qemu-system-x86_64 \
    -enable-kvm \
    -boot order=d \
    -drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
    -drive if=pflash,format=raw,file=OVMF_VARS_ubuntu_server_gpt.4m.fd \
    -drive file=ubuntu-server.img,format=qcow2 \
    -m 4G \
    -smp 4 \
    -netdev user,id=net0,hostfwd=tcp::20022-:22 \
    -device e1000,netdev=net0 \
    -netdev tap,id=net1,ifname=tap1,script=no,downscript=no \
    -device virtio-net-pci,netdev=net1,mac=02:11:2a:3b:aa:c4 \
    -vga virtio
```

nb: jangan lupa `sudo apt-get update && sudo apt-get upgrade && sudo apt-get install openssh-server`, karna di vm tidak bisa copy paste (mau dari dalam ataupun keluar), dan juga tidak bisa scroll atas bawah. maka proses me-config nya akan pakai ssh saja

![image](../_images/6216af66c741aa5c444f4e3f3c92f5cd5cff2b16d84e1ce7959fb3022404de548d8e3d12b5792f871bc5d68599a8ff141d866ec9af17bdf15822e380.png)

intinya biarkan vm nya jalan begitu saja, bisa di minimize atau dipindah ke tab lain yang tidak menganggu. selanjutnya remote vm nya pakai

```sh
ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null  fadhil_riyanto@127.0.0.1 -p 20022
```

nb: ganti `fadhil_riyanto` dengan username yang sudah diset tadi

![image](../_images/e1b3a2a87f2147be937d1c1604519f52d7979acf87d6ed653f1319393fa3d9099b1562a1b6d1bef94c0b907c5c142fd2f00428ddd5b6266bc854c826.png)

setidaknya seperti itu remote-an nya

## freeradius
jalankan `sudo apt-get install freeradius`, lalu test dengan `sudo freeradius -X`

![image](../_images/c94a211608a1db50024e52889c911f4ba6d5b894301a6c0676ce0d0529b7830a4dd824567d341d9f82c91165bcf77b1b5dfcb914183c5e466c150fa9.png)

pastikan ada tulisan ready to process request

## winbox
karna winbox pakai port 8291 untuk merepote mikrotik, maka kita konek dengan host 127.0.0.1:8291, password sesuai config awal mikrotik ketika awal tadi

winbox localhost

![image](../_images/5c2d5ee56f841a1c270df51d085e5506a2582a05610927ddcd84820cd3002f689dcc4170ec3fe3af3b77ecf3e1e61d98ea2e7ca6cc5f51b3d8b9e770.png)

### setup mikrotik dhcp server 
ip -> address
![image](../_images/cdc8c75a5259e1dd336291a4d4991eb1301e32f68b5f1ac46f12d27a33c6b7716b3ef0cb260d58477d1b8d054ee449f378aeeb1e1331b5ec84b45569.png)


ip -> dhcp server

![image](../_images/6133719edf4cf0c1e46b9284e559fa88868cf8a60d103446d3f1d522f5754df314c82cab832272a9b683b823750ff3470e005c49780858db86e16ebc.png)

![image](../_images/1429917ae1cc7caa5b655d3b3dc59264012d026ed3c20e1ec825d5719d6e22e81bf686ba3b9013b9a00050b6a4da887d1d9d418ddfa025c7e4e1162e.png)

![image](../_images/321b4b134b67a9be0c091c9ae2093bbca9edb62df2799cc3b4339665e178102b8afc4e09d7125d01665356e77c2b2f9b938e3fded7bcb192445ec3ff.png)

![image](../_images/76a1f9eae8f7a57a5d426ce2a9e5562d69d4d71237c707bb6af5cd8483dddb3fe227a9ffa0b127a91ee85b4ea4a20813b53c11f78033e5c9ba75f77d.png)

![image](../_images/425c569d1b6df4dee6f4e64925263eda657131e8b70af0f8248a330aef0a92f514b5ae6cbcb2b5e8266ad0520b83a44ef20536490d66323dd6c80767.png)

dns server kita biarkan dahulu

![image](../_images/8380a0b6d16f00b1d879e38b6bd10c71142750ae6c1df4325f6176b255f1e1e89845912464c7c3f7ee27a63bf44886982f0312807e3e038d4122c2ad.png)

pembuktian: 
jalankan `sudo dhclient enp4` (karna interface tun1 dia dibaca sebagai enp4 di ubuntu server)
![image](../_images/2025-06-10_13-20.png)

ping ke router

![image](../_images/e44475652a0685c34088f0709bbce20eb1c8e14e3ef28fdb0df1d8f8fcfaf57af06cc14d7fd57c2db2937f2969c538fb1eb922f0a3ca490246bf2744.png)

router ke ubuntu server 
![image](../_images/cb465e579a0eb33086d6a74da97b51470a70d2d114ec5fe7c00c155c95590524e81d0eaf9036a7e973aaf58c909174d5eae9387b59e324efde5f6f47.png)

## setting up Archlinux (GUI)
download dahulu bahan nya di [https://sourceforge.net/projects/arch-linux-gui/](https://sourceforge.net/projects/arch-linux-gui/), pakai xfce (paling ringan)

run archlinux gui sebagai `tap2`

```sh
qemu-system-x86_64 \
    -enable-kvm \
    -boot order=d \
    -cdrom archlinux-gui-xfce-2022.07-x86_64.iso \
    -m 4G \
    -smp 4 \
    -netdev tap,id=net1,ifname=tap2,script=no,downscript=no \
    -device virtio-net-pci,netdev=net1,mac=02:11:5c:1b:aa:c9 \
    -vga virtio
```
catatan: macnya dikarang lagi, agar tidak sama. jika sama ternyata bakal dapat ip yang sama

![image](../_images/6dbca4ece71a387364fe6d5368d8b1c6431c3d3ab2f9f366f9d34c07aa81327e44fb8b757e6ae98906cf4ae440ca26c020a249db84c78060abb37442.png)

![image](../_images/dbadc00c801066a13f108acff5eb48186a0931e7f6071f3f8a7733406b357e6d8c9a8453fe03f60d13e85a3fa2b547591029535ce3b727720902a3a3.png)

nb: archlinux makan 2 ip karna NetworkManager dan systemd-resolved bentrok (bawaannta sepertinya). tapi harusnya no problem at all

## setup hotspot winbox

ip -> hotspot

![image](../_images/320a0dc0cd86c6f47ad63480a9570276e208c48b60099f3a320ef890aa3bb7c06604c32b157531104b5f5edc51853d2732c25403a84f737406780e31.png)

next next saja, kecuali dns nanti diisi 1.1.1.1, dan dns-name diisi nama domain untuk captive portalnya
![image](../_images/988a96f698f5bdbd154f04c7523e1dd24d88853b451c6e887122bbf82c54d00f86ab0f688d3303e478e9cc1c016272d84e1937049e5e454119939477.png)


# test
![image](../_images/a402fb33b60465533c6e5bdc6762359c82f692492362ec74d96e8c440c90fba385489ba574cdfe6ed8254d4852e8ea55b368a4f5ab98d74ca75d5e30.png)

## karna `192.168.1.254` ip freeradius
maka kita ignore pakai 

![image](../_images/000cd141407bb54adf25c3c11ceefa575a528165b64a30e3eb444b8620b926e094dd5ef3841ff0c082def4c08b13fdf29bf9f9e1e8e1760ef739fcaf.png)

ip binding

## static ip versions

- `sudo ip addr add 192.168.1.2/24 dev ens4`
- `sudo ip link set dev ens4 up`
- `sudo ip route append default via 192.168.1.1`

# freeradius

ubah `/etc/freeradius/3.0/clients.conf`, tambah

```
client private-network-1 {
    ipaddr      = 192.192.1.1/24
    secret      = testing123
}


```

lalu `/etc/freeradius/3.0/users`
```
bob Cleartext-Password := "password"
```

## winbox
![image](../_images/50f3df1d429445c00433163d8e1c79a253f2cef67178d21c5a811f8bd23350d9c557ba0b174c7fddcb7bbed88e3261c8ed3beb84f01932a8e3ae73fc.png)

system -> AAA
![image](../_images/cee05007032ea0004685a07cffdffcfb957095daae4524a931d8a374c06a6ab190ce8ca75a394f33e42e58c6af012761539621bbb28e2dc1214860b6.png)