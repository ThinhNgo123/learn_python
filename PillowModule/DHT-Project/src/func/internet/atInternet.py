import os 
import sys
from time import sleep
import threading
import json
sys.path.insert(0,"json")
from atJsonData import atData
try:
    import ifcfg
except:
    os.system("pip install ifcfg")
    import ifcfg

try:
    import public_ip as publish_ip
except:
    os.system("pip install public-ip")
    import public_ip as publish_ip

class atInternet_Class():
    def __init__(self) -> None:
        self.thread = threading.Thread(target= self._thread)
        pass
    
    def read_info(self):
        
        for name, interface in ifcfg.interfaces().items():
            # do something with interface
            # print (interface['device'] )      # Device name
            # print (interface['inet'] )        # First IPv4 found
            # print (interface['inet4']   )     # List of ips
            # print (interface['inet6']   )     # List of ips
            # print (interface['netmask']  )    # Backwards compat: First netmask
            # print (interface['netmasks']   )  # List of netmasks
            # print (interface['broadcast']   ) # Backwards compat: First broadcast
            # print (interface['broadcasts']  ) # List of broadcast

            if str(interface['device']) == "eth0":
                
                # print(info)
                atData.data["Internet"]["Local IP"] = str(interface['inet'])

                atData.data["Internet"]["Ethernet"]["Status"] = "Connecting"
                atData.data["Internet"]["Ethernet"]['IP'] = str(interface['inet'])
                # atData.data["Internet"]["Ethernet"]["Gateway"] = 
                atData.data["Internet"]["Ethernet"]["Netmask"] = str(interface['netmask'])
                atData.data["Internet"]["Ethernet"]["MAC"] = str(interface['ether'])
                atData.setGlobalNotification(str(interface['inet']))

            if str(interface['device']) == "wlan0":
                atData.data["Internet"]["Wifi"]["Status"] = "Disconnect"
                atData.data["Internet"]["Wifi"]['IP'] = str(interface['inet'])
                # atData.data["Internet"]["Wifi"]["Gateway"] = 
                atData.data["Internet"]["Wifi"]["Netmask"] = str(interface['netmask'])
                atData.data["Internet"]["Wifi"]["MAC"] = str(interface['ether'])

            if str(interface['device']) == "tun0":
                atData.data["Internet"]["OpenVPN"]["Status"] = "Connecting"
                atData.data["Internet"]["OpenVPN"]['IP'] = str(interface['inet'])
                # atData.data["Internet"]["OpenVPN"]["Gateway"] = 
                atData.data["Internet"]["OpenVPN"]["Netmask"] = str(interface['netmask'])
            

    def _thread(self):
        sleep(5)
        while 1:
            self.read_info()
            atData.save('Internet')
            sleep(2)

atInternet = atInternet_Class()

if __name__ == "__main__":
    atInternet.thread.start()

