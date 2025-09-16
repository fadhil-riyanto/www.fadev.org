# Tealinux qemu promp & testing

## create image
`qemu-img create -f qcow2 <NAME>.img 45G`

- Change 45G with your desired size

## running system on BIOS mode

this will open SSH connection on port 20022

## live
```sh
qemu-system-x86_64 \
                -enable-kvm \
                -boot order=d \
                -cdrom tealinux-2025.02.16-x86_64.iso \
                -drive file=tealinux.img,format=qcow2 \
                -m 4G \
                -enable-kvm \
                -smp 4 \
                -net user,hostfwd=tcp::20022-:22 \
                -net nic
```

## non-live
```sh
qemu-system-x86_64 \
                -enable-kvm \
                -boot order=d \
                -drive file=tealinux.img,format=qcow2 \
                -m 4G \
                -enable-kvm \
                -smp 4 \
                -net user,hostfwd=tcp::20022-:22 \
                -net nic
```

## running on UEFI mode
in order to running qemu on UEFI mode, we need [edk2-ovmf](https://archlinux.org/packages/extra/any/edk2-ovmf/)

get your ovmf vars by running `cp /usr/share/edk2/x64/OVMF_VARS.4m.fd .`

## live
```sh
qemu-system-x86_64 \
                -enable-kvm \
                -cdrom tealinux-2025.02.16-x86_64.iso \
                -boot order=d \
                -drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
                -drive if=pflash,format=raw,file=OVMF_VARS.4m.fd \
                -drive file=tealinux.img,format=qcow2 \
                -m 4G \
                -enable-kvm \
                -smp 4 \
                -net user,hostfwd=tcp::20022-:22 \
                -net nic
```

## non-live
```sh
qemu-system-x86_64 \
                -enable-kvm \
                -boot order=d \
                -drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
                -drive if=pflash,format=raw,file=OVMF_VARS.4m.fd \
                -drive file=tealinux.img,format=qcow2 \
                -m 4G \
                -enable-kvm \
                -smp 4 \
                -net user,hostfwd=tcp::20022-:22 \
                -net nic
```

## windows
```sh
qemu-system-x86_64 \
                -enable-kvm \
                -boot order=d \
                -cdrom Win10_22H2_English_x64v1.iso \
                -drive file=windows-tealinux-mbr.img,format=qcow2 \
                -m 4G \
                -enable-kvm \
                -smp 4 \
                -net user,hostfwd=tcp::20022-:22 \
                -net nic
```

uefi version
```sh
qemu-system-x86_64 \
                 -enable-kvm \
                 -boot order=d \
                 -cdrom Win10_22H2_English_x64v1.iso \
                 -drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
                 -drive if=pflash,format=raw,file=OVMF_VARS.4m.fd \
                 -drive file=tealinux.img,format=qcow2 \
                 -m 4G \
                 -enable-kvm \
                 -smp 4 \
                 -net user,hostfwd=tcp::20022-:22
```

note: bug unwrap error
```sh
qemu-system-x86_64 \
                      -enable-kvm \
                      -boot order=d \
                      -cdrom tealinux-2025.02.16-x86_64.iso \
      -drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
                      -drive if=pflash,format=raw,file=OVMF_VARS.4m.fd \
                      -drive file=tealinux.img,format=qcow2 \
                      -m 4G \
                      -enable-kvm \
                      -smp 4 \
                      -net user,hostfwd=tcp::20022-:22 \
      -net nic
```


## misc
### add more drive
in order add more drive, use this param
- `-drive file=img1.img,format=qcow2`
- `-drive file=img1.img,format=qcow2`

## forward more port
imagine you need to forward another port, not only ssh, the correct command is
`-net user,hostfwd=tcp::10022-:22,hostfwd=tcp::8080-:8080,hostfwd=tcp::5173-:5173`

5173 is our port.