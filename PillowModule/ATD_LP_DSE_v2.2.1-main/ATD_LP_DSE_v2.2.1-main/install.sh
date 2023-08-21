#!/bin/bash

# Author : Nguyen Trinh Tuan
# Copyright (c) atlab.vn
# Script follows here:

echo "ATD-LP2.1"
yes | sudo apt update
yes | sudo apt upgrade
echo "Installing all lib and module"
echo "Setting hardware"
sudo mkdir -p /sys/kernel/config/device-tree/overlays/ttys5
sleep 0.1
sudo cat /boot/dtb/allwinner/overlay/sun50i-h616-uart5.dtbo /sys/kernel/config/device-tree/overlays/ttys5/dtbo
sleep 0.1
sudo mkdir -p /sys/kernel/config/device-tree/overlays/i2c-3
sleep 0.1
sudo cat /boot/dtb/allwinner/overlay/sun50i-h616-i2c3.dtbo /sys/kernel/config/device-tree/overlays/i2c-3/dtbo
sleep 0.1

sudo mkdir -p /sys/kernel/config/device-tree/overlays/spi
sleep 0.1
sudo cat /boot/dtb/allwinner/overlay/sun50i-h616-spi-spidev.dtbo /sys/kernel/config/device-tree/overlays/spi/dtbo

sudo echo "overlays=uart5 i2c3 i2c-dev spi-spidev" >> /boot/orangepiEnv.txt
sudo echo "param_spidev_spi_bus=1" >> /boot/orangepiEnv.txt
sudo echo "param_spidev_spi_cs=1" >> /boot/orangepiEnv.txt

## 1) install python-dev
yes | sudo apt-get install python-dev
## 2) install python3-dev
yes | sudo apt-get install python3-dev
## 3) Install 
yes | sudo apt install python3-pip
yes | sudo apt-get install libffi-dev


# # Create folder atd_lp
# sudo mkdir /atd
# # Install Samba
# # 1.Install samba
# yes | sudo apt-get install samba samba-common-bin
# # 2.Config samba to map openhab directory
# # and cope the below code to end of file smc.conf

# sleep 0.2
# sudo echo "[ATD-LP2.1-Embedded]" >> /etc/samba/smb.conf
# sudo echo "path=/atd_lp" >> /etc/samba/smb.conf
# sudo echo "browseable = yes" >> /etc/samba/smb.conf
# sudo echo "read only = no" >> /etc/samba/smb.conf
# sudo echo "guest ok = yes" >> /etc/samba/smb.conf
# sudo echo "writeable = yes" >> /etc/samba/smb.conf

# Influxdb2
## Tutorials: https://portal.influxdata.com/downloads/
wget -q https://repos.influxdata.com/influxdata-archive_compat.key
sleep 1
##
echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null
sleep 1
## 
echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list
##
sleep 1
yes | sudo apt update
yes | sudo apt-get install influxdb2
sleep 1
yes | sudo apt-get install influxdb2-cli
sleep 1
sudo systemctl daemon-reload
sleep 1
sudo systemctl start influxdb
sleep 1
    # sudo systemctl status influxdb
### Configure the influxDB to start at boot:
sudo systemctl enable influxdb.service
sleep 1

## init influxdb
influx setup \
--org atlab \
--bucket atlab \
--username atlab \
--password abc123123 \
--force
## create a config for influxdb2-cli
influx config create \
-n atlab_config \
-u http://localhost:8086 \
-p atlab:abc123123 \
-o atlab
# Install openvpn and unzip
yes | sudo apt-get install openvpn unzip

# NGINX
yes | sudo apt install nginx
sudo rm -rf /var/www/html/*
sleep 1
sudo cp -R web_server/* /var/www/html
# Install npm
yes | sudo apt install npm
# Json-server
yes | npm install -g json-server

# source python
sudo mkdir /atd
sudo mkdir /atd/src
sleep 1
sudo cp -r src/* /atd/src
# Services
## Copy the all files in services folder to the /etc/systemd/system 
sudo cp services/atDSE.service /etc/systemd/system/atDSE.service
sudo cp services/atOpenVPN.service /etc/systemd/system/atOpenVPN.service
sleep 1

# Set time zone 
sudo timedatectl set-timezone Asia/Ho_Chi_Minh

# Set these services start up when power up
echo "start atDSE service"
sudo systemctl start atDSE.service
echo "start OpenVPN service"
sudo systemctl start atOpenVPN.service
sleep 1

# Set these services start up when power up
sudo systemctl enable atDSE.service
sudo systemctl enable atOpenVPN.service


echo "Restart in 5"
sleep 1
echo "Restart in 3"
sleep 1
echo "Restart in 2"
sleep 1
echo "Restart in 1"
sleep 1
echo "Restart in 0"

sudo reboot
