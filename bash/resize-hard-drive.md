# Extend /dev/sda
```bash
lvs
df -h
fdisk -l
fdisk /dev/sda
# enter following commands to partition extra space
# p -> print drive space
# n -> new (use defaults)
# t -> use defaults and 8e hex code for Linux LVM
# w -> write settings
partprobe
vgextend rhel /dev/sda3
lvextend -l+100%FREE -r /dev/mapper/rhel-root
df -h
```

# Extend /dev/sdb
```bash
lvs
fdisk -l
vgextend rhel /dev/sdb
lvextend -l+100%FREE -r /dev/mapper/rhel-root
df -h
```
