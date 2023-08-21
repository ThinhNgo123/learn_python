import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Information import atFrame_Information

sys.path.insert(0, 'json')
from atJsonData import atData

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_About

class atFrame_About(atFrame_Information):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["About"]["screen name"]
        # read list sensor from data json

        self.image = "image/ATLab_QR_210x210.jpg"
        
        super().__init__(
            name = name,
            # image_url= self.image
        )

        # self.set_pointer(0)
        
        self.rended = False

        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["screen name"]
            )
        )
        
    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.set_information(
                    image_url= self.image
                )
                self.set_pointer(self.pointer)
                self.rended = True
            # button
            self.polling_button()
        else:
            self.rended = False

atScreen_About = atFrame_About()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_About.name)
    while 1:
        atScreen_About.load()
