#!/usr/bin/env bash

for i in `seq 1 3`;
do
    echo $i] test cp from nfs
    time cp -r /home/fedy95/Documents/project/xzzzaiaxhh/ /home/fedy95/Documents/
    rm -r /home/fedy95/Documents/xzzzaiaxhh/
done

for i in `seq 1 3`;
do
    echo $i] test mv from nfs
    time mv /home/fedy95/Documents/project/xzzzaiaxhh/ /home/fedy95/Documents/

    echo $i] test mv to nfs
    time mv /home/fedy95/Documents/xzzzaiaxhh/ /home/fedy95/Documents/project/
done
