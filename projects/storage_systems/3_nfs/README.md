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

1. txt 

| operation | # | dataset | real_time, [s] |
|:---:|:---:|:---:|:---:|
|**cp from nfs**|1|txt|5,38|
|-|2|txt|4,93|
|-|3|txt|4,97|
|-|1|binary zip|4,64|
|-|2|binary zip|4,47|
|-|3|binary zip|4,48|
|-|1|binary|4,69|
|-|2|binary|4,46|
|-|3|binary|4,27|
|**-**|**avg**|**txt**|**5,09**|
|**-**|**avg**|**binary zip**|**4,53**|
|**-**|**avg**|**binary**|**4,47**|
|**mv from nfs**|1|txt|5,45|
|-|2|txt|8,90|
|-|3|txt|5,99|
|-|1|binary zip|4,56|
|-|2|binary zip|5,06|
|-|3|binary zip|4,45|
|-|1|binary|4,46|
|-|2|binary|4,91|
|-|3|binary|4,34|
|**-**|**avg**|**txt**|**6,78**|
|**-**|**avg**|**binary zip**|**4,69**|
|**-**|**avg**|**binary**|**4,57**|
|**mv to nfs**|1|txt|8,85|
|-|2|txt|5,92|
|-|3|txt|8,87|
|-|1|binary zip|9,58|
|-|2|binary zip|4,28|
|-|3|binary zips|4,91|
|-|1|binary|4,91|
|-|2|binary|4,50|
|-|3|binary|5,05|
|**-**|**avg**|**txt**|**7,88**|
|**-**|**avg**|**binary zip**|**6,26**|
|**-**|**avg**|**binary**|**4,82**|
