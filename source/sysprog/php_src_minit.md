# PHP-SRC minit()

[https://github.com/php/php-src/blob/3704947696fe0ee93e025fa85621d297ac7a1e4d/main/main.c#L2009](https://github.com/php/php-src/blob/3704947696fe0ee93e025fa85621d297ac7a1e4d/main/main.c#L2009)

Ketika module PHP diload ke zend engine, yang dipanggil adalah MINIT(), di step ini yg terjadi cuman memory alokasi di ZendMM, dan disini engga ada process atau thread yg dijalan, pure cuman initialisasi data

nah, yang mentrigger MINIT() adalah zend_startup_modules(), trus secara beurutan, ia jg manggil RINIT() via PHP_RINIT_FUNCTION()

struct nya
![image](../_images/71ee438d7728f41eb71942cc4e8b9693efcc03aa4ffd227e6c035b6aa383863ef79c48eb122af41f7ef3ec4eb4623a48560272461dc5ba20f83fd296.png) zend_result (*request_startup_func)(INIT_FUNC_ARGS);