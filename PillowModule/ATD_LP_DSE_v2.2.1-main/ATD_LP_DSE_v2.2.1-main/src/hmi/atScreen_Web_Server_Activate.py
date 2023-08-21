import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Menu import atFrame_Menu

sys.path.insert(0, 'json')
from atJsonData import atData


# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Web_Server_Activate

class atFrame_Web_Server_Activate(atFrame_Menu):
    def __init__(self,) -> None:



        name= atData.screen_names["Setting"]["Web_Server"]["Activate"]["screen name"]
        # read list sensor from data json

        
        super().__init__(
            name = name,
            list=[
                "Enable",
                "Disable"
            ]
        )

        # self.set_pointer(0)
        
        self.rended = False

        self.set_OK_callback(
            lambda: self.save_callback()
        )
        
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Web_Server"]["screen name"]
            )
        )

        
    def save_callback(self):
        atData.data["Web_Server"]["Activate"] = self.get_chosen_submenu()
        atData.save("Web_Server")
        notification = "WS:Act:" + atData.data["Web_Server"]["Activate"]
        self.set_notification(notification)
        sleep(0.5)
        self.set_notification("---")

    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.set_pointer(self.pointer)
                self.rended = True
            # button
            self.polling_button()
        else:
            self.rended = False

atScreen_Web_Server_Activate = atFrame_Web_Server_Activate()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Web_Server_Activate.name)
    while 1:
        atScreen_Web_Server_Activate.load()
