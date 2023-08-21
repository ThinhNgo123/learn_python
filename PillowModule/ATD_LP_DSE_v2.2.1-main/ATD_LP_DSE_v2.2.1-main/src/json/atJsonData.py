#!/usr/bin/env python
import json
import os
import sys
sys.path.insert(0, 'func/json_client')
from atJsonClient  import atJsonClient
from time import sleep
import threading

sys.path.insert(0, 'hmi')
from Current_Screen import Current_Screen 

class atJsonData():
    """
    Manage da
    """
    file_json = None
    DATA_PATH = "json/Data.json"
    BACK_UP_DATA_PATH = "json/BackUpData.json"
    DEFAULT_DATA_PATH = "json/DefaultData.json"
    SCREEN_NAME_PATH = "json/ScreenName.json"
    _is_saving = False
    def __init__(self) -> None:
        """
        Init data 
        """
        self.data = {}
        try :
            os.system("sudo chmod 777 " + self.DATA_PATH)
            # open and load data form Path
            self.file_json = open(self.DATA_PATH)
            self.data = json.load(self.file_json)

            self.data["Sensors"]["Setting Sensor"] = "1"
        except:
            # print("Data.json is missing or error, generating ....")
            os.system("sudo chmod 777 " + self.DATA_PATH)
            # back to lat backup
            self.set_to_back_up()
            self.data["Sensors"]["Setting Sensor"] = "1"
            os.system("sudo chmod 777 " + self.DATA_PATH)
        
        file_screen_name = open(self.SCREEN_NAME_PATH)
        self.screen_names = json.load(file_screen_name)
        self.thread = threading.Thread(target= self._thread)
        self.thread_back_up = threading.Thread(target= self._thread_back_up)

    def reload(self):
        """
        reload the data.json again to update all saved setting
        """
        self.file_json = open(self.DATA_PATH)
        self.data = json.load(self.file_json)
        self.file_json.close()

    def save(self, option = None):
        self._is_saving = True
        """
        Save all the setting in data in to Data.json
        """
        # with open(self.DATA_PATH, "w") as writefile:
        #     json.dump(self.data, writefile, indent=2)

        #  write to json_server by atJsonClient
        try:
            if option == None:
                atJsonClient.setJson("Sensors",     self.data['Sensors'])
                atJsonClient.setJson("FTP_Servers", self.data['FTP_Servers'])
                atJsonClient.setJson("Database",    self.data['Database'])
                atJsonClient.setJson("Memory",      self.data['Memory'])
                atJsonClient.setJson("Errors",      self.data['Errors'])
                atJsonClient.setJson("Internet",    self.data['Internet'])
                atJsonClient.setJson("Web_Server",  self.data['Web_Server'])
                atJsonClient.setJson("Power",       self.data['Power'])
                atJsonClient.setJson("Advances",    self.data['Advances'])
                atJsonClient.setJson("Device",      self.data['Device'])
                atJsonClient.setJson("User",        self.data['User'])
                atJsonClient.setJson("About",       self.data['About'])
                atJsonClient.setJson("Sensors",     self.data['Sensors'])
            else:
                atJsonClient.setJson(option,     self.data[option])
        except Exception as error:
            print("[Error] atData",error)
        self._is_saving = False
        
    def set_to_back_up(self):
        file_backup_data = open(self.BACK_UP_DATA_PATH)
        back_up_data = json.load(file_backup_data)

        self.data = back_up_data

        # print("Set to last backup of json data")
        os.system("sudo chmod 777 " + self.DATA_PATH)
        with open(self.DATA_PATH, "w") as writefile:
            json.dump(self.data, writefile, indent=4)
        os.system("sudo chmod 777 " + self.DATA_PATH)
        sleep(1)
        self.setGlobalNotification("---")

    def back_up(self):
        
        # print("back up data json")
        with open(self.BACK_UP_DATA_PATH, "w") as writefile:
            json.dump(self.data, writefile, indent=4)
        pass

    def set_to_default(self):
        """
        Restore all setting and data to default as DefaultJson.json
        """
        file_default_data = open(self.DEFAULT_DATA_PATH)
        default_data = json.load(file_default_data)

        self.data = default_data
        
        self.setGlobalNotification("Default restore")
        os.system("sudo chmod 777 " + self.DATA_PATH)
        with open(self.DATA_PATH, "w") as writefile:
            json.dump(self.data, writefile, indent=4)
        os.system("sudo chmod 777 " + self.DATA_PATH)
        
    def add_Sensor(self):
        """
        Add a sensor and save it into the Data.json
        """
        new_Sensor_Index = self.data["Sensors"]["Number"] + 1
        self.data["Sensors"]["Number"] = new_Sensor_Index
        new_Sensor_Index_str = str(new_Sensor_Index)
        self.data["Sensors"]["List"][new_Sensor_Index_str] = self.data["Sensors"]["Default"]
        self.save("Sensors")
        
    def clone_Sensor(self,ID):
        new_Sensor_Index = self.data["Sensors"]["Number"] + 1
        self.data["Sensors"]["Number"] = new_Sensor_Index
        new_Sensor_Index_str = str(new_Sensor_Index)
        self.data["Sensors"]["List"][new_Sensor_Index_str] = self.data["Sensors"]["List"][str(ID)]
        self.save("Sensors")

    def add_Relay(self):
        new_Relay_Index = self.data["Relays"]["Number"] + 1
        self.data["Relays"]["Number"] = new_Relay_Index
        new_Relay_Index_str = str(new_Relay_Index)
        self.data["Relays"]["List"][new_Relay_Index_str] = self.data["Relays"]["Default"]
        self.save("Relays")
 
    def clone_Relay(self,ID):
        new_Relay_Index = self.data["Relays"]["Number"] + 1
        self.data["Relays"]["Number"] = new_Relay_Index
        new_Relay_Index_str = str(new_Relay_Index)
        self.data["Relays"]["List"][new_Relay_Index_str] = self.data["Relays"]["List"][str(ID)]
        self.save("Relays")

    def delete_Sensor(self, ID):
        """
        Delete sensor from data anf save to data.json
        """
        # for delete all
        old_list_length = len(self.data["Sensors"]["List"])
        for count in range(1,old_list_length):
            if count >= int(ID):
                self.data["Sensors"]["List"][str(count)] = self.data["Sensors"]["List"][str(count+1)]
        self.data["Sensors"]["List"].pop(str(old_list_length))
        self.data["Sensors"]["Number"] = len(self.data["Sensors"]["List"])
        self.save("Sensors")

    def delete_Relay(self,ID):
        old_list_length = len(self.data["Relays"]["List"])
        for count in range(1,old_list_length):
            if count >= int(ID):
                self.data["Relays"]["List"][str(count)] = self.data["Relays"]["List"][str(count+1)]
        self.data["Relays"]["List"].pop(str(old_list_length))
        self.data["Relays"]["Number"] = len(self.data["Relays"]["List"])
        self.save("Relays")

    def login(self, user_name = None, password = None):
        for id in self.data["User"]["List"]:
            if self.data["User"]["List"][id]["User Name"] == user_name:
                if self.data["User"]["List"][id]["Password"] == password:
                    self.data["User"]["User"] = user_name
                    self.data["User"]["User Permission"] = self.data["User"]["List"][id]["Permission"]
                    self.data["User"]["Password"] = password
                    return "Login successfully"
        return "Login fail"

    def setGlobalNotification(self,notification):
        if self.data["Notification"]["Info"] != str(notification):
            self.data["Notification"]["Info"] = str(notification)
            self.data["Notification"]["Update"] = 1
    
    def save_error(self,error:str):
        self.data["Errors"]['Last'] = error
        self.data["Errors"]['List'].append(error)
        self.save("Errors")

    def request_reboot(self):
        self.data["Power"]['Reset'] = "Yes"
        self.save("Power")

    def delete_request_reboot(self):
        self.data["Power"]['Reset'] = "No"
        self.save("Power")

    def _thread_back_up(self):
        while 1:
            sleep(60*60)
            # save back up datajson 
            self.back_up()
    
    def _thread(self):
        # Update all json server to atData.data
        sleep(10)
        self.thread_back_up.start()
        while 1:
            sleep(3)
            # print("Check update from remote")
            while self._is_saving == True :
                # wait for saving function is done
                sleep(0.1)
            try:
                self.data["Remote"] = atJsonClient.getJson("Remote")
                # print(Remote)
                if  self.data["Remote"]["Request"] == "Update":
                        
                    # update all setting data from 
                    self.data["Sensors"]    = atJsonClient.getJson("Sensors")
                    self.data["Relays"]    = atJsonClient.getJson("Relays")
                    self.data["FTP_Servers"]= atJsonClient.getJson("FTP_Servers")
                    self.data["Database"]   = atJsonClient.getJson("Database")
                    self.data["Errors"]     = atJsonClient.getJson("Errors")
                    self.data["Web_Server"] = atJsonClient.getJson("Web_Server")
                    self.data["Power"]      = atJsonClient.getJson("Power")
                    self.data["Advances"]   = atJsonClient.getJson("Advances")
                    self.data["Device"]     = atJsonClient.getJson("Device")
                    self.data["User"]       = atJsonClient.getJson("User")

                    # response remote
                    self.data["Remote"]["Request"] = "None"
                    self.data["Remote"]["Target"] = "None"
                    self.data["Remote"]["Response"] = "Update Successfully"
                    print("[Event]:Update All From Remote Successfully")
                    atJsonClient.setJson("Remote",self.data["Remote"])
                    
                    # notification
                    self.data["Notification"]["Info"] = "Remote edited setting"
                    self.data["Notification"]["Update"] = 1
                    sleep(0.5)
                    self.data["Notification"]["Info"] = "---"
                    self.data["Notification"]["Update"] = 1
                    Current_Screen.set_name(
                        name= self.screen_names["Monitoring"]["screen name"]
                    )
            except Exception as error:
                    print("[Error 3]",error)
             

atData = atJsonData()

if __name__ == "__main__":
   
    pass
    