import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Information import atFrame_Information

sys.path.insert(0, 'json')
from atJsonData import atData

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Memory_Disk

class atFrame_Memory_Disk(atFrame_Information):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["Memory"]["Disk"]["screen name"]
        # read list sensor from data json

        # information = atData.data["Memory"]["Disk"]
        
        super().__init__(
            name = name,
            # detail = information
        )

        self.rended = False

        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Memory"]["screen name"]
            )
        )
        
    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                information = atData.data["Memory"]["Disk"]["Status"] + "\n"
                information +="Name: "  + atData.data["Memory"]["Disk"]["Name"] + "\n"
                information +="Total: " + atData.data["Memory"]["Disk"]["Total"] + "\n"
                information +="Used: "  + atData.data["Memory"]["Disk"]["Used"] + "\n"
                information +="Free: "  + atData.data["Memory"]["Disk"]["Free"] + "\n"

                self.set_information(
                    detail= information
                )
                self.set_pointer(self.pointer)
                self.rended = True
            # button
            self.polling_button()
        else:
            self.rended = False

atScreen_Memory_Disk = atFrame_Memory_Disk()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Memory_Disk.name)
    while 1:
        atScreen_Memory_Disk.load()
