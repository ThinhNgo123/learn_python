import sys
from time  import sleep
import os
import threading
sys.path.insert(0,"json")
from atJsonData import atData

class atPower_Class():
    def __init__(self) -> None:
        self.thread = threading.Thread(target=self._thread_update)
        pass
    def reset(self):
        os.system("sudo reboot")
    def power_off(self):
        os.system("sudo systemctl poweroff")
    def _thread_update(self):
        sleep(20)
        while(1):
            sleep(5)
            if atData.data["Power"]["Reset"] == "Yes":
                atData.delete_request_reboot()
                self.reset()

atPower = atPower_Class()