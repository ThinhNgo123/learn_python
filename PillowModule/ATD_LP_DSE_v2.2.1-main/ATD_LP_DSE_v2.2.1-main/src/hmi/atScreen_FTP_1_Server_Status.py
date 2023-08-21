import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Information import atFrame_Information

sys.path.insert(0, 'json')
from atJsonData import atData

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_FTP_1_Server

class atFrame_FTP_1_Server_Status(atFrame_Information):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["Status"]["screen name"]
        super().__init__(
            name = name,
            detail= atData.data["FTP_Servers"]["FTP1"]["Status"]
        )

        # self.set_pointer(0)
        
        self.rended = False

        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["screen name"]
            )
        )
        
    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
                self.set_information(
                    detail=atData.data["FTP_Servers"]["FTP1"]["Status"]
                )
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_FTP_1_Server_Status = atFrame_FTP_1_Server_Status()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_FTP_1_Server_Status.name)
    while 1:
        atScreen_FTP_1_Server_Status.load()
