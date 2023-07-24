import sys
from time  import sleep
import threading
import os
import json
sys.path.insert(0,"json")
from atJsonData import atData
sys.path.insert(0,"func/mem")
from atUSB import atUSB
class atRestore_USB_Database_Class():
    def __init__(self) -> None:
        self.data = {}
        pass

    def restore(self):
        for usbIndex in atData.data['Memory']['USB']:
            if atData.data['Memory']['USB'][usbIndex]['Status'] == 'Mounted':
                try:
                    file_list = os.listdir( atUSB.USBs_Dir[int(usbIndex)-1])
                    print("List file:",file_list)
                    if "Database" in file_list :
                        path_to_restored = atUSB.USBs_Dir[int(usbIndex)-1] + '/Database/'
                        # delete old bucket
                        os.system("influx bucket delete --name "+atData.data["Database"]["Influxdb2"]['bucket'])
                        # restore
                        os.system(  "influx restore "+path_to_restored )
                        return True
                    else:
                        return False
                except Exception as error:
                    print(error)
        return False

atRestore_USB_Database = atRestore_USB_Database_Class()
if __name__ == '__main__':
    pass
        