# working_environment

- [neon kde](https://neon.kde.org/)
- [ubuntu](https://ubuntu.com)
- [debian](https://www.debian.org/)
- [raspberry](https://www.raspberrypi.org/downloads/)

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
  - PHP
    - [7.1](https://github.com/fedy95/working_environment#71--to-contents)
    - [7.3](https://github.com/fedy95/working_environment#73--to-contents)
    - [oci8](https://github.com/fedy95/working_environment#oci8-php70-instantclient121020-oci82012--to-contents)
    - [PDO_OCI](https://github.com/fedy95/working_environment#pdo_oci--to-contents)
    - [composer](https://github.com/fedy95/working_environment#composer--to-contents)
  - IDE
    - [phpstorm](https://github.com/fedy95/working_environment#phpstorm--to-contents)
    - [pycharm](https://github.com/fedy95/working_environment#pycharm--to-contents)
    - [idea](https://github.com/fedy95/working_environment#pycharm--to-contents)
    - [clion](https://github.com/fedy95/working_environment#clion--to-contents)
      - [GTest](https://github.com/fedy95/working_environment#gtest--to-contents)
    - [webstorm](https://github.com/fedy95/working_environment#webstorm--to-contents)
  - VM
    - [VMware](https://github.com/fedy95/working_environment#vmware--to-contents)
    - [VirtualBox](https://github.com/fedy95/working_environment#virtualbox--to-contents)
  - [nodeJS](https://github.com/fedy95/working_environment#nodejs--to-contents)
  - [filezilla](https://github.com/fedy95/working_environment#filezilla--to-contents)
  - [teamviewer](https://github.com/fedy95/working_environment#teamviewer--to-contents)
  - [KRDC](https://github.com/fedy95/working_environment#krdc--to-contents)
  - [Visual Paradigm](https://github.com/fedy95/working_environment#vp-reset--to-contents)
---
  - ### update | [to contents](https://github.com/fedy95/working_environment#system-packages)
    ```
    apt update
    apt dist-upgrade
    ```
    
  - ### development | [to contents](https://github.com/fedy95/working_environment#system-packages)
    ```
    apt install openjdk-11-jre -y
    apt install snapd -y
    apt install git -y
    snap install postman
    ```
      
    - #### SSH | [to contents](https://github.com/fedy95/working_environment#system-packages)
      ```
      apt install ssh -y
      ```
      
      ```
      ssh-keygen -t rsa -C "fedy95@protonmail.com"
      cat .ssh/id_rsa.pub
      https://github.com/settings/keys
      ```
      
      - ##### [second account on machine](https://gist.github.com/jexchan/2351996)
      ```
      nano config 
       - Host github.com       
       - HostName github.com
       - User git
       - IdentityFile ~/.ssh/id_rsa_github
      ssh-keygen -t rsa -C "fedy95@protonmail.com"
       - Enter file in which to save the key (/home/ifedorov/.ssh/id_rsa): /home/ifedorov/.ssh/id_rsa_github_fedy95
       - Enter passphrase (empty for no passphrase): 
       - Enter same passphrase again: 
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
      exit
      ```   
      ```
      nano /etc/mysql/my.cnf
      ```
      ```
      [mysqld]
      character-set-server=utf8
      collation-server=utf8_general_ci
      ```
      ```
      /etc/init.d/mysql restart
      ```
      
  - ### PHP
    - #### 7.1 | [to contents](https://github.com/fedy95/working_environment#system-packages)
      ```
      add-apt-repository ppa:ondrej/php *(apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv-keys 14AA40EC0831756756D7F66C4F4EA0AAE5267A6C)*
      apt update -y
      ```
      ```
      apt install php7.1 php7.1-dev php7.1-common libapache2-mod-php7.1 php7.1-fpm php7.1-mysql php7.1-mbstring php7.1-readline php7.1-fpm php7.1-cli php7.1-curl php7.1-gd php7.1-xdebug php7.1-soap php7.1-curl php7.1-xsl php7.1-xml php7.1-intl php7.1-zip php7.1-curl php7.1-apcu php7.1-odbc php7.1-sqlite3 php7.1-curl php7.1-bcmath php7.1-imagick -y
      nano /etc/php/7.1/mods-available/xdebug.ini
       - `xdebug.remote_enable=1`
       - `xdebug.idekey="PHPSTORM"`
       - `xdebug.max_nesting_level=150`
       - `xdebug.default_enable=1`
       - `xdebug.remote_host=127.0.0.1`
       - `xdebug.remote_port=9000`
       - `xdebug.remote_handler=dbgp`
       - `xdebug.remote_connect_back=1`
       - `xdebug.remote_autostart=1`
      systemctl restart apache2.service
      a2enmod proxy_fcgi setenvif
      a2enconf php7.1-fpm
      nano /etc/php/7.1/apache2/php.ini
      nano /etc/php/7.1/cli/php.ini
      nano /etc/php/7.1/fpm/php.ini
       - `short_open_tag = On`
      systemctl restart apache2.service
      ```
    - #### 7.3 | [to contents](https://github.com/fedy95/working_environment#system-packages)
      ```
      add-apt-repository ppa:ondrej/php
      - or (apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv-keys 14AA40EC0831756756D7F66C4F4EA0AAE5267A6C)
      apt update -y
      apt dist-upgrade
      ```
      ```
      apt install php7.3 php7.3-dev php7.3-common php7.3-fpm php7.3-mysql php7.3-mbstring php7.3-readline php7.3-fpm php7.3-cli php7.3-curl php7.3-gd php7.3-xdebug php7.3-soap php7.3-curl php7.3-xsl php7.3-xml php7.3-intl php7.3-zip php7.3-curl php7.3-apcu php7.3-odbc php7.3-sqlite3 php7.3-curl php7.3-bcmath php7.3-imagick -y
      
      apt install php php-dev php-common php-fpm php-mysql php-mbstring php-readline php-fpm php-cli php-curl php-gd php-xdebug php-soap php-curl php-xsl php-xml php-intl php-zip php-curl php-apcu php-odbc php-sqlite3 php-curl php-bcmath php-imagick -y
      
      nano /etc/php/7.3/mods-available/xdebug.ini
      ```
      ```
      xdebug.remote_enable=1
      xdebug.idekey="PHPSTORM"
      xdebug.max_nesting_level=1000
      xdebug.default_enable=1
      xdebug.remote_host=127.0.0.1
      xdebug.remote_port=9000
      xdebug.remote_handler=dbgp
      xdebug.remote_connect_back=1
      xdebug.remote_autostart=1
      ```
    - #### oci8 (*PHP>=7.0, instantclient>=12.1.0.2.0, oci8>=2.0.12*) | [to contents](https://github.com/fedy95/working_environment#system-packages)
      ```
      - Download packages [instantclient](https://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html)
        - instantclient-basic-linux.x64-12.2.0.1.0.zip;
        - iinstantclient-sdk-linux.x64-12.2.0.1.0.zip.
       
      apt-get install php-pear build-essential libaio1
      unzip instantclient-basic-linux.x64-12.2.0.1.0.zip
      unzip instantclient-sdk-linux.x64-12.2.0.1.0.zip
      mkdir /opt/oracle
      mv /home/ifedorov/Downloads/instantclient_12_2/ /opt/oracle/
      cd /opt/oracle/instantclient_12_2/
      ln -s /opt/oracle/instantclient_12_2/libclntsh.so.12.1 /opt/oracle/instantclient_12_2/libclntsh.so
      ln -s /opt/oracle/instantclient_12_2/libocci.so.12.1 /opt/oracle/instantclient_12_2/libocci.so
      echo "/opt/oracle/instantclient_12_2" >> /etc/ld.so.conf.d/oracle-instantclient
      pecl install oci8-2.2.0
       - instantclient,/opt/oracle/instantclient_12_2
        
      echo "extension = oci8.so" >> /etc/php/7.1/apache2/php.ini
      echo "extension = oci8.so" >> /etc/php/7.1/fpm/php.ini
      echo "extension = oci8.so" >> /etc/php/7.1/cli/php.ini
      nano /etc/profile
       - LD_LIBRARY_PATH=/opt/oracle/instantclient_12_2:$LD_LIBRARY_PATH
       - PATH=/opt/oracle/instantclient_12_2:$PATH
      nano /etc/environment
       - LD_LIBRARY_PATH=/opt/oracle/instantclient_12_2:$LD_LIBRARY_PATH
       - ORACLE_HOME=/opt/oracle/instantclient_12_2:$ORACLE_HOME
      nano /etc/apache2/envvars
       - export LD_LIBRARY_PATH=/opt/oracle/instantclient_12_2
       - export ORACLE_HOME=/opt/oracle/instantclient_12_2
      echo "/opt/oracle/instantclient_12_2" >> /etc/ld.so.conf.d/oracle-instantclient.conf
      ldconfig
      service php7.1-fpm restart
      service apache2 restart
      ```
      
    - #### PDO_OCI | [to contents](https://github.com/fedy95/working_environment#system-packages)
      ```
      git clone -b PHP-7.#.# https://github.com/php/php-src && cd php-src 
      cd ext/pdo_oci
      phpize
       - ./configure --with-pdo-oci=instantclient,/opt/oracle/instantclient_12_2,12.2  
      make 
      make install 
      echo "extension = pdo_oci.so" >> /etc/php/7.1/apache2/php.ini
      echo "extension = pdo_oci.so" >> /etc/php/7.1/fpm/php.ini
      echo "extension = pdo_oci.so" >> /etc/php/7.1/cli/php.ini
      service php7.1-fpm restart
      service apache2 restart
      ```
      
    - #### composer | [to contents](https://github.com/fedy95/working_environment#system-packages)
      ```
      - [install](https://getcomposer.org/download/)
      mv composer.phar /usr/local/bin/composer 
      ```
      
  - ### IDE
    - #### [phpStorm](https://www.jetbrains.com/phpstorm/?fromMenu) | [to contents](https://github.com/fedy95/working_environment#system-packages)
      - [install from package](https://www.jetbrains.com/help/phpstorm/install-and-set-up-product.html)
      ```
      snap install phpstorm --classic
      ```
      
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
      snap install intellij-idea-ultimate --classic
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
    ```
    snap install webstorm --classic
    ```
 
  - ### VM
    - ### VMware | [to contents](https://github.com/fedy95/working_environment#system-packages)
      ```
      apt install build-essential
      apt install open-vm-tools-desktop
      - [install from package](https://www.vmware.com/products/workstation-player.html)
      chmod +x ~/Downloads/VMware-Player*
      ~/Downloads/VMware-Player*
      
      apt install open-vm-tools-desktop
      apt install open-vm-tools
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
  ```
  timedatectl set-timezone Europe/Moscow
  apt install ntp -y
  ```
- mysql remove
  ```
  apt remove dbconfig-mysql 
  apt remove --purge mysql*  -y
  apt --purge remove mysql-server 
  apt --purge remove mysql-client 
  apt --purge remove mysql-common 
  apt purge mysql-server mysql-client mysql-common mysql-server-core-5.7 mysql-client-core-5.7 
  rm -rf /etc/mysql /var/lib/mysql 
  apt autoremove -y
  apt autoclean
  ```
