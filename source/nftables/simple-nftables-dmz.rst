Simple nftables DMZ
===================

I will show you, that

I have a router, which has interface

- veth_pc1 (think this a wan interface)
- veth_pc2 

I will allow pc2 to ping into pc1, and deny pc1 to pinging pc2.

nftables command
----------------

.. code-block:: 

        nft add table filter
        nft "add chain ip filter forward { type filter hook forward priority 0; policy drop; }"
        nft add rule ip filter forward iif veth_pc1 oif veth_pc2 ct state new drop
        nft add rule ip filter forward iif veth_pc2 oif veth_pc1 ct state new accept
        nft add rule ip filter forward ct state established,related accept


or more simply, 


.. code-block::

        table ip filter {
        	chain forward {
        		type filter hook forward priority filter; policy drop;
        		iif "veth_pc1" oif "veth_pc2" ct state new drop
        		iif "veth_pc2" oif "veth_pc1" ct state new accept
        		ct state established,related accept
        	}
        }


PS: I use my own setup, see :doc:`nftables-lab-setup`