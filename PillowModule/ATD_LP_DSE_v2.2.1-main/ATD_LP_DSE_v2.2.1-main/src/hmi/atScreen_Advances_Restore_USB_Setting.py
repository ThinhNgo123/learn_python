import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Menu import atFrame_Menu

sys.path.insert(0, 'json')
from atJsonData import atData
sys.path.insert(0,'func/restore')
from atRestoreUSBSetting import atRestore_USB_Setting

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Advances_Restore_USB

class atFrame_Advances_Restore_USB_Setting(atFrame_Menu):
    def __init__(self,) -> None:



        name= atData.screen_names["Setting"]["Advances"]["Restore_USB"]["Setting"]["screen name"]
        # read list sensor from data json

        super().__init__(
            name = name,
            list=[
                "No",
                "Yes"
            ]
        )

        self.rended = False
        self.set_OK_callback(
            lambda: self.screen_function()
        )
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Advances"]["Restore_USB"]["screen name"]
            )
        )
        
    def screen_function(self):
        self.set_notification("Restoring")
        if (self.get_chosen_submenu() == "Yes"):
            successful_restore = atRestore_USB_Setting.restore()
            if(successful_restore):
                self.set_notification("Restored")
                sleep(0.5)
                self.set_notification("---")
            else:
                self.set_notification("These is no USB, file")
                sleep(0.5)
                self.set_notification("---")
        else:
            Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Advances"]["Restore_USB"]["screen name"]
            )
        # pass

    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.set_pointer(self.pointer)
                self.rended = True
            # button
            self.polling_button()
        else:
            self.rended = False

atScreen_Advances_Restore_USB_Setting = atFrame_Advances_Restore_USB_Setting()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Advances_Restore_USB_Setting.name)
    while 1:
        atScreen_Advances_Restore_USB_Setting.load()
