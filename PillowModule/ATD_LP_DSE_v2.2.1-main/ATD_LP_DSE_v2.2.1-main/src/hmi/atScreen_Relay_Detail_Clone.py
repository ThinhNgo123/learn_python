import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Menu import atFrame_Menu

sys.path.insert(0, 'json')
from atJsonData import atData

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Relay_Detail

class atFrame_Relay_Detail_Clone(atFrame_Menu):
    def __init__(self,) -> None:



        name= atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["Clone"]["screen name"]
        super().__init__(
            name = name,
            list= [
                "No",
                "Yes"
            ]
        )

        # self.set_pointer(0)

        self.rended = False
        self.set_OK_callback(
            lambda: self.screen_function()
        )
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["screen name"]
            )
        )
        
    def screen_function(self):
        atData.clone_Relay(atData.data["Relays"]["Setting Relay"])
        Current_Screen.set_name(
            name= atData.screen_names["Setting"]["Relays"]["screen name"]
        )
    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_Relay_Detail_Clone = atFrame_Relay_Detail_Clone()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Relay_Detail_Clone.name)
    while 1:
        atScreen_Relay_Detail_Clone.load()
