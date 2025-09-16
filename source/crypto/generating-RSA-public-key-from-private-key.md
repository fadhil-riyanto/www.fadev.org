# generating RSA public key from private key

- [https://docs.openssl.org/3.2/man1/openssl-format-options/#format-options](https://docs.openssl.org/3.2/man1/openssl-format-options/#format-options)
- [https://knowledge.digicert.com/general-information/openssl-quick-reference-guide](https://knowledge.digicert.com/general-information/openssl-quick-reference-guide)
- [https://developers.yubico.com/PIV/Guides/Generating_keys_using_OpenSSL.html](https://developers.yubico.com/PIV/Guides/Generating_keys_using_OpenSSL.html)

## generating private key

```
openssl genrsa -out private.key 8192
```

this command will generate private key with length 

let's extract public key from newly generated private key

```
openssl rsa -pubout -in ./private.key -outform PEM -out public.key

# or, whatever

openssl rsa -outform PEM -in ./private.key -pubout -out public.pem
```

## 