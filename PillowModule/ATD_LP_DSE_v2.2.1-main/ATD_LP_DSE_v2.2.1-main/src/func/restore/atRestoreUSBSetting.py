import sys
from time  import sleep
import threading
import os
import json
sys.path.insert(0,"json")
from atJsonData import atData
sys.path.insert(0,"func/mem")
from atUSB import atUSB
class atRestore_USB_Setting_Class():
    def __init__(self) -> None:
        self.data = {}
        pass

    def restore(self):
        for usbIndex in atData.data['Memory']['USB']:
            if atData.data['Memory']['USB'][usbIndex]['Status'] == 'Mounted':
                path_to_restored = atUSB.USBs_Dir[int(usbIndex)-1] + '/Data.json'
                try:
                    # open and load data form Path
                    self.file_json = open(path_to_restored)
                    self.data = json.load(self.file_json)
                    atData.data = self.data
                    atData.save()
                    return True
                except Exception as error:
                    print(error)
        return False

atRestore_USB_Setting = atRestore_USB_Setting_Class()
if __name__ == '__main__':
    pass
        