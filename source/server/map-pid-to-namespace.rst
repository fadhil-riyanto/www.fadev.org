Map PID to namespace
====================

this script doing map pid to namespace

example, I doing ``unshare -r --net bash``, and get the pid via ``echo $$``. now I want map this pid into namespace
that be executed using ``ip link set <IFACE> netns <HERE_OUR_NS>``

.. code-block:: bash

        jump_mk_netns() {
                mkdir -p /var/run/netns
        }

        map_pid2ns() {
                pid=$1
                nsname=$2

                ln -s /proc/$pid/ns/net /var/run/netns/$nsname
        }

        echo "mapping $1 into $2"

        if [[ -d "/var/run/netns" ]]; then
                echo "netns detected"
                map_pid2ns $1 $2
        else
                jump_mk_netns
                map_pid2ns $1 $2
        fi
