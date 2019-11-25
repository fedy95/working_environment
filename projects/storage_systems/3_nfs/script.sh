#!/usr/bin/env bash

echo i] text

for i in `seq 1 3`;
do
    echo $i] test cp from nfs
    time cp -r ~/Documents/project/text/ ~/Documents/
    rm -r ~/Documents/text/
done

for i in `seq 1 3`;
do
    echo $i] test mv from nfs
    time mv ~/Documents/project/text/ ~/Documents/

    echo $i] test mv to nfs
    time mv ~/Documents/text/ ~/Documents/project/
done

#---
echo ii] single_binary

for i in `seq 1 3`;
do
    echo $i] test cp from nfs
    time cp -r ~/Documents/project/binary/single_binary.zip ~/Documents/
    rm -r ~/Documents/single_binary.zip
done

for i in `seq 1 3`;
do
    echo $i] test mv from nfs
    time mv ~/Documents/project/binary/single_binary.zip ~/Documents/

    echo $i] test mv to nfs
    time mv ~/Documents/single_binary.zip ~/Documents/project/binary/
done

#---
echo iii] multi_binary

for i in `seq 1 3`;
do
    echo $i] test cp from nfs
    time cp -r ~/Documents/project/binary/multi_binary.zip ~/Documents/
    rm -r ~/Documents/multi_binary.zip
done

for i in `seq 1 3`;
do
    echo $i] test mv from nfs
    time mv ~/Documents/project/binary/multi_binary.zip ~/Documents/

    echo $i] test mv to nfs
    time mv ~/Documents/multi_binary.zip ~/Documents/project/binary/
done