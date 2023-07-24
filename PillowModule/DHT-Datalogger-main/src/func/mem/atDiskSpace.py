import sys
from time import sleep
import threading
import os

sys.path.insert(0,"json")
from atJsonData import atData
try:
    import psutil
except:
    os.system("pip install psutil")
    import psutil

class atDisk_Space_Class():
    def __init__(self) -> None:
        # self.total = 0
        # self.used = 0
        # self.free = 0
        self.thread = threading.Thread(target= self._thread)
        pass
    
    def check_disk(self):
        disk =  psutil.disk_usage('/')
        self.total = float(disk.total) /(2**30) #GiB
        self.used = float(disk.used) /(2**30) #GiB
        self.free = float(disk.free) /(2**30) #GiB
                
        atData.data["Memory"]["Disk"]["Status"] = "Mounted"
        atData.data["Memory"]["Disk"]["Name"] = "Micro SD"
        atData.data["Memory"]["Disk"]["Total"] = "{0:0=4.2f} GiB".format( self.total)
        atData.data["Memory"]["Disk"]["Used"]  = "{0:0=4.2f} GiB".format( self.used)
        atData.data["Memory"]["Disk"]["Free"]  = "{0:0=4.2f} GiB".format( self.free)
        atData.save("Memory")
        infor = "Micro SD" + "\n" +\
                "Total: {0:0=4.2f} GiB".format( self.total) + "\n" +\
                "Used : {0:0=4.2f} GiB".format( self.used) + "\n" +\
                "Free : {0:0=4.2f} Gib".format( self.free) + "\n" 
                
        return  infor

    def _thread(self):
        while 1:
            self.check_disk()
            sleep(60)

atDisk_Space = atDisk_Space_Class()
if __name__ == "__main__":
    print(atDisk_Space.check_disk())
    pass
