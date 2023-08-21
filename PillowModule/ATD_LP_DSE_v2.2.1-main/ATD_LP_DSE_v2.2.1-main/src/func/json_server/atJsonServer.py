import os
import sys
import threading

class atJson_Server_Class():
    jsonDataPath = 'json/Data.json'
    def __init__(self) -> None:
        self.thread = threading.Thread(target=self._thread)
        self.isHosted = False
        pass
    def _thread(self):
        self.isHosted = True
        os.system("json-server -q -H 0.0.0.0 -w " + self.jsonDataPath + " -p 8000")
        # while 1:
        #     pass
atJsonServer = atJson_Server_Class()
if __name__ == "__main__":
    atJsonServer.thread.start()