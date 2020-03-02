import os
os.system('sudo ovs-vsctl add-br ovs-br1')
os.system('sudo ovs-vsctl set bridge ovs-br1 fail_mode=secure')
os.system('sudo ifconfig ovs-br1 173.16.1.1 netmask 255.255.255.0 up')
os.system('sudo ovs-vsctl set Bridge ovs-br1 protocols=OpenFlow13')
os.system('sudo ovs-vsctl set-controller ovs-br1 tcp:127.0.0.1:6653')
os.system('sudo ovs-ofctl show -O OpenFlow13 ovs-br1')
