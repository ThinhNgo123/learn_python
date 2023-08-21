import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Edit import atFrame_Edit

sys.path.insert(0, 'json')
from atJsonData import atData

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_FTP_1_Server

class atFrame_FTP_1_Server_Port(atFrame_Edit):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["Port"]["screen name"]
        super().__init__(
            name = name,
            detail= str(atData.data["FTP_Servers"]["FTP1"]["Port"]),
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
            atData.data["FTP_Servers"]["FTP1"]["Port"] = int(self.detail)
            atData.save()
            notification = "FTP:Port:" + self.detail
        except:
            notification = "Must be an int"
        self.set_notification(notification)
        sleep(0.5)
        self.set_notification("---")

    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
                self.detail = str(atData.data["FTP_Servers"]["FTP1"]["Port"])
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_FTP_1_Server_Port = atFrame_FTP_1_Server_Port()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_FTP_1_Server_Port.name)
    while 1:
        atScreen_FTP_1_Server_Port.load()
