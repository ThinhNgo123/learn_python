import sys
from time import sleep
import ipaddress
sys.path.insert(0, 'atFrame')
from atFrame_Menu import atFrame_Menu
import json 
sys.path.insert(0, 'json')
from atJsonData import atData
sys.path.insert(0,'func/json_client')
from atJsonClient import atJsonClient
# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_FTP_1_Server

class atFrame_FTP_1_Server_Activate(atFrame_Menu):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["Activate"]["screen name"]
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
                name= atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["screen name"]
            )
        )

    def save_callback(self):
        try:
            notification = "Saving"
            self.set_notification(notification)
            atData.data["FTP_Servers"]["FTP1"]["Activate"] = self.get_chosen_submenu()
            atData.save("FTP_Servers")
            notification = "FTP:Activate:" + atData.data["FTP_Servers"]["FTP1"]["Activate"]
        except Exception as error:
            print(error)
            
        self.set_notification(notification)
        sleep(0.5)
        self.set_notification("---")

    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
                self.detail= atData.data["FTP_Servers"]["FTP1"]["Activate"]
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_FTP_1_Server_Activate = atFrame_FTP_1_Server_Activate()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_FTP_1_Server_Activate.name)
    while 1:
        atScreen_FTP_1_Server_Activate.load()
