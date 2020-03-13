import os
os.system('sudo wget https://raw.githubusercontent.com/openvswitch/ovs/master/utilities/ovs-docker')
os.system('sudo chmod a+rwx ovs-docker')
os.system('sudo ovs-vsctl show')
os.system('sudo ovs-vsctl add-br ovs-br1 -- set bridge ovs-br1 protocols=OpenFlow13')
os.system('ifconfig')
os.system('sudo ifconfig ovs-br1 173.16.1.1 netmask 255.255.255.0 up')
os.system('sudo ovs-vsctl set bridge ovs-br1 fail_mode=secure')
os.system('sudo ovs-vsctl set-controller ovs-br1 tcp:127.0.0.1:6653')
os.system('sudo ovs-ofctl show -O OpenFlow13 ovs-br1')
print("DONE")
#sudo docker run -it --name box1 ubuntu:16.04 /bin/sh
#sudo docker run -it --name box2 ubuntu:16.04 /bin/sh

## Install ping and ifconfig using
'''
apt-get update
apt-get install iputils-ping
apt-get install net-tools
'''

## Modify faucet.yaml file using:
'''
vi etc/faucet/faucet.yaml
vlans:
    lab:
        vid: 100
        description: "lab network"
        unicast_flood: True       
dps:                       
    Open vSwitch:
        dp_id: 0x000012579719c04a
        hardware: "Open vSwitch" 
        interfaces:             
            1:     
                name: "h1"
                description: "host1 container"
                native_vlan: lab              
            2:                  
                name: "h2"
                description: "host2 container"
                native_vlan: lab
                acls_in: [block-ping]           
            3:                  
                name: "Poseidon"
                description: "Mirrors Traffic of port 2 to Poseidon"
                native_vlan: lab
acls:
    block-ping:
        - rule:
            dl_type: 0x800      # IPv4
            ip_proto: 1         # ICMP
            actions:
                allow: False
        - rule:
            dl_type: 0x86dd     # IPv6
            ip_proto: 58        # ICMPv6
            actions:
                allow: False


'''
#sudo docker run -it --name faucetctl --network=host faucet/faucet /bin/bash
os.system('sudo ovs-docker add-port ovs-br1 eth0 box1 --ipaddress=173.16.1.2/24')
os.system('sudo ovs-docker add-port ovs-br1 eth0 box2 --ipaddress=173.16.1.3/24')

print("BRIDGES CREATED")
