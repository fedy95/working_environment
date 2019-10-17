# 970

## w32
```txt
Command Line: X:\diskspd\diskspd.exe -b4K -d30 -o4 -t1 -h -r -w0 -D -Z1G -c20G X:\diskspd\iotest.dat

Input parameters:

	timespan:   1
	-------------
	duration: 30s
	warm up time: 5s
	cool down time: 0s
	gathering IOPS at intervals of 1000ms
	random seed: 0
	path: 'X:\diskspd\iotest.dat'
		think time: 0ms
		burst size: 0
		software cache disabled
		hardware write cache disabled, writethrough on
		write buffer size: 1073741824
		performing read test
		block size: 4096
		using random I/O (alignment: 4096)
		number of outstanding I/O operations: 4
		thread stride size: 0
		threads per file: 1
		using I/O Completion Ports
		IO priority: normal

System information:

	computer name: fedyPC
	start time: 2019/10/17 05:58:46 UTC

Results for timespan 1:
*******************************************************************************

actual test time:	30.00s
thread count:		1
proc count:		16

CPU |  Usage |  User  |  Kernel |  Idle
-------------------------------------------
   0|  99.95%|   2.76%|   97.19%|   0.05%
   1|   0.31%|   0.05%|    0.26%|  99.69%
   2|   3.75%|   2.14%|    1.61%|  96.25%
   3|   1.98%|   0.94%|    1.04%|  98.02%
   4|   3.23%|   1.72%|    1.51%|  96.77%
   5|   0.88%|   0.47%|    0.42%|  99.12%
   6|   4.32%|   2.81%|    1.51%|  95.68%
   7|   0.78%|   0.36%|    0.42%|  99.22%
   8|   3.85%|   2.45%|    1.41%|  96.15%
   9|   1.61%|   0.78%|    0.83%|  98.39%
  10|   3.28%|   1.82%|    1.46%|  96.72%
  11|   0.52%|   0.31%|    0.21%|  99.48%
  12|   1.98%|   1.41%|    0.57%|  98.02%
  13|   1.77%|   1.41%|    0.36%|  98.23%
  14|   2.50%|   1.56%|    0.94%|  97.50%
  15|   1.30%|   0.88%|    0.42%|  98.70%
-------------------------------------------
avg.|   8.25%|   1.37%|    6.88%|  91.75%

Total IO
thread |       bytes     |     I/Os     |    MiB/s   |  I/O per s | IopsStdDev |  file
-------------------------------------------------------------------------------------------
     0 |     10680209408 |      2607473 |     339.51 |   86915.29 |    1557.39 | X:\diskspd\iotest.dat (20GiB)
-------------------------------------------------------------------------------------------
total:       10680209408 |      2607473 |     339.51 |   86915.29 |    1557.39

Read IO
thread |       bytes     |     I/Os     |    MiB/s   |  I/O per s | IopsStdDev |  file
-------------------------------------------------------------------------------------------
     0 |     10680209408 |      2607473 |     339.51 |   86915.29 |    1557.39 | X:\diskspd\iotest.dat (20GiB)
-------------------------------------------------------------------------------------------
total:       10680209408 |      2607473 |     339.51 |   86915.29 |    1557.39

Write IO
thread |       bytes     |     I/Os     |    MiB/s   |  I/O per s | IopsStdDev |  file
-------------------------------------------------------------------------------------------
     0 |               0 |            0 |       0.00 |       0.00 |       0.00 | X:\diskspd\iotest.dat (20GiB)
-------------------------------------------------------------------------------------------
total:                 0 |            0 |       0.00 |       0.00 |       0.00

```

## w1
```txt

Command Line: X:\diskspd\diskspd.exe -b4K -d30 -o4 -t1 -h -r -w100 -D -Z1G -c20G X:\diskspd\iotest.dat

Input parameters:

	timespan:   1
	-------------
	duration: 30s
	warm up time: 5s
	cool down time: 0s
	gathering IOPS at intervals of 1000ms
	random seed: 0
	path: 'X:\diskspd\iotest.dat'
		think time: 0ms
		burst size: 0
		software cache disabled
		hardware write cache disabled, writethrough on
		write buffer size: 1073741824
		performing write test
		block size: 4096
		using random I/O (alignment: 4096)
		number of outstanding I/O operations: 4
		thread stride size: 0
		threads per file: 1
		using I/O Completion Ports
		IO priority: normal

System information:

	computer name: fedyPC
	start time: 2019/10/17 05:55:34 UTC

Results for timespan 1:
*******************************************************************************

actual test time:	30.00s
thread count:		1
proc count:		16

CPU |  Usage |  User  |  Kernel |  Idle
-------------------------------------------
   0| 100.00%|   1.72%|   98.28%|   0.00%
   1|   0.26%|   0.00%|    0.26%|  99.74%
   2|   1.35%|   0.47%|    0.89%|  98.65%
   3|   0.99%|   0.42%|    0.57%|  99.01%
   4|   3.59%|   1.56%|    2.03%|  96.41%
   5|   0.26%|   0.10%|    0.16%|  99.74%
   6|   2.66%|   1.35%|    1.30%|  97.34%
   7|   0.10%|   0.10%|    0.00%|  99.90%
   8|   1.51%|   0.99%|    0.52%|  98.49%
   9|   0.99%|   0.36%|    0.62%|  99.01%
  10|   1.88%|   0.89%|    0.99%|  98.13%
  11|   0.31%|   0.21%|    0.10%|  99.69%
  12|   1.46%|   0.63%|    0.83%|  98.54%
  13|   0.63%|   0.31%|    0.31%|  99.38%
  14|   1.30%|   0.47%|    0.83%|  98.70%
  15|   0.26%|   0.16%|    0.10%|  99.74%
-------------------------------------------
avg.|   7.35%|   0.61%|    6.74%|  92.65%

Write IO
thread |       bytes     |     I/Os     |    MiB/s   |  I/O per s | IopsStdDev |  file
-------------------------------------------------------------------------------------------
     0 |      8599310336 |      2099441 |     273.36 |   69980.93 |     688.53 | X:\diskspd\iotest.dat (20GiB)
-------------------------------------------------------------------------------------------
total:        8599310336 |      2099441 |     273.36 |   69980.93 |     688.53

```

## r32
```txt

Command Line: X:\diskspd\diskspd.exe -b4K -d30 -o4 -t32 -h -r -w0 -D -Z1G -c20G X:\diskspd\iotest.dat

Input parameters:

	timespan:   1
	-------------
	duration: 30s
	warm up time: 5s
	cool down time: 0s
	gathering IOPS at intervals of 1000ms
	random seed: 0
	path: 'X:\diskspd\iotest.dat'
		think time: 0ms
		burst size: 0
		software cache disabled
		hardware write cache disabled, writethrough on
		write buffer size: 1073741824
		performing read test
		block size: 4096
		using random I/O (alignment: 4096)
		number of outstanding I/O operations: 4
		thread stride size: 0
		threads per file: 32
		using I/O Completion Ports
		IO priority: normal

System information:

	computer name: fedyPC
	start time: 2019/10/17 05:57:49 UTC

Results for timespan 1:
*******************************************************************************

actual test time:	30.00s
thread count:		32
proc count:		16

CPU |  Usage |  User  |  Kernel |  Idle
-------------------------------------------
   0|  99.84%|   4.95%|   94.90%|   0.16%
   1|  99.90%|   2.81%|   97.08%|   0.10%
   2|  99.79%|   2.14%|   97.66%|   0.21%
   3|  99.90%|   2.60%|   97.29%|   0.10%
   4|  99.79%|   3.13%|   96.67%|   0.21%
   5|  99.74%|   2.29%|   97.45%|   0.26%
   6|  99.79%|   2.76%|   97.03%|   0.21%
   7|  99.79%|   3.28%|   96.51%|   0.21%
   8|  99.90%|   5.57%|   94.32%|   0.10%
   9|  99.79%|   3.96%|   95.83%|   0.21%
  10|  99.79%|   2.55%|   97.24%|   0.21%
  11|  99.90%|   2.45%|   97.45%|   0.10%
  12|  99.79%|   3.44%|   96.35%|   0.21%
  13|  99.69%|   3.85%|   95.83%|   0.31%
  14|  99.90%|   3.39%|   96.51%|   0.10%
  15|  99.84%|   3.75%|   96.09%|   0.16%
-------------------------------------------
avg.|  99.82%|   3.31%|   96.51%|   0.18%

Read IO
thread |       bytes     |     I/Os     |    MiB/s   |  I/O per s | IopsStdDev |  file
-------------------------------------------------------------------------------------------
     0 |      2240290816 |       546946 |      71.22 |   18231.49 |     725.94 | X:\diskspd\iotest.dat (20GiB)
     1 |      2360934400 |       576400 |      75.05 |   19213.29 |     458.34 | X:\diskspd\iotest.dat (20GiB)
     2 |      2372976640 |       579340 |      75.43 |   19311.29 |     454.97 | X:\diskspd\iotest.dat (20GiB)
     3 |      2387709952 |       582937 |      75.90 |   19431.19 |     440.43 | X:\diskspd\iotest.dat (20GiB)
     4 |      2368114688 |       578153 |      75.28 |   19271.72 |     563.35 | X:\diskspd\iotest.dat (20GiB)
     5 |      2426433536 |       592391 |      77.13 |   19746.32 |     376.31 | X:\diskspd\iotest.dat (20GiB)
     6 |      2411036672 |       588632 |      76.64 |   19621.02 |     522.86 | X:\diskspd\iotest.dat (20GiB)
     7 |      2412580864 |       589009 |      76.69 |   19633.59 |     484.67 | X:\diskspd\iotest.dat (20GiB)
     8 |      2155012096 |       526126 |      68.51 |   17537.49 |    1228.58 | X:\diskspd\iotest.dat (20GiB)
     9 |      2330341376 |       568931 |      74.08 |   18964.32 |     636.15 | X:\diskspd\iotest.dat (20GiB)
    10 |      2453860352 |       599087 |      78.01 |   19969.52 |     412.45 | X:\diskspd\iotest.dat (20GiB)
    11 |      2446458880 |       597280 |      77.77 |   19909.29 |     462.44 | X:\diskspd\iotest.dat (20GiB)
    12 |      2318479360 |       566035 |      73.70 |   18867.79 |     958.03 | X:\diskspd\iotest.dat (20GiB)
    13 |      2381103104 |       581324 |      75.69 |   19377.42 |     726.82 | X:\diskspd\iotest.dat (20GiB)
    14 |      2392854528 |       584193 |      76.07 |   19473.05 |     513.37 | X:\diskspd\iotest.dat (20GiB)
    15 |      2398027776 |       585456 |      76.23 |   19515.15 |     523.43 | X:\diskspd\iotest.dat (20GiB)
    16 |      2239537152 |       546762 |      71.19 |   18225.36 |     707.97 | X:\diskspd\iotest.dat (20GiB)
    17 |      2363772928 |       577093 |      75.14 |   19236.39 |     455.58 | X:\diskspd\iotest.dat (20GiB)
    18 |      2378612736 |       580716 |      75.61 |   19357.15 |     355.81 | X:\diskspd\iotest.dat (20GiB)
    19 |      2392530944 |       584114 |      76.06 |   19470.42 |     409.87 | X:\diskspd\iotest.dat (20GiB)
    20 |      2368679936 |       578291 |      75.30 |   19276.32 |     532.19 | X:\diskspd\iotest.dat (20GiB)
    21 |      2416893952 |       590062 |      76.83 |   19668.69 |     420.22 | X:\diskspd\iotest.dat (20GiB)
    22 |      2406944768 |       587633 |      76.51 |   19587.72 |     601.27 | X:\diskspd\iotest.dat (20GiB)
    23 |      2414567424 |       589494 |      76.76 |   19649.75 |     576.28 | X:\diskspd\iotest.dat (20GiB)
    24 |      2177474560 |       531610 |      69.22 |   17720.29 |    1422.24 | X:\diskspd\iotest.dat (20GiB)
    25 |      2332299264 |       569409 |      74.14 |   18980.25 |     626.92 | X:\diskspd\iotest.dat (20GiB)
    26 |      2446823424 |       597369 |      77.78 |   19912.25 |     595.05 | X:\diskspd\iotest.dat (20GiB)
    27 |      2442592256 |       596336 |      77.65 |   19877.82 |     437.53 | X:\diskspd\iotest.dat (20GiB)
    28 |      2310938624 |       564194 |      73.46 |   18806.42 |     950.48 | X:\diskspd\iotest.dat (20GiB)
    29 |      2382045184 |       581554 |      75.72 |   19385.09 |     815.48 | X:\diskspd\iotest.dat (20GiB)
    30 |      2410606592 |       588527 |      76.63 |   19617.52 |     699.81 | X:\diskspd\iotest.dat (20GiB)
    31 |      2387374080 |       582855 |      75.89 |   19428.45 |     596.12 | X:\diskspd\iotest.dat (20GiB)
-------------------------------------------------------------------------------------------
total:       75727908864 |     18488259 |    2407.32 |  616273.82 |   12758.88
```

## r1
```txt

Command Line: X:\diskspd\diskspd.exe -b4K -d30 -o4 -t1 -h -r -w0 -D -Z1G -c20G X:\diskspd\iotest.dat

Input parameters:

	timespan:   1
	-------------
	duration: 30s
	warm up time: 5s
	cool down time: 0s
	gathering IOPS at intervals of 1000ms
	random seed: 0
	path: 'X:\diskspd\iotest.dat'
		think time: 0ms
		burst size: 0
		software cache disabled
		hardware write cache disabled, writethrough on
		write buffer size: 1073741824
		performing read test
		block size: 4096
		using random I/O (alignment: 4096)
		number of outstanding I/O operations: 4
		thread stride size: 0
		threads per file: 1
		using I/O Completion Ports
		IO priority: normal

System information:

	computer name: fedyPC
	start time: 2019/10/17 05:58:46 UTC

Results for timespan 1:
*******************************************************************************

actual test time:	30.00s
thread count:		1
proc count:		16

CPU |  Usage |  User  |  Kernel |  Idle
-------------------------------------------
   0|  99.95%|   2.76%|   97.19%|   0.05%
   1|   0.31%|   0.05%|    0.26%|  99.69%
   2|   3.75%|   2.14%|    1.61%|  96.25%
   3|   1.98%|   0.94%|    1.04%|  98.02%
   4|   3.23%|   1.72%|    1.51%|  96.77%
   5|   0.88%|   0.47%|    0.42%|  99.12%
   6|   4.32%|   2.81%|    1.51%|  95.68%
   7|   0.78%|   0.36%|    0.42%|  99.22%
   8|   3.85%|   2.45%|    1.41%|  96.15%
   9|   1.61%|   0.78%|    0.83%|  98.39%
  10|   3.28%|   1.82%|    1.46%|  96.72%
  11|   0.52%|   0.31%|    0.21%|  99.48%
  12|   1.98%|   1.41%|    0.57%|  98.02%
  13|   1.77%|   1.41%|    0.36%|  98.23%
  14|   2.50%|   1.56%|    0.94%|  97.50%
  15|   1.30%|   0.88%|    0.42%|  98.70%
-------------------------------------------
avg.|   8.25%|   1.37%|    6.88%|  91.75%

Total IO
thread |       bytes     |     I/Os     |    MiB/s   |  I/O per s | IopsStdDev |  file
-------------------------------------------------------------------------------------------
     0 |     10680209408 |      2607473 |     339.51 |   86915.29 |    1557.39 | X:\diskspd\iotest.dat (20GiB)
-------------------------------------------------------------------------------------------
total:       10680209408 |      2607473 |     339.51 |   86915.29 |    1557.39

Read IO
thread |       bytes     |     I/Os     |    MiB/s   |  I/O per s | IopsStdDev |  file
-------------------------------------------------------------------------------------------
     0 |     10680209408 |      2607473 |     339.51 |   86915.29 |    1557.39 | X:\diskspd\iotest.dat (20GiB)
-------------------------------------------------------------------------------------------
total:       10680209408 |      2607473 |     339.51 |   86915.29 |    1557.39
```

# 850

## w32
```txt

Command Line: C:\diskspd\diskspd.exe -b4K -d30 -o4 -t32 -h -r -w100 -D -Z1G -c20G C:\diskspd\iotest.dat

Input parameters:

	timespan:   1
	-------------
	duration: 30s
	warm up time: 5s
	cool down time: 0s
	gathering IOPS at intervals of 1000ms
	random seed: 0
	path: 'C:\diskspd\iotest.dat'
		think time: 0ms
		burst size: 0
		software cache disabled
		hardware write cache disabled, writethrough on
		write buffer size: 1073741824
		performing write test
		block size: 4096
		using random I/O (alignment: 4096)
		number of outstanding I/O operations: 4
		thread stride size: 0
		threads per file: 32
		using I/O Completion Ports
		IO priority: normal

System information:

	computer name: fedyPC
	start time: 2019/10/17 06:01:00 UTC

Results for timespan 1:
*******************************************************************************

actual test time:	30.00s
thread count:		32
proc count:		16

CPU |  Usage |  User  |  Kernel |  Idle
-------------------------------------------
   0|  32.60%|   1.77%|   30.83%|  67.40%
   1|  14.11%|   2.24%|   11.88%|  85.89%
   2|  12.24%|   2.60%|    9.64%|  87.76%
   3|  10.31%|   1.56%|    8.75%|  89.69%
   4|  11.15%|   1.51%|    9.64%|  88.85%
   5|   9.27%|   0.89%|    8.39%|  90.73%
   6|  11.46%|   2.71%|    8.75%|  88.54%
   7|   9.64%|   0.94%|    8.70%|  90.36%
   8|  12.97%|   3.85%|    9.11%|  87.03%
   9|  10.42%|   0.47%|    9.95%|  89.58%
  10|  11.82%|   2.24%|    9.58%|  88.18%
  11|   9.17%|   0.63%|    8.54%|  90.83%
  12|  10.83%|   1.35%|    9.48%|  89.17%
  13|   9.79%|   1.15%|    8.65%|  90.21%
  14|  10.47%|   1.41%|    9.06%|  89.53%
  15|  12.34%|   2.19%|   10.16%|  87.66%
-------------------------------------------
avg.|  12.41%|   1.72%|   10.69%|  87.59%

Write IO
thread |       bytes     |     I/Os     |    MiB/s   |  I/O per s | IopsStdDev |  file
-------------------------------------------------------------------------------------------
     0 |       250105856 |        61061 |       7.95 |    2035.34 |     642.50 | C:\diskspd\iotest.dat (20GiB)
     1 |       250736640 |        61215 |       7.97 |    2040.47 |     641.83 | C:\diskspd\iotest.dat (20GiB)
     2 |       251355136 |        61366 |       7.99 |    2045.51 |     650.95 | C:\diskspd\iotest.dat (20GiB)
     3 |       251359232 |        61367 |       7.99 |    2045.54 |     640.84 | C:\diskspd\iotest.dat (20GiB)
     4 |       251478016 |        61396 |       7.99 |    2046.51 |     647.57 | C:\diskspd\iotest.dat (20GiB)
     5 |       252555264 |        61659 |       8.03 |    2055.27 |     647.69 | C:\diskspd\iotest.dat (20GiB)
     6 |       252014592 |        61527 |       8.01 |    2050.87 |     650.08 | C:\diskspd\iotest.dat (20GiB)
     7 |       252198912 |        61572 |       8.02 |    2052.37 |     645.52 | C:\diskspd\iotest.dat (20GiB)
     8 |       250810368 |        61233 |       7.97 |    2041.07 |     652.42 | C:\diskspd\iotest.dat (20GiB)
     9 |       252137472 |        61557 |       8.02 |    2051.87 |     647.04 | C:\diskspd\iotest.dat (20GiB)
    10 |       250236928 |        61093 |       7.95 |    2036.41 |     644.05 | C:\diskspd\iotest.dat (20GiB)
    11 |       252735488 |        61703 |       8.03 |    2056.74 |     647.46 | C:\diskspd\iotest.dat (20GiB)
    12 |       251658240 |        61440 |       8.00 |    2047.97 |     647.41 | C:\diskspd\iotest.dat (20GiB)
    13 |       251994112 |        61522 |       8.01 |    2050.71 |     648.91 | C:\diskspd\iotest.dat (20GiB)
    14 |       251277312 |        61347 |       7.99 |    2044.87 |     644.12 | C:\diskspd\iotest.dat (20GiB)
    15 |       250753024 |        61219 |       7.97 |    2040.61 |     650.92 | C:\diskspd\iotest.dat (20GiB)
    16 |       250118144 |        61064 |       7.95 |    2035.44 |     642.90 | C:\diskspd\iotest.dat (20GiB)
    17 |       250753024 |        61219 |       7.97 |    2040.61 |     641.45 | C:\diskspd\iotest.dat (20GiB)
    18 |       251297792 |        61352 |       7.99 |    2045.04 |     650.28 | C:\diskspd\iotest.dat (20GiB)
    19 |       251355136 |        61366 |       7.99 |    2045.51 |     641.10 | C:\diskspd\iotest.dat (20GiB)
    20 |       251469824 |        61394 |       7.99 |    2046.44 |     647.18 | C:\diskspd\iotest.dat (20GiB)
    21 |       252555264 |        61659 |       8.03 |    2055.27 |     647.58 | C:\diskspd\iotest.dat (20GiB)
    22 |       252014592 |        61527 |       8.01 |    2050.87 |     649.94 | C:\diskspd\iotest.dat (20GiB)
    23 |       252219392 |        61577 |       8.02 |    2052.54 |     645.48 | C:\diskspd\iotest.dat (20GiB)
    24 |       250777600 |        61225 |       7.97 |    2040.81 |     652.34 | C:\diskspd\iotest.dat (20GiB)
    25 |       252141568 |        61558 |       8.02 |    2051.91 |     646.79 | C:\diskspd\iotest.dat (20GiB)
    26 |       250273792 |        61102 |       7.96 |    2036.71 |     643.91 | C:\diskspd\iotest.dat (20GiB)
    27 |       252715008 |        61698 |       8.03 |    2056.57 |     647.33 | C:\diskspd\iotest.dat (20GiB)
    28 |       251707392 |        61452 |       8.00 |    2048.37 |     647.63 | C:\diskspd\iotest.dat (20GiB)
    29 |       252043264 |        61534 |       8.01 |    2051.11 |     648.86 | C:\diskspd\iotest.dat (20GiB)
    30 |       251318272 |        61357 |       7.99 |    2045.21 |     644.64 | C:\diskspd\iotest.dat (20GiB)
    31 |       250769408 |        61223 |       7.97 |    2040.74 |     650.86 | C:\diskspd\iotest.dat (20GiB)
-------------------------------------------------------------------------------------------
total:        8046936064 |      1964584 |     255.80 |   65485.23 |   20695.06

```

## w1
```txt

Command Line: C:\diskspd\diskspd.exe -b4K -d30 -o4 -t1 -h -r -w100 -D -Z1G -c20G C:\diskspd\iotest.dat

Input parameters:

	timespan:   1
	-------------
	duration: 30s
	warm up time: 5s
	cool down time: 0s
	gathering IOPS at intervals of 1000ms
	random seed: 0
	path: 'C:\diskspd\iotest.dat'
		think time: 0ms
		burst size: 0
		software cache disabled
		hardware write cache disabled, writethrough on
		write buffer size: 1073741824
		performing write test
		block size: 4096
		using random I/O (alignment: 4096)
		number of outstanding I/O operations: 4
		thread stride size: 0
		threads per file: 1
		using I/O Completion Ports
		IO priority: normal

System information:

	computer name: fedyPC
	start time: 2019/10/17 06:02:30 UTC

Results for timespan 1:
*******************************************************************************

actual test time:	30.00s
thread count:		1
proc count:		16

CPU |  Usage |  User  |  Kernel |  Idle
-------------------------------------------
   0|  78.70%|   2.97%|   75.73%|  21.30%
   1|   3.23%|   0.73%|    2.50%|  96.77%
   2|   2.40%|   1.30%|    1.09%|  97.60%
   3|   1.35%|   0.89%|    0.47%|  98.65%
   4|   2.76%|   1.30%|    1.46%|  97.24%
   5|   0.52%|   0.26%|    0.26%|  99.48%
   6|   2.08%|   1.15%|    0.94%|  97.92%
   7|   0.73%|   0.42%|    0.31%|  99.27%
   8|   2.60%|   1.30%|    1.30%|  97.40%
   9|   0.52%|   0.10%|    0.42%|  99.48%
  10|   2.50%|   1.09%|    1.41%|  97.50%
  11|   0.26%|   0.21%|    0.05%|  99.74%
  12|   1.35%|   0.52%|    0.83%|  98.65%
  13|   0.89%|   0.73%|    0.16%|  99.11%
  14|   1.15%|   0.47%|    0.68%|  98.85%
  15|   3.33%|   0.89%|    2.45%|  96.67%
-------------------------------------------
avg.|   6.52%|   0.90%|    5.63%|  93.48%

Write IO
thread |       bytes     |     I/Os     |    MiB/s   |  I/O per s | IopsStdDev |  file
-------------------------------------------------------------------------------------------
     0 |      5752299520 |      1404370 |     182.86 |   46812.21 |    5769.47 | C:\diskspd\iotest.dat (20GiB)
-------------------------------------------------------------------------------------------
total:        5752299520 |      1404370 |     182.86 |   46812.21 |    5769.47

```

## r32
```txt

Command Line: C:\diskspd\diskspd.exe -b4K -d30 -o4 -t32 -h -r -w0 -D -Z1G -c20G C:\diskspd\iotest.dat

Input parameters:

	timespan:   1
	-------------
	duration: 30s
	warm up time: 5s
	cool down time: 0s
	gathering IOPS at intervals of 1000ms
	random seed: 0
	path: 'C:\diskspd\iotest.dat'
		think time: 0ms
		burst size: 0
		software cache disabled
		hardware write cache disabled, writethrough on
		write buffer size: 1073741824
		performing read test
		block size: 4096
		using random I/O (alignment: 4096)
		number of outstanding I/O operations: 4
		thread stride size: 0
		threads per file: 32
		using I/O Completion Ports
		IO priority: normal

System information:

	computer name: fedyPC
	start time: 2019/10/17 06:03:35 UTC

Results for timespan 1:
*******************************************************************************

actual test time:	30.00s
thread count:		32
proc count:		16

CPU |  Usage |  User  |  Kernel |  Idle
-------------------------------------------
   0|  25.68%|   1.30%|   24.38%|  74.32%
   1|  13.44%|   2.08%|   11.35%|  86.56%
   2|  10.68%|   2.45%|    8.23%|  89.32%
   3|   7.92%|   1.93%|    5.99%|  92.08%
   4|   8.65%|   1.72%|    6.93%|  91.35%
   5|   6.93%|   0.68%|    6.25%|  93.07%
   6|   9.84%|   1.98%|    7.86%|  90.16%
   7|   7.19%|   0.36%|    6.82%|  92.81%
   8|  10.10%|   1.93%|    8.18%|  89.90%
   9|  23.13%|   0.52%|   22.60%|  76.88%
  10|  10.68%|   2.24%|    8.44%|  89.32%
  11|   8.39%|   0.47%|    7.92%|  91.61%
  12|   9.58%|   1.15%|    8.44%|  90.42%
  13|   8.02%|   1.20%|    6.82%|  91.98%
  14|   8.33%|   1.30%|    7.03%|  91.67%
  15|  26.41%|   1.46%|   24.95%|  73.59%
-------------------------------------------
avg.|  12.18%|   1.42%|   10.76%|  87.82%

Read IO
thread |       bytes     |     I/Os     |    MiB/s   |  I/O per s | IopsStdDev |  file
-------------------------------------------------------------------------------------------
     0 |       216055808 |        52748 |       6.87 |    1758.24 |    1337.92 | C:\diskspd\iotest.dat (20GiB)
     1 |       215965696 |        52726 |       6.87 |    1757.51 |    1337.39 | C:\diskspd\iotest.dat (20GiB)
     2 |       216875008 |        52948 |       6.89 |    1764.91 |    1346.34 | C:\diskspd\iotest.dat (20GiB)
     3 |       217677824 |        53144 |       6.92 |    1771.44 |    1351.11 | C:\diskspd\iotest.dat (20GiB)
     4 |       217669632 |        53142 |       6.92 |    1771.38 |    1352.21 | C:\diskspd\iotest.dat (20GiB)
     5 |       218787840 |        53415 |       6.95 |    1780.48 |    1359.65 | C:\diskspd\iotest.dat (20GiB)
     6 |       217305088 |        53053 |       6.91 |    1768.41 |    1347.77 | C:\diskspd\iotest.dat (20GiB)
     7 |       218857472 |        53432 |       6.96 |    1781.04 |    1360.48 | C:\diskspd\iotest.dat (20GiB)
     8 |       217423872 |        53082 |       6.91 |    1769.38 |    1348.80 | C:\diskspd\iotest.dat (20GiB)
     9 |       218402816 |        53321 |       6.94 |    1777.34 |    1355.36 | C:\diskspd\iotest.dat (20GiB)
    10 |       216285184 |        52804 |       6.88 |    1760.11 |    1341.47 | C:\diskspd\iotest.dat (20GiB)
    11 |       218664960 |        53385 |       6.95 |    1779.48 |    1360.23 | C:\diskspd\iotest.dat (20GiB)
    12 |       217534464 |        53109 |       6.92 |    1770.28 |    1349.77 | C:\diskspd\iotest.dat (20GiB)
    13 |       216936448 |        52963 |       6.90 |    1765.41 |    1346.01 | C:\diskspd\iotest.dat (20GiB)
    14 |       217292800 |        53050 |       6.91 |    1768.31 |    1349.13 | C:\diskspd\iotest.dat (20GiB)
    15 |       215527424 |        52619 |       6.85 |    1753.94 |    1336.33 | C:\diskspd\iotest.dat (20GiB)
    16 |       215961600 |        52725 |       6.87 |    1757.48 |    1337.91 | C:\diskspd\iotest.dat (20GiB)
    17 |       215941120 |        52720 |       6.86 |    1757.31 |    1338.45 | C:\diskspd\iotest.dat (20GiB)
    18 |       216948736 |        52966 |       6.90 |    1765.51 |    1346.98 | C:\diskspd\iotest.dat (20GiB)
    19 |       217665536 |        53141 |       6.92 |    1771.34 |    1351.25 | C:\diskspd\iotest.dat (20GiB)
    20 |       217726976 |        53156 |       6.92 |    1771.84 |    1352.33 | C:\diskspd\iotest.dat (20GiB)
    21 |       218808320 |        53420 |       6.96 |    1780.64 |    1359.31 | C:\diskspd\iotest.dat (20GiB)
    22 |       217309184 |        53054 |       6.91 |    1768.44 |    1347.57 | C:\diskspd\iotest.dat (20GiB)
    23 |       218951680 |        53455 |       6.96 |    1781.81 |    1360.47 | C:\diskspd\iotest.dat (20GiB)
    24 |       217337856 |        53061 |       6.91 |    1768.68 |    1348.26 | C:\diskspd\iotest.dat (20GiB)
    25 |       218374144 |        53314 |       6.94 |    1777.11 |    1356.26 | C:\diskspd\iotest.dat (20GiB)
    26 |       216285184 |        52804 |       6.88 |    1760.11 |    1341.40 | C:\diskspd\iotest.dat (20GiB)
    27 |       218632192 |        53377 |       6.95 |    1779.21 |    1360.10 | C:\diskspd\iotest.dat (20GiB)
    28 |       217485312 |        53097 |       6.91 |    1769.88 |    1349.64 | C:\diskspd\iotest.dat (20GiB)
    29 |       217137152 |        53012 |       6.90 |    1767.04 |    1345.67 | C:\diskspd\iotest.dat (20GiB)
    30 |       217513984 |        53104 |       6.91 |    1770.11 |    1348.59 | C:\diskspd\iotest.dat (20GiB)
    31 |       215531520 |        52620 |       6.85 |    1753.98 |    1336.88 | C:\diskspd\iotest.dat (20GiB)
-------------------------------------------------------------------------------------------
total:        6954872832 |      1697967 |     221.09 |   56598.20 |   43159.20
```

## r1
```txt

Command Line: C:\diskspd\diskspd.exe -b4K -d30 -o4 -t1 -h -r -w0 -D -Z1G -c20G C:\diskspd\iotest.dat

Input parameters:

	timespan:   1
	-------------
	duration: 30s
	warm up time: 5s
	cool down time: 0s
	gathering IOPS at intervals of 1000ms
	random seed: 0
	path: 'C:\diskspd\iotest.dat'
		think time: 0ms
		burst size: 0
		software cache disabled
		hardware write cache disabled, writethrough on
		write buffer size: 1073741824
		performing read test
		block size: 4096
		using random I/O (alignment: 4096)
		number of outstanding I/O operations: 4
		thread stride size: 0
		threads per file: 1
		using I/O Completion Ports
		IO priority: normal

System information:

	computer name: fedyPC
	start time: 2019/10/17 06:05:48 UTC

Results for timespan 1:
*******************************************************************************

actual test time:	30.00s
thread count:		1
proc count:		16

CPU |  Usage |  User  |  Kernel |  Idle
-------------------------------------------
   0|  94.22%|   3.28%|   90.94%|   5.78%
   1|   2.81%|   0.36%|    2.45%|  97.19%
   2|   4.95%|   2.50%|    2.45%|  95.05%
   3|   2.45%|   1.41%|    1.04%|  97.55%
   4|   3.70%|   1.72%|    1.98%|  96.30%
   5|   0.88%|   0.36%|    0.52%|  99.12%
   6|   3.44%|   2.24%|    1.20%|  96.56%
   7|   1.56%|   0.73%|    0.83%|  98.44%
   8|   5.99%|   2.66%|    3.33%|  94.01%
   9|   1.09%|   0.63%|    0.47%|  98.91%
  10|   3.59%|   1.77%|    1.82%|  96.41%
  11|   0.63%|   0.57%|    0.05%|  99.38%
  12|   2.45%|   1.35%|    1.09%|  97.55%
  13|   1.98%|   1.41%|    0.57%|  98.02%
  14|   2.71%|   1.15%|    1.56%|  97.29%
  15|   5.00%|   1.61%|    3.39%|  95.00%
-------------------------------------------
avg.|   8.59%|   1.48%|    7.11%|  91.41%

Read IO
thread |       bytes     |     I/Os     |    MiB/s   |  I/O per s | IopsStdDev |  file
-------------------------------------------------------------------------------------------
     0 |      7132295168 |      1741283 |     226.73 |   58042.42 |     771.66 | C:\diskspd\iotest.dat (20GiB)
-------------------------------------------------------------------------------------------
total:        7132295168 |      1741283 |     226.73 |   58042.42 |     771.66
```
