# Tealinux qemu promp & testing 2

## Windows 10 section
this section show various command that windows related
### running on GPT
- live 
```bash
# clone uefi vars
cp /usr/share/edk2/x64/OVMF_VARS.4m.fd .
mv OVMF_VARS.4m.fd OVMF_VARS_windows_gpt.4m.fd

# create image
qemu-img create -f qcow2 windows_10_gpt_no_fb.img 50G

# run iso
qemu-system-x86_64 \
	-enable-kvm \
	-cdrom Win10_22H2_English_x64v1.iso \
	-drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
	-drive if=pflash,format=raw,file=OVMF_VARS_windows_gpt.4m.fd \
	-drive file=windows_10_gpt_no_fb.img,format=qcow2 \
	-m 4G \
	-smp 4

```

- non live 
```bash
# run iso
qemu-system-x86_64 \
	-enable-kvm \
	-drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
	-drive if=pflash,format=raw,file=OVMF_VARS.4m.fd \
	-drive file=windows_10_gpt_no_fb.img,format=qcow2 \
	-m 4G \
	-smp 4

```

notes:
run with vga
- `-vga virtio`

### running tealinux (alongside windows)

```bash
qemu-system-x86_64 \
	-enable-kvm \
	-cdrom tealinux-2025.02.16-x86_64.iso \
	-drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
	-drive if=pflash,format=raw,file=OVMF_VARS_windows_gpt.4m.fd \
	-drive file=windows_10_gpt_no_fb.img,format=qcow2 \
	-m 4G \
	-smp 4
```