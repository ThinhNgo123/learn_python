#  to maintain current screen
import threading
import sys
sys.path.insert(0, 'json')
from atJsonData import atData

from Current_Screen import Current_Screen

from atScreen_Booting import atScreen_Booting
from atScreen_Setting import atScreen_Setting
from atScreen_Monitoring import atScreen_Monitoring
from atScreen_Login import atScreen_Login

from atScreen_Sensors import atScreen_Sensors
from atScreen_Sensor_Detail import atScreen_Sensor_Detail
from atScreen_Sensor_Detail_Data import atScreen_Sensor_Detail_Data
from atScreen_Sensor_Detail_Data_Diagram import atScreen_Sensor_Detail_Data_Diagram
from atScreen_Sensor_Detail_Config import atScreen_Sensor_Detail_Config
from atScreen_Sensor_Detail_Config_Name import atScreen_Sensor_Detail_Config_Name
from atScreen_Sensor_Detail_Config_ID import atScreen_Sensor_Detail_Config_ID
from atScreen_Sensor_Detail_Config_Unit import atScreen_Sensor_Detail_Config_Unit
from atScreen_Sensor_Detail_Config_Sampling_Time import atScreen_Sensor_Detail_Config_Sampling_Time
from atScreen_Sensor_Detail_Config_Source import atScreen_Sensor_Detail_Config_Source
from atScreen_Sensor_Detail_Config_Source_MBTCP import atScreen_Sensor_Detail_Config_Source_MBTCP
from atScreen_Sensor_Detail_Config_Source_MBTCP_Select import atScreen_Sensor_Detail_Config_Source_MBTCP_Select
from atScreen_Sensor_Detail_Config_Source_MBTCP_Config import atScreen_Sensor_Detail_Config_Source_MBTCP_Config
from atScreen_Sensor_Detail_Config_Source_MBTCP_Config_IP import atScreen_Sensor_Detail_Config_Source_MBTCP_Config_IP
from atScreen_Sensor_Detail_Config_Source_MBTCP_Config_ID import atScreen_Sensor_Detail_Config_Source_MBTCP_Config_ID
from atScreen_Sensor_Detail_Config_Source_MBTCP_Config_Type import atScreen_Sensor_Detail_Config_Source_MBTCP_Config_Type
from atScreen_Sensor_Detail_Config_Source_MBTCP_Config_Address import atScreen_Sensor_Detail_Config_Source_MBTCP_Config_Address

from atScreen_Sensor_Detail_Config_Source_MBRTU import atScreen_Sensor_Detail_Config_Source_MBRTU
from atScreen_Sensor_Detail_Config_Source_MBRTU_Select import atScreen_Sensor_Detail_Config_Source_MBRTU_Select
from atScreen_Sensor_Detail_Config_Source_MBRTU_Config import atScreen_Sensor_Detail_Config_Source_MBRTU_Config
from atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port import atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port
from atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1 import atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1
from atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1_Select import atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1_Select
from atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1_Baudrate import atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1_Baudrate
from atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1_Data_bits import atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1_Data_bits
from atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1_Stop_bits import atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1_Stop_bits
from atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1_Parity import atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1_Parity

from atScreen_Sensor_Detail_Config_Source_MBRTU_Config_ID import atScreen_Sensor_Detail_Config_Source_MBRTU_Config_ID
from atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Type import atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Type
from atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Address import atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Address

from atScreen_Sensor_Detail_Config_Source_4_20mA import atScreen_Sensor_Detail_Config_Source_4_20mA
from atScreen_Sensor_Detail_Config_Source_Data_Type import atScreen_Sensor_Detail_Config_Source_Data_Type
from atScreen_Sensor_Detail_Config_Calib import atScreen_Sensor_Detail_Config_Calib
from atScreen_Sensor_Detail_Config_Calib_Function import atScreen_Sensor_Detail_Config_Calib_Function
from atScreen_Sensor_Detail_Config_Calib_Index import atScreen_Sensor_Detail_Config_Calib_Index
from atScreen_Sensor_Detail_Config_Calib_Index_A import atScreen_Sensor_Detail_Config_Calib_Index_A
from atScreen_Sensor_Detail_Config_Calib_Index_B import atScreen_Sensor_Detail_Config_Calib_Index_B
from atScreen_Sensor_Detail_Config_Calib_Index_C import atScreen_Sensor_Detail_Config_Calib_Index_C
from atScreen_Sensor_Detail_Config_Calib_Index_D import atScreen_Sensor_Detail_Config_Calib_Index_D

from atScreen_Sensor_Detail_Config_Alarm import atScreen_Sensor_Detail_Config_Alarm
from atScreen_Sensor_Detail_Config_Alarm_Raw_Lower import atScreen_Sensor_Detail_Config_Alarm_Raw_Lower
from atScreen_Sensor_Detail_Config_Alarm_Raw_Upper import atScreen_Sensor_Detail_Config_Alarm_Raw_Upper
from atScreen_Sensor_Detail_Config_Alarm_Calib_Lower import atScreen_Sensor_Detail_Config_Alarm_Calib_Lower
from atScreen_Sensor_Detail_Config_Alarm_Calib_Upper import atScreen_Sensor_Detail_Config_Alarm_Calib_Upper

from atScreen_Sensor_Detail_Config_Error import atScreen_Sensor_Detail_Config_Error
from atScreen_Sensor_Detail_Config_Error_Raw_Lower import   atScreen_Sensor_Detail_Config_Error_Raw_Lower
from atScreen_Sensor_Detail_Config_Error_Raw_Upper import   atScreen_Sensor_Detail_Config_Error_Raw_Upper
from atScreen_Sensor_Detail_Config_Error_Calib_Lower import atScreen_Sensor_Detail_Config_Error_Calib_Lower
from atScreen_Sensor_Detail_Config_Error_Calib_Upper import atScreen_Sensor_Detail_Config_Error_Calib_Upper

from atScreen_Sensor_Detail_Config_Limit import atScreen_Sensor_Detail_Config_Limit
from atScreen_Sensor_Detail_Config_Limit_Activation import atScreen_Sensor_Detail_Config_Limit_Activation
from atScreen_Sensor_Detail_Config_Limit_Upper import atScreen_Sensor_Detail_Config_Limit_Upper
from atScreen_Sensor_Detail_Config_Limit_Lower import atScreen_Sensor_Detail_Config_Limit_Lower

from atScreen_Sensor_Detail_Delete import atScreen_Sensor_Detail_Delete
from atScreen_Sensor_Detail_Clone import atScreen_Sensor_Detail_Clone

from atScreen_Relays import atScreen_Relays
from atScreen_Relay_Detail import atScreen_Relay_Detail
from atScreen_Relay_Detail_Data import atScreen_Relay_Detail_Data
from atScreen_Relay_Detail_Config import atScreen_Relay_Detail_Config
from atScreen_Relay_Detail_Config_Name import atScreen_Relay_Detail_Config_Name
from atScreen_Relay_Detail_Config_ID import atScreen_Relay_Detail_Config_ID
from atScreen_Relay_Detail_Config_Source import atScreen_Relay_Detail_Config_Source
from atScreen_Relay_Detail_Config_Source_Input import atScreen_Relay_Detail_Config_Source_Input
from atScreen_Relay_Detail_Config_Source_Input_Protocol import atScreen_Relay_Detail_Config_Source_Input_Protocol
from atScreen_Relay_Detail_Config_Source_Input_MQTT import atScreen_Relay_Detail_Config_Source_Input_MQTT
from atScreen_Relay_Detail_Config_Source_Input_MQTT_Host import atScreen_Relay_Detail_Config_Source_Input_MQTT_Host
from atScreen_Relay_Detail_Config_Source_Input_MQTT_Password import atScreen_Relay_Detail_Config_Source_Input_MQTT_Password
from atScreen_Relay_Detail_Config_Source_Input_MQTT_Port import atScreen_Relay_Detail_Config_Source_Input_MQTT_Port
from atScreen_Relay_Detail_Config_Source_Input_MQTT_Topic import atScreen_Relay_Detail_Config_Source_Input_MQTT_Topic
from atScreen_Relay_Detail_Config_Source_Input_MQTT_User import atScreen_Relay_Detail_Config_Source_Input_MQTT_User
from atScreen_Relay_Detail_Config_Source_Input_MQTT_Messages import atScreen_Relay_Detail_Config_Source_Input_MQTT_Messages
from atScreen_Relay_Detail_Config_Source_Input_MQTT_Messages_On import atScreen_Relay_Detail_Config_Source_Input_MQTT_Messages_On
from atScreen_Relay_Detail_Config_Source_Input_MQTT_Messages_Off import atScreen_Relay_Detail_Config_Source_Input_MQTT_Messages_Off
from atScreen_Relay_Detail_Config_Source_Input_Local import atScreen_Relay_Detail_Config_Source_Input_Local
from atScreen_Relay_Detail_Config_Source_Input_Local_Mode import atScreen_Relay_Detail_Config_Source_Input_Local_Mode
from atScreen_Relay_Detail_Config_Source_Input_Local_Manual import atScreen_Relay_Detail_Config_Source_Input_Local_Manual
from atScreen_Relay_Detail_Config_Source_Input_Local_Timers import atScreen_Relay_Detail_Config_Source_Input_Local_Timers
# -------------------------------------------------------
from atScreen_Relay_Detail_Config_Source_Output import atScreen_Relay_Detail_Config_Source_Output
from atScreen_Relay_Detail_Delete import atScreen_Relay_Detail_Delete
from atScreen_Relay_Detail_Clone import atScreen_Relay_Detail_Clone
from atScreen_FTP_Servers import atScreen_FTP_Servers
from atScreen_FTP_1_Server import atScreen_FTP_1_Server
from atScreen_FTP_1_Server_Status import atScreen_FTP_1_Server_Status
from atScreen_FTP_1_Server_IP import atScreen_FTP_1_Server_IP
from atScreen_FTP_1_Server_Activate import atScreen_FTP_1_Server_Activate
from atScreen_FTP_1_Server_Port import atScreen_FTP_1_Server_Port
from atScreen_FTP_1_Server_User import atScreen_FTP_1_Server_User
from atScreen_FTP_1_Server_Password import atScreen_FTP_1_Server_Password
from atScreen_FTP_1_Server_Folder import atScreen_FTP_1_Server_Folder
from atScreen_FTP_1_Server_File_Name import atScreen_FTP_1_Server_File_Name
from atScreen_FTP_1_Server_Send_Time import atScreen_FTP_1_Server_Send_Time
from atScreen_FTP_1_Server_Check_Time import atScreen_FTP_1_Server_Check_Time
from atScreen_FTP_1_Server_Time_Out import atScreen_FTP_1_Server_Time_Out

from atScreen_Database import atScreen_Database
from atScreen_Database_List import atScreen_Database_List
from atScreen_Database_Delete import atScreen_Database_Delete
from atScreen_Database_Store_Time import atScreen_Database_Store_Time

from atScreen_Device import atScreen_Device
from atScreen_Device_ID import atScreen_Device_ID
from atScreen_Device_subID import atScreen_Device_subID
from atScreen_Device_Location import atScreen_Device_Location
from atScreen_Device_Location_X import atScreen_Device_Location_X
from atScreen_Device_Location_Y import atScreen_Device_Location_Y
from atScreen_Device_Time_Zone import atScreen_Device_Time_Zone
from atScreen_Device_Type import atScreen_Device_Type
from atScreen_Device_Station import atScreen_Device_Station

from atScreen_Memory import atScreen_Memory
from atScreen_Memory_Disk import atScreen_Memory_Disk
from atScreen_Memory_USB import atScreen_Memory_USB

from atScreen_Errors import atScreen_Errors
from atScreen_Errors_Last import atScreen_Errors_Last
from atScreen_Errors_List import atScreen_Errors_List

from atScreen_Internet import atScreen_Internet
from atScreen_Internet_Wifi import atScreen_Internet_Wifi
from atScreen_Internet_OpenVPN import atScreen_Internet_OpenVPN
from atScreen_Internet_Ethernet import atScreen_Internet_Ethernet

from atScreen_Web_Server import atScreen_Web_Server
from atScreen_Web_Server_Status import atScreen_Web_Server_Status
from atScreen_Web_Server_Activate import atScreen_Web_Server_Activate
from atScreen_Web_Server_Auto_Config import atScreen_Web_Server_Auto_Config

from atScreen_Power import atScreen_Power
from atScreen_Power_Reset import atScreen_Power_Reset
from atScreen_Power_Shut_Down import atScreen_Power_Shut_Down

from atScreen_Advances import atScreen_Advances
from atScreen_Advances_Device_Analytic import atScreen_Advances_Device_Analytic
from atScreen_Advances_Default_Restore import atScreen_Advances_Default_Restore
from atScreen_Advances_Backup_USB import atScreen_Advances_Backup_USB
from atScreen_Advances_Backup_USB_Setting import atScreen_Advances_Backup_USB_Setting
from atScreen_Advances_Backup_USB_Database import atScreen_Advances_Backup_USB_Database
from atScreen_Advances_Backup_USB_Boot_Image import atScreen_Advances_Backup_USB_Boot_Image
from atScreen_Advances_Restore_USB import atScreen_Advances_Restore_USB
from atScreen_Advances_Restore_USB_Setting import atScreen_Advances_Restore_USB_Setting
from atScreen_Advances_Restore_USB_Database import atScreen_Advances_Restore_USB_Database

from atScreen_User import atScreen_User
from atScreen_User_Information import atScreen_User_Information
from atScreen_User_Change_Password import atScreen_User_Change_Password
from atScreen_About import atScreen_About


class atScreens_Manager():
    def __init__(self) -> None:
        Current_Screen.set_name(atScreen_Booting.name)
        self.thread = threading.Thread(target= self._thread)
        pass

    def load(self):
        atScreen_Booting.load()
        atScreen_Monitoring.load()
        atScreen_Setting.load()
        atScreen_Login.load()

        atScreen_Sensors.load()
        atScreen_Sensor_Detail.load()
        atScreen_Sensor_Detail_Data.load()
        atScreen_Sensor_Detail_Data_Diagram.load()
        atScreen_Sensor_Detail_Config.load()
        atScreen_Sensor_Detail_Config_Name.load()
        atScreen_Sensor_Detail_Config_ID.load()
        atScreen_Sensor_Detail_Config_Unit.load()
        atScreen_Sensor_Detail_Config_Sampling_Time.load()
        
        atScreen_Sensor_Detail_Config_Source.load()
        atScreen_Sensor_Detail_Config_Source_MBTCP.load()
        atScreen_Sensor_Detail_Config_Source_MBTCP_Select.load()
        atScreen_Sensor_Detail_Config_Source_MBTCP_Config.load()
        atScreen_Sensor_Detail_Config_Source_MBTCP_Config_IP.load()
        atScreen_Sensor_Detail_Config_Source_MBTCP_Config_ID.load()
        atScreen_Sensor_Detail_Config_Source_MBTCP_Config_Type.load()
        atScreen_Sensor_Detail_Config_Source_MBTCP_Config_Address.load()

        atScreen_Sensor_Detail_Config_Source_MBRTU.load()
        atScreen_Sensor_Detail_Config_Source_MBRTU_Select.load() 
        atScreen_Sensor_Detail_Config_Source_MBRTU_Config.load() 
        atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port.load() 
        atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1.load() 
        atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1_Select.load() 
        atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1_Baudrate.load() 
        atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1_Data_bits.load() 
        atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1_Stop_bits.load() 
        atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Port_RS485_1_Parity.load() 

        atScreen_Sensor_Detail_Config_Source_MBRTU_Config_ID.load() 
        atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Type.load() 
        atScreen_Sensor_Detail_Config_Source_MBRTU_Config_Address.load() 

        atScreen_Sensor_Detail_Config_Source_4_20mA.load()
        atScreen_Sensor_Detail_Config_Source_Data_Type.load()

        atScreen_Sensor_Detail_Config_Calib.load()
        atScreen_Sensor_Detail_Config_Calib_Function.load()
        atScreen_Sensor_Detail_Config_Calib_Index.load()
        atScreen_Sensor_Detail_Config_Calib_Index_A.load()
        atScreen_Sensor_Detail_Config_Calib_Index_B.load()
        atScreen_Sensor_Detail_Config_Calib_Index_C.load()
        atScreen_Sensor_Detail_Config_Calib_Index_D.load()

        atScreen_Sensor_Detail_Config_Alarm.load()
        atScreen_Sensor_Detail_Config_Alarm_Raw_Lower.load()
        atScreen_Sensor_Detail_Config_Alarm_Raw_Upper.load()
        atScreen_Sensor_Detail_Config_Alarm_Calib_Lower.load()
        atScreen_Sensor_Detail_Config_Alarm_Calib_Upper.load()

        atScreen_Sensor_Detail_Config_Error.load()
        atScreen_Sensor_Detail_Config_Error_Raw_Lower.load()
        atScreen_Sensor_Detail_Config_Error_Raw_Upper.load()
        atScreen_Sensor_Detail_Config_Error_Calib_Lower.load()
        atScreen_Sensor_Detail_Config_Error_Calib_Upper.load()

        atScreen_Sensor_Detail_Config_Limit.load()
        atScreen_Sensor_Detail_Config_Limit_Activation.load()
        atScreen_Sensor_Detail_Config_Limit_Upper.load()
        atScreen_Sensor_Detail_Config_Limit_Lower.load()

        atScreen_Sensor_Detail_Delete.load()
        atScreen_Sensor_Detail_Clone.load()

        atScreen_Relays.load()
        atScreen_Relay_Detail.load()
        atScreen_Relay_Detail_Data.load()
        atScreen_Relay_Detail_Config.load()
        atScreen_Relay_Detail_Config_Name.load()
        atScreen_Relay_Detail_Config_ID.load()
        atScreen_Relay_Detail_Config_Source.load()
        atScreen_Relay_Detail_Config_Source_Input.load()
        atScreen_Relay_Detail_Config_Source_Input_Protocol.load()
        atScreen_Relay_Detail_Config_Source_Input_MQTT.load()
        atScreen_Relay_Detail_Config_Source_Input_MQTT_Host.load()
        atScreen_Relay_Detail_Config_Source_Input_MQTT_Topic.load()
        atScreen_Relay_Detail_Config_Source_Input_MQTT_User.load()
        atScreen_Relay_Detail_Config_Source_Input_MQTT_Password.load()
        atScreen_Relay_Detail_Config_Source_Input_MQTT_Port.load()
        atScreen_Relay_Detail_Config_Source_Input_MQTT_Messages.load()
        atScreen_Relay_Detail_Config_Source_Input_MQTT_Messages_On.load()
        atScreen_Relay_Detail_Config_Source_Input_MQTT_Messages_Off.load()
        atScreen_Relay_Detail_Config_Source_Input_Local.load()
        atScreen_Relay_Detail_Config_Source_Input_Local_Mode.load()
        atScreen_Relay_Detail_Config_Source_Input_Local_Manual.load()
        atScreen_Relay_Detail_Config_Source_Input_Local_Timers.load()
        # -------------------------------------------------------------------------------------
        atScreen_Relay_Detail_Config_Source_Output.load()
        atScreen_Relay_Detail_Delete.load()
        atScreen_Relay_Detail_Clone.load()

        atScreen_FTP_Servers.load()        
        atScreen_FTP_1_Server.load()      
        atScreen_FTP_1_Server_Status.load()      
        atScreen_FTP_1_Server_IP.load()      
        atScreen_FTP_1_Server_Activate.load()      
        atScreen_FTP_1_Server_Port.load()      
        atScreen_FTP_1_Server_User.load()      
        atScreen_FTP_1_Server_Password.load()      
        atScreen_FTP_1_Server_Folder.load()      
        atScreen_FTP_1_Server_File_Name.load()      
        atScreen_FTP_1_Server_Send_Time.load()       
        atScreen_FTP_1_Server_Check_Time.load()
        atScreen_FTP_1_Server_Time_Out.load()

        atScreen_Database.load()
        atScreen_Database_List.load()
        atScreen_Database_Delete.load()
        atScreen_Database_Store_Time.load()

        atScreen_Device.load()
        atScreen_Device_ID.load()
        atScreen_Device_subID.load()
        atScreen_Device_Location.load()
        atScreen_Device_Location_X.load()
        atScreen_Device_Location_Y.load()
        atScreen_Device_Time_Zone.load()
        atScreen_Device_Type.load()
        atScreen_Device_Station.load()

        atScreen_Memory.load()  
        atScreen_Memory_Disk.load()  
        atScreen_Memory_USB.load()  

        atScreen_Errors.load()
        atScreen_Errors_Last.load()
        atScreen_Errors_List.load()

        atScreen_Internet.load()
        atScreen_Internet_Ethernet.load()
        atScreen_Internet_Wifi.load()
        atScreen_Internet_OpenVPN.load()

        atScreen_Web_Server.load()
        atScreen_Web_Server_Status.load()
        atScreen_Web_Server_Activate.load()
        atScreen_Web_Server_Auto_Config.load()

        atScreen_Power.load()
        atScreen_Power_Reset.load()
        atScreen_Power_Shut_Down.load()

        atScreen_Advances.load()
        atScreen_Advances_Device_Analytic.load()
        atScreen_Advances_Default_Restore.load()
        atScreen_Advances_Backup_USB.load()
        atScreen_Advances_Backup_USB_Setting.load()
        atScreen_Advances_Backup_USB_Database.load()
        atScreen_Advances_Backup_USB_Boot_Image.load()
        atScreen_Advances_Restore_USB.load()
        atScreen_Advances_Restore_USB_Setting.load()
        atScreen_Advances_Restore_USB_Database.load()

        atScreen_User.load()
        atScreen_User_Information.load()
        atScreen_User_Change_Password.load()
        
        atScreen_About.load()

        pass
    
    def _thread(self):
        while 1:
            self.load()

atScreens = atScreens_Manager()

if __name__ == "__main__":
    
    atScreens.thread.start()