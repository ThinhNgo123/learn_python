import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Menu import atFrame_Menu

sys.path.insert(0, 'json')
from atJsonData import atData



from Current_Screen import Current_Screen
    
class atFrame_Sensors(atFrame_Menu):
    def __init__(self) -> None:

        name= atData.screen_names["Setting"]["Sensors"]["screen name"]

        super().__init__(
            name=name,
        )
        
        self.set_F1_callback(
            lambda: self.add_sensor_task()
        )
        self.set_OK_callback(
            lambda: self.new_callback()
        )
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                atData.screen_names["Setting"]["screen name"]
            )
        )
    def new_callback(self):
        """
        Set the Setting pointer to the pointer of list of sensors
        """
        
        atData.data["Sensors"]["Setting Sensor"] = str(self.get_pointer() + 1)
        atData.save("Sensors")
        print("Set the setting senor to ID " +  str(atData.data["Sensors"]["Setting Sensor"]))
        if atData.data["Sensors"]["Number"] != 0:
            Current_Screen.set_name(
                atData.screen_names["Setting"]["Sensors"]["Sensor_Detail"]["screen name"]
            )
    def add_sensor_task(self):
        notification = "adding sensor"
        self.set_notification(notification)
        atData.add_Sensor()
        self.update_list_sensor()
        notification = "added sensor"
        self.set_notification(notification)

        print(notification)
        sleep(0.5)
        self.set_notification("---")

    def update_list_sensor(self):
        sensor_list_json = atData.data["Sensors"]["List"].keys()
        sensor_list = []
        for sensor in sensor_list_json:
            submenu =   "[" + \
                        atData.data["Sensors"]["List"][sensor]["ID"] + \
                        "]: " + \
                        atData.data["Sensors"]["List"][sensor]["Name"]
            sensor_list.append(submenu)
        # Update list from data json
        if atData.data["Sensors"]["Number"] == 0:
            sensor_list.append("F1: add sensor")
            self.set_menu(
                list= sensor_list
            )
            self.set_pointer(0)
            return True
        self.set_menu(
            list= sensor_list
        )

    def load(self):
        if self.name == Current_Screen.name:
            
            if self.rended == False:
                self.rended = True
                self.update_list_sensor()
                if (int(atData.data["Sensors"]["Setting Sensor"]) > atData.data["Sensors"]["Number"]) :
                    atData.data["Sensors"]["Setting Sensor"] = str(atData.data["Sensors"]["Number"])
                    self.set_pointer(atData.data["Sensors"]["Number"] -1 )
                else:
                    self.set_pointer(self.pointer)

            # button
            self.polling_button()
        else:
            self.rended = False

atScreen_Sensors = atFrame_Sensors()

if __name__ == "__main__":
    while 1:
        atScreen_Sensors.load(current_screen="Sensors")
