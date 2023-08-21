import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Edit import atFrame_Edit

sys.path.insert(0, 'json')
from atJsonData import atData

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Device_Location_X

class atFrame_Device_Location_X(atFrame_Edit):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["Device"]["Location"]["X"]["screen name"]
        super().__init__(
            name = name,
            # detail= str(atData.data["Device"]["Location"]["X"]),
            edit_mode="Number"
        )

        self.rended = False

        self.set_F1_callback( 
            lambda: self.save()
        )
        self.set_F4_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Device"]["Location"]["screen name"]
            )
        )
    def save(self):
        try:
            atData.data["Device"]["Location"]["X"] = float(self.detail)
            atData.save("Device")
            self.set_notification("Saved")
            sleep(0.5)
            self.set_notification("---")
        except:
            self.set_notification("Must be a float")
            sleep(0.5)
            self.set_notification("---")
        
    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
                self.set_detail(str(atData.data["Device"]["Location"]["X"]))
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_Device_Location_X = atFrame_Device_Location_X()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Device_Location_X.name)
    while 1:
        atScreen_Device_Location_X.load()
