import sys
from time import sleep
import json 
sys.path.insert(0, 'atFrame')
from atFrame_Menu import atFrame_Menu

sys.path.insert(0, 'json')
from atJsonData import atData



from Current_Screen import Current_Screen
    
class atFrame_Relays(atFrame_Menu):
    def __init__(self) -> None:


        name= atData.screen_names["Setting"]["Relays"]["screen name"]

        super().__init__(
            name=name,
            # list= Relay_list
        )
        

        self.set_F1_callback(
            lambda: self.add_Relay_task()
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
        Set the Setting pointer to the pointer of list of Relays
        """
        
        atData.data["Relays"]["Setting Relay"] = str(self.get_pointer() + 1)
        atData.save("Relays")
        print("Set the setting senor to ID " +  str(atData.data["Relays"]["Setting Relay"]))
        if atData.data["Relays"]["Number"] != 0:
            Current_Screen.set_name(
                atData.screen_names["Setting"]["Relays"]["Relay_Detail"]["screen name"]
            )
    def add_Relay_task(self):
        notification = "adding Relay"
        self.set_notification(notification)
        atData.add_Relay()
        self.update_list_Relay()
        notification = "added Relay"
        self.set_notification(notification)

        print(notification)
        sleep(0.5)
        self.set_notification("---")

    def update_list_Relay(self):
        Relay_list_json = atData.data["Relays"]["List"].keys()
        Relay_list = []
        for Relay in Relay_list_json:
            submenu =   "[" + \
                        atData.data["Relays"]["List"][Relay]["ID"] + \
                        "]: " + \
                        atData.data["Relays"]["List"][Relay]["Name"]
            Relay_list.append(submenu)
        # Update list from data json
        if atData.data["Relays"]["Number"] == 0:
            Relay_list.append("F1: add Relay")
            self.set_menu(
                list= Relay_list
            )
            self.set_pointer(0)
            return True
        self.set_menu(
            list= Relay_list
        )

    def load(self):
        if self.name == Current_Screen.name:
            
            if self.rended == False:
                self.rended = True
                self.update_list_Relay()
                if (int(atData.data["Relays"]["Setting Relay"]) > atData.data["Relays"]["Number"]) :
                    atData.data["Relays"]["Setting Relay"] = str(atData.data["Relays"]["Number"])
                    self.set_pointer(atData.data["Relays"]["Number"] -1 )
                else:
                    self.set_pointer(self.pointer)

            # button
            self.polling_button()
        else:
            self.rended = False

atScreen_Relays = atFrame_Relays()

if __name__ == "__main__":
    while 1:
        atScreen_Relays.load(current_screen="Relays")
