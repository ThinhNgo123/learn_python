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

class atFrame_Relay_Detail_Config_Source_Input_Protocol(atFrame_Menu):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["Config"]["Source"]["Input"]["Protocol"]["screen name"]

        self.Setting_Relay_ID = atData.data["Relays"]["Setting Relay"]

        # self.Setting_Relay_ID = atData.data["Relays"]["Setting Relay"]
        super().__init__(
            name = name,
            list=[
                "Local",
                "MQTT",
            ]
        )

        # self.set_pointer(0)

        self.rended = False
        
        self.set_OK_callback(
            lambda: self.new_OK_callback()
        )
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["Config"]["Source"]["screen name"]
            )
        )
    def new_OK_callback(self):
        self.Setting_Relay_ID = atData.data["Relays"]["Setting Relay"]
        atData.data["Relays"]["List"][self.Setting_Relay_ID]["Source"]["Input"]["Protocol"] = self.get_chosen_submenu()
        atData.save("Relays")
        notification = "R" + \
                self.Setting_Relay_ID + \
                ":Source:" + \
                self.get_chosen_submenu()
        self.set_notification(notification)
        print(notification)
        sleep(0.5)
        self.set_notification("---")


    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
                # read the setting Relay ID
                self.Setting_Relay_ID = atData.data["Relays"]["Setting Relay"]

                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_Relay_Detail_Config_Source_Input_Protocol = atFrame_Relay_Detail_Config_Source_Input_Protocol()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Relay_Detail_Config_Source_Input_Protocol.name)
    while 1:
        atScreen_Relay_Detail_Config_Source_Input_Protocol.load()
