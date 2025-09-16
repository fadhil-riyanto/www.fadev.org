# sshfs

the setup is very easy

- in your home, run `mkdir mount`
- `mkdir vm_001_ubuntu` or whatever
- mount it `sshfs root@127.0.0.1:/ -p 20022 ./vm_001_ubuntu`
- verify with `findmnt`

enjoy