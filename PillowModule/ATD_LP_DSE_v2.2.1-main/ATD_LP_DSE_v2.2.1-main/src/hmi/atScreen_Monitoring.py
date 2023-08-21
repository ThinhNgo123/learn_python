import sys
from time import sleep
import json
import threading
from datetime import datetime
sys.path.insert(0, 'atFrame')
from atFrame_Monitor import atFrame_Monitor

sys.path.insert(0, 'json')
from atJsonData import atData
from Current_Screen import Current_Screen

class atFrame_Monitoring(atFrame_Monitor):
    object_path = "json/Monitor.json"
    relay_path = "json/Relay.json"
    UPDATE_TIME = 1 #second
    last_update_time = datetime.now()

    def __init__(self) -> None:


        name= atData.screen_names["Monitoring"]["screen name"]
        self.get_objects_json()
        # read objects from jon
        super().__init__(
            name = name,
            object_dict = self.objects
        )
        

        print(self.last_update_time)

        self.rended = False

        print("Loading")
        self.set_F1_callback(
            lambda: Current_Screen.set_name(
                name=  atData.screen_names["Login"]["screen name"]
            )
        )
        self.set_OK_callback(
            lambda: self.new_ok_callback()
        )

    def new_ok_callback(self):
        object_list = list(self.objects.keys())
        choosing_object = object_list[self.get_pointer()]

        print(object_list[self.get_pointer()])
        #  in the case of FTP
        if  self.objects[choosing_object]["Type"] == "FTP Server" :
            print('Can not change status of FTP servers')
            self.set_notification("Can not execute")
            sleep(0.5)
            self.set_notification("---")
        
        # in the case of sensors 
        elif self.objects[choosing_object]["Type"] == "Sensor":
            #  find the sensor have this name
            for sensor in atData.data["Sensors"]['List']:
                print(sensor)
                if atData.data["Sensors"]['List'][sensor]['Name'] == object_list[self.get_pointer()]:
                    # change the status of sensors
                    self.set_notification("Changing")
                    if self.objects[choosing_object]["Status"] == "Normal":
                        
                        self.objects[choosing_object]["Status"] = "Calib"
                        while atData.data["Sensors"]["List"][sensor]["Status"] != "Calib":
                            atData.data["Sensors"]["List"][sensor]["Status"] = "Calib"
                        # name = atData.data["Sensors"]["List"][sensor]["Name"]
                        # status = atData.data["Sensors"]["List"][sensor]["Status"]
                        # print(name + " set to " +status)

                    elif self.objects[choosing_object]["Status"] == "Calib":
                      self.objects[choosing_object]["Status"] = "Error"
                      while atData.data["Sensors"]["List"][sensor]["Status"] != "Error":
                          atData.data["Sensors"]["List"][sensor]["Status"] = "Error"
                      # name = atData.data["Sensors"]["List"][sensor]["Name"]
                      # status = atData.data["Sensors"]["List"][sensor]["Status"]
                      # print(name + " set to " +status)

                    elif self.objects[choosing_object]["Status"] == "Error":
                      self.objects[choosing_object]["Status"] = "Normal"
                      while atData.data["Sensors"]["List"][sensor]["Status"] != "Normal":
                          atData.data["Sensors"]["List"][sensor]["Status"] = "Normal"
                      # name = atData.data["Sensors"]["List"][sensor]["Name"]
                      # status = atData.data["Sensors"]["List"][sensor]["Status"]
                      # print(name + " set to " +status)

                    self._import_object_dict()
                    self.set_pointer(self.pointer)
                    self.set_notification("---")
                    # save to monitoring object to the atData.data
                    
                    # atData.save("Monitor")
                    break
        
        # in the case of relays
        elif self.objects[choosing_object]["Type"] == "Relay":
            for relay in atData.data["Relays"]['List']:
                # print(relay)
                if atData.data["Relays"]['List'][relay]['Name'] == object_list[self.get_pointer()]:
                    self.set_notification("Changing")
                    if atData.data["Relays"]["List"][relay]["Source"]["Input"]["Protocol"]=="Local" :

                        if atData.data["Relays"]["List"][relay]["Source"]["Input"]["Local"]["Mode"]=="Manual":
                            
                            if self.objects[choosing_object]["Value"] == "On":
                                self.objects[choosing_object]["Infor"] == "Off"
                                self.objects[choosing_object]["Value"] == "Off"
                                atData.data["Relays"]["List"][relay]["Source"]["Input"]["Local"]["Manual"] = "Off"
                                while atData.data["Relays"]["List"][relay]["Value"] != "Off":
                                    atData.data["Relays"]["List"][relay]["Value"] = "Off"
                                atData.save("Relays")
                            else:
                                self.objects[choosing_object]["Value"] == "On"
                                self.objects[choosing_object]["Infor"] == "On"
                                atData.data["Relays"]["List"][relay]["Source"]["Input"]["Local"]["Manual"] = "On"
                                while atData.data["Relays"]["List"][relay]["Value"] != "On":
                                    atData.data["Relays"]["List"][relay]["Value"] = "On"
                                atData.save("Relays")

                            self._import_object_dict()
                            self.set_pointer(self.pointer)
                            self.set_notification("Changed")
                            break
                        else:
                            self.set_notification(atData.data["Relays"]['List'][relay]['Name'] + " is not Manual")
                            sleep(0.5)
                            self.set_notification("---")
                    else:
                        self.set_notification(atData.data["Relays"]['List'][relay]['Name'] + " is not Local")
                        sleep(0.5)
                        self.set_notification("---")
                    self.set_notification("---")

        # update to json-server
        atData.data["Monitor"] = self.objects

    def get_objects_json(self):
        self.objects = atData.data["Monitor"]
        

    def update_info(self):
        """
        call frequently to update information to monitoring scree
        """

        wait_time = datetime.now() - self.last_update_time
        if wait_time.total_seconds() > self.UPDATE_TIME:
            self.get_objects_json()
            self._import_object_dict()
            self.set_pointer(self.pointer)
            self.last_update_time = datetime.now()

    def load(self):
        if self.name == Current_Screen.name: 
            if self.rended == False:
                self.rended = True
                self.set_pointer(self.pointer)
            # button
            self.polling_button()
            self.update_info()
        else:
            self.rended = False

atScreen_Monitoring = atFrame_Monitoring()

if __name__ =="__main__":
    Current_Screen.set_name( atScreen_Monitoring.name)
    while 1:
        atScreen_Monitoring.load()