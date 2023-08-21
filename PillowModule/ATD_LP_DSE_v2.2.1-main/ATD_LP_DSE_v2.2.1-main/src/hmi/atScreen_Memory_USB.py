import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Information import atFrame_Information

sys.path.insert(0, 'json')
from atJsonData import atData

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Memory_USB

class atFrame_Memory_USB(atFrame_Information):
    def __init__(self,) -> None:



        name= atData.screen_names["Setting"]["Memory"]["USB"]["screen name"]
        # read list sensor from data json

        # information = atData.data["Memory"]["USB"]
        
        super().__init__(
            name = name,
            # detail = information
        )

        # self.set_pointer(0)
        
        self.rended = False

        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Memory"]["screen name"]
            )
        )
        
    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                information ="USB1:" + atData.data["Memory"]["USB"]["1"]["Status"] + "\n"
                if  atData.data["Memory"]["USB"]["1"]["Status"] != "Unmounted":
                    information += "Name: " + atData.data["Memory"]["USB"]["1"]["Name"] + "\n"
                    information += "Total: "+ atData.data["Memory"]["USB"]["1"]["Total"] + "\n"
                    information += "Used: " + atData.data["Memory"]["USB"]["1"]["Used"] + "\n"
                    information += "Free: " + atData.data["Memory"]["USB"]["1"]["Free"] + "\n"
                
                information +="USB2:" + atData.data["Memory"]["USB"]["2"]["Status"] + "\n"
                if  atData.data["Memory"]["USB"]["2"]["Status"] != "Unmounted":
                    information += "Name: " + atData.data["Memory"]["USB"]["2"]["Name"] + "\n"
                    information += "Total: "+ atData.data["Memory"]["USB"]["2"]["Total"] + "\n"
                    information += "Used: " + atData.data["Memory"]["USB"]["2"]["Used"] + "\n"
                    information += "Free: " + atData.data["Memory"]["USB"]["2"]["Free"] + "\n"
                
                information +="USB3:" + atData.data["Memory"]["USB"]["3"]["Status"] + "\n"
                if  atData.data["Memory"]["USB"]["3"]["Status"] != "Unmounted":
                    information += "Name: " + atData.data["Memory"]["USB"]["3"]["Name"] + "\n"
                    information += "Total: "+ atData.data["Memory"]["USB"]["3"]["Total"] + "\n"
                    information += "Used: " + atData.data["Memory"]["USB"]["3"]["Used"] + "\n"
                    information += "Free: " + atData.data["Memory"]["USB"]["3"]["Free"] + "\n"

                self.set_information(
                    detail= information
                )
                self.set_pointer(self.pointer)
                self.rended = True
            # button
            self.polling_button()
        else:
            self.rended = False

atScreen_Memory_USB = atFrame_Memory_USB()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Memory_USB.name)
    while 1:
        atScreen_Memory_USB.load()
