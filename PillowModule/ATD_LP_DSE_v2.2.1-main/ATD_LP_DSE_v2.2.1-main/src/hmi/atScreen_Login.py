import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Login import atFrame_Login

sys.path.insert(0, '../json')
from atJsonData import atData

sys.path.insert(0, '../json')
# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen

class atFrame_Logging_In(atFrame_Login):

    def __init__(self) -> None:
        

        
        name= atData.screen_names["Login"]["screen name"]
        super().__init__(
            name = name,
            user_name= str(atData.data["User"]["User"]),
            password=str(atData.data["User"]["Password"])
        )

        self.rended = False

        self.set_F4_callback(
            lambda: Current_Screen.set_name(
                name= atData.screen_names["Monitoring"]["screen name"]
            )
        )
        self.set_OK_long_press_callback(
            lambda: self.login()
        )
        self.set_BACK_long_press_callback(
            lambda: self.logout()
        )

    def login(self):
        print("Save infor and login with user/password: " +  self.user_name + "/" + self.password)  
        if atData.data["User"]["User Permission"] != 0:
            notification = "Logged in"
            self.set_notification(notification)
            print(self.notification)
            sleep(0.5)
            self.set_notification("---")
            Current_Screen.set_name(
                name= atData.screen_names["Setting"]["screen name"]
            )
        else:
            result = atData.login(
                user_name= self.user_name,
                password= self.password
            )
            
            self.set_notification(result)
            atData.save("User")
            print(self.notification)
            sleep(0.5)
            self.set_notification("---")
            if result == "Login successfully":
                Current_Screen.set_name(
                    name= atData.screen_names["Setting"]["screen name"]
                )
                
    def logout(self):
        self.user_name = "___"
        self.password = "___"
        self.editing_object = "__"
        atData.data["User"]["User Permission"] = 0
        atData.data["User"]["User"] = 0
        atData.data["User"]["Password"] = 0
        atData.save("User")
        self.set_notification("Logged out")
        self.set_pointer(0)

    def load(self):
        if self.name == Current_Screen.name:
            if self.rended == False:
                self.rended = True
                self.set_pointer(self.pointer)
            # button
            self.polling_button()

        else:
            self.rended = False

atScreen_Login = atFrame_Logging_In()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Login.name)
    while 1:
        # update to 
        atScreen_Login.load()
