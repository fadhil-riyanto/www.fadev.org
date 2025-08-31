.. _nftables_tables:

nftables tables
===============

.. rubric:: Quick Reference

- **ip**: For IPv4 packet filtering.
- **arp**: To handle ARP resolution.
- **ip6**: For IPv6 packet filtering.
- **bridge**: To handle packets passing through a bridged device.
- **inet**: Allows applying rules for both IPv4 and IPv6 simultaneously.
- **netdev**: Used for ingress packet handling.



    ``Chains``
    ------

.. container:: type

Types
------

- **filter**: Applicable to ``arp``, ``bridge``, ``ip``, ``ip6``, and ``inet`` families.
- **route**: Applicable to ``ip`` and ``ip6`` families.
- **nat**: Applicable to ``ip`` and ``ip6`` families.

.. container:: list_tables

Listing Tables
--------------

The command ``nft list tables [<family>]`` is used to list tables, where ``<family>`` is optional.

.. code-block:: sh

root@integral2:~# nft list tables ip
table ip nat
table ip filter
table ip raw