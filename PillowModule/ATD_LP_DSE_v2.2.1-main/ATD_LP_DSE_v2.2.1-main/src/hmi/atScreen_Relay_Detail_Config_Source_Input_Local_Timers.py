import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Information import atFrame_Information

sys.path.insert(0, 'json')
from atJsonData import atData


# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Relay_Detail

class atFrame_Relay_Detail_Config_Source_Input_Local_Timers(atFrame_Information):
    def __init__(self,) -> None:

        name= atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["Config"]["Source"]["Input"]["Local"]["Timers"]["screen name"]

        super().__init__(
            name = name,
        )

        # self.set_pointer(0)

        self.rended = False
        

        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["Config"]["Source"]["Input"]["Local"]["screen name"]
            )
        )

    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
                # read the setting Relay ID
                self.Setting_Relay_ID = atData.data["Relays"]["Setting Relay"]
                self.set_information(
                    "be in developing"
                )
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_Relay_Detail_Config_Source_Input_Local_Timers = atFrame_Relay_Detail_Config_Source_Input_Local_Timers()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Relay_Detail_Config_Source_Input_Local_Timers.name)
    while 1:
        atScreen_Relay_Detail_Config_Source_Input_Local_Timers.load()
