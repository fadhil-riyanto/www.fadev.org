# Run router-OS on qemu

on normal interface
```sh
qemu-system-x86_64 \
          -enable-kvm \
          -boot order=d \
          -cdrom chr-6.49.18.img \
          -drive file=chr.qcow2,format=qcow2 \
          -m 4G \
          -smp 4 \
          -net user,hostfwd=tcp::10022-:22,hostfwd=tcp::8291-:8291 \
          -net nic
```