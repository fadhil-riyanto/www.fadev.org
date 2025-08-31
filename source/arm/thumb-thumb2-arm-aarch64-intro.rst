Thumb, Thumb-2, ARM, AArch64 introduction
=========================================

Thumb
-----

Apa itu thumb instruction?

Mengutip dari dokumentasi https://developer.arm.com/documentation/ddi0210/c/CACBCAAE:

	The Thumb instruction set is a subset of the most commonly used 32-bit ARM instructions. Thumb instructions are each 16 bits long, and have a corresponding 32-bit ARM instruction that has the same effect on the processor model. Thumb instructions operate with the standard ARM register configuration, allowing excellent interoperability between ARM and Thumb states.

	On execution, 16-bit Thumb instructions are transparently decompressed to full 32-bit ARM instructions in real time, without performance loss.

	Thumb has all the advantages of a 32-bit core:
		- 32-bit address space
		- 32-bit registers
		- 32-bit shifter, and Arithmetic Logic Unit (ALU)
		- 32-bit memory transfer.

Tambahan: Thumb juga disebut A32/T32.

Thumb ISA adalah versi lite dari full ARM instruction, tapi di-encode ke versi kecil, 16 bit format, dimana format ini tidak akan menghabiskan banyak space program.

Tapi ada caveat di sini, processor tidak mengeksekusi 16 bit instruction langsung, tapi ia mendekompresi-nya dahulu, baru masuk stage final execution.

Dan juga, kata "transparent" yang berarti ARM-nya hanya mengeksekusi standard 32 bit instruction, kita sebagai programmer tidak perlu bingung & mengurus conversion antara 16 bit ke 32 bit. Ini murni "fitur hw".

```
"...in real time, without performance loss."
```
Itu berarti, instruction-nya dijalankan secara langsung, dari 16 bit instruction diinterpretkan sebagai instruksi 32 bit (tanpa ada loss performance).

	16-bit, halfword-aligned Thumb instructions are executed in this state.

Contoh:

- ARM7TDMI:
	- https://developer.arm.com/documentation/ka001209/latest/
	- https://www.linkedin.com/pulse/why-arm7-called-tdmi-shanmukhapriya-g-2pgmc/

thumb-2
-------

Sama seperti thumb 1, hanya saja ia bisa memuat either 32 bit, atau 16 bit instruction.

ARM
---

Normal instruksi ARM yang berjalan di Android, selayaknya normal CPU.

AArch64
-------

Versi 64 bit dari ARM, yang biasanya dipakai di Raspberry Pi 5, server, dsb.

Biasa disebut ARMv8-A.

ARMv6-M
-------

ARM ini support thumb 1 ISA, dan merupakan versi paling lite dari ARM, bisa dibaca di https://www.st.com/content/st_com/en/arm-32-bit-microcontrollers/arm-cortex-m0.html#:~:text=Arm%C2%AE%2032%2Dbit%20Microcontrollers,Arm%20Cortex%2DM3