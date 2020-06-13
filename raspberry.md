# ssh
```bash
adduser fedy95
usermod -aG sudo fedy95
su - fedy95

apt install ssh -y
ssh-keygen -t rsa -C "fedy95@protonmail.com"

sudo -i
mkdir /media/usb
mount -t vfat /dev/sda1 /media/usb -o uid=1000
cp -r /home/fedy95/.ssh /media/usb

cd
umount /media/usb
```

### [docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script)
```bash
mkdir _temp
cd _temp
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo usermod -aG docker USER_NAME
```

### update
```bash
apt update
apt dist-upgrade
```
