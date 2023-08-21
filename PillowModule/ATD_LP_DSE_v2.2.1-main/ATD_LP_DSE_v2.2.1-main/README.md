# Local_Server_Orangepi_Zero2
This git will competitive with ATLab LCM software

# Uart 5
## 1) create file for uarts
    mkdir -p /sys/kernel/config/device-tree/overlays/ttys5
## 2) create system driver for uart
    sudo cat /boot/dtb/allwinner/overlay/sun50i-h616-uart5.dtbo /sys/kernel/config/device-tree/overlays/ttys5/dtbo
## 3) add uart to uboot : sudo nano /boot/orangepiEnv.txt
    overlays=uart5
## 4) reboot system
    sudo reboot
## 5) check if enable UARTs successfully
    dmesg | grep tty

# I2C3
## 1) create file module
    mkdir -p /sys/kernel/config/device-tree/overlays/i2c-3
## 2) system driver for i2c-3
    sudo cat /boot/dtb/allwinner/overlay/sun50i-h616-i2c3.dtbo /sys/kernel/config/device-tree/overlays/i2c-3/dtbo
## 3) reboot
    sudo reboot
## 3) add i2c-3 to uboot : sudo nano /boot/orangepiEnv.txt
    overlays=i2c3 i2c-dev

# SPI
## 1) create file for spi
    mkdir -p /sys/kernel/config/device-tree/overlays/spi
## 2) create system driver for spi
    sudo cat /boot/dtb/allwinner/overlay/sun50i-h616-spi-spidev.dtbo /sys/kernel/config/device-tree/overlays/spi/dtbo
## 3) add uart to uboot:  sudo nano /boot/orangepiEnv.txt
    overlays=spi-spidev
    param_spidev_spi_bus=1
    param_spidev_spi_cs=1
## 4) reboot system
    sudo reboot
## 5) check if enable UARTs successfully
    dmesg | grep spi


# Install some module for python script

## 1) install python-dev
    sudo apt-get install python-dev
## 2) install python3-dev
    sudo apt-get install python3-dev

## 3) Install 
    apt install python3-pip
    apt-get install libffi-dev

# Create folder atlab
    sudo mkdir /atlab

# Install Samba
# 1.Install samba
    sudo apt-get install samba samba-common-bin
# 2.Config samba to map openhab directory
    sudo nano /etc/samba/smb.conf
# and cope the below code to end of file smc.conf
    [ATD-LP2.1-Embedded]
    path=/atd
    browseable = yes
    read only = no
    guest ok = yes
    writeable = yes

# Influxdb2
## Tutorials: https://portal.influxdata.com/downloads/
    wget -q https://repos.influxdata.com/influxdata-archive_compat.key
##
    echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null
## 
    echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list
##
    sudo apt-get update && sudo apt-get install influxdb2
    sudo apt-get install influxdb2-cli
    sudo systemctl daemon-reload
    sudo systemctl start influxdb
    sudo systemctl status influxdb
### Configure the influxDB to start at boot:
    sudo systemctl enable influxdb.service

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

# OpenVPN server
    sudo apt-get install openvpn unzip

# Services
## Copy the all files in services folder to the /etc/systemd/system 
    sudo systemctl enable atDSE.service
    sudo systemctl enable atOpenVPN.service
    
# NGINX
    sudo apt update
    sudo apt install nginx
# Install npm
    sudo apt install npm
# Json-server
    npm install -g json-server
    
# Database
## After first boot coder need to log inn influxdb2 web-hmi to create a api and copy to database of data.json
