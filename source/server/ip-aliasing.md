# ip aliasing

satu interface bisa punya lebih dari 1 IP dinamai sebagai IP aliasing. contoh

`eth0` bisa punya 2 ip dengan cara
- `ip addr add 192.168.1.100/24 dev eth0`
- `ip addr add 192.168.1.101/24 dev eth0`

atau bisa juga ada 2 interface, katakanlah `eth0` dengan `eth1`, masing2 punya ip nya sendiri2 dengan cara

```sh
ip addr add 192.168.1.10/24 dev eth0
ip addr add 10.0.0.5/24 dev eth1
```

# tambahan
untuk ngeremove salah satu ip nya, bisa dengan `ip addr del <IP NYA>/<CIDR> dev <IFACE>`

