# Setup shadowsocks proxy server

shadowsocks-libev is available in the official repository for Debian 9("Stretch"), unstable, Ubuntu 16.10 and later derivatives:

```sh
sudo apt update
sudo apt install shadowsocks-libev
```

then, create a file config on `/etc/shadowsocks-libev/config.json` which has contents something like this

```json
{
    "server":["::1", "10.1.1.4"],
    "mode":"tcp_and_udp",
    "server_port":8388,
    "local_port":1080,
    "password":"1u21wW3E0bwu",
    "timeout":86400,
    "method":"chacha20-ietf-poly1305"
}

```

in this case, I use `10.1.1.4` as local ip, then forwarded through firewall to the public addr.

then, `sudo systemctl start shadowsocks-libev`

ref: [https://shadowsocks.org/doc/configs.html](https://shadowsocks.org/doc/configs.html)

# connect