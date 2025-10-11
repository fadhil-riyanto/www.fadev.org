# analisis patch movq pakai 0xffffffff

ada asm

![image](../_images/396baa16bda2bcebbef7d1403edf680c8f5c58d1e5d13e396d9187a7e106a69d95b21a892095d794cf8d80e03fba5ee8faa3d61e3eab21d78d2fb9b1.png)

kita akan memaksa dari 0x7fffffff menjadi 0xffffffff untuk membuktikan bahwa harusnya movq error, dan digantikan oleh movabsq

initial dulu
![image](../_images/46453cea0bda238960726005cf23bc143f51ffe55f0b632fec36ca3b4846d7dee3ad43e7ab4841b29e64d1a9344ee30bbb3ea46e8812f2b3f9f64a24.png)

lalu, next replace address 0x555555555119 dengan 
```
set {unsigned char[8]}0x555555555119 = {0x48, 0xc7, 0xc0, 0xff, 0xff, 0xff, 0xff, 0x90}
```

confirmed berubah jadi 0xffffffff disini
![image](../_images/183193f1ed20460acef3b46f25d34f4362c97d685aa27c440ecf464d0036cddab2a92fad306c6018a9911aa10b27b1ab130a443ca9c0edcbe6f61a68.png)

saatnya kita lanjutkan, apakah error
![image](../_images/c160ad95471ba78693869c17396b2ce78d2dd142abfb1232dfd08532438a3823f5746823e3061b802421b731067d432ee3dc7df6dd1980159bfd4d10.png)