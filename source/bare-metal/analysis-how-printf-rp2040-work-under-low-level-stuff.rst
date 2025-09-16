Analysis: How printf Works on RP2040 at a Low Level
===================================================

In order to understand how ``printf`` works in the RP2040 UART bridge, let's compile a simple program, build it with debug symbols, and then run GDB.

Consider this very simple Hello World example:

.. code-block:: c

        #include <pico/printf.h>
        #include <pico/time.h>

        int main() {
                int n = 0;
                stdio_init_all();
                while (true) {
                        printf("Hello, world! %d\n", n);
                        sleep_ms(1000);
                        n = n + 1;
                }
        }

Analysis
--------

.. image:: ../_images/c9a172f5c6ce190e648f88df4af894d4d115b23d2128cad758833395f62d3f5e5d2ef9cb3dc4d695806f538fa26510bf6bc0da2b995b7fceeaff4899.png

See?

.. code-block:: c

        => 0x100002b4 <+12>:    bl      0x10003a64 <__wrap_printf>

It calls ``__wrap_printf``, which means the backend uses ``-Wl,--wrap=printf`` internally. If we refer to ``/home/fadhil_riyanto/git_clone/pico-sdk/src/rp2_common/pico_stdio/stdio.c:347``:

.. image:: ../_images/44f66f5c4e0c51a2c0b4bc3885079beb5de306725363b91ba2a38898bf59d0e76fe467ec3abf98eb4881aaf0ce408cf5ebd19b28747ef3720bb99107.png

The signature is different. This function has the signature:

.. code-block:: c

        int __printflike(1, 0) PRIMARY_STDIO_FUNC(printf)(const char* format, ...)

So, what exactly happens?

Result
------

Let's look at ``stdio.c`` line 289:

.. image:: ../_images/a00ffec057742b32cb76c8db0d3da75c299ceba49a218edf9d559fb31eb9ae029da9b798e2d255ca0af5754dcd7ac62929645ad3aa63155c62bf61a8.png

When the macro ``PICO_STDIO_SHORT_CIRCUIT_CLIB_FUNCS`` is active, we replace the function name by ``WRAPPER_FUNC(x)``, not ``stdio_printf``.

After that, let's jump into the `pico-sdk compiler.h <https://github.com/raspberrypi/pico-sdk/blob/9a4113fbbae65ee82d8cd6537963bc3d3b14bcca/src/rp2_common/pico_platform_compiler/include/pico/platform/compiler.h#L185>`_ for a very clear definition.

So, basically, this function:

.. image:: ../_images/b0dbbe24380b5411221dbffcf2cb8409180135d704b9ede610a1e8f3e032a9ce6071551b9c2628a7d85fec6dcb88aa3f8b529d15999cdf75570fdab8.png

calls ``__wrap_printf``.

Make sense?
