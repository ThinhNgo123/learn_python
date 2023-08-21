import sys

sys.path.insert(0,"json")
from atJsonData import atData

sys.path.insert(0,'hmi')
from atScreens import atScreens

# sys.path.insert(0,'func/sensor')
# from atSensor import atSensor

# sys.path.insert(0,'func/monitor')
# from atMonitor import atMonitor

# sys.path.insert(0, 'func/influx')
# from atInfluxDB import atInfluxDB

# sys.path.insert(0, 'func/ftp')
# from atFTPServer import atFTP_1_Server

# sys.path.insert(0, 'func/logger')
# from atLogger_TT10 import atLogger_TT10

# sys.path.insert(0, 'func/mem')
# from atDiskSpace import atDisk_Space
# from atUSB import atUSB

# sys.path.insert(0, 'func/internet')
# from atInternet  import atInternet

sys.path.insert(0, 'func/json_server')
from atJsonServer  import atJsonServer

# sys.path.insert(0, 'func/relay')
# from atRelay  import atRelay

# sys.path.insert(0, 'func/power')
# from atPower  import atPower

# sys.path.insert(0, 'func/watchdog')
# from atWatchDog  import atWatchDog

if __name__ == "__main__":
    atJsonServer.thread.start()
    
    # atSensor.thread.start()
    # atMonitor.thread.start()
    atScreens.thread.start()

    # atFTP_1_Server.thread_check_connect.start()
    
    # atLogger_TT10.thread.start()
    # atLogger_TT10.thread_check.start()

    # atInfluxDB.thread.start()

    # atDisk_Space.thread.start()
    # atUSB.thread.start()

    atData.thread.start()
    # atRelay.thread.start()

    # atPower.thread.start()
    # atWatchDog.thread.start()

    # atInternet.thread.start()