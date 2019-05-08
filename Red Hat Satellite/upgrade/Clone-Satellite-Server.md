## Preparation

Take katello-backup snapshot of production server. See https://github.com/RedHatSatellite/satellite-clone


```sh
## copy backup file to host
scp katello-backup.tar.gz [host-ip]:

## ssh to host
subscription-manager register

## Note: change pool id for production license
subscription-manager subscribe --pool="POOL ID HERE"

## install git
yum install git -y

## install ansible
subscription-manager repos --enable rhel-7-server-extras-rpms
yum install ansible -y

## download satellite-clone project from github
git -c http.sslVerify=false clone https://github.com/RedHatSatellite/satellite-clone.git
cd satellite-clone

## copy default vars
cp satellite-clone-vars.sample.yml satellite-clone-vars.yml

## Unarchive katello-backup and rename
tar -xvzf katello-backup.tar.gz
mv katello-backup-* /backup

## Run playbook on fresh RHEL install
ansible-playbook satellite-clone-playbook.yml

## Open https/http ports
firewall-cmd --add-port=443/tcp --permanent
firewall-cmd --add-port=80/tcp --permanent
firewall-cmd --reload
firewall-cmd --list-all
```
