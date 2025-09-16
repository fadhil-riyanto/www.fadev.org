# logic netfilter linux kernel

# Logic NAT
misalkan kita ada virtual interface br0, dengan anggotanya tap0, tap1 lalu ingin forward semua traffic ke wlan0 (karna memang wlan0 tidak bisa di jadikan master dari x y z)

maka solusinya iptables

```sh
sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
```

logic nya
- fill dulu tabel nat
- append ke postrouting, jadi setelah packet di routing oleh linux kernel, ada 2 field, source addr (katakanlah ip tap0) lalu destination addr (misal 8.8.8.8)
- nah, semisal tidak di apa apakan, packet sent ke 8.8.8.8, tapi 8.8.8.8 tidak bisa mengirim back packetnya karna source addr nya invalid (di stage ini, source ip nya adalah IP LAN)
- maka, setelah linux kernel meng-routingkan packet nya, seketika setelah itu (postrouting), kita ganti source addrnya dengan source ip PUBLIK milik firewall, jadi 8.8.8.8 bisa tahu kemana packet harus dikirim kembali
- didalam firewall, packet yang tadi diterima, direverse balik oleh nat, dan dikirim balik ke perangkat aslinya.
- pakai MASQUERADE


# logic forward data dari br0 ke wlan
```sh
sudo iptables -A FORWARD -i br0 -o wlan0 -j ACCEPT
```
important notes:

- chain FORWARD: This chain is only used for packets that are not destined for the local machine, but are routed through it (i.e., from one interface to another).
- In this case: a device connected to br0 (e.g., a VM or container) wants to access the internet via wlan0.

analoginya

```
[Device 192.168.100.2] ──> [br0 (Linux bridge)] ──> Linux router ──> [wlan0] ──> Internet
```

bisa juga -j diganti drop, maka aliran data akan terputus

# logic forward dari wlan0 ke br0 (sebaliknya)

```sh
sudo iptables -A FORWARD -i wlan0 -o br0 -m state --state RELATED,ESTABLISHED -j ACCEPT
```

logic:

- misal vm tap0 buat koneksi keluar, misal ke 8.8.8.8
- dari tap0 -> br0 -> wlan0 di allow oleh rule `sudo iptables -A FORWARD -i br0 -o wlan0 -j ACCEPT`
- ketika server mengirim respon balik, maka alurnya dari wlan0 ke br0, nah ini fungsi dari `sudo iptables -A FORWARD -i wlan0 -o br0 -j ACCEPT`

KENAPA harus pakai `--state RELATED,ESTABLISHED`
karna kita butuh packet yg sudah estab duluan yg boleh lewat. ini akan menghindari jaringan luar (wlan0) mengakses br0 -> tap0 & tap1