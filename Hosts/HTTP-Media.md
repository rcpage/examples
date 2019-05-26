### Install HTTP Service
```sh
dnf install httpd
systemctl enable httpd
systemctl start httpd
```
### Download Fedora ISO to HTTP host
```sh
mkdir -p /media/iso /media/iso/fedora/30
cd /media/iso
curl -O https://download.fedoraproject.org/pub/fedora/linux/releases/30/Server/x86_64/iso/Fedora-Server-dvd-x86_64-30-1.2.iso
```

### Append line to /etc/fstab to auto mount iso at /media/iso/fedora/30
```txt
/media/iso/Fedora-Server-dvd-x86_64-30-1.2.iso /media/iso/fedora/30 iso9660 loop 0 0
```

### Create static link to /var/www/http
```sh
ln -s /media/iso/ /var/www/http/media
```

### Mount Media and Restart HTTP Service
```sh
mount --all
systemctl restart httpd
```

