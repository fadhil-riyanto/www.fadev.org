# stdio_init_all() analysis

first, lets debug this with real hardware & openocd

do not forget to add breakpoint in this func
![image](../_images/d79a009da96a33c92b6b2ab63c28ed1181c1737c08fc3a9c81e1a8307687ceea6cf4823ebfccb102464099ec2aca35f2ba6c030577ac2097826aa79f.png)

the sequence of execution:

- `/home/fadhil_riyanto/git_clone/pico-sdk/src/rp2_common/pico_stdio/stdio.c:200` -> stdio_init_all()
- `/home/fadhil_riyanto/git_clone/pico-sdk/src/rp2_common/pico_stdio_uart/stdio_uart.c:37` -> stdio_uart_init()
- `/home/fadhil_riyanto/git_clone/pico-sdk/src/rp2_common/pico_stdio_uart/stdio_uart.c:93` -> stdio_uart_init_full()
- `/home/fadhil_riyanto/git_clone/pico-sdk/src/rp2_common/hardware_gpio/gpio.c:38` -> gpio_set_function()
- `/home/fadhil_riyanto/git_clone/pico-sdk/src/rp2_common/hardware_uart/uart.c:42` -> uart_init()

WIP (SOON)