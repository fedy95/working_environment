# nfs
 
- [ubuntu wiki](https://help.ubuntu.com/lts/serverguide/network-file-system.html)

### architecture
![img](https://github.com/fedy95/working_enviroment/tree/master/projects/storage_systems/3_nfs/schema/png/deployment.png)
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