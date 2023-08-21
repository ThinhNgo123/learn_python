import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Edit import atFrame_Edit

sys.path.insert(0, 'json')
from atJsonData import atData

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Database_Store_Time

class atFrame_Database_Store_Time(atFrame_Edit):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["Database"]["Store_Time"]["screen name"]
        # read Store_Time sensor from data json

        super().__init__(
            name = name,
            detail= str(atData.data["Database"]["Store Time"]),
            edit_mode= "Number"
        )

        # self.set_pointer(0)
        
        self.rended = False

        self.set_F1_callback(
            lambda: self.save_callback()
        )
        self.set_F4_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Database"]["screen name"]
            )
        )
        
    def save_callback(self):

        try:
            atData.data["Database"]["Store Time"] = float(self.detail)
            if (float(self.detail) < 1.0):
                notification = "Must be >=1.0"
            else:
                atData.save()
                notification = "DB:ST:" + self.detail
        except:
            notification = "Must be an float"

        self.set_notification(notification)
        sleep(0.5)
        self.set_notification("---")

    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.set_detail(
                    detail= str(atData.data["Database"]["Store Time"])
                )
                self.set_pointer(self.pointer)
                self.rended = True
            # button
            self.polling_button()
        else:
            self.rended = False

atScreen_Database_Store_Time = atFrame_Database_Store_Time()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Database_Store_Time.name)
    while 1:
        atScreen_Database_Store_Time.load()
