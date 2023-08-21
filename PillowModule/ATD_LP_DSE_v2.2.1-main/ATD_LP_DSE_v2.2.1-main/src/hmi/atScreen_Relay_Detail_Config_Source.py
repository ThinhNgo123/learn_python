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

class atFrame_Relay_Detail_Config_Source(atFrame_Menu):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["Config"]["Source"]["screen name"]

        super().__init__(
            name = name,
            # list=[
            #     atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["Config"]["Source"]["Input"]["screen name"],
            #     atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["Config"]["Source"]["Output"]["screen name"],
            # ]
        )

        self.rended = False
        
        self.set_OK_callback(
            lambda: Current_Screen.set_name(
                name= self.get_chosen_submenu()
            )
        )
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["Config"]["screen name"]
            )
        )

    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
                self.set_menu(
                    list=[
                        atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["Config"]["Source"]["Input"]["screen name"],
                        atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["Config"]["Source"]["Output"]["screen name"],
                    ]
                )
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_Relay_Detail_Config_Source = atFrame_Relay_Detail_Config_Source()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Relay_Detail_Config_Source.name)
    while 1:
        atScreen_Relay_Detail_Config_Source.load()
