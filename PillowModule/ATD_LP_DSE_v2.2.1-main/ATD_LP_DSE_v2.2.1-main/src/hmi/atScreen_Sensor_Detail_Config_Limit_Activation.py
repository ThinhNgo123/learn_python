import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Menu import atFrame_Menu

sys.path.insert(0, 'json')
from atJsonData import atData


# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Sensor_Detail

class atFrame_Sensor_Detail_Config_Limit_Activation(atFrame_Menu):
    def __init__(self,) -> None:

        name= atData.screen_names["Setting"]["Sensors"]["Sensor_Detail"]["Config"]["Limit"]["Activation"]["screen name"]

        self.Setting_Sensor_ID = atData.data["Sensors"]["Setting Sensor"]
        super().__init__(
            name = name,
            list= [
                "Enable",
                "Disable"
            ]
        )

        self.rended = False
        
        self.set_OK_callback(
            lambda: self.save_callback()
        )
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Sensors"]["Sensor_Detail"]["Config"]["Limit"]["screen name"]
            )
        )
    def save_callback(self):
        try:
            self.Setting_Sensor_ID = atData.data["Sensors"]["Setting Sensor"]
            atData.data["Sensors"]["List"][self.Setting_Sensor_ID]["Limit"]["Activation"] = self.get_chosen_submenu()
            atData.save("Sensors")
            notification = "S" + self.Setting_Sensor_ID +":LA:"+ self.get_chosen_submenu()
            
        except:
            notification = "Must be a Float"
        self.set_notification(notification)
        print(notification)
        sleep(0.5)
        self.set_notification("---")
        pass

    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
 
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_Sensor_Detail_Config_Limit_Activation = atFrame_Sensor_Detail_Config_Limit_Activation()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Sensor_Detail_Config_Limit_Activation.name)
    while 1:
        atScreen_Sensor_Detail_Config_Limit_Activation.load()
