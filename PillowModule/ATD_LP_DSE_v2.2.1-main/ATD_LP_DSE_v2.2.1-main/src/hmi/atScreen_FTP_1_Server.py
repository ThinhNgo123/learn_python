import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Menu import atFrame_Menu

sys.path.insert(0, 'json')
from atJsonData import atData

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_FTP_1_Server

class atFrame_FTP_1_Server(atFrame_Menu):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["screen name"]
        super().__init__(
            name = name,
            list= [
                atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["Status"]["screen name"],
                atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["Activate"]["screen name"],
                atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["IP"]["screen name"],
                atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["Port"]["screen name"],
                atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["User"]["screen name"],
                atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["Password"]["screen name"],
                atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["Folder"]["screen name"],
                atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["File Name"]["screen name"],
                atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["Send Time"]["screen name"],
                atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["Check Time"]["screen name"],
                atData.screen_names["Setting"]["FTP_Servers"]["FTP1"]["Time Out"]["screen name"],
            ]
        )

        self.rended = False

        self.set_OK_callback( 
            lambda: Current_Screen.set_name(
                name= self.get_chosen_submenu()
            )
        )
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["FTP_Servers"]["screen name"]
            )
        )
        
    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_FTP_1_Server = atFrame_FTP_1_Server()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_FTP_1_Server.name)
    while 1:
        atScreen_FTP_1_Server.load()
