import os
import sys
import threading
try:
    import requests
except:
    os.system("pip install requests")
    import requests
from datetime import datetime
from time import sleep
sys.path.insert(0, 'func/json_server')
from atJsonServer  import atJsonServer

class atJson_Client_Class():
    SERVER_IP = "localhost"
    SERVER_PORT = 8000

    def __init__(self) -> None:
        self.thread = threading.Thread(target=self._thread)

        pass
    def getJson(self,dict:str):
        if atJsonServer.isHosted :
            try:
                getter = requests.get('http://'+ self.SERVER_IP+':'+ str(self.SERVER_PORT)+'/'+dict)
                return getter.json()
            except:
                return False
        else:
            return False
        
    def setJson(self,dict, json):
        if atJsonServer.isHosted :
            try:
                response = requests.post(
                    url= 'http://'+ self.SERVER_IP+':'+ str(self.SERVER_PORT)+'/'+dict,
                    json= json
                )
                return response
            except:
                return False
        else:
            return False
    
    def _thread(self):
        while 1:
            sleep(2)
            pass
    
atJsonClient = atJson_Client_Class()
if __name__ == "__main__":
    print(datetime.now())
    notification = atJsonClient.getJson("Notification")

    print()
    print(datetime.now())

    print(atJsonClient.getJson("Boot"))
    print(datetime.now())

    # print(atJsonClient.setJson("Boot"))
    # print(datetime.now())
