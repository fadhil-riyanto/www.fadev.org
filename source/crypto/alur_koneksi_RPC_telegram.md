# Alur konek ke RPC server telegram

step ini dibuat oleh seseorang dari masa lalu sekitar tahun 2020 yang akunnya telah terhapus, credit kepada Butthx

`originals written in telegram chat, but because I want to preserve it. I write it here

## step 1:

Bikin koneksi ke server telegram pakai TCP yang tersedia (disini gwa pakai TCPIntermediate)

## step 2:
Bikin random nonce dengan value int128

## step 3:
Kirim bytes dari ReqPqMulti dengan value bytes dari nonce tadi. 

## step 4: 
pick salah satu dari beberapa publick fingerprints yang diberikan dari results step3.

## step 5: 
Lakuin faktor bilangan pq yang diberikan dari results step3, dapetin lagi hasil pembagian dari pq tadi dengan hasil faktor, terus urutkan dari yang terkecil. untuk yang kecil di kasih nama p dan yang besar kasih nama g.

## step 6:

bikin nonce baru (jangan ubah nonce yang lama) dengan value random int256.

## step 7:
bikin hash (sha1) dari bytes PQInnerData ke telegram: bytes[pq,bytes p,bytes q,nonce,nonce baru,server nonce (dapet dari step3)]

## step 8:
bikin padding dengan random bytes dengan panjang -(length bytes PQInnerData + length sha1) mod 255

## step 9:
encrypt bytes[sha,bytes PQInnerData,padding] dengan RSA (pakai publik fingerprints tadi)

## step 10:
kirim bytes ReqDhParams: bytes[nonce,server nonce, bytes p, bytes q, encrypted data (step9) ,fingerprint] 

## step 11:
bikin temporary aes key: bytes[sha1[bytes nonce baru, bytes server nonce],sha1[bytes server nonce, bytes nonce baru] slice 0 – 12]

## step 12: 
bikin temporary aes initial vector (IV): bytes[sha1[bytes server nonce, bytes nonce baru] slice 12 – end, sha1[bytes nonce baru,bytes nonce baru], bytes[nonce baru] slice 0 – 4 ]  

## step 13:
decrypt encryptedAnswer (dapet dari step 10) menggunakan AES-256-IGE pakai key sama iv tadi. 

## step 14: 
parse decrypted answer tadi ke TLSchema/TLObject 

## step 15:
bikin random int(panjang 256 bytes, bukan int256 ygy) kita beri nama b

## step 16:
dapetin g_b dengan (g ** b) mod dh_prime
* g, dh_prime → dapet dari step 14

## step 17: 
bikin hash sha1 dari bytes[ClientDhInnerData[nonce, server nonce, 0,unsigned big bytes g_b length 256]]

## step 18:
bikin padding dengan length -(length bytes ClientDhInnerData + length sha1) mod 16

## step 19: 
encrypt bytes[bytes step 17,bytes ClientDhInnerData, padding ] dengan AES-256-IGE, key sama iv masih menggunakan yang step 11.

## step 20: 

kirim bytes[SetClientDhParams[nonce, server nonce, bytes step 19]]

## step 21: 
Bikin auth key dengan big-unsigned-bytes[big-u-int(g_a) ** b mod dhPrime] length 256

## step 22: 
Lakuin security check..

notes: 
Untuk format pengiriman bytes:

```
bytes[sessionId,messageId,length content,content]
karena belum ada authkey, jadi sessionId  = Buffer.alloc(8)
```

untuk dapetin real data dari telegram, slice bytes yang di terima dari 20 – end

pengiriman content selalu bentuk bytes, jadi semua parameter jadiin bytes :)


```ts
/**
 * tgsnake - Telegram MTProto framework for nodejs.
 * Copyright (C) 2022 butthx <https://github.com/butthx>
 *
 * THIS FILE IS PART OF TGSNAKE
 *
 * tgsnake is a free software : you can redistribute it and/or modify
 * it under the terms of the MIT License as published.
 */

export const DCTest = {
  1: '149.154.175.10',
  2: '149.154.167.40',
  3: '149.154.175.117',
};
export const DCProd = {
  1: '149.154.175.53',
  2: '149.154.167.51',
  3: '149.154.175.100',
  4: '149.154.167.91',
  5: '91.108.56.130',
};
export const DCProdMedia = {
  2: '149.154.167.151',
  4: '149.154.164.250',
};
export const DCTestIPV6 = {
  1: '2001:b28:f23d:f001::e',
  2: '2001:67c:4e8:f002::e',
  3: '2001:b28:f23d:f003::e',
};
export const DCProdIPV6 = {
  1: '2001:b28:f23d:f001::a',
  2: '2001:67c:4e8:f002::a',
  3: '2001:b28:f23d:f003::a',
  4: '2001:67c:4e8:f004::a',
  5: '2001:b28:f23f:f005::a',
};
export const DCProdMediaIPV6 = {
  2: '2001:067c:04e8:f002:0000:0000:0000:000b',
  4: '2001:067c:04e8:f004:0000:0000:0000:000b',
};
export function DataCenter(
  dcId: number,
  testMode: boolean,
  ipv6: boolean,
  media: boolean
): [ip: string, port: number] {
  if (testMode) {
    return [ipv6 ? DCTestIPV6[dcId] : DCTest[dcId], 80];
  } else {
    if (media) {
      return [ipv6 ? DCProdMediaIPV6[dcId] : DCProdMedia[dcId], 443];
    } else {
      return [ipv6 ? DCProdIPV6[dcId] : DCProd[dcId], 443];
    }
  }
}

``` 