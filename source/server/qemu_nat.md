# Linux QEMU network address translation

first all, set setup our interface

- `sudo ip tuntap add tap0 mode tap`
- `sudo ip tuntap add tap1 mode tap` (optional, if there has any more vm)
- `sudo ip link add br0-lan type bridge` (our switch)
- `sudo ip addr add 192.168.12.1/24 dev br0-lan`
- `sudo ip link set br0-lan up`
- `sudo ip link set tap0 up`, also with tap1 if needed

# Run alpine guest hosts
```sh
qemu-system-x86_64 \
            -enable-kvm \
            -m 256 \
            -smp 4 \
            -cpu host \
            -drive file=pc-2.qcow2,format=qcow2 \
            -cdrom alpine-virt-3.21.3-x86_64.iso \
            -boot d \
            -nographic \
            -netdev tap,id=net0,ifname=tap0,script=no,downscript=no \
            -device virtio-net-pci,netdev=net0
```

# Inside of guest VM
Your `ip addr` output might something like this

```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state DOWN qlen 1000
    link/ether 52:54:00:12:34:56 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::5054:ff:fe12:3456/64 scope link 
       valid_lft forever preferred_lft forever
```

now set eth0 up by typing 

- `ip link set eth0 up`
- `ip addr add 192.168.12.2/24 dev eth0` (I manually setting up IP)

check ip route
```sh
pc-2:~# ip r
192.168.12.0/24 dev eth0 scope link  src 192.168.12.2 
```

there is no route, run `ip route add default via 192.168.12.1`, check again with ip route
```
pc-2:~# ip r
default via 192.168.12.1 dev eth0 
192.168.12.0/24 dev eth0 scope link  src 192.168.12.2 
```

# setting up firewall

we want everyting from br0-lan is forwarded into wlan0, vice versa. in order to do that, we need NAT (network address translation)

here
## check your nat table first

`sudo iptables --table nat --list -v`, make sure there is no 

```
 2151  499K MASQUERADE  all  --  any    wlan0   anywhere             anywhere            
```

now run

- `sudo iptables --table nat --append POSTROUTING --out-interface wlan0 -j MASQUERADE`
- `sudo iptables -t filter -A FORWARD -i wlan0 -o br0-lan -m state --state RELATED,ESTABLISHED -j ACCEPT`
- `sudo iptables -t filter -A FORWARD -i br0-lan -o wlan0 -j ACCEPT`

