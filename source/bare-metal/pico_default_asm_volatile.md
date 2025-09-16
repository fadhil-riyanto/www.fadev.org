# pico_default_asm_volatile

after a long time, I discover this macro from this screenshoot

![image](../_images/fe28d3decea5adad85287258acbfe1798633ddb0a31f160672716fc61632ab2866b9c0a853b77973296555b2e411342cee912b0cbc9a990ecacbed37.png)

and I found it

[https://github.com/raspberrypi/pico-sdk/blob/9a4113fbbae65ee82d8cd6537963bc3d3b14bcca/src/rp2_common/pico_platform_compiler/include/pico/platform/compiler.h#L149-L159](https://github.com/raspberrypi/pico-sdk/blob/9a4113fbbae65ee82d8cd6537963bc3d3b14bcca/src/rp2_common/pico_platform_compiler/include/pico/platform/compiler.h#L149-L159)


```c
#define pico_default_asm_volatile(...) __asm volatile (".syntax unified\n" __VA_ARGS__)
```
and the explanation why use `__VA_ARGS__`: [https://gcc.gnu.org/onlinedocs/cpp/Variadic-Macros.html](https://gcc.gnu.org/onlinedocs/cpp/Variadic-Macros.html)

here the example

![image](../_images/3f10433700ab0dbc062496ebf165befd3f1f55a283d912a7efcc09bf8dc6329ae0812cc1e0acb3e5b3a0fc39f3399bd794c66054ff1f919c3df6e703.png)

![image](../_images/7e4c168002be67f1892819134d389599878fa6ba856daa874fdb6273681b437fea071e16dbc52e877969d5efad3eff65283ab0337d9a054bb703e65b.png)