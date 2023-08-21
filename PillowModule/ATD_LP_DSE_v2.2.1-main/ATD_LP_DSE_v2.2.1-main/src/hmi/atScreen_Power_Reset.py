import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Menu import atFrame_Menu

sys.path.insert(0, 'json')
from atJsonData import atData

sys.path.insert(0,'func/power')
from atPower import atPower
# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Power_Reset

class atFrame_Power_Reset(atFrame_Menu):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["Power"]["Reset"]["screen name"]
        # read list sensor from data json

        information = atData.data["Power"]["Reset"]
        
        super().__init__(
            name = name,
            list=[
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
                name= atData.screen_names["Setting"]["Power"]["screen name"]
            )
        )
    def screen_function(self):
        if(self.get_chosen_submenu() == "Yes"):
            self.set_notification("Rebooting")
            atPower.reset()
        else:
            Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Power"]["screen name"]
            )
    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.set_pointer(self.pointer)
                self.rended = True
            # button
            self.polling_button()
        else:
            self.rended = False

atScreen_Power_Reset = atFrame_Power_Reset()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Power_Reset.name)
    while 1:
        atScreen_Power_Reset.load()
