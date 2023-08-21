import sys
from time import sleep
import threading
import os
import ftplib
from datetime import datetime
sys.path.insert(0,"json")
from atJsonData import atData

# for sensor function
sys.path.insert(0,'func/sensor')
from atSensor import atSensor

# for influx function
sys.path.insert(0, 'func/influx')
from atInfluxDB import atInfluxDB

# for ping function
sys.path.insert(0, 'func/ping')
from atPing import atPing

sys.path.insert(0,'func/json_client')
from atJsonClient import atJsonClient

class atFTP_Server_Class():

    def __init__(self, FTP_Server_Name = "FTP1") -> None:
        self.FTP_Server_Name = FTP_Server_Name
        self.status = "Failed"
        self.error_connection = False
        self.error_connection_count = 0
        self.error_send_file = False
        self._update_ftp_infor()
        self.thread_check_connect = threading.Thread(target= self._thread_check_connect)
    
    def _update_ftp_infor(self):
        self.activate = atData.data["FTP_Servers"][self.FTP_Server_Name]["Activate"]
        self.ftp_ip = atData.data["FTP_Servers"][self.FTP_Server_Name]["IP"]
        self.ftp_port = int(atData.data["FTP_Servers"][self.FTP_Server_Name]["Port"])
        self.ftp_user = atData.data["FTP_Servers"][self.FTP_Server_Name]["User"]
        self.ftp_password = atData.data["FTP_Servers"][self.FTP_Server_Name]["Password"]
        self.ftp_folder = atData.data["FTP_Servers"][self.FTP_Server_Name]["Folder"]
        self.send_time = int(atData.data["FTP_Servers"][self.FTP_Server_Name]["Send Time"])
        self.time_out = int(atData.data["FTP_Servers"][self.FTP_Server_Name]["Time Out"])
    
    def check_connection(self):
        self._update_ftp_infor()
        try:
            # urllib.request.urlopen('http://google.com')
            if atPing.average_ping("8.8.8.8") != False:
                ftp_server = ftplib.FTP(
                    host=   self.ftp_ip,
                    timeout=self.time_out,
                    user=   self.ftp_user,
                    passwd= self.ftp_password
                )
                ftp_server.quit()
                self.status = "Connecting"
                self.error_connection = False
            else:
                self.status = "No internet"
                error_log = "[ERROR-0] "+ \
                            self.FTP_Server_Name  + \
                            ' check_connection - '+ \
                            str(datetime.now())+ \
                            ' - No internet'
                if self.error_connection == False:
                    self.error_connection = True
                    atData.save_error(error_log)
                print('[ERROR]',error_log)
            # print('***************************************************')
        except Exception as error :
            self.status = "Disconnect"
            error_log = "[ERROR-0] "+ \
                        self.FTP_Server_Name  + \
                        ' check_connection - '+ \
                        str(datetime.now())+ \
                        ' - '+ \
                        str(error)
            if self.error_connection == False:
                self.error_connection = True
                atData.save_error(error_log)
            print('[ERROR]',error_log)
        finally:
            if atData.data["FTP_Servers"][self.FTP_Server_Name]["Status"] != self.status:
                atData.data["FTP_Servers"][self.FTP_Server_Name]["Status"] = self.status
                atData.save("FTP_Servers")

    def send_file(self,des_folder_path,source_file_path = None):
        self._update_ftp_infor()
        
        try:
            ftp_server = ftplib.FTP(host= self.ftp_ip,
                                    user= self.ftp_user,
                                    passwd= self.ftp_password, 
                                    timeout= 1)
            self._go_make_dir(ftp_server, des_folder_path)
            self._send_ftp(ftp_server, source_file_path)
            ftp_server.close()
            # update status
            self.status = "Connecting"
            self.error_send_file = False
            return "Done"
        except Exception as error:
            # ftp_server.close()
            self.status = "Disconnected"
            error_log = "[ERROR-1] "+ \
                    self.FTP_Server_Name + \
                    " - Can not send file - "+ \
                    str(datetime.now())+ \
                    " - "+ \
                    str(error)
            if self.error_connection == False:
                self.error_connection = True
                atData.save_error(error_log)
            print(error_log)
            return "Failed"
    
    def _go_make_dir(self, ftp_server, folder_path):
        # get the destination folder
        if folder_path[0] == "/":
            ftp_server.cwd("/")
        dir_path_list = folder_path.split("/")

        if dir_path_list[0] == "":
            dir_path_list.pop(0)
        # change to working dir to the folder, and make if the folder is not existed
        for folder in dir_path_list:
            try:
                ftp_server.cwd(folder)
            except Exception as error:
                # print(error)
                print("Try to create the folder: " + folder)
                try:
                    ftp_server.mkd(folder)
                    ftp_server.cwd(folder)
                except Exception as error:
                    # print(error)
                    print("Can not create the folder: " + folder)
                    return "Failed"
    
    def _send_ftp(self,ftp_server,file_path ):
        try:
            file_name = os.path.basename(file_path).split('/')[-1]
            # send the file to server
            log_file = open(file_path, 'rb')
            file_size = os.stat(file_path).st_size*8
            # Send the text file to the FTP server
            ftp_server.storbinary('STOR %s' % file_name, log_file, file_size)
            # close all engine
            log_file.close()
        except Exception as error:
            error_log = "[ERROR-2]"+ \
                        self.FTP_Server_Name + \
                        "_send_ftp()"+ \
                        str(datetime.now())+ \
                        " : "+ \
                        str(error)
            atData.save_error(error_log)
            print(error_log)

    def _thread_check_connect(self):
        while 1:
            sleep(2)
            self._update_ftp_infor()
            if self.activate == "Enable":
                self.check_connection()
                # print(self.FTP_Server_Name," check")
            
atFTP_1_Server = atFTP_Server_Class(
    FTP_Server_Name = "FTP1")

if __name__ == "__main__":
    
    atFTP_1_Server.thread_check_connect.start()
    while 1:
        print(atData.data["FTP_Servers"]["FTP1"]["Status"])
    pass