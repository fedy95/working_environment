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

### [docker-compose](https://docs.docker.com/compose/install/)
```bash
sudo apt install docker-compose -y
```
or
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

### update
```bash
sudo apt update -y && sudo apt dist-upgrade -y
```

### kubernates
https://wiki.learnlinux.tv/index.php/Setting_up_a_Raspberry_Pi_Kubernetes_Cluster_with_Ubuntu_20.04

```bash
sudo nano /etc/hostname
k8s-master-01 (k8s-worker-01)

sudo nano /etc/hosts
127.0.1.1 k8s-master-01 (127.0.1.1 k8s-worker-01)

sudo reboot
```

```bash
sudo nano /boot/firmware/cmdline.txt 
cgroup_enable=cpuset cgroup_enable=memory cgroup_memory=1 swapaccount=1
sudo apt update -y && sudo apt dist-upgrade -y
sudo reboot
```

```bash
sudo nano /etc/docker/daemon.json
{
 "exec-opts": ["native.cgroupdriver=systemd"],
 "log-driver": "json-file",
 "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
 
sudo nano /etc/sysctl.conf
net.ipv4.ip_forward=1
sudo reboot

sudo nano /etc/apt/sources.list.d/kubernetes.list
deb http://apt.kubernetes.io/ kubernetes-xenial main
 
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt update -y

sudo apt install kubeadm kubectl kubelet -y
```

#### master-only
```bash
sudo kubeadm init --pod-network-cidr=10.244.0.0/16

# copy and save kubeamd join..

mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
kubectl get pods --all-namespaces
kubectl get nodes

```

##### run sudo kubeamd joi for workers