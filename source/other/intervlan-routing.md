# Inter-VLAN routing

how to config vlan inter-VLAN routing

topology:
- VNET1:192.168.10.0/24 (vlan 10)
- PC1: 192.168.10.2
- PC2: 192.168.10.3
- VNET2:192.168.20.0/24 (vlan 20)
- PC3: 192.168.20.2
- PC4: 192.168.20.3
- ROUTER IP (fa0/0.10): 192.168.10.1
- ROUTER IP (fa0/0.20): 192.168.20.1

# SCRIPTS
## management
### - `show vlan brief`: show all configured vlan

## setup vlan (tanpa setup ip dulu)
```sh
Switch>enable
Switch#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Switch(config)#vlan 10
Switch(config-vlan)#name SALES
Switch(config-vlan)#ex
Switch(config)#vlan 20
Switch(config-vlan)#name IT
```

## lalu setup mode
- trunk: untuk switch ke router
- access: untuk switch ke PC

setup untuk vlan 10 dan 10, masing2 dengan network 192.168.10.0/24 dan 192.168.20.0/24

script: 
```sh
Switch#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Switch(config)#int fa0/1
Switch(config-if)#switchport mode access
Switch(config-if)#switchport access vlan 10
Switch(config-if)#ex
Switch(config)#int fa0/2
Switch(config-if)#switchport mode access
Switch(config-if)#switchport access vlan 10
Switch(config-if)#ex
Switch(config)#int fa0/3
Switch(config-if)#switchport mode access
Switch(config-if)#switchport access vlan 20
Switch(config-if)#ex
Switch(config)#int fa0/4
Switch(config-if)#switchport mode access
Switch(config-if)#switchport access vlan 20
Switch(config-if)#ex
Switch(config)#
```

alternative script
```sh
Switch(config-if)#int range fa0/1-4
Switch(config-if-range)#switchport mode access
```
## config untuk port fa0/5 ke router (pakai mode trunk)
```sh
Switch(config)#int fa0/5
Switch(config-if)#switchport mode trunk
Switch(config-if)#
```


# inter-VLAN routing
## enable port Fa0/0 (tanpa assign ip dahulu)
```sh
Router(config)#int fa0/0
Router(config-if)#no shut

Router(config-if)#
%LINK-5-CHANGED: Interface FastEthernet0/0, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/0, changed state to up
```

## assign ip untuk masing2 vlan
```sh
Router(config)#interface FastEthernet0/0
Router(config-if)#int fa0/0.10
Router(config-subif)#
%LINK-5-CHANGED: Interface FastEthernet0/0.10, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/0.10, changed state to up

Router(config-subif)#encapsulation dot1q 10 
Router(config-subif)#ip add 192.168.10.1 255.255.255.0
Router(config-subif)#ex
Router(config)#int fa0/0.20
Router(config-subif)#
%LINK-5-CHANGED: Interface FastEthernet0/0.20, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/0.20, changed state to up

Router(config-subif)#encapsulation dot1q 20
Router(config-subif)#ip add 192.168.20.1 255.255.255.0
Router(config-subif)#
```


## hasil output `show vlan brief`
```sh
Switch>show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/6, Fa0/7, Fa0/8, Fa0/9
                                                Fa0/10, Fa0/11, Fa0/12, Fa0/13
                                                Fa0/14, Fa0/15, Fa0/16, Fa0/17
                                                Fa0/18, Fa0/19, Fa0/20, Fa0/21
                                                Fa0/22, Fa0/23, Fa0/24, Gig0/1
                                                Gig0/2
10   SALES                            active    Fa0/1, Fa0/2
20   IT                               active    Fa0/3, Fa0/4
1002 fddi-default                     active    
1003 token-ring-default               active    
1004 fddinet-default                  active    
1005 trnet-default                    active    
Switch>
```

## tambahan 
- encapsulation dot1q: router on stick routing


### Advanced switch cisco command