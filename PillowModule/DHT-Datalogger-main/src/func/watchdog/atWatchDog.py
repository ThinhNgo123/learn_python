import sys
from time  import sleep
import threading
import sys

sys.path.insert(0,"json")
from atJsonData import atData

# sys.path.insert(0,'hmi')
# from atScreens import atScreens

sys.path.insert(0,'func/sensor')
from atSensor import atSensor

# sys.path.insert(0,'func/monitor')
# from atMonitor import atMonitor

sys.path.insert(0, 'func/influx')
from atInfluxDB import atInfluxDB

sys.path.insert(0, 'func/ftp')
from atFTPServer import atFTP_1_Server

sys.path.insert(0, 'func/logger')
from atLogger_TT10 import atLogger_TT10

sys.path.insert(0, 'func/mem')
from atDiskSpace import atDisk_Space
from atUSB import atUSB

sys.path.insert(0, 'func/internet')
from atInternet  import atInternet

sys.path.insert(0, 'func/json_server')
from atJsonServer  import atJsonServer

# sys.path.insert(0, 'func/relay')
# from atRelay  import atRelay

sys.path.insert(0, 'func/power')
from atPower  import atPower

class atWatchDog_Class():
    def __init__(self) -> None:
        self.error_count = 0
        self.error_number_to_reboot = 50
        self.thread = threading.Thread(target=self._thread_auto_reset_to_fix_error)
        pass

    def _thread_auto_reset_to_fix_error(self):
        sleep(10)
        while(1):
            sleep(2)
            for ftp_server_name in atData.data["FTP_Servers"]:
                ftp_server = atData.data["FTP_Servers"][ftp_server_name]
                if  ftp_server["Activate"] == "Enable" and \
                    atData.data["Internet"]["Ethernet"]["IP"] is not None and \
                    ftp_server["Status"] == "No internet":
                    # increase error count
                    self.error_count += 1

            if self.error_count >= self.error_number_to_reboot :
                atPower.reset()

            # print("Error count is : ", self.error_count)
            # print("Error count number to reboot is : ", self.error_number_to_reboot)
                
atWatchDog = atWatchDog_Class()