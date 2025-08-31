Calling a main function
=======================

Di sini, saya akan memperlihatkan *kenapa* fungsi `init` di RP2040 bisa bernama `main`, dan bagaimana langkah-langkahnya.

Pertama-tama, saya mencoba mem-flash kode asm yang isinya hanya *jump* dan *exit*, seperti yang terlihat di bawah:

.. image:: ../_images/b2b3b96f8c0cddf06860d7198a04f2b9d127da925dc91d703e6f4b610ab2a5805be30372eb52d29c7490587856eff9352f31f60cb6ca70eeb9174e51.png

Lalu saya jalankan, terlihat saya memberi breakpoint di `main`, bukan?

.. image:: ../_images/1f9c9b01546d4faf7b1e805a045ca222500ed9f23f096963a302cb0260060c4eabc0b0a1d24476885d3e478fbb33b37d470a6b542f113150299fb519.png

Sebenarnya sudah benar bagian berikut:

.. code-block:: c

   (gdb) disass
   Dump of assembler code for function main:
   => 0x100002a8 <+0>:	b.n	0x100002aa <jump_here>

Selanjutnya, *jump* ke `jump_here`:

.. code-block::

   (gdb) disass
   Dump of assembler code for function jump_here:
   => 0x100002aa <+0>:	movs	r0, #0
      0x100002ac <+2>:	bx	lr
      0x100002ae <+4>:	movs	r0, r0
   End of assembler dump.

Terlihat sudah sampai di `movs r0, #0`, sama seperti assembly kita di atas, tapi ada beberapa hal yang aneh (*need triage*).

Tiba-tiba muncul:

.. code-block:: c

   movs	r0, r0

Jika kita lihat juga, setelah *jump* `jump_here` dieksekusi, ia pindah ke:

   /home/fadhil_riyanto/git_clone/pico-sdk/src/rp2_common/pico_crt0/crt0.S:456

Akhirnya, tidak sengaja menemukan asm yang memanggil si `main`:

.. image:: ../_images/e4d2f43598a6ede1d6e849fc30035b2df58a45619053524684b8563112890debca482cce96d66ec1d13c9e9140bb9665dd180d8c4b98c298f5df7c08.png