import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Menu import atFrame_Menu

sys.path.insert(0, 'json')
from atJsonData import atData

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Errors_List

class atFrame_Errors_List(atFrame_Menu):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["Errors"]["List"]["screen name"]
        # read list sensor from data json

        list = atData.data["Errors"]["List"]
        
        super().__init__(
            name = name,
            list = list
        )

        # self.set_pointer(0)
        
        self.rended = False

        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Errors"]["screen name"]
            )
        )
        
    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.set_menu(
                    list= atData.data["Errors"]["List"]
                )
                self.set_pointer(self.pointer)
                self.rended = True
            # button
            self.polling_button()
        else:
            self.rended = False

atScreen_Errors_List = atFrame_Errors_List()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Errors_List.name)
    while 1:
        atScreen_Errors_List.load()
