import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Information import atFrame_Information

sys.path.insert(0, 'json')
from atJsonData import atData


# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Sensor_Detail

class atFrame_Sensor_Detail_Data_Diagram(atFrame_Information):
    def __init__(self,) -> None:

        
        super().__init__(
            name = atData.screen_names["Setting"]["Sensors"]["Sensor_Detail"]["Data"]["Diagram"]["screen name"],
            detail="in developing"
        )

        
        self.rended = False

        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Sensors"]["Sensor_Detail"]["Data"]["screen name"]
            )
        )
        
    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_Sensor_Detail_Data_Diagram = atFrame_Sensor_Detail_Data_Diagram()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Sensor_Detail_Data_Diagram.name)
    while 1:
        atScreen_Sensor_Detail_Data_Diagram.load()
