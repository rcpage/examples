
# 6.3 Upgrade

```sh

subscription-manager repos --disable "*"
subscription-manager repos --enable rhel-7-server-satellite-maintenance-6-rpms
yum install rubygem-foreman_maintain -y

subscription-manager repos \
--enable rhel-7-server-rpms \
--enable rhel-server-rhscl-7-rpms \
--enable rhel-7-server-satellite-6.3-rpms

yum clean all

yum repolist enabled

#check upgrade
foreman-maintain upgrade list-versions
foreman-maintain upgrade check --target-version 6.3

# may run into disk performance failure
# we override since running on a VM
foreman-maintain upgrade run --target-version 6.3 --whitelist="disk-performance"



```
