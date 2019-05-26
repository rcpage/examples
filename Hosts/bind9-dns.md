
## Install BIND9 DNS Service

```sh
dnf install -y bind
systemctl enable named
firewall-cmd --add-service=dns --permanent
firewall-cmd --reload
```
### Allow query from 3.2.1.0/24 by updating /etc/named.conf

```sh
sudo sed -e "s:allow-query.*:allow-query { 3.2.1.0/24; localhost; };:g" \
       -e "s:listen-on port .*:listen-on port 53 { 3.2.1.0/24; 127.0.0.1; };:g" \
       -i /etc/named.conf
```

### Create /var/named/example.com.zone

```sh
cat <<EOF | sudo tee /var/named/example.com.zone
\$TTL 86400

@ IN SOA example.com root.example.com (
  2017010302
  3600
  900
  604800
  86400
)

@      IN NS ns1
ns1 IN A  3.2.1.12
EOF
```
### Append zone file to /etc/named.conf

```sh
cat <<EOF | sudo tee -a /etc/named.conf
zone "example.com" in {
    type master;
    file "example.com.zone";
};
EOF
```

### Verify DNS service

```sh
### Restart named.service
systemctl restart named

### validate /etc/named.conf
named-checkconf

### validate zone file
named-checkzone example.com /var/named/example.com.zone
```

### Update /etc/resolv.conf
```sh
search example.com
nameserver 3.2.1.12
nameserver 3.2.1.1
```

### Ping ns1.example.com
```sh
ping ns1.example.com
```
