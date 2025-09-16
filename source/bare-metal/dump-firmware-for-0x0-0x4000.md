# dump firmware for from 0x0 ~ 0x4000

this is how you can dump first 16Kbytes

based on this docs, its feel intresting look inside about rom

![image](../_images/36fa643113ee83bacaed05afdcf1f991a3abb9babc8dda99ff8c29a0022aab2dc2b1a5a2d99db2363b4b1f0fc99a2ec4136dae53c41e814030e60f0d.png)

let's dump it

# openocd

this tutorial uses secondary pico, which connected with other pico's

```
openocd -f interface/cmsis-dap.cfg -f target/rp2040.cfg -c "adapter speed 5000"
```

after it

```
telnet localhost 4444
> halt
> dump_image pico_first_16kb_bootloader.bin 0x0 0x4000
```

show the binary

```sh
arm-none-eabi-objdump -D -b binary -marm -Mforce-thumb ./pico_first_16kb_bootloader.bin
```

![image](../_images/66f6af036ba7e606bba4caebe6e3a9f80a0acfbf57678feead6f9ae2744ff4c15c9746f9c917780fd3206d00c207dd30a221170fce83c5ef4c55616f.png)

# another way

let's use GDB stuff, first download [this](https://github.com/raspberrypi/pico-bootrom-rp2040/releases/tag/b2), run as regular gdb debug mode + openocd. then dump

![image](../_images/e0eaca53bc870194ce824091d84157932092e68ce61d038635d8119634ddc73948f567954b535c53cadef2c690779326140113b4e2a16632ffdf21a8.png)

here the intresting part

![image](../_images/f96682752a323620a2e45aded89bdde392df227a03e62d2239247a515b19cba2a7ed8af1557562455ff2eef5d015f22d1043f823a7de6c3eb0a49d64.png)

which part of [https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_rt0.S#L48](https://github.com/raspberrypi/pico-bootrom-rp2040/blob/ef22cd8ede5bc007f81d7f2416b48db90f313434/bootrom/bootrom_rt0.S#L48)