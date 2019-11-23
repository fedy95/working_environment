# nfs
 
- [ubuntu wiki](https://help.ubuntu.com/lts/serverguide/network-file-system.html)

### architecture
![img](https://github.com/fedy95/working_environment/blob/master/projects/storage_systems/3_nfs/schema/png/deployment.png)

#### iops

```txt
fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=test --bs=4k --iodepth=1 --size=1G --readwrite=randread
test: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=1

   read: IOPS=9389, BW=36.7MiB/s (38.5MB/s)(1024MiB/27920msec)
   iops: min= 5770, max=11202, avg=9391.98, stdev=804.85, samples=55

fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=test --bs=4k --iodepth=1 --size=1G --readwrite=randwrite 
test: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=1

  write: IOPS=8590, BW=33.6MiB/s (35.2MB/s)(1024MiB/30516msec)
  iops: min= 8092, max= 9206, avg=8590.03, stdev=208.97, samples=61

```
### install
- server
```bash
sudo -i
apt install nfs-kernel-server nfs-common

nano /etc/exports
/home/fedy95/Documents/archives 192.168.30.130/255.255.255.0(rw,insecure,nohide,all_squash,anonuid=1000,anongid=1000,no_subtree_check)

/etc/init.d/nfs-kernel-server restart
```

- client
```bash
sudo -i
apt install nfs-kernel-server nfs-common

mount -t nfs -O uid=1000,iocharset=utf-8 192.168.30.129:/home/fedy95/Documents/archives /home/fedy95/Documents/project
```

### datasets
1. txt 
- 1 Gb (1 074,7 Mb) 52407 files by 512 str form [link](https://habr.com/en/post/357402/)

| Operation | real_time, [s] | user_time, [s] | sys_time, [s] |
|:---:|:---:|:---:|:---:|
|cp from nfs|133,83|4,26|6,31|
|cp from nfs|134,54|6,72|6,33|
|cp from nfs|134,44|7,68|6,25|
|**avg**|**134,27**|**6,22**|**6,30**|
|mv from nfs|215,94|1,16|12,79|
|mv from nfs|242,44|1,09|12,85|
|mv from nfs|214,42|0,90|12,82|
|**avg**|**224,27**|**1,05**|**12,82**|
|mv to nfs|254,21|1,04|13,99|
|mv to nfs|255,61|1,09|14,53|
|mv to nfs|256,01|0,97|13,94|
|**avg**|**255,27**|**1,04**|**14,15**|
