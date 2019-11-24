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
echo ii] binary zip

for i in `seq 1 3`;
do
    echo $i] test cp from nfs
    time cp -r ~/Documents/project/binary/randombinary1.zip ~/Documents/
    rm -r ~/Documents/randombinary1.zip
done

for i in `seq 1 3`;
do
    echo $i] test mv from nfs
    time mv ~/Documents/project/binary/randombinary1.zip ~/Documents/

    echo $i] test mv to nfs
    time mv ~/Documents/randombinary1.zip ~/Documents/project/binary/
done

#---
echo iii] binary

for i in `seq 1 3`;
do
    echo $i] test cp from nfs
    time cp -r ~/Documents/project/binary/randombinary1 ~/Documents/
    rm -r ~/Documents/randombinary1
done

for i in `seq 1 3`;
do
    echo $i] test mv from nfs
    time mv ~/Documents/project/binary/randombinary1 ~/Documents/

    echo $i] test mv to nfs
    time mv ~/Documents/randombinary1 ~/Documents/project/binary/
done