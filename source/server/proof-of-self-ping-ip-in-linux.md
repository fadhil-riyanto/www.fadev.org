# proof of Self-Ping ip in Linux

## proof 1
this clearly say that `lo` interface is down, and I try to ping my own IP. but failed. after turn on `lo` interface, the ping get normal
![image](../_images/f81ecae8808ec672c324ce9c2d186b09febb8dee40ab2276b9ef4dde6a7714e88dc30a8ed2fdf41bc1215ffe32781c94c9631b1ece1bc7af27d4d11b.png)

## proof 2

clearly that TCPDUMP didnt record anything on `enp2s0` interface
![image](../_images/36819adf86139a32939f98150eccb9aff9b061b10a2bcafb6aa7f590a3e796b35ca02f81d5bd6f938a3864d9a2381af878046608eb6ca1d8bdcd5b34.png)

meanwhile
![image](../_images/b1a09f4cee0e080e0a49e78459b1510585e17ddfaa55d73a2ee16919eede47d9aa04a65e557fe4b80d757d622bb53f86dd9e631a49f7c964fc932889.png)

proof, that packet for x ip, where the x is our own machine IP, is not routed through NIC, it just pass over `lo` interface even there has no correlation about 127.0.0.1 and 10.0.0.254, the packet still reach `lo`