import sys
from time import sleep
import threading
from datetime import datetime, timedelta, timezone
import ftplib

import os
from dateutil import tz
try:
    from datetimerange import DateTimeRange
except:
    os.system("pip install DateTimeRange")
    from datetimerange import DateTimeRange

sys.path.insert(0,"func/tool")
from atTimeConvert import atTimeConvert


sys.path.insert(0,"json")
from atJsonData import atData

# for influx function
sys.path.insert(0, 'func/influx')
from atInfluxDB import atInfluxDB

# for FTP server function
sys.path.insert(0, 'func/ftp')
from atFTPServer import atFTP_1_Server

class atLogger_TT10_Class():

    LOG_FILE_PATH = "buf/"    
    def __init__(self,FTP_Server_Name = "FTP-1 Server") :
        self.FTP_Server_Name = FTP_Server_Name
        self.thread = threading.Thread(target=self._thread )
        self.thread_check = threading.Thread(target=self._thread_check )
        pass

    def create_file_log(self, start_time = "-1m30s", stop_time = None):
        """
        - start_time: not fill to check at present, file datetime type to check a time rang,
        """
        # context of log file
        log = ""
        sensor_name_list = []

        context = {}
        context_line = ""
        # read sensor name list:
        for sensor in atData.data["Sensors"]["List"]:
            # name
            sensor_name = atData.data["Sensors"]["List"][sensor]["Name"]
            sensor_name_list.append(sensor_name)
            context[sensor_name] = {
                "value" : "",
                "status" :[]
            }


            if(stop_time == None):
                tables = atInfluxDB.read(
                    start_time= start_time,
                    measurement= sensor_name,
                    field_list= ["Calib Value"],
                    last= True
                )
                time = datetime.now()
                time_stamp= "{0:0=4d}".format(time.year)  + \
                            "{0:0=2d}".format(time.month) + \
                            "{0:0=2d}".format(time.day)   + \
                            "{0:0=2d}".format(time.hour)  + \
                            "{0:0=2d}".format(time.minute)+ \
                            "00".format(time.second)
            else:
                start_time_delta = (datetime.now() - start_time).total_seconds() /60
                stop_time_delta = (datetime.now() - stop_time).total_seconds() /60

                tables = atInfluxDB.read(
                    start_time= "-{0:0}m".format(int(start_time_delta)),
                    stop_time= "-{0:0}m".format(int(stop_time_delta)),
                    measurement= sensor_name,
                    field_list= ["Calib Value"],
                    last= True
                )
                time = stop_time
                time_stamp= "{0:0=4d}".format(time.year)  + \
                            "{0:0=2d}".format(time.month) + \
                            "{0:0=2d}".format(time.day)   + \
                            "{0:0=2d}".format(time.hour)  + \
                            "{0:0=2d}".format(time.minute)+ \
                            "00".format(time.second)

            # print(tables)
            
            # read the last value of every sensor
            for table in tables:
                # # for record in table:
                for record in table.records:
                    context_line =  sensor_name + \
                            "   " + \
                            str(record["_value"]) + \
                            "   " + \
                            record["Unit"] + \
                            "   " + \
                            time_stamp +\
                            "   "
                    context[sensor_name]["value"] = context_line
                    context[sensor_name]["status"].append(record["Status"])

        # print(context)
        for sensor in context:
            log += context[sensor]['value']
            if "Error" in context[sensor]['status']:
                log += "02\n"
            elif "Calib" in context[sensor]['status']:
                log += "01\n"
            elif "Normal" in context[sensor]['status']:
                log += "00\n"

        # create file 
        log_file_name = atData.data[ "FTP_Servers"][self.FTP_Server_Name]["File Name"] + \
            "_" + \
            time_stamp +\
            ".txt"

        # print(log)
        log_file_path = self.LOG_FILE_PATH + log_file_name

        try:
            log_file = open( log_file_path, "w")
            log_file.write(log)
            log_file.close()
            os.system("sudo chmod 777 " + log_file_path)
        except Exception as error:
            os.system("sudo chmod 777 " + log_file_path)
            print("[Error]-create-file-log: ", error)

        return log_file_path

    def make_send_log(self):
        time_log_delay = int(atData.data["FTP_Servers"][self.FTP_Server_Name]["Send Time"])
        # check time to create log and send 
        time_now = datetime.now()
        time_now = datetime(
            year=time_now.year,
            month=time_now.month,
            day=time_now.day,
            hour= time_now.hour,
            minute= time_now.minute,
            second= 0
        )
        delta = time_now - datetime(2022,1,1)
        total_minutes = delta.total_seconds() /60
        if (total_minutes % time_log_delay == 0):
            # make path 
            year = datetime.now().year
            month = datetime.now().month
            day = datetime.now().day
            ftp_des_folder_path =   atFTP_1_Server.ftp_folder + \
                                    '/'+\
                                    "{0:0=4d}".format(year)+\
                                    '/'+\
                                    "{0:0=2d}".format(month)+\
                                    '/'+\
                                    "{0:0=2d}".format(day)
            # create the log 
            log_file_path = self.create_file_log()
            # send log to ftp server
            atFTP_1_Server.send_file(
                des_folder_path= ftp_des_folder_path,
                source_file_path=log_file_path
            )
            os.system("sudo rm " + log_file_path)
        pass

    def _thread(self):
        while 1:
            if  atData.data["FTP_Servers"][self.FTP_Server_Name]["Status"] == "Connecting" and \
                atData.data["FTP_Servers"][self.FTP_Server_Name]["Activate"] == "Enable":
                try:
                    self.make_send_log()
                    sleep(45)
                except Exception as error:
                    error_log = "[error]]"
                    print('[ERROR]',error)
                    sleep(1)
            else:
                sleep(1)
    
    def _thread_check(self):
        while 1:
            if  atData.data["FTP_Servers"][self.FTP_Server_Name]["Status"] == "Connecting" and \
                atData.data["FTP_Servers"][self.FTP_Server_Name]["Activate"] == "Enable":
                
                sleep(int(atData.data["FTP_Servers"][self.FTP_Server_Name]["Check Time"]) * 60 *60)
                try:
                    atData.setGlobalNotification( "Checking FTP1 Logs")
                    self.check_make_send_log()
                except Exception as error:
                    error_log = '[ERROR] - ' +\
                                self.FTP_Server_Name +\
                                " - " +\
                                str(datetime.now()) +\
                                ' : ' +\
                                str(error)

                    atData.data['Errors']["Last"] = error_log
                    atData.data['Errors']["List"].append(error_log)
                    atData.save('Errors')
                    print(error_log)

                atData.data["Notification"]["Info"] = "---"
                atData.data["Notification"]["Update"] = 1
                sleep(1)
            else:
                sleep(1)
    
    def check_make_send_log(self):
        sensor_name_list = []
        
        time_now = datetime.now()
        first_record_time = time_now

        # read sensor name list:
        for sensor in atData.data["Sensors"]["List"]:
            # name
            sensor_name = atData.data["Sensors"]["List"][sensor]["Name"]
            sensor_name_list.append(sensor_name)

            tables = atInfluxDB.read(
                start_time= "-10y",
                measurement= sensor_name,
                field_list= ["Calib Value"],
                first=True
            )

            # print("Time now : " + str(first_record_time))
            # read the last value of every sensor
            for table in tables:
                # # for record in table:
                for record in table.records:
                    # change record["_time"] to datetime
                    datetime_local = atTimeConvert.to_local(record["_time"])
                    if datetime_local < first_record_time:
                        first_record_time = datetime_local
                
        # print("First Time of records: "+ str(first_record_time))
        

        # create a ftp connection 
        ftp_server = ftplib.FTP(
                host= atData.data["FTP_Servers"][self.FTP_Server_Name]["IP"],
                user= atData.data["FTP_Servers"][self.FTP_Server_Name]["User"],
                passwd= atData.data["FTP_Servers"][self.FTP_Server_Name]["Password"],
                # timeout= int(atData.data["FTP_Servers"][self.FTP_Server_Name]["Time Out"])
                # timeout= 100000000
            )
        
        ftp_server_wd = atData.data["FTP_Servers"][self.FTP_Server_Name]["Folder"]

        #  check. make and send missing file
        time_range      = DateTimeRange(first_record_time,time_now)
        delay_send_time = int(atData.data["FTP_Servers"][ self.FTP_Server_Name]["Send Time"]) # minute
        for time in time_range.range(timedelta(minutes=1)):
            time = datetime(
                year=time.year,
                month=time.month,
                day=time.day,
                hour= time.hour,
                minute= time.minute,
                second= 0
            )
            delta = time - datetime(2023,1,1)
            total_minutes = delta.total_seconds() /60

            if total_minutes % delay_send_time == 0:
                print("Time to check: " + str(time))
                new_ftp_server_wd = '/'  + \
                        atData.data["FTP_Servers"][self.FTP_Server_Name]["Folder"] +\
                        '/'  + \
                        "{0:0=4d}".format(time.year)  + \
                        '/'  + \
                        "{0:0=2d}".format(time.month) + \
                        '/'  + \
                        "{0:0=2d}".format(time.day)
                if ftp_server_wd !=new_ftp_server_wd :
                    ftp_server_wd = new_ftp_server_wd
                    try:
                        ftp_server.cwd(ftp_server_wd)
                        file_name_list_wd = ftp_server.nlst()
                    except:
                        atFTP_1_Server._go_make_dir(ftp_server,ftp_server_wd)
                        file_name_list_wd = ftp_server.nlst()

                # print("Folder to check: " + ftp_server_wd)

                time_stamp= "{0:0=4d}".format(time.year)  + \
                            "{0:0=2d}".format(time.month) + \
                            "{0:0=2d}".format(time.day)   + \
                            "{0:0=2d}".format(time.hour)  + \
                            "{0:0=2d}".format(time.minute)+ \
                            "00".format(time.second)
                checking_file_name = atData.data[ "FTP_Servers"][self.FTP_Server_Name]["File Name"] + \
                                "_" + \
                                time_stamp +\
                                ".txt"

                print(checking_file_name)

                # check the checking file name is existed
                if not checking_file_name in file_name_list_wd:
                    print(checking_file_name + " is not existed, creating")
                    new_file_log_path =  self.create_file_log(
                        start_time= time - timedelta(hours= 24),
                        stop_time = time
                    )
                    atFTP_1_Server._send_ftp(ftp_server,new_file_log_path)
                    os.system("sudo rm " + new_file_log_path)
                    pass
                else:
                    pass
        ftp_server.close()
        # os.system("sudo rm buf/*")
                                    
atLogger_TT10 = atLogger_TT10_Class(FTP_Server_Name = "FTP1")

if __name__ == "__main__":
    # create log and send to FTP
    atLogger_TT10.check_make_send_log()