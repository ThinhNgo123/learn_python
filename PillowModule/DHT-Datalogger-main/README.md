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

# Enable SPI port 4.2
  sudo nano /boot/orangepiEnv.txt
## paste it into the last line
  overlays=spi4-m0-cs1-spidev