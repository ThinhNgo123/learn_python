import sys
from time import sleep
import json
sys.path.insert(0, 'atFrame')
from atFrame_Menu import atFrame_Menu

sys.path.insert(0, 'json')
from atJsonData import atData

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Advances_Default_Restore

class atFrame_Advances_Default_Restore(atFrame_Menu):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["Advances"]["Default_Restore"]["screen name"]
        # read list sensor from data json

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
            lambda : self.execute_function()
        )
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Advances"]["screen name"]
            )
        )
    def execute_function(self):
        if self.get_chosen_submenu() == 'Yes':
            atData.setGlobalNotification("Restoring")
            atData.set_to_default()
            atData.setGlobalNotification("Default Restored")
            Current_Screen.set_name(
                name= atData.screen_names["Monitoring"]["screen name"]
            )
        else:
            Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Advances"]["screen name"]
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

atScreen_Advances_Default_Restore = atFrame_Advances_Default_Restore()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Advances_Default_Restore.name)
    while 1:
        atScreen_Advances_Default_Restore.load()
