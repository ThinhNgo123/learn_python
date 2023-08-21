import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Information import atFrame_Information

sys.path.insert(0, 'json')
from atJsonData import atData
# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Internet_Ethernet

class atFrame_Internet_Ethernet(atFrame_Information):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["Internet"]["Ethernet"]["screen name"]
        # read list sensor from data json

        # information = atData.data["Internet"]["Ethernet"]
        
        super().__init__(
            name = name,
            # detail = information
        )

        
        self.rended = False

        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Internet"]["screen name"]
            )
        )
        
    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                information = atData.data["Internet"]["Ethernet"]["Status"] + "\n"
                information +="IP:" +atData.data["Internet"]["Ethernet"]["IP"] + "\n"
                information +="Gw:" +atData.data["Internet"]["Ethernet"]["Gateway"] + "\n"
                information +="Nm:" +atData.data["Internet"]["Ethernet"]["Netmask"] + "\n"
                information +="Sp:" +atData.data["Internet"]["Ethernet"]["Speed"] + "\n"
                information +="MAC:" +atData.data["Internet"]["Ethernet"]["MAC"] + "\n"
                self.set_information(
                    detail= information
                )
                self.set_pointer(self.pointer)
                self.rended = True
            # button
            self.polling_button()
        else:
            self.rended = False

atScreen_Internet_Ethernet = atFrame_Internet_Ethernet()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Internet_Ethernet.name)
    while 1:
        atScreen_Internet_Ethernet.load()
