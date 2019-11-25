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

- [generate_datasets](https://github.com/fedy95/working_environment/blob/master/projects/storage_systems/3_nfs/datasets/generate_datasets.py)

| operation | # | dataset | real_time, [s] |
|:---:|:---:|:---:|:---:|
|**cp from nfs**|1|txt|6,35|
|-|2|txt|5,38|
|-|3|txt|5,23|
|-|1|single_binary|4,60|
|-|2|single_binary|4,56|
|-|3|single_binary|4,52|
|-|1|multi_binary|4,77|
|-|2|multi_binary|4,66|
|-|3|multi_binary|4,67|
|**-**|**avg**|**txt**|**5,65**|
|**-**|**avg**|**single_binary**|**4,56**|
|**-**|**avg**|**multi_binary**|**4,63**|
|**mv from nfs**|1|txt|5,87|
|-|2|txt|8,47|
|-|3|txt|6,41|
|-|1|single_binary|4,47|
|-|2|single_binary|4,70|
|-|3|single_binary|4,56|
|-|1|multi_binary|4,60|
|-|2|multi_binary|4,77|
|-|3|multi_binary|4,65|
|**-**|**avg**|**txt**|**7,01**|
|**-**|**avg**|**single_binary**|**4,58**|
|**-**|**avg**|**multi_binary**|**4,67**|
|**mv to nfs**|1|txt|8,61|
|-|2|txt|6,40|
|-|3|txt|8,72|
|-|1|single_binary|4,79|
|-|2|single_binary|4,54|
|-|3|single_binarys|4,68|
|-|1|multi_binary|4,64|
|-|2|multi_binary|4,57|
|-|3|multi_binary|4,69|
|**-**|**avg**|**txt**|**7,91**|
|**-**|**avg**|**single_binary**|**4,67**|
|**-**|**avg**|**multi_binary**|**4,63**|
