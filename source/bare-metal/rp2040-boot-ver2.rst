RP2040 BOOT version 2
=====================

this series is some sorts of completion of :doc:`rp2040-boot`


This below is the sequence how RP2040 chip is actually boot, until we hit main function. 
The Bootrom size is limited to 16kB. It contains

- Processor core 0 initial boot sequence
- Processor core 1 low power wait and launch protocol
- USB MSC class-compliant bootloader with UF2 support for downloading code/data to FLASH or RAM
- USB PICOBOOT bootloader interface for advanced management

nvm, let's take how rp2040 is boot.

lab setup
---------
let's download the bootrom binary code first

.. code:: sh

        wget https://github.com/raspberrypi/pico-bootrom-rp2040/releases/download/b2/b2.elf

why I should download the ``b2.elf`` first? because the bootrom code iself is "baked" into silicon metal, and unlike
the normal program that we can flash custom code, the bootrom is fixed. this is the reason
why we need a .elf, because we want do something with binary in the chip, and the elf itself is
just a "map" for us.

before all happens, let's find your RP2040 SWD to USB device driver, im on ``/dev/ttyACM0``

.. image:: ../_images/45ba5414192b149b290998c6ec15a55e544812d31556a41980e80a9578fe68908ecc9ec6ea6fa264237086403606cf7aae5275e065fd7fa87092a8c2.png

firing our openocd (the debugger)

.. image:: ../_images/6289648549e53b6f30bc665dbe6f9341729fcd934a230e9e6b39ece7c7b541dbc1af39d466a807036692d8366e29020f8d430e0cec94afa1884dd3b3.png

step 1
------
load your b2.elf into gdb 

.. image:: ../_images/67574b4eea6e7f45870bb39f3c03b95179af65e0a5c6794436fd5ca2b81d82e9f06e7bc98312871d808c14323a38178e6299ae97258470b1c483e532.png

after it, let's analyze the source code 

- https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/CMakeLists.txt#L39, this confirm us that ``bootrom/bootrom_rt0.S``
  is used. let's check it

step 2
------
verifying if "that is actually" the bootloader, by dumping its assembly and compare it with real source code

here real source code

.. image:: ../_images/12b9df884f28e71a271b1250596846dd86f775ea4ac38aa3a35cb7163c9c2a362369d1eaadd98467e947e29a86618ff5db281941c2f1b09267f5dee6.png

step 3
------
walk through bootloader 

.. image:: ../_images/933aed4660462380a906654c8935736a9b42c74adac09ab3bdd3fd150101434e8678065c8174c4f6842e87c4db0d6b26d3fe2cd7e02596b9b687a66e.png

how I can find 0xea offsets? this is very simple.

.. code-block:: 

  pwndbg> monitor reset init
  target halted due to debug-request, current mode: Thread 
  xPSR: 0xf1000000 pc: 0x000000ea msp: 0x20041f00
  target halted due to debug-request, current mode: Thread 
  xPSR: 0xf1000000 pc: 0x000000ea msp: 0x20041f00

note:

xPSR is a x program status register, contains
  - Application Program Status Register
  - Interrupt Program Status Register
  - Execution Program Status Register
  

I will cover this later, but let's see the ``pc``, it show us that 0xea is next instruction, let's add
hardware breakpoint here. 

.. image:: ../_images/81d2b8dfb452a39ecf16801fe36893280adec35d499656dc867b3b3d285fdcf034a79e7ebaed0b53fa4ff89fc2971d25350f38e311350279def82987.png

step 4
------
processor controlled boot sequence, here how rp2040 is boot

walk 0
^^^^^^
Reset to both processors released: both enter ROM at same location

walk 1
^^^^^^
Processors check SIO.CPUID
here the link: https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_rt0.S#L233

because the SIO register is word-aligned and started from address 0xd0000000, so let's deep dive in this

.. image:: ../_images/440b9c254fa6ae9f72bd70c9325923bf545b82ffb00dd0a3c04b1a996c6253278dc6b01fe44d7c726b8366df976084919035aa9f3cddb0fd1bc9923a.png

after it, this asm code is launched by both processor, TL;DR. if core0, go ahead, if core1 go to sleep.

.. code-block::

    check_core:
        // NOTE: We DO NOT use any stack prior to possible watchdog entry (this includes NMI vector handler)
        ldr r0, =SIO_BASE
        ldr r1, [r0, #SIO_CPUID_OFFSET]
        cmp r1, #0

this code show us that 
- load 0xd0000000 into r0 
- then, compute r0 + CPUDID_OFFSET, which 

.. image:: ../_images/9639c29c765354ab14585ac8fb4c16351cfc4bd8aaf171d724a178ec26c582ec4a273507c2b6edf91f7a362296d7021b594b96d1b4e900fff7b031b3.png

- then, store the result into r1 
    
.. note::

  because the docs itself say "Value is 0 when read from processor core 0, and 1 when read from processor core 1.", so we need to check if r1 is equal with 0. we do this with ``cmp r1, #0``

other cond, when its not a core0, jump to :ref:`here <wait_for_vector>` 

.. _wait_for_vector:


https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_rt0.S#L329

walk 2
^^^^^^
If power up event was from Rescue DP, clear this flag and halt immediately

I think this code do best job: https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_rt0.S#L248-L260