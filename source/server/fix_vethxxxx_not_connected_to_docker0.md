# fix vthxxxxxxxx is not connected to docker0

consider

```
> ip  a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute 
       valid_lft forever preferred_lft forever
2: enp2s0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether 2c:4d:54:c6:f2:0c brd ff:ff:ff:ff:ff:ff
    altname enx2c4d54c6f20c
3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether f0:03:8c:66:9c:21 brd ff:ff:ff:ff:ff:ff
    inet 192.168.105.162/24 metric 1024 brd 192.168.105.255 scope global dynamic wlan0
       valid_lft 2920sec preferred_lft 2920sec
    inet 192.168.105.163/24 brd 192.168.105.255 scope global secondary dynamic noprefixroute wlan0
       valid_lft 2921sec preferred_lft 2921sec
    inet6 fe80::ee67:75f9:fa9c:2561/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
4: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 86:1e:e0:72:f4:8d brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::841e:e0ff:fe72:f48d/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
17: veth914db4f@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether d2:02:61:f4:12:d0 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::d002:61ff:fef4:12d0/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever

```

you can see, veth914db4f is not connected to br0. let's try hard

- run image (explicitly) as bridge network: `docker run --network bridge -it --rm -p 127.0.0.1:8000:4000 php-test-server` (this is nothing happen)
- force connect: `docker network connect bridge 2cf520235e6a` (this is show Error response from daemon: endpoint with name mystifying_yonath already exists in network bridge, but `ip a` says vethxxxx is not master to anyone). you can try `disconnect` & `connect` again

also

```
docker inspect -f '{{json .NetworkSettings.Networks}}' 2cf520235e6a | jq
{
  "bridge": {
    "IPAMConfig": null,
    "Links": null,
    "Aliases": null,
    "MacAddress": "5a:2d:5d:7c:c1:86",
    "DriverOpts": null,
    "GwPriority": 0,
    "NetworkID": "08f151565c95ba052f682c7560e55199e2d75f3d2348af8f98a9711e9294b3fd",
    "EndpointID": "0522c15ad18fbae05071a7d5e09944b7777deaafd3490082cac237fdfcd14f0c",
    "Gateway": "172.17.0.1",
    "IPAddress": "172.17.0.2",
    "IPPrefixLen": 16,
    "IPv6Gateway": "",
    "GlobalIPv6Address": "",
    "GlobalIPv6PrefixLen": 0,
    "DNSNames": null
  }
}

```

the medicine: [https://forums.docker.com/t/no-connection-to-the-bridge-by-default/134619/8](https://forums.docker.com/t/no-connection-to-the-bridge-by-default/134619/8)

```
sudo systemctl stop systemd-networkd.service                                                    
sudo systemctl disable systemd-networkd.service                                                        
sudo systemctl stop systemd-networkd.socket                                                            
sudo systemctl disable systemd-networkd.socket
sudo systemctl start NetworkManager
sudo systemctl enable NetworkManager
```