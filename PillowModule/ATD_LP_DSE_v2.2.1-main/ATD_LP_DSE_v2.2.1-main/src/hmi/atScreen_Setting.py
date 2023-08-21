import sys
from time import sleep

import json

sys.path.insert(0, 'atFrame')
from atFrame_Menu import atFrame_Menu

sys.path.insert(0, 'json')
from atJsonData import atData
from func.user.atJsonUserData import atJsonUserData

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Setting

class atFrame_Setting(atFrame_Menu):
    def __init__(self,) -> None:

        super().__init__(
            name = atData.screen_names["Setting"]["screen name"]
        )

        # self.set_pointer(0)
        
        self.rended = False

        self.set_OK_callback( 
            lambda: Current_Screen.set_name(
                name= self.get_chosen_submenu()
            )
        )
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Monitoring"]["screen name"]
            )
        )
        
    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
                if atData.data["User"]["User Permission"] == "admin":
                    self.set_menu(
                        list= [
                            atData.screen_names["Setting"]["Sensors"]["screen name"],
                            atData.screen_names["Setting"]["Relays"]["screen name"],
                            atData.screen_names["Setting"]["FTP_Servers"]["screen name"],
                            atData.screen_names["Setting"]["Database"]["screen name"],
                            atData.screen_names["Setting"]["Device"]["screen name"],
                            atData.screen_names["Setting"]["Memory"]["screen name"],
                            atData.screen_names["Setting"]["Errors"]["screen name"],
                            atData.screen_names["Setting"]["Internet"]["screen name"],
                            atData.screen_names["Setting"]["Web_Server"]["screen name"],
                            atData.screen_names["Setting"]["Power"]["screen name"],
                            atData.screen_names["Setting"]["Advances"]["screen name"],
                            atData.screen_names["Setting"]["User"]["screen name"],
                            atData.screen_names["Setting"]["About"]["screen name"],
                        ]
                    )
                else:
                    self.set_menu(
                        list= [
                            atData.screen_names["Setting"]["Sensors"]["screen name"],
                            atData.screen_names["Setting"]["Relays"]["screen name"],
                            atData.screen_names["Setting"]["FTP_Servers"]["screen name"],
                            atData.screen_names["Setting"]["Memory"]["screen name"],
                            atData.screen_names["Setting"]["Errors"]["screen name"],
                            atData.screen_names["Setting"]["Internet"]["screen name"],
                            # atData.screen_names["Setting"]["Web_Server"]["screen name"],
                            atData.screen_names["Setting"]["Power"]["screen name"],
                            atData.screen_names["Setting"]["Advances"]["screen name"],
                            atData.screen_names["Setting"]["User"]["screen name"],
                            atData.screen_names["Setting"]["About"]["screen name"],
                        ]
                    )
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_Setting = atFrame_Setting()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Setting.name)
    while 1:
        atScreen_Setting.load()
