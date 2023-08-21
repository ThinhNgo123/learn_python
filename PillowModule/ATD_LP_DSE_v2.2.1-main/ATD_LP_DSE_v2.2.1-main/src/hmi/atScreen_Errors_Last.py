import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Information import atFrame_Information

sys.path.insert(0, 'json')
from atJsonData import atData

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Errors_Last

class atFrame_Errors_Last(atFrame_Information):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["Errors"]["Last"]["screen name"]
        # read list sensor from data json

        information = atData.data["Errors"]["Last"]
        
        super().__init__(
            name = name,
            detail = information
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
                self.set_information(detail= atData.data["Errors"]["Last"])
                self.set_pointer(self.pointer)
                self.rended = True
            # button
            self.polling_button()
        else:
            self.rended = False

atScreen_Errors_Last = atFrame_Errors_Last()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Errors_Last.name)
    while 1:
        atScreen_Errors_Last.load()
