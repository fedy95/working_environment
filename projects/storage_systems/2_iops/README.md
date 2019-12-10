# iops
 
- [iops](https://habr.com/ru/post/164325/)
- [smart](https://ru.wikipedia.org/wiki/S.M.A.R.T.)

### smart (vm 850)
```bash
sudo smartctl -a /dev/sda

smartctl 6.6 2016-05-31 r4324 [x86_64-linux-4.18.0-20-generic] (local build)
Copyright (C) 2002-16, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF INFORMATION SECTION ===
Vendor:               VMware,
Product:              VMware Virtual S
Revision:             1.0
User Capacity:        85 899 345 920 bytes [85,8 GB]
Logical block size:   512 bytes
Rotation Rate:        Solid State Device
Device type:          disk
Local Time is:        Tue Oct 15 20:51:45 2019 MSK
SMART support is:     Unavailable - device lacks SMART capability.

=== START OF READ SMART DATA SECTION ===
Current Drive Temperature:     0 C
Drive Trip Temperature:        0 C

Error Counter logging not supported

Device does not support Self Test logging
```

### iostat (vm 850)
```bash
iostat
Linux 4.18.0-20-generic (vm-kde)        15.10.2019      _x86_64_        (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0,50    0,00    0,56    0,01    0,00   98,93

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
loop0             0,00         0,01         0,00       1165          0
loop1             0,00         0,01         0,00       1137          0
loop2             0,00         0,01         0,00       1145          0
loop3             0,00         0,01         0,00       1121          0
loop4             0,00         0,01         0,00       1220          0
loop5             0,10         0,11         0,00      10899          0
loop6             0,12         0,13         0,00      12277          0
loop7             0,00         0,00         0,00          8          0
scd0              0,01         0,61         0,00      59560          0
sda               5,15        21,11       179,79    2056201   17514944
```

- IOPS

| test | vm 970  [specs](https://www.samsung.com/ru/memory-storage/970-pro-nvme-m2-ssd-/MZ-V7P1T0BW/) | vm 970 tests | vm 850 [specs](https://www.samsung.com/ru/memory-storage/850-evo-sata-3-2-5-inch-ssd/MZ-75E500BW/) | vm 850 tests |
|:---:|:---:|:---:|:---:|:---:|
| RANDREAD 4KB, QD1 | < 500 000 | 21 900 | 98 000 | 17 500 |
| RANDWHITE 4KB, QD32 | < 500 000 | 19 500 | 90 000 | 11 600 |
| RANDREAD 4KB, QD1 | < 15 000 | 17 900 | 10 000 | 8 811 |
| RANDWRITE 4KB, QD2 | < 55 000 | 14 500| 40 000 | 8 387 |

- RANDREAD 4KB, QD1 (vm 850)
```bash
fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=test --bs=4k --iodepth=1 --size=4G --readwrite=randread

test: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=1
fio-3.1
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=32.3MiB/s,w=0KiB/s][r=8268,w=0 IOPS][eta 00m:00s]
test: (groupid=0, jobs=1): err= 0: pid=122682: Wed Oct 16 22:21:03 2019
   read: IOPS=8811, BW=34.4MiB/s (36.1MB/s)(4096MiB/118995msec)
   bw (  KiB/s): min=30192, max=40240, per=99.95%, avg=35229.27, stdev=1763.29, samples=237
   iops        : min= 7548, max=10060, avg=8807.19, stdev=440.79, samples=237
  cpu          : usr=0.19%, sys=48.28%, ctx=1052057, majf=0, minf=12
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=1048576,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=34.4MiB/s (36.1MB/s), 34.4MiB/s-34.4MiB/s (36.1MB/s-36.1MB/s), io=4096MiB (4295MB), run=118995-118995msec

Disk stats (read/write):
  sda: ios=1047688/63, merge=0/45, ticks=0/1168, in_queue=107692, util=89.68%
```

- RANDREAD 4KB, QD32 (vm 850)
```bash
fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=test --bs=4k --iodepth=32 --size=4G --readwrite=randread
test: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=32
fio-3.1
Starting 1 process
Jobs: 1 (f=1): [r(1)][98.4%][r=72.6MiB/s,w=0KiB/s][r=18.6k,w=0 IOPS][eta 00m:01s]
test: (groupid=0, jobs=1): err= 0: pid=122670: Wed Oct 16 22:18:35 2019
   read: IOPS=17.5k, BW=68.5MiB/s (71.8MB/s)(4096MiB/59825msec)
   bw (  KiB/s): min=64598, max=75840, per=99.87%, avg=70015.66, stdev=2106.89, samples=119
   iops        : min=16149, max=18960, avg=17503.76, stdev=526.76, samples=119
  cpu          : usr=0.17%, sys=96.33%, ctx=485623, majf=0, minf=39
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=100.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.1%, 64=0.0%, >=64=0.0%
     issued rwt: total=1048576,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=32

Run status group 0 (all jobs):
   READ: bw=68.5MiB/s (71.8MB/s), 68.5MiB/s-68.5MiB/s (71.8MB/s-71.8MB/s), io=4096MiB (4295MB), run=59825-59825msec

Disk stats (read/write):
  sda: ios=1045069/37, merge=1/27, ticks=768/1820, in_queue=96144, util=99.01%
```

- RANDWRITE 4KB, QD1 (vm 850)
```bash
fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=test --bs=4k --iodepth=1 --size=4G --readwrite=randwrite 

test: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=1
fio-3.1
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][r=0KiB/s,w=34.2MiB/s][r=0,w=8755 IOPS][eta 00m:00s]
test: (groupid=0, jobs=1): err= 0: pid=122634: Wed Oct 16 22:16:30 2019
  write: IOPS=8387, BW=32.8MiB/s (34.4MB/s)(4096MiB/125019msec)
   bw (  KiB/s): min=26826, max=45808, per=99.98%, avg=33542.22, stdev=3166.00, samples=250
   iops        : min= 6706, max=11452, avg=8385.51, stdev=791.51, samples=250
  cpu          : usr=0.35%, sys=48.10%, ctx=1051728, majf=0, minf=7
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=0,1048576,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
  WRITE: bw=32.8MiB/s (34.4MB/s), 32.8MiB/s-32.8MiB/s (34.4MB/s-34.4MB/s), io=4096MiB (4295MB), run=125019-125019msec

Disk stats (read/write):
  sda: ios=0/1047612, merge=0/235, ticks=0/2968, in_queue=114444, util=89.29%
```

- RANDWRITE 4KB, QD32 (vm 850)
```bash
fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=test --bs=4k --iodepth=32 --size=4G --readwrite=randwrite

test: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=32
fio-3.1
Starting 1 process
test: Laying out IO file (1 file / 4096MiB)
Jobs: 1 (f=1): [w(1)][100.0%][r=0KiB/s,w=50.3MiB/s][r=0,w=12.9k IOPS][eta 00m:00s]
test: (groupid=0, jobs=1): err= 0: pid=122484: Wed Oct 16 22:12:33 2019
  write: IOPS=11.6k, BW=45.2MiB/s (47.4MB/s)(4096MiB/90644msec)
   bw (  KiB/s): min=17552, max=58344, per=99.88%, avg=46215.79, stdev=7380.50, samples=181
   iops        : min= 4388, max=14586, avg=11553.81, stdev=1845.13, samples=181
  cpu          : usr=0.45%, sys=81.22%, ctx=866040, majf=0, minf=9
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=100.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.1%, 64=0.0%, >=64=0.0%
     issued rwt: total=0,1048576,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=32

Run status group 0 (all jobs):
  WRITE: bw=45.2MiB/s (47.4MB/s), 45.2MiB/s-45.2MiB/s (47.4MB/s-47.4MB/s), io=4096MiB (4295MB), run=90644-90644msec

Disk stats (read/write):
  sda: ios=2/1050913, merge=0/46527, ticks=100/82328, in_queue=227244, util=98.33%
```

- RANDWRITE 4KB, QD32 (vm 970)
```bash
fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=test --bs=4k --iodepth=32 --size=4G --readwrite=randwrite

test: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=32
fio-3.1
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][r=0KiB/s,w=80.8MiB/s][r=0,w=20.7k IOPS][eta 00m:00s]
test: (groupid=0, jobs=1): err= 0: pid=48185: Wed Oct 16 22:04:15 2019
  write: IOPS=19.5k, BW=76.2MiB/s (79.9MB/s)(4096MiB/53754msec)
   bw (  KiB/s): min=74688, max=85216, per=99.95%, avg=77990.02, stdev=1873.32, samples=107
   iops        : min=18672, max=21304, avg=19497.47, stdev=468.34, samples=107
  cpu          : usr=0.68%, sys=99.31%, ctx=29, majf=0, minf=9
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=100.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.1%, 64=0.0%, >=64=0.0%
     issued rwt: total=0,1048576,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=32

Run status group 0 (all jobs):
  WRITE: bw=76.2MiB/s (79.9MB/s), 76.2MiB/s-76.2MiB/s (79.9MB/s-79.9MB/s), io=4096MiB (4295MB), run=53754-53754msec

Disk stats (read/write):
  nvme0n1: ios=0/1046370, merge=0/28, ticks=0/0, in_queue=92060, util=100.00%
```

- RANDREAD 4KB, QD32 (vm 970)
```bash
fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=test --bs=4k --iodepth=32 --size=4G --readwrite=randread
test: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=32
fio-3.1
Starting 1 process
Jobs: 1 (f=1): [r(1)][98.0%][r=92.7MiB/s,w=0KiB/s][r=23.7k,w=0 IOPS][eta 00m:01s]
test: (groupid=0, jobs=1): err= 0: pid=48166: Wed Oct 16 22:00:26 2019
   read: IOPS=21.9k, BW=85.6MiB/s (89.7MB/s)(4096MiB/47865msec)
   bw (  KiB/s): min=82339, max=96672, per=99.87%, avg=87508.76, stdev=2290.96, samples=95
   iops        : min=20584, max=24168, avg=21877.13, stdev=572.78, samples=95
  cpu          : usr=0.62%, sys=99.37%, ctx=24, majf=0, minf=41
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=100.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.1%, 64=0.0%, >=64=0.0%
     issued rwt: total=1048576,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=32

Run status group 0 (all jobs):
   READ: bw=85.6MiB/s (89.7MB/s), 85.6MiB/s-85.6MiB/s (89.7MB/s-89.7MB/s), io=4096MiB (4295MB), run=47865-47865msec

Disk stats (read/write):
  nvme0n1: ios=1043150/15, merge=0/26, ticks=0/0, in_queue=86832, util=100.00%
```

- RANDWRITE 4KB, QD1 (vm 970)
```bash
fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=test --bs=4k --iodepth=1 --size=4G --readwrite=randwrite
test: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=1
fio-3.1
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][r=0KiB/s,w=50.0MiB/s][r=0,w=12.8k IOPS][eta 00m:00s]
test: (groupid=0, jobs=1): err= 0: pid=48201: Wed Oct 16 22:05:51 2019
  write: IOPS=14.5k, BW=56.8MiB/s (59.6MB/s)(4096MiB/72094msec)
   bw (  KiB/s): min=44968, max=68415, per=99.95%, avg=58151.54, stdev=6518.44, samples=144
   iops        : min=11242, max=17103, avg=14537.85, stdev=1629.53, samples=144
  cpu          : usr=0.20%, sys=73.87%, ctx=1038345, majf=0, minf=9
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=0,1048576,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
  WRITE: bw=56.8MiB/s (59.6MB/s), 56.8MiB/s-56.8MiB/s (59.6MB/s-59.6MB/s), io=4096MiB (4295MB), run=72094-72094msec

Disk stats (read/write):
  nvme0n1: ios=0/1045869, merge=0/61, ticks=0/0, in_queue=72008, util=100.00%
--
