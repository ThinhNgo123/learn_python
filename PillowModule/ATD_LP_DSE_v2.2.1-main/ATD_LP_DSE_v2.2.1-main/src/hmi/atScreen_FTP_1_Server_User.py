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

class atFrame_FTP_1_Server_User(atFrame_Edit):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["User"]["screen name"]
        super().__init__(
            name = name,
            detail= atData.data["FTP_Servers"]["FTP1"]["User"],
            edit_mode="String"
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
        atData.data["FTP_Servers"]["FTP1"]["User"] = self.detail
        atData.save()
        notification = "FTP:User:" + atData.data["FTP_Servers"]["FTP1"]["User"]
        self.set_notification(notification)
        sleep(0.5)
        self.set_notification("---")

    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
                self.detail = atData.data["FTP_Servers"]["FTP1"]["User"]
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_FTP_1_Server_User = atFrame_FTP_1_Server_User()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_FTP_1_Server_User.name)
    while 1:
        atScreen_FTP_1_Server_User.load()
