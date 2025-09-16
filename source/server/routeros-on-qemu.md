# install routerOS.iso (not chr) on qemu

please download this [https://download.mikrotik.com/routeros/7.19.3/mikrotik-7.19.3.iso](https://download.mikrotik.com/routeros/7.19.3/mikrotik-7.19.3.iso), [https://mikrotik.com/download](https://mikrotik.com/download)

select x86

after that, run this command (dry run)

```sh
qemu-img create -f qcow2 mikrotik-7.qcow2 4G
```

install
```sh
qemu-system-x86_64 \
      -enable-kvm \
      -smp 4 -m 256M \
      -drive file=mikrotik-7.qcow2,format=qcow2 \
      -boot order=d \
      -cdrom ./iso/mikrotik-7.19.3.iso \
      -net user,hostfwd=tcp::8291-:8291,hostfwd=tcp::10022-:22 \
      -net nic
```


select wireless, and system

after that, run this
```sh
wget https://gist.githubusercontent.com/fadhil-riyanto/d370c3551426ced874f7c0e0e6f62800/raw/9ef4886bcb5c49137b47a2ce60f49a840751e753/setup-network.sh && chmod 777 setup-network.sh && sudo sh setup-network.sh
```

now, we have virtual lan that uses tun-tap network. now run chr on `tap0`

```sh
qemu-system-x86_64 \
      -enable-kvm \
      -smp 4 -m 256M \
      -drive file=mikrotik-7.qcow2,format=qcow2 \
      -boot order=d \
      -netdev user,id=net0,hostfwd=tcp::8291-:8291,hostfwd=tcp::10022-:22 \
      -device virtio-net-pci,netdev=net0 \
      -netdev tap,id=net1,ifname=tap1,script=no,downscript=no \
      -device virtio-net-pci,netdev=net1,mac=02:11:2a:3b:aa:c4 \
      -nographic
```

# post install

do not forget to enable DHCP in order to get internet from qemu internal routes