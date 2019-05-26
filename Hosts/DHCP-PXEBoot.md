# Install DHCP Service
```sh
dnf install dhcp
systemctl enable dhcpd
firewall-cmd --add-service=dhcp --permanent
firewall-cmd --reload
```

## PXE Boot DHCP Config
- DCHP Host: 3.2.1.14
- Config: /etc/dhcp/dhcpd.conf
- Subnet: 3.2.1.0/24
- DHCP Range: 3.2.1.200-240
- TFTP: 3.2.1.17
- Filename: pxelinux.0

```sh
#
# DHCP Server Configuration file.
#   see /usr/share/doc/dhcp-server/dhcpd.conf.example
#   see dhcpd.conf(5) man page
#
allow booting; 
allow bootp; 
ddns-update-style interim; 
ignore client-updates; 
subnet 3.2.1.0 netmask 255.255.255.0 { 
    option subnet-mask 255.255.255.0; 
    option broadcast-address 3.2.1.255; 
    range dynamic-bootp 3.2.1.200 3.2.1.240; 
    next-server 3.2.1.17; 
    filename "pxelinux.0";
}
```

## Start DHCP Service
```sh
systemctl start dhcpd
```
