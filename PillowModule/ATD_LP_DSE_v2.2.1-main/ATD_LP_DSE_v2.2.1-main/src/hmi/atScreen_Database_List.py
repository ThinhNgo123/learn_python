import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Menu import atFrame_Menu

sys.path.insert(0, 'json')
from atJsonData import atData

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Database_List

class atFrame_Database_List(atFrame_Menu):
    def __init__(self,) -> None:

  

        name= atData.screen_names["Setting"]["Database"]["List"]["screen name"]
        # read list sensor from data json

        list = []
        for sensor in atData.data["Database"]["List"]:
            list.append(sensor)
        
        super().__init__(
            name = name,
            list = list
        )

        # self.set_pointer(0)
        
        self.rended = False
        self.set_OK_callback(
            lambda: self.new_ok_callback()
        )
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["Database"]["screen name"]
            )
        )
        
    def new_ok_callback(self):
        atData.data["Database"]["Delete"] = self.get_chosen_submenu()
        Current_Screen.set_name(
            name= atData.screen_names["Setting"]["Database"]["Delete"]["screen name"]
        )
    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:

                list = []
                for sensor in atData.data["Database"]["List"]:
                    list.append(sensor)
                
                self.set_menu(
                    list= list
                )
                self.set_pointer(self.pointer)
                self.rended = True
            # button
            self.polling_button()
        else:
            self.rended = False

atScreen_Database_List = atFrame_Database_List()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Database_List.name)
    while 1:
        atScreen_Database_List.load()
