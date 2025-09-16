# printf format specifier

general

```
%[flags][width][.precision][length]specifier
```

## flag 

| Flag      | Description                                                  |
| :-------- | :----------------------------------------------------------- |
| `-`       | **Left-justify**: The result is left-aligned within the specified field width. By default, it is right-aligned. |
| `+`       | **Sign**: The result of a signed conversion will always begin with a sign (`+` or `-`). By default, only negative values have a sign. |
| ` ` (space) | **Space**: If the first character of a signed conversion is not a sign, a space is prepended. This is ignored if the `+` flag is present. |
| `#`       | **Alternate Form**: For `o`, the output is prefixed with `0`. For `x` and `X`, it's prefixed with `0x` and `0X` respectively. For `a`, `A`, `e`, `E`, `f`, `F`, `g`, and `G`, the output will always contain a decimal point. |
| `0`       | **Zero-padding**: For numeric types, the output is padded with leading zeros instead of spaces to fill the field width. This is ignored if the `-` flag is present. |

## width

The width sub-specifier sets the minimum number of characters to be printed.

| Width     | Description                                                  |
| :-------- | :----------------------------------------------------------- |
| `number`  | A non-negative integer specifying the minimum number of characters to print. If the printed value is shorter, it is padded with spaces (or zeros if the `0` flag is used). |
| `*`       | The width is not specified in the format string itself, but as an additional integer argument preceding the argument to be formatted. |


## precision

| Precision   | Description                                                  |
| :---------- | :----------------------------------------------------------- |
| `.number`   | For integer specifiers (`d`, `i`, `u`, `o`, `x`, `X`), it specifies the minimum number of digits to be written. For `e`, `E`, and `f`, it is the number of digits to appear after the decimal point. For `g` and `G`, it's the maximum number of significant digits. For `s`, it's the maximum number of characters to be printed. |
| `.*`        | The precision is not specified in the format string itself, but as an additional integer argument preceding the argument to be formatted. |


## length

| Modifier | For Integer Specifiers (`d`, `i`, `u`, `o`, `x`, `X`) | For Floating-Point Specifiers (`f`, `e`, `g`, `a`) |
| :------- | :-------------------------------------------------- | :----------------------------------------------- |
| `h`      | `short int` or `unsigned short int`                 | -                                                |
| `hh`     | `signed char` or `unsigned char`                    | -                                                |
| `l`      | `long int` or `unsigned long int`                   | -                                                |
| `ll`     | `long long int` or `unsigned long long int`         | -                                                |
| `L`      | -                                                   | `long double`                                    |
| `j`      | `intmax_t` or `uintmax_t`                           | -                                                |
| `z`      | `size_t` or the corresponding signed type           | -                                                |
| `t`      | `ptrdiff_t` or the corresponding unsigned type      | -                                                |

## specifier


| Specifier | Data Type                               | Output Format                                                 |
| :-------- | :-------------------------------------- | :------------------------------------------------------------ |
| `%c`      | `char`                                  | A single character.                                           |
| `%s`      | `char*`                                 | A string of characters.                                       |
| `%d` or `%i` | `int`                                   | Signed decimal integer.                                       |
| `%u`      | `unsigned int`                          | Unsigned decimal integer.                                     |
| `%o`      | `unsigned int`                          | Unsigned octal integer.                                       |
| `%x`      | `unsigned int`                          | Unsigned hexadecimal integer (lowercase letters).             |
| `%X`      | `unsigned int`                          | Unsigned hexadecimal integer (uppercase letters).             |
| `%f`      | `double`                                | Decimal floating-point number.                                |
| `%F`      | `double`                                | Decimal floating-point number (uppercase 'INF' and 'NAN').    |
| `%e`      | `double`                                | Scientific notation (lowercase 'e').                          |
| `%E`      | `double`                                | Scientific notation (uppercase 'E').                          |
| `%g`      | `double`                                | Uses the shorter of `%f` or `%e`.                             |
| `%G`      | `double`                                | Uses the shorter of `%F` or `%E`.                             |
| `%a`      | `double`                                | Hexadecimal floating-point number (lowercase 'p').            |
| `%A`      | `double`                                | Hexadecimal floating-point number (uppercase 'P').            |
| `%p`      | `void*`                                 | Pointer address.                                              |
| `%n`      | `int*`                                  | The number of characters written so far is stored in the integer pointed to by the argument. Nothing is printed. |
| `%%`      | *None* | A literal '%' character is printed.                           |

