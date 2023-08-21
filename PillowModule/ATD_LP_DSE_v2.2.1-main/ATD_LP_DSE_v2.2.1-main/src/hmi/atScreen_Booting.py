import sys
from time import sleep
import json 
sys.path.insert(0, 'hmi/atFrame')
from atFrame_Boot import atFrame_Boot

sys.path.insert(0, 'json')
from atJsonData import atData

# if not "Current_Screen" in sys.modules:
from Current_Screen import Current_Screen

class atFrame_Booting(atFrame_Boot):

    def __init__(self) -> None:
 

        name= atData.screen_names["Booting"]["screen name"]
        super().__init__(
            name=name
        )
        print("Loading")


    def load(self):
        if  self.name == Current_Screen.name:
            self.set_version_info(atData.data["Boot"]["Version Information"])
            self.set_loading_percent(atData.data["Boot"]["Loading Percentage"])
            self.set_loading_info(atData.data["Boot"]["Loading Information"])
            print(".")
            sleep(0.5)
            # loading complete
            if atData.data["Boot"]["Loading Percentage"] == 100:
                print("Loading complete")
                self.set_loading_info("Installing complete")
                print("Change screen to " + atData.screen_names["Monitoring"]["screen name"])
                sleep(1)
                Current_Screen.name = atData.screen_names["Monitoring"]["screen name"]

atScreen_Booting = atFrame_Booting()

if __name__ == "__main__":
    Current_Screen.set_name(atScreen_Booting.name)
    while 1:
        sleep(1)
        # change data json
        atData.data["Boot"]["Loading Percentage"] +=10
        if atData.data["Boot"]["Loading Percentage"] > 100:
            atData.data["Boot"]["Loading Percentage"] = 0
        atData.save()
        # update to 
        atScreen_Booting.load()
