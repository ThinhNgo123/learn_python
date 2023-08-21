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

class atFrame_Sensor_Detail_Data(atFrame_Menu):
    def __init__(self,) -> None:

        super().__init__(
            name = atData.screen_names["Setting"]["Sensors"]["Sensor_Detail"]["Data"]["screen name"]
        )

        self.rended = False
        self.set_OK_callback( 
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Sensors"]["Sensor_Detail"]["Data"]["Diagram"]["screen name"]
            )
        )
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Sensors"]["Sensor_Detail"]["screen name"]
            )
        )
        
    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True

                self.Setting_Sensor_ID = atData.data["Sensors"]["Setting Sensor"]
                self.set_menu(
                    list= [
                        "Name: " + atData.data["Sensors"]["List"][self.Setting_Sensor_ID]["Name"],
                        "ID: " + str(atData.data["Sensors"]["List"][self.Setting_Sensor_ID]["ID"]),
                        "Unit: " + atData.data["Sensors"]["List"][self.Setting_Sensor_ID]["Unit"],
                        str(atData.data["Sensors"]["List"][self.Setting_Sensor_ID]["Sampling Time"]) + " sec/Spl",
                        atData.data["Sensors"]["List"][self.Setting_Sensor_ID]["Source"]["Protocol"],
                        "Raw: " + str(atData.data["Sensors"]["List"][self.Setting_Sensor_ID]["Raw Value"]),
                        "Calib: " + str(atData.data["Sensors"]["List"][self.Setting_Sensor_ID]["Calib Value"]),
                    ]
                )
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_Sensor_Detail_Data = atFrame_Sensor_Detail_Data()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Sensor_Detail_Data.name)
    while 1:
        atScreen_Sensor_Detail_Data.load()
