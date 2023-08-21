import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Edit import atFrame_Edit

sys.path.insert(0, 'json')
from atJsonData import atData


# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Sensor_Detail

class atFrame_Sensor_Detail_Config_ID(atFrame_Edit):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["Sensors"]["Sensor_Detail"]["Config"]["ID"]["screen name"]

        self.Setting_Sensor_ID = atData.data["Sensors"]["Setting Sensor"]
        super().__init__(
            name = name,
            # detail= atData.data["Sensors"]["List"][self.Setting_Sensor_ID]["ID"],
            edit_mode= "Number"
        )

        self.rended = False
        
        self.set_F4_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Sensors"]["Sensor_Detail"]["Config"]["screen name"]
            )
        )
        self.set_F1_callback(
            lambda: self.save_callback()
        )
    def save_callback(self):
        try:
            self.Setting_Sensor_ID = atData.data["Sensors"]["Setting Sensor"]
            atData.data["Sensors"]["List"][self.Setting_Sensor_ID]["ID"] = self.detail
            atData.save("Sensors")
            notification = "S" + self.Setting_Sensor_ID + ":ID:"+self.detail
        except:
            notification = "Must be an string"
        self.set_notification(notification)
        print(notification)
        sleep(0.5)
        self.set_notification("---")

    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
                # read the setting sensor ID
                atData.reload()
                self.Setting_Sensor_ID = atData.data["Sensors"]["Setting Sensor"]
                self.set_detail(
                    detail= atData.data["Sensors"]["List"][self.Setting_Sensor_ID]["ID"]
                )
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_Sensor_Detail_Config_ID = atFrame_Sensor_Detail_Config_ID()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Sensor_Detail_Config_ID.name)
    while 1:
        atScreen_Sensor_Detail_Config_ID.load()
