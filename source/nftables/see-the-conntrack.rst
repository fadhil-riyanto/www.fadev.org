See the connection track (conntrack)
====================================

today, I doing intresting stuff. I setup veth with configuration like this

pc1: 10.0.80.2 (10.0.80.0/24)
pc2: 10.0.200.2 (10.0.200.0/24)

and the router, that has 3 interface
veth_pc1: 10.0.80.1
veth_pc2: 10.0.200.1
veth_router: 10.0.0.2

and, the veth_router is connected to my machine via 10.0.0.1, here iptables

.. code-block:: bash

        sudo iptables -A FORWARD -i veth_host -o enp2s0 -j ACCEPT
        sudo iptables -A FORWARD -i enp2s0 -o veth_host -m state --state ESTABLISHED,RELATED -j ACCEPT
        iptables -t nat -A POSTROUTING -s 10.0.0.0/24 -o enp2s0 -j MASQUERADE
        sudo sysctl -w net.ipv4.ip_forward=1

and, here the conntrack

run ``sudo conntrack -E``

.. image:: ../_images/260f2c009e472ba1cab895d9b931e9ba552167f092bebbe6b32cdb3323403ac37dc5f27b67b2657b5ae62c9b419f0b8cc843b3d6863bc152dddaea41.png

example 1
---------

lets open a dummy connection to 1.1.1.1

.. image:: ../_images/c9efa0f8e1893ecbdd575725a2dfaad40423b4fba6909a958223ad06691a3b776e3bba986f5ef151787ea4e2e257d75ed5277fe7d12fe39b7d54fbb5.png

then watch the conntrack

.. image:: ../_images/58073d340e77907b1a1f360983d629ce7b12c1087f34a2d7ce11bb3e0905ea63bbc74adbe635782a86a05303c4f02a9e864763a35f1a4c7859d36840.png
