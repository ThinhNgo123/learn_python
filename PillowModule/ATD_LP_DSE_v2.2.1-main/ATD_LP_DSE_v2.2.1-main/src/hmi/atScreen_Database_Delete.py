import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Menu import atFrame_Menu

sys.path.insert(0, 'json')
from atJsonData import atData

sys.path.insert(0, 'func/influx')
from atInfluxDB import atInfluxDB

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Database_Delete

class atFrame_Database_Delete(atFrame_Menu):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["Database"]["Delete"]["screen name"]
        # read list sensor from data json

        
        
        super().__init__(
            name = name,
            list = [
                "No",
                "Yes"
            ]
        )

        # self.set_pointer(0)
        
        self.rended = False
        self.set_OK_callback(
            lambda: self.new_ok_callback()
        )
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Database"]["List"]["screen name"]
            )
        )
        
    def new_ok_callback(self):
        choice = self.get_chosen_submenu()
        if choice == "Yes":
            deleting_sensor = atData.data["Database"]["Delete"]
            notification = "Deleting " + deleting_sensor
            self.set_notification(notification)

            atInfluxDB.delete_measurement(measurement= deleting_sensor)
            
            notification = "Deleted " + deleting_sensor
            self.set_notification(notification)
            pass

    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.set_pointer(self.pointer)
                self.rended = True
            # button
            self.polling_button()
        else:
            self.rended = False

atScreen_Database_Delete = atFrame_Database_Delete()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Database_Delete.name)
    while 1:
        atScreen_Database_Delete.load()
