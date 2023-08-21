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

class atFrame_Relay_Detail_Config_Source_Input_Local_Mode(atFrame_Menu):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["Config"]["Source"]["Input"]["Local"]["Mode"]["screen name"]


        super().__init__(
            name = name,
        )

        # self.set_pointer(0)

        self.rended = False
        
        self.set_OK_callback(
            lambda: self.save()
        )
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["Config"]["Source"]["Input"]['Local']["screen name"]
            )
        )
    def save(self):
        self.set_notification("Saved")
        self.Setting_Relay_ID = atData.data["Relays"]["Setting Relay"]
        atData.data["Relays"]["List"][self.Setting_Relay_ID]["Source"]["Input"]["Local"]["Mode"] = self.get_chosen_submenu()
        atData.save("Relays")
        sleep(0.5)
        self.set_notification("---")
    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
                # read the setting Relay ID
                self.Setting_Relay_ID = atData.data["Relays"]["Setting Relay"]
                self.set_menu(
                    list=[
                        "Manual",
                        "Timers"
                    ]
                )
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_Relay_Detail_Config_Source_Input_Local_Mode = atFrame_Relay_Detail_Config_Source_Input_Local_Mode()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Relay_Detail_Config_Source_Input_Local_Mode.name)
    while 1:
        atScreen_Relay_Detail_Config_Source_Input_Local_Mode.load()
