# working_environment


- [kubuntu](https://kubuntu.org/)
- [ubuntu](https://ubuntu.com)
- [debian](https://www.debian.org/)
- [raspberry](https://www.raspberrypi.org/downloads/)
- [neon kde](https://neon.kde.org/)

- ## system packages
  - [update](https://github.com/fedy95/working_environment#update--to-contents)
  - [development](https://github.com/fedy95/working_environment#development--to-contents)
    - [ssh](https://github.com/fedy95/working_environment#ssh--to-contents)
    - servers
      - [nginx](https://github.com/fedy95/working_environment#nginx--to-contents)
      - [apache2](https://github.com/fedy95/working_environment#apache2--to-contents)
    - [VPN](https://protonvpn.com/support/linux-vpn-setup/)
  - DB
    - [MySQL](https://github.com/fedy95/working_environment#mysql--to-contents)
    - [MariaDB](https://github.com/fedy95/working_environment#mariadb--to-contents)
  - IDE
    - [phpstorm](https://github.com/fedy95/working_environment#phpstorm--to-contents)
    - [pycharm](https://github.com/fedy95/working_environment#pycharm--to-contents)
    - [idea](https://github.com/fedy95/working_environment#pycharm--to-contents)
    - [clion](https://github.com/fedy95/working_environment#clion--to-contents)
      - [GTest](https://github.com/fedy95/working_environment#gtest--to-contents)
    - [webstorm](https://github.com/fedy95/working_environment#webstorm--to-contents)
    - [upsource](https://github.com/fedy95/working_environment#upsource--to-contents)
  - VM
    - [VMware](https://github.com/fedy95/working_environment#vmware--to-contents)
    - [VirtualBox](https://github.com/fedy95/working_environment#virtualbox--to-contents)
  - [typora](https://www.typora.io/#linux)
  - [nodeJS](https://github.com/fedy95/working_environment#nodejs--to-contents)
  - [filezilla](https://github.com/fedy95/working_environment#filezilla--to-contents)
  - [teamviewer](https://github.com/fedy95/working_environment#teamviewer--to-contents)
  - [zoom](https://github.com/fedy95/working_environment#zoom--to-contents)
  - [KRDC](https://github.com/fedy95/working_environment#krdc--to-contents)
  - [Visual Paradigm](https://github.com/fedy95/working_environment#vp-reset--to-contents)
---
  - ### update | [to contents](https://github.com/fedy95/working_environment#system-packages)
```bash
sudo apt update && sudo apt dist-upgrade
```
    
  - ### development | [to contents](https://github.com/fedy95/working_environment#system-packages)
    - [java](https://www.oracle.com/technetwork/java/javase/downloads/jdk11-downloads-5066655.html)
    - puml
    ```bash
    apt install openjdk-11-jdk -y
    apt install graphviz
    
    ```
    ```
    apt install snapd -y
    apt install git -y
    echo ".idea" > ~/.gitignore
    git config --global core.excludesfile ~/.gitignore
    
    snap install postman
    ```
    - docker
    ```bash
    apt install docker-compose

    ```
    - #### SSH | [to contents](https://github.com/fedy95/working_environment#system-packages)
      ```bash
      apt install ssh -y
      ```
      
      ```bash
      ssh-keygen -t rsa -C "fedy95@protonmail.com"
      cat .ssh/id_rsa.pub
      https://github.com/settings/keys
      ```
      
      - ##### [second account on machine](https://gist.github.com/jexchan/2351996)
      ```bash
      nano config 
         Host github.com       
         HostName github.com
         User git
         IdentityFile ~/.ssh/id_rsa_github
      ssh-keygen -t rsa -C "fedy95.work@protonmail.com"
         /home/ifedorov/.ssh/id_rsa_github_fedy95
      ssh-add id_rsa_github_fedy95
      ssh-add -l
      cat id_rsa_github_fedy95.pub
      https://github.com/settings/keys
      ```
          
    - #### servers
      - ##### nginx | [to contents](https://github.com/fedy95/working_environment#system-packages)
      ```
        apt install nginx -y
      ```
      
      - ##### apache2 | [to contents](https://github.com/fedy95/working_environment#system-packages)
      ```
        apt install apache2 apache2-utils apache2-dev -y
        nano /etc/apache2/ports.conf (8080 8443)
        a2enmod rewrite
        a2enmod expires
        systemctl restart apache2.service
      ```   

  - ### DB
    - #### MySQL | [to contents](https://github.com/fedy95/working_environment#system-packages)
      ```
      apt install mysql-server mysql-client -y
      mysql -uroot
      ```
      ```
      REVOKE ALL ON *.* FROM 'root'@'localhost';
      DROP USER 'root'@'localhost';
      FLUSH PRIVILEGES;
      CREATE USER 'root'@'localhost' IDENTIFIED BY 'rootroot';
      GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';
      exit
      ```
      ```
      nano /etc/mysql/mysql.conf.d/mysqld.cnf
      ```
      ```
      [mysqld]
      character-set-server=utf8
      collation-server=utf8_general_ci
      ```
      ```
      /etc/init.d/mysql restart
      ```
  - #### MariaDB | [to contents](https://github.com/fedy95/working_environment#system-packages)
      ```
      apt install mariadb-server mariadb-client
      mysql -uroot
      ```
      ```
      REVOKE ALL ON *.* FROM 'root'@'localhost';
      DROP USER 'root'@'localhost';
      FLUSH PRIVILEGES;
      CREATE USER 'root'@'localhost' IDENTIFIED BY 'rootroot';
      GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';
      UPDATE mysql.user SET Grant_priv='Y' WHERE User='root';
      exit
      ```   
      ```
      nano /etc/mysql/mariadb.conf.d/50-server.cnf
      ```
      ```
      [mysqld]
      bind-address = 0.0.0.0
      character-set-server=utf8mb4
      collation-server=utf8mb4_general_ci
      ```
      ```
      /etc/init.d/mysql restart
      ```
      
  - ### IDE
    - #### [phpStorm](https://www.jetbrains.com/phpstorm/?fromMenu) | [to contents](https://github.com/fedy95/working_environment#system-packages)
      - [install from package](https://www.jetbrains.com/help/phpstorm/install-and-set-up-product.html)
      
    - #### [pyCharm](https://www.jetbrains.com/pycharm/?fromMenu) | [to contents](https://github.com/fedy95/working_environment#system-packages)
      - [install from package](https://www.jetbrains.com/help/pycharm/install-and-set-up-product.html)
      ```
      snap install pycharm-professional --classic (snap install pycharm-community --classic)
      apt install python3
      update-alternatives --install /usr/bin/python python /usr/bin/python3
      ```
      
    - #### [IDEA](https://www.jetbrains.com/idea/?fromMenu) | [to contents](https://github.com/fedy95/working_environment#system-packages)
      - [install from package](https://www.jetbrains.com/help/idea/install-and-set-up-product.html)
      ```
      sudo apt install gradle
      ```
      
    - #### andorid studio
       ```bash
       sudo apt install qemu-kvm
       sudo adduser <Replace with username> kvm
       sudo chown <Replace with username> /dev/kvm
       ```
 
    - #### [cLion](https://www.jetbrains.com/clion/?fromMen) | [to contents](https://github.com/fedy95/working_environment#system-packages)
      - [install from package](https://www.jetbrains.com/help/clion/install-and-set-up-product.html)   
      - [guide](http://wiki.cs.huji.ac.il/wiki/Installing_CLion_on_Linux)
      ```
      apt install cmake gcc g++ clang gcc-multilib libgtest-dev
      tar xfz ~/Downloads/CLion-*.tar.gz -C /opt
      cd /opt/clion-2018.3.4/bin/
      ./clion.sh
      ```
      
      - ##### GTest | [to contents](https://github.com/fedy95/working_environment#system-packages) | [to contents](https://github.com/fedy95/working_environment#system-packages)
      ```
      apt install libgtest-dev
      cd /usr/src/gtest
      cmake CMakeLists.txt
      make
      cp *.a /usr/lib
      ```
      
    - #### [webstorm](https://www.jetbrains.com/webstorm/?fromMen) | [to contents](https://github.com/fedy95/working_environment#system-packages)
      - [install from package](https://www.jetbrains.com/help/webstorm/install-and-set-up-product.html)
    
    - #### [upsource](https://www.jetbrains.com/upsource/download/#section=linux)  | [to contents](https://github.com/fedy95/working_environment#system-packages)
      - [install](https://www.jetbrains.com/help/upsource/zip-installation.html)
    
  - ### VM
    - ### VMware | [to contents](https://github.com/fedy95/working_environment#system-packages)
      ```bash
      apt install build-essential
      apt install open-vm-tools-desktop
      ```
      
      - [install from package](https://www.vmware.com/products/workstation-player.html)
      ```bash
      chmod +x ~/Downloads/VMware-Player*
      ```
     
      - [tools repository](https://packages.vmware.com/tools/esx/latest/index.html)
      
    - ### VirtualBox | [to contents](https://github.com/fedy95/working_environment#system-packages)
      ```
      apt install virtualbox -y
      ```
  
  - ### [nodeJS](https://github.com/nodesource/distributions/blob/master/README.md#installation-instructions) | [to contents](https://github.com/fedy95/working_environment#system-packages)
    ```
    curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash -
    apt install nodejs -y
    apt install npm -y
    ```
  
  - ### filezilla | [to contents](https://github.com/fedy95/working_environment#system-packages)
    ```
    apt install filezilla -y
    ```
  
  - ### teamviewer | [to contents](https://github.com/fedy95/working_environment#system-packages)
    ```
    apt install gdebi-core
    wget https://download.teamviewer.com/download/linux/teamviewer_amd64.deb
    gdebi teamviewer_amd64.deb
    teamviewer
    ```
  - ### [zoom](https://zoom.us/) | [to contents](https://github.com/fedy95/working_environment#system-packages)
    ```
    apt install libgl1-mesa-glx libegl1-mesa libxcb-xtest0
    dpkg -i zoom_amd64.deb
    sudo apt-get install -f
    ```
    
  - ### KRDC | [to contents](https://github.com/fedy95/working_environment#system-packages)
    ```
    apt install krdc
    ```
    
  - ### VP reset | [to contents](https://github.com/fedy95/working_environment#system-packages)
    ```
    rm -R ~/.config/VisualParadigm/
    ```
### other
- update server timezone
  ```bash
  timedatectl set-timezone Europe/Moscow
  apt install ntp -y
  ```
- mysql remove
  ```bash
  apt remove dbconfig-mysql 
  apt remove --purge mysql*  -y
  apt --purge remove mysql-server 
  apt --purge remove mysql-client 
  apt --purge remove mysql-common 
  apt purge mysql-server mysql-client mysql-common mysql-server-core-5.7 mysql-client-core-5.7 
  rm -rf /etc/mysql /var/lib/mysql 
  apt autoremove -y
  apt autoclean
  
  echo "/usr/sbin/mysqld { }" > /etc/apparmor.d/usr.sbin.mysqld
  apparmor_parser -v -R /etc/apparmor.d/usr.sbin.mysqld
  systemctl restart mariadb
  ```
- mysql
  ```mysql
  CREATE DATABASE NAME;
  CREATE USER 'NAME'@'192.168.%.%' IDENTIFIED BY 'PASS';
  GRANT ALL ON NAME.* TO 'NAME'@'192.168.%.%' IDENTIFIED BY 'PASS' WITH GRANT OPTION;
  
  DROP USER 'mobile_dev'@'192.168.%.%';
  
  SHOW VARIABLES LIKE "%version%";
  ```
