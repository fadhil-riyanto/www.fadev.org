# GDB attach

jadi ceritanya, ada bug yg kala di run di terminal, ia buggy, pas di run di gdb, dia gak error sama sekali

gw bingung dah, nah disini. ternyata ada trick nya

- jalanin dulu programnya kek biasa di terminal, dah running kan
- ambil pid nya pakai ps aux | grep xyz

- setelah dapet pid nya, jalankan gdb dengan mode attach pid

pakai `sudo gdb -p 12345`

- program akan freeze sejenak, pencet `c`, `enter`

nah, lakukan cara yg dipake buat reproduce bug nya, misal pakai nc buat nyepam tcp ke program. ok dapet bug nya

ni kalau kata orang internet, beberapa bug kek app multi thread agak susah di caught. pakai valgrind pun perlu flags2 khusus buat inspect sampai thread nya