## Install TFTP Service and syslinux
```sh 
dnf install tftp-server syslinux
```
## Copy syslinux files to TFTP directory

Note: HTTP media server hosts vmlinuz and initrd.img files.

```sh
cd /var/lib/tftpboot
cp /usr/lib/syslinux/pxelinux.0 .
```

## Create pxelinux.conf/default file
```sh
default vesamenu.c32
prompt 0
timeout 600

label server
menu label ^Install Fedora 29 x86_64
menu default
kernel http://3.2.1.14/media/fedora/29/images/pxeboot/vmlinuz
append initrd=http://3.2.1.14/media/fedora/29/images/pxeboot/initrd.img inst.repo=http://3.2.1.14/media/fedora/29

label local
menu label Boot from ^local drive
localboot 0xffff
```

## Start TFTP Service
```sh
systemctl start xinetd
chkconfig tftp on
```
