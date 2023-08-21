import sys
from time  import sleep
import threading
sys.path.insert(0,"json")
from atJsonData import atData


class atMonitor_Class():
    DELAY_TIME = 1 # second
    def __init__(self) -> None:
        
      self.thread = threading.Thread(target= self._thread)

    def reload(self):
        new_monitor_json = {}
        # FTP Servers
        for fpt_server in atData.data["FTP_Servers"]:
            if atData.data["FTP_Servers"][fpt_server]["Activate"] == "Enable" :
                new_monitor_json[fpt_server]= {
                    "Type":"FTP Server",
                    "Status": "Normal",
                    "Infor": atData.data["FTP_Servers"][fpt_server]["Status"]
                }
                if atData.data["FTP_Servers"][fpt_server]["Status"] != "Connecting":
                    new_monitor_json[fpt_server]['Status'] = "Error"

        # Sensors 
        for sensor in atData.data["Sensors"]["List"]:
            sensor_name = atData.data["Sensors"]["List"][sensor]["Name"]
            
            sensor_status = atData.data["Sensors"]["List"][sensor]["Status"]
            
            calib_value = atData.data["Sensors"]["List"][sensor]["Calib Value"]
            calib_value_str =   "{:.2f}".format(calib_value) + \
                                " " + \
                                atData.data["Sensors"]["List"][sensor]["Unit"]

            raw_value = atData.data["Sensors"]["List"][sensor]["Raw Value"]

            try:
                user_set_sensor_status = atData.data["Monitor"][sensor_name]["Status"]
                # print(sensor_name,user_set_sensor_status)
            except:
                atData.data["Monitor"][sensor_name] = {
                    "Type":"Sensor",
                    "Status" : sensor_status,
                    "Infor" : calib_value_str,
                    "Raw" : raw_value,
                    "Calib" : calib_value
                }
                user_set_sensor_status = atData.data["Monitor"][sensor_name]["Status"]
                # print(sensor_name,user_set_sensor_status)
            
            if user_set_sensor_status == "Calib":
                atData.data["Sensors"]["List"][sensor]["Status"] = "Calib"
                new_monitor_json[sensor_name] = {
                    "Type":"Sensor",
                    "Status" : user_set_sensor_status,
                    "Infor" : calib_value_str,
                    "Raw" : raw_value,
                    "Calib" : calib_value
                }
            else:
                new_monitor_json[sensor_name] = {
                    "Type":"Sensor",
                    "Status" : sensor_status,
                    "Infor" : calib_value_str,
                    "Raw" : raw_value,
                    "Calib" : calib_value
                }
        # Relays
        for relay in atData.data["Relays"]["List"]:
            relay_name = atData.data["Relays"]["List"][relay]["Name"]
            relay_status = atData.data["Relays"]["List"][relay]["Status"]
            relay_value = atData.data["Relays"]["List"][relay]["Value"]
            
            try:
                user_set_value = atData.data["Monitor"][relay_name]["Value"]
            except:
                atData.data["Monitor"][relay_name] = {
                    "Type":"Relay",
                    "Status" : relay_status,
                    "Infor" : relay_value,
                    "Value" : relay_value,
                }
                user_set_value = atData.data["Monitor"][relay_name]["Value"]

            new_monitor_json[relay_name] = {
                "Type":"Relay",
                "Status" : relay_status,
                "Infor" : relay_value,
                "Value" : relay_value,
            }
            
            # if atData.data["Relays"]["List"][relay]["Source"]["Input"]["Protocol"]=="Local" :
            #     if atData.data["Relays"]["List"][relay]["Source"]["Input"]["Local"]["Mode"]=="Manual":
            #         atData.data["Relays"]["List"][relay]["Source"]["Value"] = user_set_value
            #         print("Relay user set: ",user_set_value)

        atData.data["Monitor"] = new_monitor_json
        atData.save("Monitor")

    def _thread(self):
        while 1:
            self.reload()
            sleep(self.DELAY_TIME)

atMonitor = atMonitor_Class()

if __name__ == "__main__":
    atMonitor.thread.start()