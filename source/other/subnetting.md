# Subnetting

pertama tama, range ip dahulu

- A: 1 - 127
- B: 128 - 191
- C: 192 - AKHIR

- `0b00000000` -> 0 (katakanlah octet ke 4, cidr 24)
- `0b10000000` -> 0 (cidr 25, 128 hosts)							// 2 network
- `0b11000000` -> 0 (cidr 26, 128 + 64)								// 4 network
- `0b11100000` -> 0 (cidr 27, 128 + 64 + 32)						// 8 network
- `0b11110000` -> 0 (cidr 28, 128 + 64 + 32 + 16)					// 16 network
- `0b11111000` -> 0 (cidr 29, 128 + 64 + 32 + 16 + 8)				// 32 network
- `0b11111100` -> 0 (cidr 30, 128 + 64 + 32 + 16 + 8 + 4)			// 64 network
- `0b11111110` -> 0 (cidr 31, 128 + 64 + 32 + 16 + 8 + 4 + 2)		// 128 network
- `0b11111111` -> 0 (cidr 32, 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1)	// 256 network

seperti yg terlihat, bahwa `128 + 64 + 32 + 16 + 8 + 4 + 2 + 1` = `255`

## contoh 192.168.10.0/24:
ada network 192.168.10.0/24, kita ingin bagi jadi 4 jaringan. maka 256 / 4 = 64 hosts, dan ini akan

- subnet nya: 255.255.255.192
- 64 hosts: 64 hosts usable, 1 untuk broadcast, 1 untuk network

pembagian nya
- network 1:  192.168.10.0, broadcast: 192.168.10.63, range ip yang usable: 192.168.10.1 - 192.168.10.62
- network 2:  192.168.10.64, broadcast: 192.168.10.127, range ip yang usable: 192.168.10.65 - 192.168.10.126
- network 3:  192.168.10.128, broadcast: 192.168.10.191, range ip yang usable: 192.168.10.129 - 192.168.10.190
- network 4:  192.168.10.192, broadcast: 192.168.10.255, range ip yang usable: 192.168.10.193 - 192.168.10.254

## oprekan hitung2 an:

origin: pakai acuan ip kelas c

jumlah hosts, misal cidr 24, itu max nya 256 kalau 0b11111111, kenapa 0b10000000 itu 128, dan kenapa 0b11000000 itu 192

ok, lalu kenapa jika cidr /26, itu 255.255.255.192, punya 64 hosts, 4 network. semua ini didapat dari
(max int case ini 8 bit) / maxint - pad network

ini start dari /24

- `0b00000000` -> 0 (katakanlah octet ke 4, cidr 24)				// 1 network
- `0b10000000` -> 0 (cidr 25, 128 hosts)							// 2 network
- `0b11000000` -> 0 (cidr 26, 128 + 64)								// 4 network
- `0b11100000` -> 0 (cidr 27, 128 + 64 + 32)						// 8 network
- `0b11110000` -> 0 (cidr 28, 128 + 64 + 32 + 16)					// 16 network
- `0b11111000` -> 0 (cidr 29, 128 + 64 + 32 + 16 + 8)				// 32 network
- `0b11111100` -> 0 (cidr 30, 128 + 64 + 32 + 16 + 8 + 4)			// 64 network
- `0b11111110` -> 0 (cidr 31, 128 + 64 + 32 + 16 + 8 + 4 + 2)		// 128 network
- `0b11111111` -> 0 (cidr 32, 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1)	// 256 network


start dari /16
- `0b0000000000000000` -> 0 (cidr 16, 65535)								// 1 net, 65535 hosts
- `0b1000000000000000` -> 0 (cidr 17, 65535 + )							// 2 net, 32767 hosts
- `0b1100000000000000` -> 0 (cidr 26, 128 + 64)								// 4 net
- `0b1110000000000000` -> 0 (cidr 27, 128 + 64 + 32)						// 8 net
- `0b1111000000000000` -> 0 (cidr 28, 128 + 64 + 32 + 16)					// 16 net
- `0b1111100000000000` -> 0 (cidr 29, 128 + 64 + 32 + 16 + 8)				// 32 net
- `0b1111110000000000` -> 0 (cidr 30, 128 + 64 + 32 + 16 + 8 + 4)			// 64 net
- `0b1111111000000000` -> 0 (cidr 31, 128 + 64 + 32 + 16 + 8 + 4 + 2)		// 128 net
- `0b1111111100000000` -> 0 (cidr 32, 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1)	// 256 net


-- stagging (perhitungan ip cidr 16 keatas)
max int 16 bit: 65536
- /16 : `0b0000000000000000` = 0
- /17 : `0b1000000000000000` = 32768, maka 65536 / 32768 = 2, alias 2 network, 32768 hosts
- /18 : `0b1100000000000000` = 49152, maka 65536 / (65536 - 49152)  = 4 network, 16384 hosts,
- /19 : `0b1110000000000000` = 57344, maka 65536 / (65536 - 57344)  = 8 network, 8192 hosts,
- /20 : `0b1111000000000000` = 61440, maka 65536 / (65536 - 61440)  = 16 network, 4096 hosts,
- /21 : `0b1111100000000000` = 61440, maka 65536 / (65536 - 61440)  = 32 network, 2048 hosts,
- /22 : `0b1111110000000000` = 64512, maka 65536 / (65536 - 64512)  = 64 network, 1024 hosts,
- /23 : `0b1111111000000000` = 64512, maka 65536 / (65536 - 64512)  = 128 network, 512 hosts,
- /24 : `0b1111111100000000` = 64512, maka 65536 / (65536 - 64512)  = 256 network, 256 hosts,


-- stagging cidr 8 keatas
max int int 24 bit: 16777216
- /9 : `0b100000000000000000000000` = 16777216 / (16777216 - 8388608) = 2 network, 8388608 hosts
- /10: `0b110000000000000000000000` = 16777216 / (16777216 - 12582912)= 4 network, 4194304 hosts
- /11: `0b111000000000000000000000` = 16777216 / (16777216 - 14680064)= 8 network, 2097152 hosts
- /12: `0b111100000000000000000000` = 16777216 / (16777216 - 15728640)= 16 network, 1048576 hosts
- /13: `0b111110000000000000000000` = 16777216 / (16777216 - 16252928)= 32 network, 524288 hosts
- /14: `0b111111000000000000000000` = 16777216 / (16777216 - 16515072) = 64 network, 262144 hosts
- /15: `0b111111100000000000000000` = 16777216 / (16777216 - 16646144) = 128 network, 131072 hosts
- /16: `0b111111110000000000000000` = 16777216 / (16777216 - 16711680) = 256 network, 65536 hosts
- /17: `0b111111111000000000000000` = 16777216 / (16777216 - 16744448) = 512 network, 32768 hosts
- /18: `0b111111111100000000000000` = 16777216 / (16777216 - 16760832) = 1024 network, 16384 hosts
- /19: `0b111111111110000000000000` = 16777216 / (16777216 - 16769024) = 2048 network, 8192 hosts
- /20: `0b111111111111000000000000` = 16777216 / (16777216 - 16773120) = 4096 network, 4096 hosts
- /21: `0b111111111111100000000000` = 16777216 / (16777216 - 16775168) = 8192 network, 2048 hosts

- /9 : 0b100000000000000000000000: 

# kumpulan rumus rumus
## subnet
rumusnya: \\( 2^{jumlah \space angka \space 1 \space di \space setiap \space padding \space subnet}\\)
### contoh
- prefix /19, pad terdekatnya /16, maka dari 16 ke 19 ada 3 angka 1 (`0b11100000`), maka jumlah subnet yang akan terbentuk adalah 2^3 = 8 subnet
- prefix /26, pad terdekatnya 24, maka dari 24 ke 26 ada 2 angka 1 (`0b11000000`), maka jumlah subnetnya 2^2 = 4

## jumlah hosts
rumusnya: \\( 2^{jumlah \space angka \space 0 \space dari \space 32} \\)
### contoh
- prefix /19, 32 - 19 = 13 angka 0, maka \\( 2^{13} = 8192 \space hosts \\)
- prefix /26, 32 - 26 = 6 angka 0, maka \\( 2^{6} = 64 \space hosts \\)
- prefix /8, 32 - 8 = 24 angka 0, maka \\( 2^{24} = 16777216 \space hosts \\)

