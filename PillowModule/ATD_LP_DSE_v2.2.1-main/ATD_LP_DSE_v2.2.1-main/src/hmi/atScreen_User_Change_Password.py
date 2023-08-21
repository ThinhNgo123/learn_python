import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Edit import atFrame_Edit

sys.path.insert(0, 'json')
from atJsonData import atData

sys.path.insert(0,'func/json_client')
from atJsonClient import atJsonClient

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen 
# from atScreen_Monitoring import atScreen_Monitoring as Backward_Screen_Of_Change_Password_Edit

class atFrame_User_Change_Password_Class(atFrame_Edit):
    def __init__(self,) -> None:
        
        super().__init__(
            name = atData.screen_names["Setting"]["User"]["Change Password"]["screen name"],
            detail = atData.data["User"]["Password"]
        )

        # self.set_pointer(0)
        
        self.rended = False
        self.set_F1_callback(
            lambda: self.save_callback()
        )
        self.set_F4_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Setting"]["User"]["screen name"]
            )
        )
    def save_callback(self):
        try:
            notification = "Saving"
            self.set_notification(notification)
            atData.data["User"] = atJsonClient.getJson("User")
            atData.data["User"]["Password"] = self.detail
            for user in atData.data["User"]["List"]:
                if (atData.data["User"]["List"][user]["User Name"] == atData.data["User"]["User"]) :
                    atData.data["User"]["List"][user]["Password"] = self.detail
            atData.save("User")
            notification = atData.data["User"]["User"] + "/" + atData.data["User"]["Password"]
        except Exception as error:
            print(error)
           

        self.set_notification(notification)
        sleep(0.5)
        self.set_notification("---")

    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.set_detail(
                    detail= atData.data["User"]["Password"]
                )
                self.set_pointer(self.pointer)
                self.rended = True
            # button
            self.polling_button()
        else:
            self.rended = False

atScreen_User_Change_Password = atFrame_User_Change_Password_Class()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_User_Change_Password.name)
    while 1:
        atScreen_User_Change_Password.load()
