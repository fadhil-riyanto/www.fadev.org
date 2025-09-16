# load effective address

 computes a memory address using the same arithmetic that a MOV instruction uses. But unlike the MOV instruction, the LEA instruction just stores the computed address in its target register, instead of loading the contents of that address and storing it.

Consider your first LEA instruction:

tldr nya: mov bisa mengkalkulasi operasi aritmetika dari alamat memori, trus ngambil isinya
kalau lea, ia cuman mengkalkulasi alamatnya, hasil itung2an nya disimpan ke operand2

```asm
lea -0x18(%ebp), %ebx
```

tambahan catatan

mov (op1, op2, op3), dest

equal (pseudo):
mov op1 + op2 * op3, dest

and
lea op1(op2), dest

equal
lea op2 + op1, dest (address of op2 + op1, store result into dest)

bahasan tentang rip
[https://stackoverflow.com/questions/54745872/how-do-rip-relative-variable-references-like-rip-a-in-x86-64-gas-intel-sy](https://stackoverflow.com/questions/54745872/how-do-rip-relative-variable-references-like-rip-a-in-x86-64-gas-intel-sy)