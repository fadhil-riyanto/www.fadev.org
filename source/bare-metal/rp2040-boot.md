# RP2040 boot

first, lets look at this docs

![image](../_images/998ec4b763d9f5425da4db21da99228af9adbd259ec40252256c75100747460e8fb538967e28a5a64fdf51c8e0a606de7f6e4bcdcaabc362584b8d02.png)

I'll prove this

- 1st, please look at this cmake, they says `bootrom_rt0.S`, which is [https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/CMakeLists.txt#L39](https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/CMakeLists.txt#L39)
- 2nd, the contents
![image](../_images/805816ee1020531480c86e19163bbbc0425bbf9a0d26b0e181a6366be635690b2892c35657469fb8336baae679588ed7029b55155fa9a9d40fb92ba2.png)

# the strange header

in `bootrom_rt0.S` contains a strange header like this


```c
#include "hardware/regs/addressmap.h"
#include "hardware/regs/pads_bank0.h"
#include "hardware/regs/resets.h"
#include "hardware/regs/sio.h"
#include "hardware/regs/watchdog.h"
#include "hardware/regs/syscfg.h"
#include "hardware/regs/clocks.h"
#include "hardware/regs/vreg_and_chip_reset.h"
#include "hardware/regs/m0plus.h"
#include "git_info.h"
```

warn:
this is just my speculation, the real location is in [https://github.com/raspberrypi/pico-sdk/tree/master/src/rp2040/hardware_regs/include/hardware/regs](https://github.com/raspberrypi/pico-sdk/tree/master/src/rp2040/hardware_regs/include/hardware/regs), but the theory IDK. i just matching the file

please inform me if you find something intresting in [https://github.com/raspberrypi/pico-sdk/blob/master/src/CMakeLists.txt](https://github.com/raspberrypi/pico-sdk/blob/master/src/CMakeLists.txt)

# boot sequence 
this is the most important stuff

- 1st, please look at this cmake, they says `bootrom_rt0.S`, which is [https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/CMakeLists.txt#L39](https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/CMakeLists.txt#L39)
- 2nd, the `bootrom_rt0.S`, this is important [https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_rt0.S#L40-L43](https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_rt0.S#L40-L43)
- 3st, `bootrom_rt0.S` jump into `main()`, [https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_rt0.S#L303](https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_rt0.S#L303)
- the boot `main()` Cmake, [https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/CMakeLists.txt#L41](https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/CMakeLists.txt#L41)
- `main()` func, [https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L226](https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L226)
- busy loop with ring-oscillator? [https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L246](https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L246)

![image](../_images/4f86ceb28ebef18c2f5b021c5bae32803869435991eaf6b2da4ecd70a73c0ff96fd7781040dce01ced5a086a4ab298bcdc0a255d52287b01f648e41a.png)
- jump into `_flash_boot()`, [https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L251](https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L251)
- crc32 checking, [https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L75-L77](https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L75-L77)
- intresting stuff, this is calculating the time taken? [https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L67-L72](https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L67-L72)
- execute boot2 stage: [https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L95](https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L95)
- [this](https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L90) variable hold pointer into boot2 stage location, which is `boot2_load`
- `boot2_load` [https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L44](https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L44)
- boot2 offset calculation, [https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L41](https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L41)
- this [define](https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_main.c#L41) need a triage, because `SRAM_END` is 0x20042000, which at end of static ram. is really boot2 stage is lives before the sram ended?

# boot2 

- `runtime_init` ?, in [crt0.S](https://github.com/raspberrypi/pico-sdk/blob/a1438dff1d38bd9c65dbd693f0e5db4b9ae91779/src/rp2_common/pico_crt0/crt0.S#L572C1-L572C13), like what [https://vanhunteradams.com/Pico/Bootloader/Boot_sequence.html](https://vanhunteradams.com/Pico/Bootloader/Boot_sequence.html) mention?

![image](../_images/9b97cd61d49ec79790a82a11ded40e61c8cf8563ccbf0d274bb2176aaac35c85d38ac9dbd1647a35f8f093a6a6ab81cb52d1b2182fea40662cdf7d5e.png)

first, we look at this file [memmap_default.ld](https://github.com/raspberrypi/pico-sdk/blob/master/src/rp2_common/pico_crt0/rp2040/memmap_default.ld)
- here, we know that, they call `pico_flash_region.ld`, which located on [src/rp2_common/pico_standard_link/pico_flash_region.template.ld](https://github.com/raspberrypi/pico-sdk/blob/master/src/rp2_common/pico_standard_link/pico_flash_region.template.ld)
- the cmake then convert `pico_flash_region.template.ld` into `pico_flash_region.ld` using [cmake](https://github.com/raspberrypi/pico-sdk/blob/a1438dff1d38bd9c65dbd693f0e5db4b9ae91779/src/rp2_common/pico_standard_link/CMakeLists.txt#L126)

[this](https://github.com/raspberrypi/pico-sdk/blob/a1438dff1d38bd9c65dbd693f0e5db4b9ae91779/src/rp2_common/pico_standard_link/CMakeLists.txt#L118-L120) code idk what its used for, also where the variable coming-off

# boot2 revision

this is the actual boot2 is located

- [https://github.com/raspberrypi/pico-sdk/tree/master/src/rp2040/boot_stage2](https://github.com/raspberrypi/pico-sdk/tree/master/src/rp2040/boot_stage2)
- inside will have many files, all of them is bootloader, but with different hardware. in my case I USE w25q080, THIS is how I know it
![image](../_images/5eedcea5cb67eae04f32366d829efa9fbad1cb8b6fe52e7eec210003cbb998fc084083b06469d2b1fc6229f9d77afabb866f9500e1b13656b5c4569a.png)

note: how I find it? its manually set program counter register to `0x20041f00`, from somewhere after ctrl + c is fired. we cant stop at 0x20041f00 because at that time. the second boot rom is not loaded yet.

another way, if you was find your "flash hardware driver", let's add breakpoint here, example

![image](../_images/069068d82549fc4332de501c92827479dfeea3a393c5afa696a4ac844891a0c8f748413299b255f15216ff762d0b6b98fc7add71b8489f3ff0d15597.png)

this will stop execution without hassle of hardware breakpoint, or watching program counter value.


if you curious how I find magic number `0x20041f00`, please look at this file

![image](../_images/46adc7e59b008bc7a45332671f809d57e5d4b49b4afa81e81290b15afa9d62e12d4eec9f04c0285ce10ef0a275da439bd401f7a55037e05379242080.png)

# linker script
there has various linker scripts

- [boot_stage2](https://github.com/raspberrypi/pico-sdk/blob/master/src/rp2040/boot_stage2/boot_stage2.ld)
- [memmap_default.ld](https://github.com/raspberrypi/pico-sdk/blob/master/src/rp2_common/pico_crt0/rp2040/memmap_default.ld)
- [pico_flash_region](https://github.com/raspberrypi/pico-sdk/blob/master/src/rp2_common/pico_standard_link/pico_flash_region.template.ld), this is included on `memmap_default.ld`


if we merge both `memmap_default.ld` and `pico_flash_region.ld`, we will got this

```c
MEMORY
{
    FLASH(rx) : ORIGIN = 0x10000000, LENGTH = ${PICO_FLASH_SIZE_BYTES_STRING}
    RAM(rwx) : ORIGIN =  0x20000000, LENGTH = 256k
    SCRATCH_X(rwx) : ORIGIN = 0x20040000, LENGTH = 4k
    SCRATCH_Y(rwx) : ORIGIN = 0x20041000, LENGTH = 4k
}
```

see missing part? yes, that is `PICO_FLASH_SIZE_BYTES_STRING`, lets find out in our *.elf.map 


![image](../_images/1cd8416a8065c0f0be4d8ccb319c644d5d2ec1f2b6ecfec3ecfb3c24c921238a1da5662379c6fd9eaa0c10d8f39166634c646b5b1caf491465ccc922.png)

![image](../_images/823238e7e864c31772fe710047ad3355085924b1d49f46723a18fd60a5494a90466d8991ecd3cfcc9a990d7bf44a8979e37f409a0408498ef71c54ad.png)

that is 2048K

# Issue that I find
I think `arm-none-eabi-objdump` is mistaken arm-thumb-1 instruction as full 32 bit arm, so they just say `.word 0xdeadbeef`