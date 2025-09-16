# hasil oprek socket programming, case socks5 server

bagian IETF SOCKS5 section 6

[https://datatracker.ietf.org/doc/html/rfc1928#section-6](https://datatracker.ietf.org/doc/html/rfc1928#section-6)

BND.ADDR haruslah berupa IPV4/IPV6 address, bukan domain :)

secara general, bentuk packet yg akan dikirim untuk versi IPV4 seperti ini

```
[0] [VER] => 0x5
[1] [REP] => 0x0
[2] [RSV] => 0x0
[3] [ATYP] => 0x1 atau 0x4
[4] [BND.ADDR] 0xac
[5] [BND.ADDR] 0x43
[6] [BND.ADDR] 0x93
[7] [BND.ADDR] 0x39
[8] [BND.PORT] 0x50 
[9] [BND.PORT] 0x50
```

maka perhitungannya memory awal + 4 (karna 4 field dah dipakai), start dari sini, insert 4 oktet lagi ipv4 address, lalu insert 2 oktet uint8 sebagai port. 

bagian BND.PORT itu unsigned int 16 bit. jadi harus digabung bitnya + diubah dari network order ke host order