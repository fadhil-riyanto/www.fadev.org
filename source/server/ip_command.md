# ip command

## `ip addr`
ip addr is used to display and manage IP addresses assigned to network interfaces.

example: 
- `ip addr`
- `ip addr show`
- `sudo ip addr add 192.168.1.100/24 dev eth0`
- `sudo ip addr del 192.168.1.100/24 dev eth0`

anything about ip assigment

## `ip link`
ip link is used to display and manage network interfaces (links), focusing on layer 2 (Ethernet, loopback, etc.), not IP addresses.

example:
- `ip link`
- `sudo ip link set dev eth0 up`
- `sudo ip link set dev eth0 down`
- `sudo ip link set dev eth0 mtu 1400`

anyting about interface

## `ip tuntap`
ip tuntap manages TUN/TAP virtual network interfaces, which provide a way for user-space programs to interact with network packets as if they were network devices.

- TUN: Simulates a point-to-point device (layer 3), used for routing IP packets (e.g., VPN tunnels).
- TAP: Simulates an Ethernet device (layer 2), used for bridging Ethernet frames (e.g., virtual switches, VMs).

example: 
- `sudo ip tuntap add mode tap dev tap0`
- `sudo ip tuntap add mode tun dev tun0`
- `sudo ip tuntap del mode tap dev tap0`

## `ip route`

IP routing is the process by which data packets are directed from their source to their destination across interconnected networks using Internet Protocol (IP). This process is fundamental to the operation of the Internet and all IP-based networks.

- [https://www.link11.com/en/glossar/ip-routing/](https://www.link11.com/en/glossar/ip-routing/)
- [https://www.cloudflare.com/learning/network-layer/what-is-routing/](https://www.cloudflare.com/learning/network-layer/what-is-routing/)
- [https://info.support.huawei.com/info-finder/encyclopedia/en/IP+routing.html](https://info.support.huawei.com/info-finder/encyclopedia/en/IP+routing.html)


View routing table:
- `ip route`

add route
- `ip route add <destination> via <gateway> dev <interface>`

example: 
```sh
pc-1:~# ip route add default via 192.168.15.1 dev eth0
pc-1:~# ip route
default via 192.168.15.1 dev eth0 
192.168.15.0/24 dev eth0 scope link  src 192.168.15.2 

```
delete route
- `sudo ip route del <destination> [via <gateway>] [dev <interface>]`

example:
```sh
pc-1:~# ip route delete default via 192.168.15.1 dev eth0
pc-1:~# ip r
192.168.15.0/24 dev eth0 scope link  src 192.168.15.2 
pc-1:~# 
```