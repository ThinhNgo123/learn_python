#!/usr/bin/env python
# pip install pcf8575
# pip install smbus
# apt-get install libffi-dev
import os
try:
    from pcf8575 import PCF8575
except:
    os.system("pip install pcf8575")
    from pcf8575 import PCF8575
from time import sleep

class atKeyboard() :
    i2c_port_num = 3
    pcf_address = 0x21
    pcf = PCF8575(i2c_port_num, pcf_address)
    BT_SW1 = 15
    BT_SW2 = 14
    BT_SW3 = 9
    BT_SW4 = 8
    BT_SW_Up = 13
    BT_SW_Down = 10
    BT_SW_Back = 12
    BT_SW_OK = 11

    LED1_Green = 0
    LED1_Red   = 1
    LED1_Blue   = 2

    LED2_Green = 3
    LED2_Red   = 4
    LED2_Blue   = 5

    BG_LED = 7
    def __init__(self) -> None:
        self.pcf.port = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        pass
    def get_SW(self, switch):
        self.pcf.port[switch] = True
        return self.pcf.port[switch]
    def set_LED(self, port, value):
        port_buffer = self.pcf.port
        port_buffer[port] = value
        self.pcf.port = port_buffer
    
if __name__ == "__main__":
    hmi = atKeyboard()
    while True:
        sleep(0.5)
        print("----------------------------")
        print("SW1: " + str(hmi.get_SW(hmi.BT_SW1)))
        print("SW2: " + str(hmi.get_SW(hmi.BT_SW2)))
        print("SW3: " + str(hmi.get_SW(hmi.BT_SW3)))
        print("SW4: " + str(hmi.get_SW(hmi.BT_SW4)))
        print("SW Up: " + str(hmi.get_SW(hmi.BT_SW_Up)))
        print("SW Down: " + str(hmi.get_SW(hmi.BT_SW_Down)))
        print("SW Back: " + str(hmi.get_SW(hmi.BT_SW_Back)))
        print("SW Ok: " + str(hmi.get_SW(hmi.BT_SW_OK)))

    