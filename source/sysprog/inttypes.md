# I/O format of integer types

The following macros are defined in `inttypes.h`. Each expands to a character string literal containing a conversion specifier which can be modified by a length modifier that can be used in the format argument of a formatted input/output function when converting the corresponding integer type. These macros have the general form of PRI (character string literals for the `fprintf()` and `fwprintf()` family of functions) or SCN (character string literals for the fscanf() and fwscanf() family of functions), followed by the conversion specifier, followed by a name corresponding to a similar type name in `<inttypes.h>`. In these names, the suffix number represents the width of the type. For example, `PRIdFAST32` can be used in a format string to print the value of an integer of type `int_fast32_t`.

# Decimal notation

| PRId8       | PRId16        | PRId32        | PRId64        |
| :---------- | :------------ | :------------ | :------------ |
| PRIdLEAST8  | PRIdLEAST16   | PRIdLEAST32   | PRIdLEAST64   |
| PRIdFAST8   | PRIdFAST16    | PRIdFAST32    | PRIdFAST64    |
| PRIdMAX     |               |               |               |
| PRIdPTR     |               |               |               |
| PRIi8       | PRIi16        | PRIi32        | PRIi64        |
| PRIiLEAST8  | PRIiLEAST16   | PRIiLEAST32   | PRIiLEAST64   |
| PRIiFAST8   | PRIiFAST16    | PRIiFAST32    | PRIiFAST64    |
| PRIiMAX     |               |               |               |
| PRIiPTR     |               |               |               |

example:
```c
#define _ISOC99_SOURCE
#include <inttypes.h>      
#include <stdio.h> 
int main(void)                                             
{                                                          

int8_t i =  40; 
printf("Demonstrating the use of the following macros:\n");
printf("Using PRId8, the printed value of 40 "                  
"is  %" PRId8"\n", i);                                    
printf("Using PRIiFAST8, the printed value of 40 "               
"is  %" PRIiFAST8"\n", i);                                 
printf("Using PRIoLEAST8, the printed value of 40 "              
"is  %" PRIoLEAST8 "\n", i);                               
return 0;                                                  
}                          


Output:

Demonstrating the use of the following macros:  
Using PRId8, the printed value of 40 is  40     
Using PRIiFAST8, the printed value of 40 is  40 
Using PRIoLEAST8, the printed value of 40 is  50
```