import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Menu import atFrame_Menu

sys.path.insert(0, 'json')
from atJsonData import atData

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Power

class atFrame_Power(atFrame_Menu):
    def __init__(self,) -> None:



        name= atData.screen_names["Setting"]["Power"]["screen name"]
        super().__init__(
            name = name,
            list= [
                atData.screen_names["Setting"]["Power"]["Reset"]["screen name"],
                atData.screen_names["Setting"]["Power"]["Shut_Down"]["screen name"],
            ]
        )

        # self.set_pointer(0)
        
        self.rended = False

        self.set_OK_callback( 
            lambda: Current_Screen.set_name(
                name= self.get_chosen_submenu()
            )
        )
        self.set_Back_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["screen name"]
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

atScreen_Power = atFrame_Power()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Power.name)
    while 1:
        atScreen_Power.load()