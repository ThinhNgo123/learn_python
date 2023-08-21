
# atPing_list.py
# this function will create multi thread to execute pinging function 

import threading
import sys
import os
import subprocess
try:
    from pythonping import ping
except:
    os.system("pip install pythonping")
    from pythonping import ping

# ping('25.7.161.66',verbose=True)
# ping('192.168.1.10',verbose=True)

class atPing_Class():
    def __init__(self, *args,  **kwargs):
        super().__init__(*args,  **kwargs)
        '''
        Initialize object 
        '''
        self.timeout = 1
        self.bytes_num_to_ping = 1

    def average_ping(self,IP, verbose = False):
        '''
        Ping return
        '''
        # print("internal pythonping ... ")
        response = ping(
            IP,
            timeout=self.timeout, 
            count=self.bytes_num_to_ping, 
            verbose=verbose,
            out=None
        )
        if (response.rtt_avg_ms == self.timeout * 1000 ):
            return False
        return response.rtt_avg_ms
    
atPing = atPing_Class()
if __name__ == "__main__":
    atPing.average_ping("8.8.8.8")
