nftables block ping
===================

this is very first my nftables configuration that

- block ping from other machine
- allow me to ping-ing other machine 
- allow ping 127.0.0.1 

this script uses default chain, and jump stuff. here what I learn

.. code-block:: 

        flush ruleset

        # allow icmp out, block incoming
        table ip filter {
                chain input {
                        type filter hook input priority 0; policy accept;
                        jump icmp_input
                }

                chain output {
                        type filter hook output priority 0; policy accept;
                        jump icmp_output
                        return
                }

                chain icmp_input {
                        ip daddr 127.0.0.1 icmp type echo-request accept;
                        
                        icmp type echo-request drop;
                        icmp type echo-reply accept;
                        return
                }

                chain icmp_output {
                        icmp type echo-request accept;
                        return
                }
        }

