#!/bin/sh

# we need some Private Area Network ID
panid="0xbeef"
# number of nodes
numnodes=6

# include the kernel module for a fake node, tell it to create six
# nodes
modprobe fakelb numlbs=$numnodes

# initialize all the nodes
for i in $(seq 0 `expr $numnodes - 1`);
do
        ip netns delete wpan${i}
        ip netns add wpan${i}
        PHYNUM=`iwpan dev | grep -B 1 wpan${i} | sed -ne '1 s/phy#\([0-9]\)/\1/p'`
        iwpan phy${PHYNUM} set netns name wpan${i}

        ip netns exec wpan${i} iwpan dev wpan${i} set pan_id $panid
        ip netns exec wpan${i} ip link add link wpan${i} name lowpan${i} type lowpan
        ip netns exec wpan${i} ip link set wpan${i} up
        ip netns exec wpan${i} ip link set lowpan${i} up
done
