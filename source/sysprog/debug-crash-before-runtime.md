# debug crash before runtime

thanks for [https://stackoverflow.com/questions/7808769/how-to-debug-a-crash-before-main/30142423#30142423](https://stackoverflow.com/questions/7808769/how-to-debug-a-crash-before-main/30142423#30142423)

let's break a thing!

![image](../_images/fd3bfc138cf34d4a6315e82866496a62f210c5225282f276ff83d047a7a8258a0e32f4b60eedfaccead95d0231e8d824232ccb3258405f009c6c7662.png)

this is normal program, the `_start` is on 0x10000000, let break it 

![image](../_images/fc8cfdc88625223f15646b6a434679b74cf897357b8f22277ce34485ab153c6cc6fff6312d93e38c055ae80ae050befcbed886dc918495fa51564083.png)

as you can see, its start from 0x0, let run it
![image](../_images/25ddfac225ad3c18aef56108bd78764e13db657688988492e197a1ad5dda6c9b6d0b171fc2aca6b2a91fb4028de8959a509b0d3d3ab856c85921f083.png)

notes: the hey is previos attempt. nvm, now how debug it

# run as usual GDB

![image](../_images/7f97a9c81ae053c0929ec6a9e5215388f3352ffcc18e8ef3f909472a5f9dff523019ffe433448227902744ba4bef1b94d9499ef7a20acb781e547cbe.png)

here the entrypoint is 0x0