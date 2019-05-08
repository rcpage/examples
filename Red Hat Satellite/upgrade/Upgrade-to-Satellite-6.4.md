

# 6.4 Upgrade

```sh

subscription-manager repos --disable "*"

subscription-manager repos --enable=rhel-7-server-rpms \
--enable=rhel-server-rhscl-7-rpms \
--enable=rhel-7-server-satellite-6.4-rpms \
--enable=rhel-7-server-satellite-maintenance-6-rpms \
--enable=rhel-7-server-ansible-2.6-rpms

yum install rubygem-foreman_maintain -y

yum clean all

yum repolist enabled

#check upgrade
foreman-maintain upgrade list-versions
foreman-maintain upgrade check --target-version 6.4

## Upgrading Satellite or Capsule To Puppet 4

Enable the Puppet 4 repository:

## On a Satellite:

subscription-manager repos \
--enable=rhel-7-server-satellite-6.3-puppet4-rpms

## On a Capsule:

subscription-manager repos \
--enable=rhel-7-server-satellite-capsule-6.3-puppet4-rpms

## Upgrade Puppet:
satellite-installer --upgrade-puppet

## may need to re-install puppetserver after running above command 
rpm -e puppetserver -y
yum install puppetserver -y
systemctl restart puppetserver

## may run into disk performance failure, we override since running on a VM
foreman-maintain upgrade run --target-version 6.4 --whitelist="disk-performance"

## If using a BASH shell, after a successful or failed upgrade, enter:
hash -d foreman-maintain service 2> /dev/null

foreman-maintain service restart

## If you have the OpenSCAP plug-in installed, but do not have the default OpenSCAP content available, enter the following command:
foreman-rake foreman_openscap:bulk_upload:default

```
