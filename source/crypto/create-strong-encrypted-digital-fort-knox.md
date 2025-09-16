# create strong encrypted digital fort knox

This is my setup for external HDD's

# formatting

```sh
sudo cryptsetup luksFormat --type luks2 \
        --cipher aes-xts-plain64 \
        --key-size 512 \
        --hash sha512 \
        --pbkdf argon2id \
        --pbkdf-memory 4194304 \
        --pbkdf-parallel 8 \
        --pbkdf-force-iterations 8 \
        /dev/sdb
```

this will 
- encrypt every sector with aes-xts-plain64
- the master key itself encrypted with argon2id
- in order open it, you need 4 GB ram, and 100% cpu for about 8 seconds, this make bruteforce impossible

# creating FS


mount it
```sh
sudo mount -o compress=zstd:15 /dev/mapper/hiddendisk /home/fadhil_riyanto/mount/hiddendisk/
```

format
```sh
sudo mkfs.btrfs /dev/mapper/hiddendisk
```

# adding more keys

```sh
sudo cryptsetup luksAddKey \
        --pbkdf argon2id \
        --pbkdf-memory 4194304 \
        --pbkdf-parallel 8 \
        --pbkdf-force-iterations 8 \
        /dev/sdb
```

# see current metadata
```sh
sudo cryptsetup luksDump /dev/sdb
```