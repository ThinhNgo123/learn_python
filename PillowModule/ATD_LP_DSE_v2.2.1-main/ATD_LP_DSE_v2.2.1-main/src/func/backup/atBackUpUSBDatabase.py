import sys
from time  import sleep
import os
import threading
sys.path.insert(0,"json")
from atJsonData import atData
sys.path.insert(0,"func/mem")
from atUSB import atUSB

class atBuck_Up_USB_Database_Class():
    token = ''
    def __init__(self) -> None:
        pass

    def save(self):
        for usbIndex in atData.data['Memory']['USB']:
            if atData.data['Memory']['USB'][usbIndex]['Status'] == 'Mounted':
                self.token = atData.data["Database"]["Influxdb2"]['token']
                try:
                    # check if the old database existed
                    if "Database" in os.listdir(atUSB.USBs_Dir[int(usbIndex)-1]):
                        os.system("sudo rm -rf "+atUSB.USBs_Dir[int(usbIndex)-1] +"/Database")
                    # backup database
                    os.system(  "influx backup "+\
                                atUSB.USBs_Dir[int(usbIndex)-1] +\
                                "/Database "+\
                                "-t " + self.token)
                except Exception as error:
                    print(error)
                return True
        return False

atBuck_Up_USB_Database = atBuck_Up_USB_Database_Class()
if __name__ == '__main__':
    atBuck_Up_USB_Database.save()
    pass
        