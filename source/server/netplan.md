# Linux netplan

ref: [https://documentation.ubuntu.com/server/explanation/networking/configuring-networks/](https://documentation.ubuntu.com/server/explanation/networking/configuring-networks/)

example

```yaml
network:
  version: 2
  ethernets:
    ens3:
      dhcp4: true
    ens4:
      addresses:
        - 192.168.1.2/24
      routes:
        - to: default
          via: 192.168.1.1
```

location: `/etc/netplan`
note: execution is ordered by file name

then run `sudo netplan generate`