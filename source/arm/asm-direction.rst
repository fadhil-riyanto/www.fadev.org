ASM gnu-as direction collection
===============================


.equ
-----
this is equalivalent of ``#define FOO 6`` in c
example: 

.. code-block:: text

	.equ LED_PIN,      25
	.equ GPIO_DIR_IN,  0
	.equ GPIO_DIR_OUT, 1
	.equ PIN_HIGH,     1
	.equ PIN_LOW,      0

https://sourceware.org/binutils/docs-2.24/as/Equ.html#Equ


.syntax
-------

https://sourceware.org/binutils/docs/as.html#Instruction-Set-Syntax
https://www.sourceware.org/binutils/docs/as/ARM-Directives.html#index-_002esyntax-directive_002c-ARM


this is either `unified` or `divided`
