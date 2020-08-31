# working_environment


- [kubuntu](https://kubuntu.org/)
- [ubuntu](https://ubuntu.com)
- [debian](https://www.debian.org/)
- [raspberry](https://www.raspberrypi.org/downloads/)
- [neon kde](https://neon.kde.org/)
- [manjaro](https://manjaro.org/)

- ## system packages
  - [update](https://github.com/fedy95/working_environment#update--to-contents)
  - [development](https://github.com/fedy95/working_environment#development--to-contents)
    - [ssh](https://github.com/fedy95/working_environment#ssh--to-contents)
  - IDE
    - [phpstorm](https://github.com/fedy95/working_environment#phpstorm--to-contents)
    - [pycharm](https://github.com/fedy95/working_environment#pycharm--to-contents)
    - [idea](https://github.com/fedy95/working_environment#pycharm--to-contents)
    - [clion](https://github.com/fedy95/working_environment#clion--to-contents)
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
    
