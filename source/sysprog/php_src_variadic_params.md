# PHP-SRC variadic params

the source code: [https://github.com/php/php-src/blob/ba6c00505d4218ff9fe4feb060f636524acfb125/ext/standard/array.c#L1204](https://github.com/php/php-src/blob/ba6c00505d4218ff9fe4feb060f636524acfb125/ext/standard/array.c#L1204)

mayan ngebantu jg gw ngepahami variadic params di php. 
ref: [https://www.zend.com/resources/php-extensions/basic-php-structures](https://www.zend.com/resources/php-extensions/basic-php-structures)


selfnote :

ZEND_PARSE_PARAMETERS_START(num_required_args, num_max_args)
Z_PARAM_VARIADIC('*' or '+', destptr, argc);

catatan: 
- \* nol atau lebih parameter
- \+ satu atau lebih parameter   

nb: akan diupdate berkala

ref: https://wiki.php.net/rfc/fast_zpp