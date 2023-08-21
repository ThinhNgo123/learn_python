import sys
from time import sleep
from datetime import datetime
import threading
import os
import ftplib

sys.path.insert(0,"json")
from atJsonData import atData

class atClock_Class():
    def __init__(self) -> None:
        self.thread = threading.Thread(target=self._thread)
    def _thread(self):
        while 1:
            time =  datetime.now()
            print(time)
            atData.data["Notification"]["Info"] = time
            atData.data["Notification"]["Update"] = 1
            sleep(1)

atClock = atClock_Class()

if __name__ == "__main__":
    atClock.thread.start()
    
