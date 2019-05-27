# working_environment


## system packages

- [development](https://github.com/fedy95/working_environment/wiki/linux#development)
- [ssh](https://github.com/fedy95/working_environment/wiki/linux#ssh)
- [apache](https://github.com/fedy95/working_environment/wiki/linux#apache)
- [mysql](https://github.com/fedy95/working_environment/wiki/linux#mysql)
- [php](https://github.com/fedy95/working_environment/wiki/linux#php)
  - [oci8](https://github.com/fedy95/working_environment/wiki/linux#oci8)
  - [pdo_oci](https://github.com/fedy95/working_environment/wiki/linux#pdo_oci)
- [composer](https://github.com/fedy95/working_environment/wiki/linux#composer)
- [ide](https://github.com/fedy95/working_environment/wiki/linux#ide)
  - [phpstorm](https://github.com/fedy95/working_environment/wiki/linux#phpstorm)
  - [pycharm](https://github.com/fedy95/working_environment/wiki/linux#pycharm)
  - [clion](https://github.com/fedy95/working_environment/wiki/linux#clion)
  - [webstorm](https://github.com/fedy95/working_environment/wiki/linux#webstorm)
  - [brackets](https://github.com/fedy95/working_environment/wiki/linux#brackets)
  - [visual code](https://github.com/fedy95/working_environment/wiki/linux#visual-code)
  - [atom](https://github.com/fedy95/working_environment/wiki/linux#atom)
  - [nuclide](https://github.com/fedy95/working_environment/wiki/linux#nuclide)
  - [android studio](https://github.com/fedy95/working_environment/wiki/linux#android-studio)
- [nodejs](https://github.com/fedy95/working_environment/wiki/linux#nodejs)
- [filezilla](https://github.com/fedy95/working_environment/wiki/linux#filezilla)
- VM
  - [vmware](https://github.com/fedy95/working_environment/wiki/linux#vmware)
  - [virtualbox](https://github.com/fedy95/working_environment/wiki/linux#virtualbox)
- [teamviewer](https://github.com/fedy95/working_environment/wiki/linux#teamviewer)
- [Visual Paradigm](https://github.com/fedy95/working_environment/wiki/linux#vp-reset)

# VMWare
- apt install build-essential
- apt install open-vm-tools-desktop
- https://www.vmware.com/products/workstation-player.html
- chmod +x ~/Downloads/VMware-Player*
- sudo ~/Downloads/VMware-Player*

# VP reset
- sudo rm -R ~/.config/VisualParadigm/

# development
- apt install snapd -y
- apt install nginx -y
- apt install git -y
- apt install ssh -y
- snap install postman

## SSH
- ssh-keygen -t rsa -C "fedy95@protonmail.com" 
- cat .ssh/id_rsa.pub 
- https://github.com/settings/keys

### [Second account on machine](https://gist.github.com/jexchan/2351996)
- nano config 
```
Host github.com       
HostName github.com
User git
IdentityFile ~/.ssh/id_rsa_github
```
- ssh-keygen -t rsa -C "fedy95@protonmail.com"
  - Enter file in which to save the key (/home/ifedorov/.ssh/id_rsa): /home/ifedorov/.ssh/id_rsa_github_fedy95
  - Enter passphrase (empty for no passphrase): 
  - Enter same passphrase again: 
- ssh-add id_rsa_github_fedy95
- ssh-add -l
- cat id_rsa_github_fedy95.pub
- https://github.com/settings/keys

## apache
   - apt install apache2 apache2-utils apache2-dev -y
   - nano /etc/apache2/ports.conf (8080 8443)
   - a2enmod rewrite
   - a2enmod expires
   - systemctl restart apache2.service
## mysql
   - apt install mysql-server mysql-client -y
   - mysql -uroot
     - REVOKE ALL ON \*.\* FROM 'root'@'localhost';
     - DROP USER 'root'@'localhost';
     - FLUSH PRIVILEGES;
     - CREATE USER 'root'@'localhost' IDENTIFIED BY 'rootroot';
     - GRANT ALL PRIVILEGES ON \*.\* TO 'root'@'localhost';
     - exit
   - update default charset
     - nano /etc/mysql/mysql.conf.d/mysqld.cnf
```
...
[mysqld]
character-set-server=utf8
collation-server=utf8_general_ci
...
```
      - /etc/init.d/mysql restart
## php
   - add-apt-repository ppa:ondrej/php *(apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv-keys 14AA40EC0831756756D7F66C4F4EA0AAE5267A6C)*
   - apt update -y

### 7.1
   - apt install php7.1 php7.1-dev php7.1-common libapache2-mod-php7.1 php7.1-fpm php7.1-mysql php7.1-mbstring php7.1-readline php7.1-fpm php7.1-cli php7.1-curl php7.1-gd php7.1-xdebug php7.1-soap php7.1-curl php7.1-xsl php7.1-xml php7.1-intl php7.1-zip php7.1-curl php7.1-apcu php7.1-odbc php7.1-sqlite3 php7.1-curl php7.1-bcmath -y
   - nano /etc/php/7.1/mods-available/xdebug.ini
     - `xdebug.remote_enable=1`
     - `xdebug.idekey="PHPSTORM"`
     - `xdebug.max_nesting_level=150`
     - `xdebug.default_enable=1`
     - `xdebug.remote_host=127.0.0.1`
     - `xdebug.remote_port=9000`
     - `xdebug.remote_handler=dbgp`
     - `xdebug.remote_connect_back=1`
     - `xdebug.remote_autostart=1`
   - systemctl restart apache2.service
   - a2enmod proxy_fcgi setenvif
   - a2enconf php7.1-fpm
   - nano /etc/php/7.1/apache2/php.ini
   - nano /etc/php/7.1/cli/php.ini
   - nano /etc/php/7.1/fpm/php.ini
     - `short_open_tag = On`
   - systemctl restart apache2.service

### oci8
*PHP>=7.0, instantclient>=12.1.0.2.0, oci8>=2.0.12*

Загрузить пакеты oracle [instantclient](https://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html)
- instantclient-basic-linux.x64-12.2.0.1.0.zip;
- iinstantclient-sdk-linux.x64-12.2.0.1.0.zip.

- apt-get install php-pear build-essential libaio1
- unzip instantclient-basic-linux.x64-12.2.0.1.0.zip
- unzip instantclient-sdk-linux.x64-12.2.0.1.0.zip
- mkdir /opt/oracle
- mv /home/ifedorov/Downloads/instantclient_12_2/ /opt/oracle/
- cd /opt/oracle/instantclient_12_2/
- ln -s /opt/oracle/instantclient_12_2/libclntsh.so.12.1 /opt/oracle/instantclient_12_2/libclntsh.so
- ln -s /opt/oracle/instantclient_12_2/libocci.so.12.1 /opt/oracle/instantclient_12_2/libocci.so
- echo "/opt/oracle/instantclient_12_2" >> /etc/ld.so.conf.d/oracle-instantclient
- pecl install oci8-2.2.0
  - instantclient,/opt/oracle/instantclient_12_2

- echo "extension = oci8.so" >> /etc/php/7.1/apache2/php.ini
- echo "extension = oci8.so" >> /etc/php/7.1/fpm/php.ini
- echo "extension = oci8.so" >> /etc/php/7.1/cli/php.ini
- nano /etc/profile
  - LD_LIBRARY_PATH=/opt/oracle/instantclient_12_2:$LD_LIBRARY_PATH
  - PATH=/opt/oracle/instantclient_12_2:$PATH
- nano /etc/environment
  - LD_LIBRARY_PATH=/opt/oracle/instantclient_12_2:$LD_LIBRARY_PATH
  - ORACLE_HOME=/opt/oracle/instantclient_12_2:$ORACLE_HOME
- nano /etc/apache2/envvars
  - export LD_LIBRARY_PATH=/opt/oracle/instantclient_12_2
  - export ORACLE_HOME=/opt/oracle/instantclient_12_2
- echo "/opt/oracle/instantclient_12_2" >> /etc/ld.so.conf.d/oracle-instantclient.conf
- ldconfig
- service php7.1-fpm restart
- service apache2 restart

### PDO_OCI
- git clone -b PHP-7.#.# https://github.com/php/php-src && cd php-src 
- cd ext/pdo_oci
- phpize
  - ./configure --with-pdo-oci=instantclient,/opt/oracle/instantclient_12_2,12.2  
- make 
- make install 
- echo "extension = pdo_oci.so" >> /etc/php/7.1/apache2/php.ini
- echo "extension = pdo_oci.so" >> /etc/php/7.1/fpm/php.ini
- echo "extension = pdo_oci.so" >> /etc/php/7.1/cli/php.ini
- service php7.1-fpm restart
- service apache2 restart

## composer
- [install](https://getcomposer.org/download/)
- mv composer.phar /usr/local/bin/composer 

# IDE
- ## [phpStorm](https://www.jetbrains.com/phpstorm/?fromMenu) 
     - [install from package](https://www.jetbrains.com/help/phpstorm/install-and-set-up-product.html)
     - sudo snap install phpstorm --classic
- ## [pyCharm](https://www.jetbrains.com/pycharm/?fromMenu)
     - [install from package](https://www.jetbrains.com/help/pycharm/install-and-set-up-product.html)
     - sudo snap install pycharm-community --classic
     - sudo snap install pycharm-professional --classic
  -  ### python
      - apt install python3
      - update-alternatives --install /usr/bin/python python /usr/bin/python3


      - apt install python3-venv
      - apt install python3-pip (sudo apt install python-pip)
      - pip install Flask
- ## [cLion](https://www.jetbrains.com/clion/?fromMen)
     - [install from package](https://www.jetbrains.com/help/clion/install-and-set-up-product.html)
     - [guide](http://wiki.cs.huji.ac.il/wiki/Installing_CLion_on_Linux)
     - sudo apt install cmake gcc g++ clang gcc-multilib libgtest-dev
     - ### Google tests
       - sudo apt install libgtest-dev
       - cd /usr/src/gtest
       - sudo cmake CMakeLists.txt
       - sudo make
       - sudo cp *.a /usr/lib
     - sudo tar xfz ~/Downloads/CLion-*.tar.gz -C /opt
     - cd /opt/clion-2018.3.4/bin/
     - ./clion.sh
- ## [webstorm](https://www.jetbrains.com/webstorm/?fromMen)
     - [install from package](https://www.jetbrains.com/help/webstorm/install-and-set-up-product.html)
     - sudo snap install webstorm --classic
- ## brackets
     - add-apt-repository ppa:webupd8team/brackets
     - apt update
     - apt install brackets
- ## visual code
- ## atom
     - // apt update
     - // apt install software-properties-common apt-transport-https wget
     - // wget -q https://packagecloud.io/AtomEditor/atom/gpgkey -O- | apt-key add -
     - // add-apt-repository "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main"
     - snap install --classic atom
- ## nuclide
- ## android studio

## [NodeJS](https://github.com/nodesource/distributions/blob/master/README.md#installation-instructions)
- curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash -
- apt install nodejs -y

## filezilla
- apt install filezilla -y

## virtualbox
- apt install virtualbox -y

## teamviewer
- sudo apt install gdebi-core
- wget https://download.teamviewer.com/download/linux/teamviewer_amd64.deb
- sudo gdebi teamviewer_amd64.deb
- teamviewer
