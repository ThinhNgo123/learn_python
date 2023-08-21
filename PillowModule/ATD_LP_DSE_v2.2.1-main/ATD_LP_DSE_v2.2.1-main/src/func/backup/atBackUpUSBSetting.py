import sys
from time  import sleep
import os
import threading
sys.path.insert(0,"json")
from atJsonData import atData
sys.path.insert(0,"func/mem")
from atUSB import atUSB
class atBuck_Up_USB_Setting_Class():
    
    PATH_USB_1 = '/media/usb1'
    def __init__(self) -> None:
        pass

    def save(self):
        for usbIndex in atData.data['Memory']['USB']:
            if atData.data['Memory']['USB'][usbIndex]['Status'] == 'Mounted':
                os.system("sudo cp "+atData.DATA_PATH+" "+atUSB.USBs_Dir[int(usbIndex)-1])
                return True
        return False

atBuck_Up_USB_Setting = atBuck_Up_USB_Setting_Class()
if __name__ == '__main__':
    atBuck_Up_USB_Setting.save()
    pass
        