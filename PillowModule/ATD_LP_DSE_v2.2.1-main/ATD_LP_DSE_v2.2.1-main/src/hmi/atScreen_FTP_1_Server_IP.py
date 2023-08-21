import sys
from time import sleep
import ipaddress
sys.path.insert(0, 'atFrame')
from atFrame_Edit import atFrame_Edit
import json 
sys.path.insert(0, 'json')
from atJsonData import atData
sys.path.insert(0,'func/json_client')
from atJsonClient import atJsonClient
# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_FTP_1_Server

class atFrame_FTP_1_Server_IP(atFrame_Edit):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["IP"]["screen name"]
        super().__init__(
            name = name,
            # detail= atData.data["FTP_Servers"]["FTP1"]["IP"],
            edit_mode="Number"
        )

        # self.set_pointer(0)
        
        self.rended = False

        self.set_F1_callback( 
            lambda: self.save_callback()
        )
        self.set_F4_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["screen name"]
            )
        )

    def save_callback(self):
        try:
            notification = "Saving"
            ipaddress.ip_address(self.detail)
            self.set_notification(notification)
            atData.data["FTP_Servers"] = atJsonClient.getJson("FTP_Servers")
            atData.data["FTP_Servers"]["FTP1"]["IP"] = self.detail
            atData.save("FTP_Servers")
            notification = "FTP:IP:" + atData.data["FTP_Servers"]["FTP1"]["IP"]
        except:
            notification = "Must be an IP"
        self.set_notification(notification)
        sleep(0.5)
        self.set_notification("---")

    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
                self.detail= atData.data["FTP_Servers"]["FTP1"]["IP"]
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_FTP_1_Server_IP = atFrame_FTP_1_Server_IP()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_FTP_1_Server_IP.name)
    while 1:
        atScreen_FTP_1_Server_IP.load()
