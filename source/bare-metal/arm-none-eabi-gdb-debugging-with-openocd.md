# arm-none-eabi-gdb debugging with openocd

the simplest thing to debug your RP2040 chip is using secondary pico as picoprobe, then running openocd.
I assume you're was ready with your pico debugprobe

# identify your TTY

check with `sudo dmesg`, the run a command like this `sudo chmod 666 /dev/ttyACM0`

# openocd
```sh
openocd -f interface/cmsis-dap.cfg -f target/rp2040.cfg -c "adapter speed 5000"
```

# cmake 
make sure your ELF was build with `cmake -DCMAKE_BUILD_TYPE=Debug -DPICO_BOARD=pico ..`

# flashing

```sh
openocd -f interface/cmsis-dap.cfg -f target/rp2040.cfg -c "adapter speed 5000" -c "program hello_usb.elf verify reset exit"
```
without sudo
