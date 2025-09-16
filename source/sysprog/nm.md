# nm

nm is a abbr of name, in linux. this tool is used to inspect binary section 

example
![image](../_images/4f3419224cc1bad6fb206703e4368ae14a707baf08bc1fb4d503fd727561ea7bff2d03d064a8870cdc6151d9d159198af2ba464c916a1a8604f81056.png)


```txt
> nm libcall.o
0000000000000000 T lib_call
0000000000000000 b lib_call.im_counting
```

capital letter mean, the `symbol is exported`