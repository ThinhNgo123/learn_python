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

class atFrame_Sensor_Detail_Config_Source_4_20mA(atFrame_Menu):
    def __init__(self,) -> None:


        name= atData.screen_names["Setting"]["Sensors"]["Sensor_Detail"]["Config"]["Source"]["4-20mA"]["screen name"]

        self.Setting_Sensor_ID = atData.data["Sensors"]["Setting Sensor"]

        # self.Setting_Sensor_ID = atData.data["Sensors"]["Setting Sensor"]
        super().__init__(
            name = name,
            list=[
                "4-20mA CH-1",
                "4-20mA CH-2",
                "4-20mA CH-3",
                "4-20mA CH-4",
                "4-20mA CH-5",
                "4-20mA CH-6",
                "4-20mA CH-7",
                "4-20mA CH-8",
            ]
        )

        # self.set_pointer(0)

        self.rended = False
        
        self.set_OK_callback(
            lambda: self.new_OK_callback()
        )
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Sensors"]["Sensor_Detail"]["Config"]["Source"]["screen name"]
            )
        )
    def new_OK_callback(self):
        self.Setting_Sensor_ID = atData.data["Sensors"]["Setting Sensor"]
        atData.data["Sensors"]["List"][self.Setting_Sensor_ID]["Source"]["Protocol"] = self.get_chosen_submenu()
        atData.save("Sensors")
        notification = "S" + \
                self.Setting_Sensor_ID + \
                ":Source:" + \
                self.get_chosen_submenu()
        self.set_notification(notification)
        print(notification)
        sleep(0.5)
        self.set_notification("---")


    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
                # read the setting sensor ID
                self.Setting_Sensor_ID = atData.data["Sensors"]["Setting Sensor"]

                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_Sensor_Detail_Config_Source_4_20mA = atFrame_Sensor_Detail_Config_Source_4_20mA()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Sensor_Detail_Config_Source_4_20mA.name)
    while 1:
        atScreen_Sensor_Detail_Config_Source_4_20mA.load()
