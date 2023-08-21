import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Menu import atFrame_Menu

sys.path.insert(0, 'json')
from atJsonData import atData

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Advances_Backup_USB

class atFrame_Advances_Backup_USB(atFrame_Menu):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["Advances"]["Backup_USB"]["screen name"]
        # read list sensor from data json
        
        super().__init__(
            name = name,
            list=[
                atData.screen_names["Setting"]["Advances"]["Backup_USB"]["Setting"]["screen name"],
                atData.screen_names["Setting"]["Advances"]["Backup_USB"]["Database"]["screen name"],
                atData.screen_names["Setting"]["Advances"]["Backup_USB"]["Boot_Image"]["screen name"],
                
            ]
        )

        # self.set_pointer(0)
        
        self.rended = False
        
        self.set_OK_callback(
            lambda: Current_Screen.set_name(
                self.get_chosen_submenu()
            )
        )
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Advances"]["screen name"]
            )
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

atScreen_Advances_Backup_USB = atFrame_Advances_Backup_USB()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Advances_Backup_USB.name)
    while 1:
        atScreen_Advances_Backup_USB.load()
