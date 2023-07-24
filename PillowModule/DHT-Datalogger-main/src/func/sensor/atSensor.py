import sys
from time import sleep
import threading
import random

sys.path.insert(0,"driver")
from atADC import at4_20mAs
from atModbus_RTU import atModbus_RTU
from atModbus_TCP import atModbus_TCP

sys.path.insert(0,"json")
from atJsonData import atData
import serial
from datetime import datetime
class atSensor_Class():
    
    def __init__(self) -> None:
        self.thread = threading.Thread(target= self._thread)
        pass

    def read(self):

        # atData.reload()
        for sensor in atData.data["Sensors"]["List"]:
            if(self.read_raw_values(sensor)):
                self.calib_sensor(sensor)
                self.limit_sensor(sensor)
                self.check_alarm(sensor)
                self.check_error(sensor)

        # atData.save_Setting()

    def read_raw_values(self, sensor):
        '''
        read all  raw value and save into data json
        '''
        
        readSuccess = True
        raw_value = {}
        try:    
            sensor_protocol = atData.data["Sensors"]["List"][sensor]["Source"]["Protocol"]

            if sensor_protocol == "4-20mA CH-1":
                raw_value = at4_20mAs.read_AI_1()
                atData.data["Sensors"]["List"][sensor]["Raw Value"] = raw_value

            elif sensor_protocol == "4-20mA CH-2":
                raw_value = at4_20mAs.read_AI_2()
                atData.data["Sensors"]["List"][sensor]["Raw Value"] = raw_value

            elif sensor_protocol == "4-20mA CH-3":
                raw_value = at4_20mAs.read_AI_3()
                atData.data["Sensors"]["List"][sensor]["Raw Value"] = raw_value

            elif sensor_protocol == "4-20mA CH-4":
                raw_value = at4_20mAs.read_AI_4()
                atData.data["Sensors"]["List"][sensor]["Raw Value"] = raw_value

            elif sensor_protocol == "4-20mA CH-5":
                raw_value = at4_20mAs.read_AI_5()
                atData.data["Sensors"]["List"][sensor]["Raw Value"] = raw_value

            elif sensor_protocol == "4-20mA CH-6":
                raw_value = at4_20mAs.read_AI_6()
                atData.data["Sensors"]["List"][sensor]["Raw Value"] = raw_value

            elif sensor_protocol == "4-20mA CH-7":
                raw_value = at4_20mAs.read_AI_7()
                atData.data["Sensors"]["List"][sensor]["Raw Value"] = raw_value

            elif sensor_protocol == "4-20mA CH-8":
                raw_value = at4_20mAs.read_AI_8()
                atData.data["Sensors"]["List"][sensor]["Raw Value"] = raw_value

            elif sensor_protocol == "Modbus RTU":
                parity=   atData.data["Sensors"]["List"][sensor]["Source"]["Modbus RTU config"]["Port"]["Config"]["RS485-1"]["Parity"]
                if parity == "none":
                    parity = serial.PARITY_NONE
                if parity == "even":
                    parity = serial.PARITY_EVEN
                if parity == "odd":
                    parity = serial.PARITY_ODD

                raw_value = atModbus_RTU.read(
                    baudrate= atData.data["Sensors"]["List"][sensor]["Source"]["Modbus RTU config"]["Port"]["Config"]["RS485-1"]["Baudrate"],
                    bytesize= atData.data["Sensors"]["List"][sensor]["Source"]["Modbus RTU config"]["Port"]["Config"]["RS485-1"]["Data bits"],
                    stopbits= atData.data["Sensors"]["List"][sensor]["Source"]["Modbus RTU config"]["Port"]["Config"]["RS485-1"]["Stop bits"],
                    parity=   parity,
                    address= atData.data["Sensors"]["List"][sensor]["Source"]["Modbus RTU config"]["ID"],
                    type= atData.data["Sensors"]["List"][sensor]["Source"]["Modbus RTU config"]["Type"],
                    register_address=  atData.data["Sensors"]["List"][sensor]["Source"]["Modbus RTU config"]["Address"],
                )
                if raw_value != False :
                    atData.data["Sensors"]["List"][sensor]["Raw Value"] = raw_value
                else:
                    readSuccess = False
                    atData.data["Sensors"]["List"][sensor]["Status"] = "Error"

            elif sensor_protocol == "Modbus TCP":
                # raw_value = 0
                try:
                    raw_value = atModbus_TCP.read(
                        IP= atData.data["Sensors"]["List"][sensor]["Source"]["Modbus TCP/IP config"]["IP"],
                        ID= atData.data["Sensors"]["List"][sensor]["Source"]["Modbus TCP/IP config"]["ID"],
                        type= atData.data["Sensors"]["List"][sensor]["Source"]["Modbus TCP/IP config"]["Type"],
                        address= atData.data["Sensors"]["List"][sensor]["Source"]["Modbus TCP/IP config"]["Address"],
                        datatype=atData.data["Sensors"]["List"][sensor]["Source"]["Datatype"]
                    )
                    atData.data["Sensors"]["List"][sensor]["Raw Value"] = raw_value
                except  Exception as error:
                    error_log = "[ERROR-4]"+ \
                        "Modbus TCP "+ \
                        atData.data["Sensors"]["List"][sensor]["Name"]+ \
                        " "+ \
                        str(datetime.now())+ \
                        " : "+ \
                        str(error)
                    atData.save_error(error_log)
                    print(error_log)
                    readSuccess = False
                    atData.data["Sensors"]["List"][sensor]["Status"] = "Error"
                
        except Exception as error:
            print("[ERROR] : Read raw data:",error)
            print('IP:',atData.data["Sensors"]["List"][sensor]["Source"]["Modbus TCP/IP config"]["IP"])
            print('ID:',atData.data["Sensors"]["List"][sensor]["Source"]["Modbus TCP/IP config"]["ID"])
            print('Type',atData.data["Sensors"]["List"][sensor]["Source"]["Modbus TCP/IP config"]["Type"])
            print('Address',atData.data["Sensors"]["List"][sensor]["Source"]["Modbus TCP/IP config"]["Address"])
            
            readSuccess = False
            atData.data["Sensors"]["List"][sensor]["Status"] = "Error"

        return readSuccess

    def calib_sensor(self,sensor):
        raw_value = atData.data["Sensors"]["List"][sensor]["Raw Value"]
        sensor_calib_function = atData.data["Sensors"]["List"][sensor]["Calib"]["Function"]
        sensor_calib_index_A = atData.data["Sensors"]["List"][sensor]["Calib"]["Index"]["A"]
        sensor_calib_index_B = atData.data["Sensors"]["List"][sensor]["Calib"]["Index"]["B"]
        sensor_calib_index_C = atData.data["Sensors"]["List"][sensor]["Calib"]["Index"]["C"]
        sensor_calib_index_D = atData.data["Sensors"]["List"][sensor]["Calib"]["Index"]["D"]
        # print(sensor_calib_function)
        if sensor_calib_function == "y = Ax + B":
            calib_value = sensor_calib_index_A*raw_value + sensor_calib_index_B
            atData.data["Sensors"]["List"][sensor]["Calib Value"] = calib_value

        if sensor_calib_function == "y = Ax^2 + Bx + C":
            calib_value = sensor_calib_index_A*raw_value**2 + sensor_calib_index_B*raw_value + sensor_calib_index_C
            atData.data["Sensors"]["List"][sensor]["Calib Value"] = calib_value

        if sensor_calib_function == "y = Ax^3 + Bx^2 + Cx + D":
            calib_value = sensor_calib_index_A*raw_value**3 + sensor_calib_index_B*raw_value**2 + sensor_calib_index_C*raw_value + sensor_calib_index_D
            atData.data["Sensors"]["List"][sensor]["Calib Value"] = calib_value
            
    def limit_sensor(self, sensor):
        # check limit:
        if atData.data["Sensors"]["List"][sensor]["Limit"]["Activation"] == "Enable":
            # read value
            limited_value = atData.data["Sensors"]["List"][sensor]["Calib Value"]
            # check upper limit
            if limited_value > atData.data["Sensors"]["List"][sensor]["Limit"]["Upper"]:

                limited_value = random.uniform(
                    atData.data["Sensors"]["List"][sensor]["Limit"]["Upper"] - 0.1,
                    atData.data["Sensors"]["List"][sensor]["Limit"]["Upper"] + 0.1
                )
                atData.data["Sensors"]["List"][sensor]["Calib Value"] = limited_value
            # check lower limit
            if limited_value < atData.data["Sensors"]["List"][sensor]["Limit"]["Lower"]:
                limited_value = random.uniform(
                    atData.data["Sensors"]["List"][sensor]["Limit"]["Lower"] - 0.1,
                    atData.data["Sensors"]["List"][sensor]["Limit"]["Lower"] + 0.1
                )
                atData.data["Sensors"]["List"][sensor]["Calib Value"] = limited_value

    def check_alarm(self,sensor):
        alarm_status = "Normal"
        # check raw value alarm
        raw_value = atData.data["Sensors"]["List"][sensor]["Raw Value"]
        alarm_raw_lower = atData.data["Sensors"]["List"][sensor]["Alarm"]["Raw"]["Lower"]
        alarm_raw_upper = atData.data["Sensors"]["List"][sensor]["Alarm"]["Raw"]["Upper"]
        if not alarm_raw_lower <= raw_value <= alarm_raw_upper:
            alarm_status = "Alarm"
            atData.data["Sensors"]["List"][sensor]["Alarm"]["Status"] = alarm_status
        # check calib value alarm
        calib_value = atData.data["Sensors"]["List"][sensor]["Calib Value"]
        alarm_calib_lower = atData.data["Sensors"]["List"][sensor]["Alarm"]["Calib"]["Lower"]
        alarm_calib_upper = atData.data["Sensors"]["List"][sensor]["Alarm"]["Calib"]["Upper"]
        if not alarm_calib_lower <= calib_value <= alarm_calib_upper:
            alarm_status = "Alarm"
            atData.data["Sensors"]["List"][sensor]["Alarm"]["Status"] = alarm_status
        # save data
    
    def check_error(self,sensor):
        error_status = "Normal"
        # check raw value alarm
        raw_value = atData.data["Sensors"]["List"][sensor]["Raw Value"]
        error_raw_lower = atData.data["Sensors"]["List"][sensor]["Error"]["Raw"]["Lower"]
        error_raw_upper = atData.data["Sensors"]["List"][sensor]["Error"]["Raw"]["Upper"]
        if not error_raw_lower <= raw_value <= error_raw_upper:
            error_status = "Error"
        # check calib value alarm
        calib_value = atData.data["Sensors"]["List"][sensor]["Calib Value"]
        error_calib_lower = atData.data["Sensors"]["List"][sensor]["Error"]["Calib"]["Lower"]
        error_calib_upper = atData.data["Sensors"]["List"][sensor]["Error"]["Calib"]["Upper"]
        if not error_calib_lower <= calib_value <= error_calib_upper:
            error_status = "Error"

        # # save tp error status
        atData.data["Sensors"]["List"][sensor]["Error"]["Status"] = error_status
        #
        #  save to sensor status
        sensor_status = atData.data["Sensors"]["List"][sensor]["Status"]

        if sensor_status == "Normal" and error_status == "Error" :
            atData.data["Sensors"]["List"][sensor]["Status"] = error_status
        if sensor_status == "Error" and error_status == "Normal":
            atData.data["Sensors"]["List"][sensor]["Status"] = error_status
    
    def _thread(self):
        while 1:
            sleep(2)
            try:
                self.read()
            except Exception as error:
                print(error)

atSensor = atSensor_Class()

if __name__ == "__main__":
    atSensor.thread.start()