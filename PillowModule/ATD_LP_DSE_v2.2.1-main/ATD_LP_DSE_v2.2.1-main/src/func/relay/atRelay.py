import os 
import sys
from time import sleep
import threading
import json

sys.path.insert(0,"json")
from atJsonData import atData

sys.path.insert(0,"driver")

from atModbus_RTU import atModbus_RTU
from atModbus_TCP import atModbus_TCP
from atRelay_GPIO import atRelay_GPIO

class atRelay_Class():
    def __init__(self) -> None:
        self.thread = threading.Thread(target= self._thread)
        pass
    def control_relay(self):
        for relay in atData.data["Relays"]["List"]:
            
            # print(atData.data["Relays"]["List"][relay]['Name'])
            control_command = None
            input_source = atData.data["Relays"]["List"][relay]["Source"]['Input']["Protocol"] 
            control_mode = atData.data["Relays"]["List"][relay]["Source"]['Input']["Local"]["Mode"]
            output_source = atData.data["Relays"]["List"][relay]["Source"]['Output']["Protocol"] 
            
            if input_source == "Local" and control_mode == "Manual":
                control_command = atData.data["Relays"]["List"][relay]["Source"]['Input']["Local"]["Manual"]

            # control output
            
            if control_command == "On":
                if output_source == "Relay CH-1":
                    atRelay_GPIO.turnOn()
                    atData.data["Relays"]["List"][relay]["Value"] = "On"

            elif control_command == "Off":
                if output_source == "Relay CH-1":
                    atRelay_GPIO.turnOff()
                    atData.data["Relays"]["List"][relay]["Value"] = "Off"

                

    def _thread(self):
        while 1:
            sleep(1)
            self.control_relay()

atRelay = atRelay_Class()
if __name__ == "__main__":
    atRelay.thread.start()