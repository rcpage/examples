df -h
fdisk -l
fdisk /dev/sda
# enter following commands to partition extra space
# print
# n -> new (use defaults)
# t -> use defaults and 8e for Linux
# w -> write settings
partprobe
vgextend rhel /dev/sda3
lvextend -l+100%FREE -r /dev/mapper/rhel-root
df -h
