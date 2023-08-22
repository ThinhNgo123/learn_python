import os 
import sys
from time import sleep
import threading
from datetime import datetime
try:
    from dateutil import tz
except:
    os.system("pip install python-dateutil")
    from dateutil import tz

try:    
    from influxdb_client import InfluxDBClient
    from influxdb_client import Point
except:
    os.system("pip3 install --upgrade influxdb-client")
    from influxdb_client import InfluxDBClient
    from influxdb_client import Point

try: 
    from influxdb_client.client.write_api import SYNCHRONOUS
except:
    os.system("pip install influxdb-client[async]")
    from influxdb_client.client.write_api import SYNCHRONOUS

sys.path.insert(0,"json")
from atJsonData import atData

sys.path.insert(0,"func/tool")
from atTimeConvert import atTimeConvert


class atInfluxDB_Class():
    
    def __init__(self) -> None:
        # self.url =atData.data["Database"]["Influxdb2"]["url"]
        # self.org = atData.data["Database"]["Influxdb2"]["org"]
        # self.bucket = atData.data["Database"]["Influxdb2"]["bucket"]
        # self.token = atData.data["Database"]["Influxdb2"]["token"]
        # self.location = atData.data["Database"]["Influxdb2"]["location"]

        # self.client = InfluxDBClient(
        #     url= self.url,
        #     token= self.token,
        #     org= self.org,
        # )
        # self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        # self.query_api = self.client.query_api()
        self.error_write_event = False
        self.error_write_sensor = False
        self.error_read = False
        self.error_list_measurements = False
        self.thread = threading.Thread( target= self._thread)

    def write_sensor(  self, 
                measurement = "Temperature", 
                field = "Raw Value",
                value = 0 ,
                unit = "unit",
                status = "Normal",
                location = "default location",
                device_ID = "default ID",
                device_subID = "default subID",
                device_type = "default type",
                station = "default station",
                ) -> None:

        url =atData.data["Database"]["Influxdb2"]["url"]
        org = atData.data["Database"]["Influxdb2"]["org"]
        bucket = atData.data["Database"]["Influxdb2"]["bucket"]
        token = atData.data["Database"]["Influxdb2"]["token"]
        location = atData.data["Database"]["Influxdb2"]["location"]

        try:
            client = InfluxDBClient(
                url= url,
                token= token,
                org= org,
            )
            write_api = client.write_api(write_options=SYNCHRONOUS)
            
            # write value
            point = Point(measurement).\
                tag("Status", status).\
                tag("Unit", unit).\
                tag("Location", location).\
                tag("Device ID", device_ID).\
                tag("Device Sub-ID", device_subID).\
                tag("Device Type", device_type).\
                tag("Station", station).\
                field(field, float(value))

            write_api.write(bucket= bucket,  record= point)
            self.error_write_sensor = False
            return True
        except Exception as e:
            error = "Influxdb-write-sensor " + \
                    str(datetime.now())+ \
                    str(e)
            if self.error_write_sensor == False:
                atData.data["Errors"]['Last'] = error
                atData.data["Errors"]["List"].append(error)
                atData.save("Errors")
                self.error_write_sensor = True
            print("[ERROR]",error)
        client.close()
        return False

    def write_event(  self, 
                measurement ="Power", 
                field = "ON", 
                value = "1" ,
                location = "Hanoi",
                device_ID = "default device id",
                device_subID = "default subID",
                device_type = "default type",
                station = "default station",
                ) -> None:
        url =atData.data["Database"]["Influxdb2"]["url"]
        org = atData.data["Database"]["Influxdb2"]["org"]
        bucket = atData.data["Database"]["Influxdb2"]["bucket"]
        token = atData.data["Database"]["Influxdb2"]["token"]
        location = atData.data["Database"]["Influxdb2"]["location"]

        client = InfluxDBClient(
            url= url,
            token= token,
            org= org,
        )
        write_api = client.write_api(write_options=SYNCHRONOUS)
        point = Point(measurement).\
            tag("Location", location).\
            tag("Device ID", device_ID).\
            tag("Device Sub-ID", device_subID).\
            tag("Device Type", device_type).\
            tag("Station", station).\
            field(field, value)

        try:
            write_api.write(bucket= bucket,  record= point)
            self.error_write_event = False
            return True
        except Exception as e:
            if self.error_write_event == False:
                error = "Influxdb-write-event " + str(e)
                atData.data["Errors"]['Last'] = error
                atData.data["Errors"]["List"].append(error)
                atData.save("Errors")
                self.error_write_event = True
                print("[ERROR]",error)
        client.close()
        return False
        
    def store(self):
        """
        this function will read data from data json and store it to database
        """
        # store sensor 
        for sensor in atData.data["Sensors"]["List"]:
            # name
            sensor_name = atData.data["Sensors"]["List"][sensor]["Name"]
            if not "Default" in sensor_name:
                # value
                calib_value = atData.data["Sensors"]["List"][sensor]["Calib Value"]
                raw_value = atData.data["Sensors"]["List"][sensor]["Raw Value"]
                # unit
                unit_sensor = atData.data["Sensors"]["List"][sensor]["Unit"]
                # Status
                sensor_status = atData.data["Sensors"]["List"][sensor]["Status"]
                # Device ID
                device_id = atData.data["Device"]["ID"]
                device_sub_id = atData.data["Device"]["subID"]
                # location
                location = str(atData.data["Device"]["Location"]["X"]) + ","+ str(atData.data["Device"]["Location"]["Y"])
                # type
                device_type = atData.data["Device"]["Type"]
                # station
                device_station = atData.data["Device"]["Station"]

                self.write_sensor(
                    measurement= sensor_name,
                    field= "Calib Value",
                    value= calib_value,
                    unit=  unit_sensor,
                    status= sensor_status,
                    device_ID= device_id,
                    device_subID= device_sub_id,
                    location= location,
                    device_type=device_type,
                    station=device_station
                )
                self.write_sensor(
                    measurement= sensor_name,
                    field= "Raw Value",
                    value= raw_value,
                    unit=  unit_sensor,
                    status= sensor_status,
                    device_ID= device_id,
                    location= location,
                    device_type=device_type,
                    station=device_station
                )
    
    def read(self, 
        bucket = "atlab",
        start_time = "-1h",
        stop_time = None,
        measurement = "Temperature",
        field_list = ["Calib Value"],
        tag_list = None,
        last = False,
        first = False,
        aggregateWindow = None
        ):
        '''
        - start_time : is a string "-1h" or or datetime.datetime
        - stop_time : a datetime.datetime
        - measurement : the _measurement with default is "Sensors"

        '''
        url =atData.data["Database"]["Influxdb2"]["url"]
        org = atData.data["Database"]["Influxdb2"]["org"]
        bucket = atData.data["Database"]["Influxdb2"]["bucket"]
        token = atData.data["Database"]["Influxdb2"]["token"]

        client = InfluxDBClient(
            url= url,
            token= token,
            org= org,
        )
        query_api = client.query_api()

        query = 'from(bucket:"' + bucket +'")'
        
        # add time range:
        if stop_time == None:
            query += '|> range(start: '+ start_time +')'
        else:
            # 
            query += '|> range(start: '+ start_time +', stop: '+ stop_time +')'
        
        # add measurement to query
        query += '|> filter(fn:(r) => r._measurement == "' + measurement + '")'

        #  add field list to query
        # '|> filter(fn:(r) => r["_field"] == "' + field + '" or r["_field"] == "Default")'
        query += '|> filter(fn:(r) =>'
        for field_index in range(0,len(field_list)):
            # read field name
            field = field_list[field_index]
            query += 'r["_field"] == "' + field +'"'
            
            if not field_index == len(field_list) - 1:
                query += ' or '
            else:
                query += ')'


        # for aggregateWindow
        if aggregateWindow != None:
            query += '|> aggregateWindow(every: '+ str(aggregateWindow['Every Minute']) + \
                     'm, fn: ' + str(aggregateWindow['FN']) + \
                     ', createEmpty: ' + str(aggregateWindow['Create Empty']) + ')'

        if last == True :
            query += '|> last()' 
        if first == True :
            query += '|> first()' 

        # Query and return
        # print(query)
        result = False
        try:
            result = query_api.query(org= org,query= query)
            self.error_read = False
            client.close()
            return result
        except Exception as e:
            error = "Influxdb-read " + \
                    str(datetime.now())+ \
                    str(e)
            if self.error_read == False:
                atData.data["Errors"]['Last'] = error
                atData.data["Errors"]["List"].append(error)
                atData.save("Errors")
                self.error_read = True
            print("[ERROR]",error)
        client.close()
        return False

    def _thread(self):
        # Device ID
        device_id = atData.data["Device"]["ID"]
        device_sub_id = atData.data["Device"]["subID"]
        # location
        location = str(atData.data["Device"]["Location"]["X"]) + ","+ str(atData.data["Device"]["Location"]["Y"])
        # type
        device_type = atData.data["Device"]["Type"]
        # station
        device_station = atData.data["Device"]["Station"]
        bucket = atData.data["Database"]["Influxdb2"]["bucket"]

        self.write_event(
            measurement="Power",
            field="ON",
            value=0,
            location=location,
            device_ID= device_id,
            device_subID=device_sub_id,
            device_type=device_type,
            station=device_station,
        )
        self.write_event(
            measurement="Power",
            field="ON",
            value=1,
            location=location,
            device_ID= device_id,
            device_subID=device_sub_id,
            device_type=device_type,
            station=device_station,
        )
        while 1:
            self.store()
            self.list_measurements(bucket=bucket)
            self.error_list_measurements = False
            sleep(atData.data["Database"]["Store Time"]) # minutes
    
    def list_measurements(self, bucket = "atlab"):
        
        url =atData.data["Database"]["Influxdb2"]["url"]
        org = atData.data["Database"]["Influxdb2"]["org"]
        bucket = atData.data["Database"]["Influxdb2"]["bucket"]
        token = atData.data["Database"]["Influxdb2"]["token"]

        client = InfluxDBClient(
            url= url,
            token= token,
            org= org,
        )
        query_api = client.query_api()

        measurement_list = []
        query = 'import "influxdata/influxdb/schema"\n\nschema.measurements(bucket: "'+ bucket+'")'

        try:
            tables = query_api.query(
                org= org,
                query= query
            )
            for table in tables:
                # print(table)
                for record in table.records:
                    measurement_list.append(record["_value"])
            new_dict = {}
            for sensor in measurement_list:
                new_dict[sensor] = "Stored"

            atData.data["Database"]["List"] = new_dict
            # print( atData.data["Database"]["List"])
            self.error_list_measurements = False
            return measurement_list

        except Exception as error:
            print("error_list_measurements",self.error_list_measurements)
            error_infor =   "InfluxDB-list-measurement: " + \
                            str(datetime.now())+ \
                            str(error)
            if self.error_list_measurements == False :
                self.error_list_measurements = True
                # atData.data["Errors"]["Last"] = error_infor
                # atData.data['Errors']['List'].append(error_infor)
                # atData.save('Errors')
                atData.save_error(error_infor)
            print("[ERROR]",error_infor)
            print("error_list_measurements",self.error_list_measurements)
            return False

    def delete_measurement(self, bucket = "atlab", measurement = "Default"):
        command =  'influx delete' +\
                    ' --bucket ' + bucket +\
                    ' --start 1970-01-01T00:00:00Z '+\
                    ' --stop $(date +"%Y-%m-%dT%H:%M:%SZ")'+\
                    ' --predicate '+"'"+'_measurement="'+ measurement +'"' +"'"
        os.system(command)
        self.list_measurements(bucket = bucket)
        pass

atInfluxDB = atInfluxDB_Class()
    

if __name__ == "__main__":
    print(atInfluxDB.list_measurements())
    atInfluxDB.delete_measurement(measurement="Eee")
    pass

    
    # tables = atInfluxDB.read(
    #     # start_time= time_start_utc,
    #     # stop_time= time_stop_utc,
    #     start_time= "-1h",
    #     stop_time= "-30m",
    #     measurement= "Sensors",
    #     field_list= ["Temperature","Default"],
    #     # aggregateWindow={
    #     #     "Every Minute" : 5,
    #     #     "FN" : "first",
    #     #     "Create Empty" : 'true'
    #     # },
    #     # last= True
    # )

    # for table in tables:
    #     # # for record in table:
    #     for record in table.records:
    #         print(str(record["_time"]) + " - " + record["_field"] + ": " + str(record["_value"]) + ": " + str(record["Status"]) )

    
    