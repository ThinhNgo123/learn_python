import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Information import atFrame_Information

sys.path.insert(0, 'json')
from atJsonData import atData


# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Web_Server_Status

class atFrame_Web_Server_Status(atFrame_Information):
    def __init__(self,) -> None:

        super().__init__(
            name = atData.screen_names["Setting"]["Web_Server"]["Status"]["screen name"]
        )

        # self.set_pointer(0)
        
        self.rended = False

        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Web_Server"]["screen name"]
            )
        )
        
    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                information = atData.data["Web_Server"]["Status"]
                self.set_information(
                    detail= information
                )
                self.set_pointer(self.pointer)
                self.rended = True
            # button
            self.polling_button()
        else:
            self.rended = False

atScreen_Web_Server_Status = atFrame_Web_Server_Status()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Web_Server_Status.name)
    while 1:
        atScreen_Web_Server_Status.load()
