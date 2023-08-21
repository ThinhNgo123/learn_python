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

class atFrame_Relay_Detail_Data(atFrame_Menu):
    def __init__(self,) -> None:

        name= atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["Data"]["screen name"]

        # data
        self.Setting_Relay_ID = atData.data["Relays"]["Setting Relay"]

        super().__init__(
            name = name
            
        )

        self.rended = False
        # self.set_OK_callback( 
        #     lambda: Current_Screen.set_name(
        #         name= atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["Data"]["Diagram"]["screen name"]
        #     )
        # )
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["screen name"]
            )
        )
        
    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True

                self.Setting_Relay_ID = atData.data["Relays"]["Setting Relay"]
                self.set_menu(
                    list= [
                        "Name: " + atData.data["Relays"]["List"][self.Setting_Relay_ID]["Name"],
                        "ID: " + str(atData.data["Relays"]["List"][self.Setting_Relay_ID]["ID"]),
                        "Status: " + atData.data["Relays"]["List"][self.Setting_Relay_ID]["Status"],
                        "Value :" + str(atData.data["Relays"]["List"][self.Setting_Relay_ID]["Value"]),
                        "IP: "+atData.data["Relays"]["List"][self.Setting_Relay_ID]["Source"]["Input"]["Protocol"],
                        "OP: "+atData.data["Relays"]["List"][self.Setting_Relay_ID]["Source"]["Output"]["Protocol"],
                    ]
                )
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_Relay_Detail_Data = atFrame_Relay_Detail_Data()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Relay_Detail_Data.name)
    while 1:
        atScreen_Relay_Detail_Data.load()
