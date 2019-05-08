
# Install Satellite 6.2

```sh
subscription-manager register

subscription-manager subscribe --pool="YOUR POOL ID"

subscription-manager repos --disable "*"

subscription-manager repos \
--enable rhel-7-server-rpms \
--enable rhel-server-rhscl-7-rpms \
--enable rhel-7-server-satellite-6.2-rpms \
--enable rhel-7-server-satellite-maintenance-6-rpms

yum clean all

yum repolist enabled

yum install satellite -y

#update /etc/hosts with hostname
hostname satellite.example.com
service network restart

ORG="My Organization" \
LOCATION="Default Location" \
satellite-installer --scenario satellite \
--foreman-initial-organization "$ORG" \
--foreman-initial-location "$LOCATION" \
--foreman-admin-password changeme \
--capsule-puppet true \
--foreman-proxy-puppetca true \
--foreman-proxy-tftp true \
--enable-foreman-plugin-discovery
Installing             Done                                               [100%] [..............................].
  Success!
  * Satellite is running at https://satellite.example.com
      Initial credentials are admin / changme
  * To install additional capsule on separate machine continue by running:

      capsule-certs-generate --capsule-fqdn "$CAPSULE" --certs-tar "~/$CAPSULE-certs.tar"

  The full log is at /var/log/foreman-installer/satellite.log
  
firewall-cmd --add-port=443/tcp --permanent
firewall-cmd --add-port=80/tcp --permanent
firewall-cmd --reload
firewall-cmd --list-all
```
