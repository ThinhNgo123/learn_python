import sys
from time import sleep

sys.path.insert(0, 'atFrame')
from atFrame_Boot import atFrame_Boot
from atFrame_Menu import atFrame_Menu
from atFrame_Edit import atFrame_Edit
from atFrame_Information import atFrame_Information

class atHMI():
    atFrame_Booting = atFrame_Boot(
        name="Booting"
    )
    atFrame_Booting.set_version_info("V2.2.1")
    atFrame_Booting.set_loading_info("Loading complete")
    atFrame_Booting.set_loading_percent(100)
    sleep(2)
    # Setting
    atFrame_Setting = atFrame_Menu(
        name="Setting",
        list= [
            "Sensors",
            "FTP Servers",
            "Memory",
            "Errors",
            "Internet",
            "Web Server",
            "Power",
            "Advances",
            "About"
        ]
    )

    # Sensors 
    atFrame_Sensors = atFrame_Menu(
        name= "Sensors",
        list=[
            "[1]: Temperature",
            "[2]: Pressure 1",
            "[3]: Pressure 2",
            "[4]: Pressure 3",
        ]
    )
    # Memory
    atFrame_Memory = atFrame_Menu(
        name= "Memory",
        list= [
            "Disk Space",
            "USB Space"
        ]
    )
    # FTP Servers
    atFrame_FTP_Servers = atFrame_Menu(
        name= "FTP Servers",
        list= [
            "FTP-1 Server",
            # "FTP server 2(*)",
            # "FTP server 3(*)",
            # "FTP server 4(*)"
        ]
    )
    # Errors
    atFrame_Errors = atFrame_Menu(
        name= "Errors",
        list= [
            "Last Error",
            "Error List"
        ]
    )
    # Internet
    atFrame_Internet = atFrame_Menu(
        name= "Internet",
        list= [
            "Ethernet",
            "Wifi",
            "4G LTE"
        ]
    )
    # Web Server
    atFrame_Web_Server = atFrame_Menu(
        name= "Web Server",
        list= [
            "WS Status",
            "WS Enable",
            "WS Auto Config"
        ]
    )
    # Power
    atFrame_Power = atFrame_Menu(
        name= "Power",
        list=[
            "Reset",
            "Shut Down"
        ]
    )
    # Advances
    atFrame_Advances = atFrame_Menu(
        name= "Advances",
        list=[
            "Device Analytic",
            "Default Restore",
            "Backup USB",
            "Restore USB"
        ]
    )
    # About
    atFrame_About = atFrame_Information(
        name="About",
        image_url="image/ATLab_QR_240x240.jpg"
    )

    # in Sensors
    atFrame_Sensor_Detail = atFrame_Menu(
        name="Sensor Detail",
        list=[
            "Sensor Data",
            "Sensor Config",
            "Delete Sensor",
            "Clone Sensor"
        ]
    )
    atFrame_Sensor_Data = atFrame_Menu(
        name= "Sensor Data",
        list= [
            "Temperature",
            "4-20mA CH-1",
            "raw: 2467",
            "calib: 26.42 oC",
            "Sensor Diagram"
        ]
    )
    atFrame_Sensor_Config = atFrame_Menu(
        name="Sensor Config",
        list=[
            "SC Name",
            "SC Unit",
            "SC Source",
            "SC Calib",
            "SC Alarm",
            "SC Error",
        ]
    )
    atFrame_Delete_Sensor = atFrame_Menu(
        name = "Delete Sensor",
        list= [
            "No",
            "Yes"
        ]
    )
    atFrame_Clone_Sensor = atFrame_Menu(
        name = "Clone Sensor",
        list= [
            "No",
            "Yes"
        ]
    )
    
    # in Sensor Data
    atFrame_Sensor_Diagram = atFrame_Information(
        name= "Sensor Diagram",
        detail="Draw a diagram "
    )
    
    #  in Sensor Config
    atFrame_Sensor_Config_Name = atFrame_Edit(
        name= "SC Name",
        detail= "Temperature",
        edit_mode="String"
    )
    atFrame_Sensor_Config_Unit = atFrame_Edit(
        name= "SC Unit",
        detail="1",
        edit_mode="Number"
    )
    atFrame_Sensor_Config_Source = atFrame_Menu(
        name= "SC Source",
        list= [
            "SCS Modbus TCP",
            "SCS Modbus RTU",
            "SCS 4-20mA",
            "SCS Data Type",
        ]
    )
    atFrame_Sensor_Config_Calib = atFrame_Menu(
        name= "SC Calib",
        list= [
            "SCC Function",
            "SCC Index",
        ]
    )
    atFrame_Sensor_Config_Alarm = atFrame_Menu(
        name= "SC Alarm",
        list= [
            "SCA Raw Lower",
            "SCA Raw Upper",
            "SCA Calib Lower",
            "SCA Calib Upper"
        ]
    )
    atFrame_Sensor_Config_Error = atFrame_Menu(
        name= "SC Error",
        list= [
            "SCE Raw Lower",
            "SCE Raw Upper",
            "SCE Calib Lower",
            "SCE Calib Upper"
        ]
    )

    # in sensor config source
    atFrame_Sensor_Config_Source_MBTCPIP = atFrame_Menu(
        name="SCS Modbus TCP",
        list=[
            "SCSMBT Select",
            "SCSMBT Config",

        ]
    )
    atFrame_Sensor_Config_Source_MBRTU = atFrame_Menu(
        name="SCS Modbus RTU",
        list=[
            "SCSMBR Select",
            "SCSMBR Config",
        ]
    )
    atFrame_Sensor_Config_Source_4_20mA = atFrame_Menu(
        name="SCS 4-20mA",
        list=[
            "4-20mA CH-1",
            "4-20mA CH-2",
            "4-20mA CH-3",
            "4-20mA CH-4",
        ]
    )
    atFrame_Sensor_Config_Source_Data_Type = atFrame_Menu(
        name="SCS Data Type",
        list=[
            "bool",
            "int16",
            "uint16",
            "int32",
            "uint32",
            "float32",
            "float64",
        ]
    )

    # for sensor config Calib function
    atFrame_Sensor_Config_Calib_Function =atFrame_Menu(
        name= "SCC Function",
        list=[
            "y = Ax + B",
            "y = Ax^2 + Bx +C",
            "y = Ax^3 + Bx^2 + Cx +D",
            "Custom"
        ]
    )
    atFrame_Sensor_Config_Calib_Index =atFrame_Menu(
        name= "SCC Index",
        list=[
            "SCC Index A",
            "SCC Index B",
            "SCC Index C",
            "SCC Index D",
        ]
    )

    #  for sensor config source modbus TCP/IP
    atFrame_Sensor_Config_Source_MBTCPIP_Select = atFrame_Menu(
        name= "SCSMBT Select",
        list= [
            "No",
            "Yes"
        ]
    )
    atFrame_Sensor_Config_Source_MBTCPIP_Config = atFrame_Menu(
        name="SCSMBT Config",
        list= [
            "SCSMBTC IP",
            "SCSMBTC ID",
            "SCSMBTC Type",
            "SCSMBTC Address",
        ]
    )

    #  for sensor config source modbus RTU
    atFrame_Sensor_Config_Source_MBRTU_Select = atFrame_Menu(
        name= "SCSMBR Select",
        list= [
            "No",
            "Yes"
        ]
    )
    atFrame_Sensor_Config_Source_MBRTU_Config = atFrame_Menu(
        name="SCSMBR Config",
        list= [
            "SCSMBRC Port",
            "SCSMBRC ID",
            "SCSMBRC Type",
            "SCSMBRC Address",
        ]
    )

    # for sensor config calib index
    atFrame_Sensor_Config_Calib_Index_A = atFrame_Edit(
        name= "SCC Index A",
        detail="1.0",
        edit_mode="Number"
    ) 
    atFrame_Sensor_Config_Calib_Index_B = atFrame_Edit(
        name= "SCC Index B",
        detail="1.0",
        edit_mode="Number"
    ) 
    atFrame_Sensor_Config_Calib_Index_C = atFrame_Edit(
        name= "SCC Index C",
        detail="1.0",
        edit_mode="Number"
    ) 
    atFrame_Sensor_Config_Calib_Index_D = atFrame_Edit(
        name= "SCC Index D",
        detail="1.0",
        edit_mode="Number"
    ) 

    #  for sensor config source modbus TCP/IP config
    atFrame_Sensor_Config_Source_MBTCPIP_Config_IP = atFrame_Edit(
        name="SCSMBTC IP",
        detail="192.168.1.10",
        edit_mode="Number"
    )
    atFrame_Sensor_Config_Source_MBTCPIP_Config_ID = atFrame_Edit(
        name="SCSMBTC ID",
        detail="1",
        edit_mode="Number"
    )
    atFrame_Sensor_Config_Source_MBTCPIP_Config_Type = atFrame_Menu(
        name="SCSMBTC Type",
        list=[
            "discrete input",
            "input register",
            "coil",
            "holding register"
        ]
    )
    atFrame_Sensor_Config_Source_MBTCPIP_Config_Address = atFrame_Edit(
        name="SCSMBTC Address",
        detail="100",
        edit_mode="Number"
    )

    # for sensor config source modbus RTU config
    atFrame_Sensor_Config_Source_MBRTU_Config_Port = atFrame_Menu(
        name= "SCSMBRC Port",
        list= [
            "RS485-1"
        ]
    )
    atFrame_Sensor_Config_Source_MBRTU_Config_ID = atFrame_Edit(
        name= "SCSMBRC ID",
        detail="1"
    )
    atFrame_Sensor_Config_Source_MBRTU_Config_Type = atFrame_Menu(
        name="SCSMBRC Type",
        list=[
            "discrete input",
            "input register",
            "coil",
            "holding register"
        ]
    )
    atFrame_Sensor_Config_Source_MBRTU_Config_Address = atFrame_Edit(
        name="SCSMBRC Address",
        detail="111",
        edit_mode="Number"
    )

    # for sensor config source modbus RTU config
    atFrame_RS485_1 =atFrame_Menu(
        name= "RS485-1",
        list=[
            "RS485-1 Select",
            "RS485-1 Baudrate",
            "RS485-1 Data bits",
            "RS485-1 Stop bits",
            "RS485-1 Parity",
        ]
    )
    atFrame_RS485_1_Select = atFrame_Menu(
        name="RS485-1 Select",
        list=[
            "No",
            "Yes"
        ]
    )
    atFrame_RS485_1_Baudrate = atFrame_Menu(
        name= "RS485-1 Baudrate",
        list=[
            "1200",
            "2400",
            "4800",
            "9600",
            "14400",
            "19200",
            "28800",
            "38400",
            "57600",
            "115200",
            "230400",
        ]
    )
    atFrame_RS485_1_Data_Bits = atFrame_Menu(
        name= "RS485-1 Data bits",
        list= [
            "5",
            "6",
            "7",
            "8",
        ]
    )
    atFrame_RS485_1_Stop_Bits = atFrame_Menu(
        name= "RS485-1 Stop bits",
        list= [
            "1",
            "2",
        ]
    )
    atFrame_RS485_1_Parity = atFrame_Menu(
        name= "RS485-1 Parity",
        list= [
            "None",
            "Even",
            "Odd",
            "Mask",
            "Space",
        ]
    )
    
# ------------------------------------------------- Coding
    # Protocol submenu
    
    #  for Memory
    atFrame_Disk_Space = atFrame_Information(
        name="Disk Space",
        detail="8GB / 64GB"
    )
    atFrame_USB_Space = atFrame_Information(
        name= "USB Space",
        detail= "0.2GB /128GB"
    )

    # for FTP Servers
    atFrame_FTP_1_Server = atFrame_Menu(
        name= "FTP-1 Server",
        list=[
            "FTP-1 Status",
            "FTP-1 IP",
            "FTP-1 Port",
            "FTP-1 User",
            "FTP-1 Password",
            "FTP-1 Folder",
        ]
    )
    atFrame_FTP_1_Status = atFrame_Information(
        name= "FTP-1 Status",
        detail="Connecting"
    )
    atFrame_FTP_1_IP = atFrame_Edit(
        name= "FTP-1 IP",
        detail="192.168.1.100",
        edit_mode="Number"
    )
    atFrame_FTP_1_Port = atFrame_Edit(
        name= "FTP-1 Port",
        detail="21",
        edit_mode="Number"
    )
    atFrame_FTP_1_User = atFrame_Edit(
        name= "FTP-1 User",
        detail="admin"
    )
    atFrame_FTP_1_Password = atFrame_Edit(
        name= "FTP-1 Password",
        detail="admin"
    )
    atFrame_FTP_1_Folder = atFrame_Edit(
        name= "FTP-1 Folder",
        detail="/Data/Station-1"
    )
    
    #  for Errors
    atFrame_Last_Error = atFrame_Information(
        name="Last Error",
        detail="16:15:30 \n21-13-2022\nLSC1\nLost sensor connect"
    )
    atFrame_Error_List = atFrame_Menu(
        name="Error List",
        list= [
            "16:15:30 LSC1\n",
            "16:15:30 LSC2\n",
            "16:15:30 LSC3\n",
            "16:15:30 LSC4\n",
            "16:15:30 LSC5\n",
            "16:15:30 LSC6\n",
            "16:15:30 LSC7\n",
            "16:15:30 LSC8\n",
            "16:15:30 LSC9\n",
            "16:15:30 LSC10\n",
            "16:15:30 LSC11\n",
            "16:15:30 LSC12\n",
            "16:15:30 LSC3\n"
        ]
    )

    # in Internet
    atFrame_Ethernet = atFrame_Information(
        name= "Ethernet",
        detail= "1000/1000 (Mbps)\n" +\
                "192.168.1.23\n" +\
                "255.255.255.255\n" +\
                "40-A8-F0-55-C6-B4"
    )
    atFrame_Wifi = atFrame_Information(
        name= "Wifi",
        detail= "1000/1000 (Mbps)\n" +\
                "192.168.1.23\n" +\
                "255.255.255.255\n" +\
                "40-A8-F0-55-C6-B4"
    )
    atFrame_4G_LTE = atFrame_Information(
        name= "4G LTE",
        detail= "1000/1000 (Mbps)\n" +\
                "192.168.1.23\n" +\
                "255.255.255.255\n" +\
                "40-A8-F0-55-C6-B4"
    )

    #  in wed server
    atFrame_Web_Server_Status = atFrame_Information(
        name= "WS Status",
        detail= "Active"
    )
    atFrame_Web_Server_Enable = atFrame_Menu(
        name= "WS Enable",
        list= [
            "Enable",
            "Disable"
        ]
    )
    atFrame_Web_Server_Auto_Config = atFrame_Menu(
        name= "WS Auto Config",
        list= [
            "Enable",
            "Disable"
        ]
    )
    
    #  in Power
    atFrame_Reset = atFrame_Menu(
        name= "Reset",
        list=[
            "No",
            "Yes"
        ]
    )
    atFrame_Shut_Down = atFrame_Menu(
        name= "Shut Down",
        list=[
            "No",
            "Yes"
        ]
    )
    
    # in Advances
    atFrame_Device_Analytic = atFrame_Information(
        name="Device Analytic",
        detail=" in develop"
    )
    atFrame_Default_Restore = atFrame_Menu(
        name="Default Restore",
        list=[
            "No",
            "Yes"
        ]
    )
    atFrame_Backup_USB = atFrame_Menu(
        name="Backup USB",
        list=[
            "No",
            "Yes"
        ]
    )
    atFrame_Restore_USB = atFrame_Menu(
        name="Restore USB",
        list=[
            "No",
            "Yes"
        ]
    )
    
    #-------------------------------------------------------------
    # for save current frame information 
    frame = atFrame_Setting.name

    def __init__(self) -> None:
        #---------------------------------------------- Init callback function
        
        # Setting call back OK button
        self.atFrame_Setting.set_OK_callback( 
            lambda: self.set_frame(self.atFrame_Setting.get_chosen_submenu()) 
        )
        # Back to Setting
        self.atFrame_Sensors.set_Back_callback( 
            lambda: self.set_frame(self.atFrame_Setting.name) 
        )

        self.atFrame_Memory.set_Back_callback( 
            lambda: self.set_frame(self.atFrame_Setting.name) 
        )
        self.atFrame_FTP_Servers.set_Back_callback( 
            lambda: self.set_frame(self.atFrame_Setting.name) 
        )
        self.atFrame_Errors.set_Back_callback( 
            lambda: self.set_frame(self.atFrame_Setting.name) 
        )
        self.atFrame_Internet.set_Back_callback( 
            lambda: self.set_frame(self.atFrame_Setting.name) 
        )
        self.atFrame_Web_Server.set_Back_callback( 
            lambda: self.set_frame(self.atFrame_Setting.name) 
        )
        self.atFrame_Power.set_Back_callback( 
            lambda: self.set_frame(self.atFrame_Setting.name) 
        )
        self.atFrame_Advances.set_Back_callback( 
            lambda: self.set_frame(self.atFrame_Setting.name) 
        )
        self.atFrame_About.set_Back_callback( 
            lambda: self.set_frame(self.atFrame_Setting.name) 
        )
        
        # for Sensor
        self.atFrame_Sensors.set_OK_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Detail.name)
        )
        # back to Sensors
        self.atFrame_Sensor_Detail.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensors.name)
        )

        #  for Sensors Detail
        self.atFrame_Sensor_Detail.set_OK_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Detail.get_chosen_submenu())
        )
        # Back to sensor detail
        self.atFrame_Sensor_Data.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Detail.name)
        )
        # Back to sensor detail
        self.atFrame_Sensor_Config.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Detail.name)
        )
        # Back to sensor detail
        self.atFrame_Delete_Sensor.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Detail.name)
        )
        # Back to sensor detail
        self.atFrame_Clone_Sensor.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Detail.name)
        )


        # for Sensor Data
        self.atFrame_Sensor_Data.set_OK_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Diagram.name)
        )
        # back to sensor data
        self.atFrame_Sensor_Diagram.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Data.name)
        )


        # for Sensor Config
        self.atFrame_Sensor_Config.set_OK_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config.get_chosen_submenu())
        )
        # back to Sensor Config
        self.atFrame_Sensor_Config_Name.set_F4_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config.name)
        )
        self.atFrame_Sensor_Config_Unit.set_F4_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config.name)
        )
        self.atFrame_Sensor_Config_Source.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config.name)
        )
        self.atFrame_Sensor_Config_Calib.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config.name)
        )
        self.atFrame_Sensor_Config_Alarm.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config.name)
        )
        self.atFrame_Sensor_Config_Error.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config.name)
        )

        # for sensor config source
        self.atFrame_Sensor_Config_Source.set_OK_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Source.get_chosen_submenu())
        )
        # back to sensor config source
        self.atFrame_Sensor_Config_Source_MBTCPIP.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Source.name)
        )
        self.atFrame_Sensor_Config_Source_MBRTU.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Source.name)
        )
        self.atFrame_Sensor_Config_Source_4_20mA.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Source.name)
        )
        self.atFrame_Sensor_Config_Source_Data_Type.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Source.name)
        )

        # for sensor config source
        self.atFrame_Sensor_Config_Calib.set_OK_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Calib.get_chosen_submenu())
        )
        # back to sensor config source
        self.atFrame_Sensor_Config_Calib_Function.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Calib.name)
        )
        self.atFrame_Sensor_Config_Calib_Index.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Calib.name)
        )
        
        # for sensor source config modbus TCP/IP
        self.atFrame_Sensor_Config_Source_MBTCPIP.set_OK_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Source_MBTCPIP.get_chosen_submenu())
        )
        # back to sensor source config modbus TCP/IP
        self.atFrame_Sensor_Config_Source_MBTCPIP_Select.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Source_MBTCPIP.name)
        )
        self.atFrame_Sensor_Config_Source_MBTCPIP_Config.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Source_MBTCPIP.name)
        )

        # for sensor source config modbus RTU
        self.atFrame_Sensor_Config_Source_MBRTU.set_OK_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Source_MBRTU.get_chosen_submenu())
        )
        # back to sensor source config modbus RTU
        self.atFrame_Sensor_Config_Source_MBRTU_Select.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Source_MBRTU.name)
        )
        self.atFrame_Sensor_Config_Source_MBRTU_Config.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Source_MBRTU.name)
        )

        # for sensor config calib index 
        self.atFrame_Sensor_Config_Calib_Index.set_OK_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Calib_Index.get_chosen_submenu())
        )
        # back to sensor config calib index
        self.atFrame_Sensor_Config_Calib_Index_A.set_F4_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Calib_Index.name)
        )
        self.atFrame_Sensor_Config_Calib_Index_B.set_F4_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Calib_Index.name)
        )
        self.atFrame_Sensor_Config_Calib_Index_C.set_F4_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Calib_Index.name)
        )
        self.atFrame_Sensor_Config_Calib_Index_D.set_F4_callback(
            lambda: self.set_frame(self.atFrame_Sensor_Config_Calib_Index.name)
        )


        #  for sensor config source modbus TCP/IP config
        self.atFrame_Sensor_Config_Source_MBTCPIP_Config.set_OK_callback(
            lambda: self.set_frame(
                self.atFrame_Sensor_Config_Source_MBTCPIP_Config.get_chosen_submenu()
            )
        )
        # back to sensor config source modbus TCP/IP config
        self.atFrame_Sensor_Config_Source_MBTCPIP_Config_IP.set_F4_callback(
            lambda: self.set_frame(
                self.atFrame_Sensor_Config_Source_MBTCPIP_Config.name
            )
        )
        self.atFrame_Sensor_Config_Source_MBTCPIP_Config_ID.set_F4_callback(
            lambda: self.set_frame(
                self.atFrame_Sensor_Config_Source_MBTCPIP_Config.name
            )
        )
        self.atFrame_Sensor_Config_Source_MBTCPIP_Config_Type.set_Back_callback(
            lambda: self.set_frame(
                self.atFrame_Sensor_Config_Source_MBTCPIP_Config.name
            )
        )
        self.atFrame_Sensor_Config_Source_MBTCPIP_Config_Address.set_F4_callback(
            lambda: self.set_frame(
                self.atFrame_Sensor_Config_Source_MBTCPIP_Config.name
            )
        )

        #  for sensor config source modbus RTU config
        self.atFrame_Sensor_Config_Source_MBRTU_Config.set_OK_callback(
            lambda: self.set_frame(
                self.atFrame_Sensor_Config_Source_MBRTU_Config.get_chosen_submenu()
            )
        )
        # back to sensor config source modbus RTU config
        self.atFrame_Sensor_Config_Source_MBRTU_Config_Port.set_Back_callback(
            lambda: self.set_frame(
                self.atFrame_Sensor_Config_Source_MBRTU_Config.name
            )
        )
        self.atFrame_Sensor_Config_Source_MBRTU_Config_ID.set_F4_callback(
            lambda: self.set_frame(
                self.atFrame_Sensor_Config_Source_MBRTU_Config.name
            )
        )
        self.atFrame_Sensor_Config_Source_MBRTU_Config_Type.set_Back_callback(
            lambda: self.set_frame(
                self.atFrame_Sensor_Config_Source_MBRTU_Config.name
            )
        )
        self.atFrame_Sensor_Config_Source_MBRTU_Config_Address.set_F4_callback(
            lambda: self.set_frame(
                self.atFrame_Sensor_Config_Source_MBRTU_Config.name
            )
        )
# ++++++++++++++++++++++++++++++++++++++++++
        # for Protocols
        self.atFrame_Sensor_Config_Source_MBRTU_Config_Port.set_OK_callback( 
            lambda: self.set_frame(
                self.atFrame_Sensor_Config_Source_MBRTU_Config_Port.get_chosen_submenu()) 
        )
        #  Back to protocol
        self.atFrame_RS485_1.set_Back_callback(
            lambda: self.set_frame(
                self.atFrame_Sensor_Config_Source_MBRTU_Config_Port.name) 
        )
        # RS485-1
        self.atFrame_RS485_1.set_OK_callback( 
            lambda: self.set_frame(self.atFrame_RS485_1.get_chosen_submenu()) 
        )
        # back to RS485-1
        self.atFrame_RS485_1_Select.set_Back_callback(
            lambda: self.set_frame(self.atFrame_RS485_1.name) 
        )
        self.atFrame_RS485_1_Baudrate.set_Back_callback(
            lambda: self.set_frame(self.atFrame_RS485_1.name) 
        )
        self.atFrame_RS485_1_Data_Bits.set_Back_callback(
            lambda: self.set_frame(self.atFrame_RS485_1.name) 
        )
        self.atFrame_RS485_1_Stop_Bits.set_Back_callback(
            lambda: self.set_frame(self.atFrame_RS485_1.name) 
        )
        self.atFrame_RS485_1_Parity.set_Back_callback(
            lambda: self.set_frame(self.atFrame_RS485_1.name) 
        )

        # for Memory
        self.atFrame_Memory.set_OK_callback( 
            lambda: self.set_frame(self.atFrame_Memory.get_chosen_submenu()) 
        )
        # back to Memory
        self.atFrame_Disk_Space.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Memory.name) 
        )
        self.atFrame_USB_Space.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Memory.name) 
        )

        # for FTP Servers
        self.atFrame_FTP_Servers.set_OK_callback(
            lambda: self.set_frame(self.atFrame_FTP_Servers.get_chosen_submenu())             
        )
        # back to FTP Servers
        self.atFrame_FTP_1_Server.set_Back_callback(
            lambda: self.set_frame(self.atFrame_FTP_Servers.name) 
        )

        #  for FTP-1 Server
        self.atFrame_FTP_1_Server.set_OK_callback(
            lambda: self.set_frame(self.atFrame_FTP_1_Server.get_chosen_submenu())             
        )
        self.atFrame_FTP_1_Status.set_Back_callback(
            lambda: self.set_frame(self.atFrame_FTP_1_Server.name) 
        )
        self.atFrame_FTP_1_IP.set_F4_callback(
            lambda: self.set_frame(self.atFrame_FTP_1_Server.name) 
        )
        self.atFrame_FTP_1_Port.set_F4_callback(
            lambda: self.set_frame(self.atFrame_FTP_1_Server.name) 
        )
        self.atFrame_FTP_1_User.set_F4_callback(
            lambda: self.set_frame(self.atFrame_FTP_1_Server.name) 
        )
        self.atFrame_FTP_1_Password.set_F4_callback(
            lambda: self.set_frame(self.atFrame_FTP_1_Server.name) 
        )
        self.atFrame_FTP_1_Folder.set_F4_callback(
            lambda: self.set_frame(self.atFrame_FTP_1_Server.name) 
        )
    
        # for Errors
        self.atFrame_Errors.set_OK_callback(
            lambda: self.set_frame(self.atFrame_Errors.get_chosen_submenu())             
        )
        # back to Errors
        self.atFrame_Last_Error.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Errors.name) 
        )
        self.atFrame_Error_List.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Errors.name) 
        )
    
        # for Internet
        self.atFrame_Internet.set_OK_callback(
            lambda: self.set_frame(self.atFrame_Internet.get_chosen_submenu())             
        )
        # back to Internet
        self.atFrame_Ethernet.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Internet.name)             
        )
        self.atFrame_Wifi.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Internet.name)             
        )
        self.atFrame_4G_LTE.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Internet.name)             
        )
    
        #  for Web Server
        self.atFrame_Web_Server.set_OK_callback(
            lambda: self.set_frame(self.atFrame_Web_Server.get_chosen_submenu())
        )
        # back tto Web Server
        self.atFrame_Web_Server_Status.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Web_Server.name)             
        )
        self.atFrame_Web_Server_Enable.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Web_Server.name)             
        )
        self.atFrame_Web_Server_Auto_Config.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Web_Server.name)             
        )

        #  for Power
        self.atFrame_Power.set_OK_callback(
            lambda: self.set_frame(self.atFrame_Power.get_chosen_submenu())             
        )
        self.atFrame_Reset.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Power.name)             
        )
        self.atFrame_Shut_Down.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Power.name)             
        )

        # for Advances
        self.atFrame_Advances.set_OK_callback(
            lambda: self.set_frame(self.atFrame_Advances.get_chosen_submenu())             
        )
        #  back to Advances
        self.atFrame_Device_Analytic.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Advances.name)             
        )
        self.atFrame_Default_Restore.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Advances.name)             
        )
        self.atFrame_Backup_USB.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Advances.name)             
        )
        self.atFrame_Restore_USB.set_Back_callback(
            lambda: self.set_frame(self.atFrame_Advances.name)             
        )


    def set_frame(self,frame_name):
        self.frame = frame_name
        print("HMI go to frame: " + self.frame)

    def set_notification(self, notification):
        '''
        set 
        '''
        self.atFrame_Setting.set_notification(notification)

    def polling_frame(self):
    
        if self.frame == self.atFrame_Setting.name:
            self.atFrame_Setting.set_pointer(self.atFrame_Setting.pointer)
            while self.frame == self.atFrame_Setting.name:
                self.atFrame_Setting.polling_button()
    
        if self.frame == self.atFrame_Sensors.name:
            self.atFrame_Sensors.set_pointer(self.atFrame_Sensors.pointer)
            while self.frame == self.atFrame_Sensors.name:
                self.atFrame_Sensors.polling_button()

        if self.frame == self.atFrame_Memory.name:
            self.atFrame_Memory.set_pointer(self.atFrame_Memory.pointer)
            while self.frame == self.atFrame_Memory.name:
                self.atFrame_Memory.polling_button()

        if self.frame == self.atFrame_FTP_Servers.name:
            self.atFrame_FTP_Servers.set_pointer(self.atFrame_FTP_Servers.pointer)
            while self.frame == self.atFrame_FTP_Servers.name:
                self.atFrame_FTP_Servers.polling_button()

        if self.frame == self.atFrame_Errors.name:
            self.atFrame_Errors.set_pointer(self.atFrame_Errors.pointer)
            while self.frame == self.atFrame_Errors.name:
                self.atFrame_Errors.polling_button()

        if self.frame == self.atFrame_Internet.name:
            self.atFrame_Internet.set_pointer(self.atFrame_Internet.pointer)
            while self.frame == self.atFrame_Internet.name:
                self.atFrame_Internet.polling_button()
                
        if self.frame == self.atFrame_Web_Server.name:
            self.atFrame_Web_Server.set_pointer(self.atFrame_Web_Server.pointer)
            while self.frame == self.atFrame_Web_Server.name:
                self.atFrame_Web_Server.polling_button()

        if self.frame == self.atFrame_Power.name:
            self.atFrame_Power.set_pointer(self.atFrame_Power.pointer)
            while self.frame == self.atFrame_Power.name:
                self.atFrame_Power.polling_button()

        if self.frame == self.atFrame_Advances.name:
            self.atFrame_Advances.set_pointer(self.atFrame_Advances.pointer)
            while self.frame == self.atFrame_Advances.name:
                self.atFrame_Advances.polling_button()

        if self.frame == self.atFrame_About.name:
            self.atFrame_About.set_pointer(self.atFrame_About.pointer)
            while self.frame == self.atFrame_About.name:
                self.atFrame_About.polling_button()

        if self.frame == self.atFrame_RS485_1.name:
            self.atFrame_RS485_1.set_pointer(self.atFrame_RS485_1.pointer)
            while self.frame == self.atFrame_RS485_1.name:
                self.atFrame_RS485_1.polling_button()

        if self.frame == self.atFrame_RS485_1_Select.name:
            self.atFrame_RS485_1_Select.set_pointer(self.atFrame_RS485_1_Select.pointer)
            while self.frame == self.atFrame_RS485_1_Select.name:
                self.atFrame_RS485_1_Select.polling_button()

        if self.frame == self.atFrame_RS485_1_Baudrate.name:
            self.atFrame_RS485_1_Baudrate.set_pointer(self.atFrame_RS485_1_Baudrate.pointer)
            while self.frame == self.atFrame_RS485_1_Baudrate.name:
                self.atFrame_RS485_1_Baudrate.polling_button()

        if self.frame == self.atFrame_RS485_1_Data_Bits.name:
            self.atFrame_RS485_1_Data_Bits.set_pointer(self.atFrame_RS485_1_Data_Bits.pointer)
            while self.frame == self.atFrame_RS485_1_Data_Bits.name:
                self.atFrame_RS485_1_Data_Bits.polling_button()
                
        if self.frame == self.atFrame_RS485_1_Stop_Bits.name:
            self.atFrame_RS485_1_Stop_Bits.set_pointer(self.atFrame_RS485_1_Stop_Bits.pointer)
            while self.frame == self.atFrame_RS485_1_Stop_Bits.name:
                self.atFrame_RS485_1_Stop_Bits.polling_button()

        if self.frame == self.atFrame_RS485_1_Parity.name:
            self.atFrame_RS485_1_Parity.set_pointer(self.atFrame_RS485_1_Parity.pointer)
            while self.frame == self.atFrame_RS485_1_Parity.name:
                self.atFrame_RS485_1_Parity.polling_button()

        if self.frame == self.atFrame_Disk_Space.name:
            self.atFrame_Disk_Space.set_pointer(self.atFrame_Disk_Space.pointer)
            while self.frame == self.atFrame_Disk_Space.name:
                self.atFrame_Disk_Space.polling_button()

        if self.frame == self.atFrame_USB_Space.name:
            self.atFrame_USB_Space.set_pointer(self.atFrame_USB_Space.pointer)
            while self.frame == self.atFrame_USB_Space.name:
                self.atFrame_USB_Space.polling_button()

        if self.frame == self.atFrame_FTP_1_Server.name:
            self.atFrame_FTP_1_Server.set_pointer(self.atFrame_FTP_1_Server.pointer)
            while self.frame == self.atFrame_FTP_1_Server.name:
                self.atFrame_FTP_1_Server.polling_button()
                
        if self.frame == self.atFrame_FTP_1_Status.name:
            self.atFrame_FTP_1_Status.set_pointer(self.atFrame_FTP_1_Status.pointer)
            while self.frame == self.atFrame_FTP_1_Status.name:
                self.atFrame_FTP_1_Status.polling_button()

        if self.frame == self.atFrame_FTP_1_IP.name:
            self.atFrame_FTP_1_IP.set_pointer(self.atFrame_FTP_1_IP.pointer)
            while self.frame == self.atFrame_FTP_1_IP.name:
                self.atFrame_FTP_1_IP.polling_button()

        if self.frame == self.atFrame_FTP_1_Port.name:
            self.atFrame_FTP_1_Port.set_pointer(self.atFrame_FTP_1_Port.pointer)
            while self.frame == self.atFrame_FTP_1_Port.name:
                self.atFrame_FTP_1_Port.polling_button()

        if self.frame == self.atFrame_FTP_1_User.name:
            self.atFrame_FTP_1_User.set_pointer(self.atFrame_FTP_1_User.pointer)
            while self.frame == self.atFrame_FTP_1_User.name:
                self.atFrame_FTP_1_User.polling_button()

        if self.frame == self.atFrame_FTP_1_Password.name:
            self.atFrame_FTP_1_Password.set_pointer(self.atFrame_FTP_1_Password.pointer)
            while self.frame == self.atFrame_FTP_1_Password.name:
                self.atFrame_FTP_1_Password.polling_button()

        if self.frame == self.atFrame_FTP_1_Folder.name:
            self.atFrame_FTP_1_Folder.set_pointer(self.atFrame_FTP_1_Folder.pointer)
            while self.frame == self.atFrame_FTP_1_Folder.name:
                self.atFrame_FTP_1_Folder.polling_button()
                
        if self.frame == self.atFrame_Last_Error.name:
            self.atFrame_Last_Error.set_pointer(self.atFrame_Last_Error.pointer)
            while self.frame == self.atFrame_Last_Error.name:
                self.atFrame_Last_Error.polling_button()

        if self.frame == self.atFrame_Error_List.name:
            self.atFrame_Error_List.set_pointer(self.atFrame_Error_List.pointer)
            while self.frame == self.atFrame_Error_List.name:
                self.atFrame_Error_List.polling_button()

        if self.frame == self.atFrame_Ethernet.name:
            self.atFrame_Ethernet.set_pointer(self.atFrame_Ethernet.pointer)
            while self.frame == self.atFrame_Ethernet.name:
                self.atFrame_Ethernet.polling_button()
                
        if self.frame == self.atFrame_Wifi.name:
            self.atFrame_Wifi.set_pointer(self.atFrame_Wifi.pointer)
            while self.frame == self.atFrame_Wifi.name:
                self.atFrame_Wifi.polling_button()

        if self.frame == self.atFrame_4G_LTE.name:
            self.atFrame_4G_LTE.set_pointer(self.atFrame_4G_LTE.pointer)
            while self.frame == self.atFrame_4G_LTE.name:
                self.atFrame_4G_LTE.polling_button()
                
        if self.frame == self.atFrame_Web_Server_Status.name:
            self.atFrame_Web_Server_Status.set_pointer(self.atFrame_Web_Server_Status.pointer)
            while self.frame == self.atFrame_Web_Server_Status.name:
                self.atFrame_Web_Server_Status.polling_button()

        if self.frame == self.atFrame_Web_Server_Enable.name:
            self.atFrame_Web_Server_Enable.set_pointer(self.atFrame_Web_Server_Enable.pointer)
            while self.frame == self.atFrame_Web_Server_Enable.name:
                self.atFrame_Web_Server_Enable.polling_button()

        if self.frame == self.atFrame_Web_Server_Auto_Config.name:
            self.atFrame_Web_Server_Auto_Config.set_pointer(self.atFrame_Web_Server_Auto_Config.pointer)
            while self.frame == self.atFrame_Web_Server_Auto_Config.name:
                self.atFrame_Web_Server_Auto_Config.polling_button()

        if self.frame == self.atFrame_Reset.name:
            self.atFrame_Reset.set_pointer(self.atFrame_Reset.pointer)
            while self.frame == self.atFrame_Reset.name:
                self.atFrame_Reset.polling_button()

        if self.frame == self.atFrame_Shut_Down.name:
            self.atFrame_Shut_Down.set_pointer(self.atFrame_Shut_Down.pointer)
            while self.frame == self.atFrame_Shut_Down.name:
                self.atFrame_Shut_Down.polling_button()

        if self.frame == self.atFrame_Device_Analytic.name:
            self.atFrame_Device_Analytic.set_pointer(self.atFrame_Device_Analytic.pointer)
            while self.frame == self.atFrame_Device_Analytic.name:
                self.atFrame_Device_Analytic.polling_button()

        if self.frame == self.atFrame_Default_Restore.name:
            self.atFrame_Default_Restore.set_pointer(self.atFrame_Default_Restore.pointer)
            while self.frame == self.atFrame_Default_Restore.name:
                self.atFrame_Default_Restore.polling_button()

        if self.frame == self.atFrame_Backup_USB.name:
            self.atFrame_Backup_USB.set_pointer(self.atFrame_Backup_USB.pointer)
            while self.frame == self.atFrame_Backup_USB.name:
                self.atFrame_Backup_USB.polling_button()

        if self.frame == self.atFrame_Restore_USB.name:
            self.atFrame_Restore_USB.set_pointer(self.atFrame_Restore_USB.pointer)
            while self.frame == self.atFrame_Restore_USB.name:
                self.atFrame_Restore_USB.polling_button()

        if self.frame == self.atFrame_Sensor_Detail.name:
            self.atFrame_Sensor_Detail.set_pointer(self.atFrame_Sensor_Detail.pointer)
            while self.frame == self.atFrame_Sensor_Detail.name:
                self.atFrame_Sensor_Detail.polling_button()

        if self.frame == self.atFrame_Sensor_Data.name:
            self.atFrame_Sensor_Data.set_pointer(self.atFrame_Sensor_Data.pointer)
            while self.frame == self.atFrame_Sensor_Data.name:
                self.atFrame_Sensor_Data.polling_button()

        if self.frame == self.atFrame_Sensor_Config.name:
            self.atFrame_Sensor_Config.set_pointer(self.atFrame_Sensor_Config.pointer)
            while self.frame == self.atFrame_Sensor_Config.name:
                self.atFrame_Sensor_Config.polling_button()

        if self.frame == self.atFrame_Delete_Sensor.name:
            self.atFrame_Delete_Sensor.set_pointer(self.atFrame_Delete_Sensor.pointer)
            while self.frame == self.atFrame_Delete_Sensor.name:
                self.atFrame_Delete_Sensor.polling_button()

        if self.frame == self.atFrame_Clone_Sensor.name:
            self.atFrame_Clone_Sensor.set_pointer(self.atFrame_Clone_Sensor.pointer)
            while self.frame == self.atFrame_Clone_Sensor.name:
                self.atFrame_Clone_Sensor.polling_button()
        
        if self.frame == self.atFrame_Sensor_Diagram.name:
            self.atFrame_Sensor_Diagram.set_pointer(self.atFrame_Sensor_Diagram.pointer)
            while self.frame == self.atFrame_Sensor_Diagram.name:
                self.atFrame_Sensor_Diagram.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Name.name:
            self.atFrame_Sensor_Config_Name.set_pointer(self.atFrame_Sensor_Config_Name.pointer)
            while self.frame == self.atFrame_Sensor_Config_Name.name:
                self.atFrame_Sensor_Config_Name.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Unit.name:
            self.atFrame_Sensor_Config_Unit.set_pointer(self.atFrame_Sensor_Config_Unit.pointer)
            while self.frame == self.atFrame_Sensor_Config_Unit.name:
                self.atFrame_Sensor_Config_Unit.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Source.name:
            self.atFrame_Sensor_Config_Source.set_pointer(self.atFrame_Sensor_Config_Source.pointer)
            while self.frame == self.atFrame_Sensor_Config_Source.name:
                self.atFrame_Sensor_Config_Source.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Calib.name:
            self.atFrame_Sensor_Config_Calib.set_pointer(self.atFrame_Sensor_Config_Calib.pointer)
            while self.frame == self.atFrame_Sensor_Config_Calib.name:
                self.atFrame_Sensor_Config_Calib.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Alarm.name:
            self.atFrame_Sensor_Config_Alarm.set_pointer(self.atFrame_Sensor_Config_Alarm.pointer)
            while self.frame == self.atFrame_Sensor_Config_Alarm.name:
                self.atFrame_Sensor_Config_Alarm.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Error.name:
            self.atFrame_Sensor_Config_Error.set_pointer(self.atFrame_Sensor_Config_Error.pointer)
            while self.frame == self.atFrame_Sensor_Config_Error.name:
                self.atFrame_Sensor_Config_Error.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Source_MBTCPIP.name:
            self.atFrame_Sensor_Config_Source_MBTCPIP.set_pointer(self.atFrame_Sensor_Config_Source_MBTCPIP.pointer)
            while self.frame == self.atFrame_Sensor_Config_Source_MBTCPIP.name:
                self.atFrame_Sensor_Config_Source_MBTCPIP.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Source_MBRTU.name:
            self.atFrame_Sensor_Config_Source_MBRTU.set_pointer(self.atFrame_Sensor_Config_Source_MBRTU.pointer)
            while self.frame == self.atFrame_Sensor_Config_Source_MBRTU.name:
                self.atFrame_Sensor_Config_Source_MBRTU.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Source_4_20mA.name:
            self.atFrame_Sensor_Config_Source_4_20mA.set_pointer(self.atFrame_Sensor_Config_Source_4_20mA.pointer)
            while self.frame == self.atFrame_Sensor_Config_Source_4_20mA.name:
                self.atFrame_Sensor_Config_Source_4_20mA.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Source_Data_Type.name:
            self.atFrame_Sensor_Config_Source_Data_Type.set_pointer(self.atFrame_Sensor_Config_Source_Data_Type.pointer)
            while self.frame == self.atFrame_Sensor_Config_Source_Data_Type.name:
                self.atFrame_Sensor_Config_Source_Data_Type.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Calib_Function.name:
            self.atFrame_Sensor_Config_Calib_Function.set_pointer(self.atFrame_Sensor_Config_Calib_Function.pointer)
            while self.frame == self.atFrame_Sensor_Config_Calib_Function.name:
                self.atFrame_Sensor_Config_Calib_Function.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Calib_Index.name:
            self.atFrame_Sensor_Config_Calib_Index.set_pointer(self.atFrame_Sensor_Config_Calib_Index.pointer)
            while self.frame == self.atFrame_Sensor_Config_Calib_Index.name:
                self.atFrame_Sensor_Config_Calib_Index.polling_button()
                
        if self.frame == self.atFrame_Sensor_Config_Source_MBTCPIP_Select.name:
            self.atFrame_Sensor_Config_Source_MBTCPIP_Select.set_pointer(self.atFrame_Sensor_Config_Source_MBTCPIP_Select.pointer)
            while self.frame == self.atFrame_Sensor_Config_Source_MBTCPIP_Select.name:
                self.atFrame_Sensor_Config_Source_MBTCPIP_Select.polling_button()
                
        if self.frame == self.atFrame_Sensor_Config_Source_MBTCPIP_Config.name:
            self.atFrame_Sensor_Config_Source_MBTCPIP_Config.set_pointer(self.atFrame_Sensor_Config_Source_MBTCPIP_Config.pointer)
            while self.frame == self.atFrame_Sensor_Config_Source_MBTCPIP_Config.name:
                self.atFrame_Sensor_Config_Source_MBTCPIP_Config.polling_button()
                
        if self.frame == self.atFrame_Sensor_Config_Source_MBRTU_Select.name:
            self.atFrame_Sensor_Config_Source_MBRTU_Select.set_pointer(self.atFrame_Sensor_Config_Source_MBRTU_Select.pointer)
            while self.frame == self.atFrame_Sensor_Config_Source_MBRTU_Select.name:
                self.atFrame_Sensor_Config_Source_MBRTU_Select.polling_button()
                
        if self.frame == self.atFrame_Sensor_Config_Source_MBRTU_Config.name:
            self.atFrame_Sensor_Config_Source_MBRTU_Config.set_pointer(self.atFrame_Sensor_Config_Source_MBRTU_Config.pointer)
            while self.frame == self.atFrame_Sensor_Config_Source_MBRTU_Config.name:
                self.atFrame_Sensor_Config_Source_MBRTU_Config.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Calib_Index_A.name:
            self.atFrame_Sensor_Config_Calib_Index_A.set_pointer(self.atFrame_Sensor_Config_Calib_Index_A.pointer)
            while self.frame == self.atFrame_Sensor_Config_Calib_Index_A.name:
                self.atFrame_Sensor_Config_Calib_Index_A.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Calib_Index_B.name:
            self.atFrame_Sensor_Config_Calib_Index_B.set_pointer(self.atFrame_Sensor_Config_Calib_Index_B.pointer)
            while self.frame == self.atFrame_Sensor_Config_Calib_Index_B.name:
                self.atFrame_Sensor_Config_Calib_Index_B.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Calib_Index_C.name:
            self.atFrame_Sensor_Config_Calib_Index_C.set_pointer(self.atFrame_Sensor_Config_Calib_Index_C.pointer)
            while self.frame == self.atFrame_Sensor_Config_Calib_Index_C.name:
                self.atFrame_Sensor_Config_Calib_Index_C.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Calib_Index_D.name:
            self.atFrame_Sensor_Config_Calib_Index_D.set_pointer(
                self.atFrame_Sensor_Config_Calib_Index_D.pointer)
            while self.frame == self.atFrame_Sensor_Config_Calib_Index_D.name:
                self.atFrame_Sensor_Config_Calib_Index_D.polling_button()

    
        if self.frame == self.atFrame_Sensor_Config_Source_MBTCPIP_Config_IP.name:
            self.atFrame_Sensor_Config_Source_MBTCPIP_Config_IP.set_pointer(
                self.atFrame_Sensor_Config_Source_MBTCPIP_Config_IP.pointer)
            while self.frame == self.atFrame_Sensor_Config_Source_MBTCPIP_Config_IP.name:
                self.atFrame_Sensor_Config_Source_MBTCPIP_Config_IP.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Source_MBTCPIP_Config_ID.name:
            self.atFrame_Sensor_Config_Source_MBTCPIP_Config_ID.set_pointer(
                self.atFrame_Sensor_Config_Source_MBTCPIP_Config_ID.pointer)
            while self.frame == self.atFrame_Sensor_Config_Source_MBTCPIP_Config_ID.name:
                self.atFrame_Sensor_Config_Source_MBTCPIP_Config_ID.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Source_MBTCPIP_Config_Type.name:
            self.atFrame_Sensor_Config_Source_MBTCPIP_Config_Type.set_pointer(
                self.atFrame_Sensor_Config_Source_MBTCPIP_Config_Type.pointer)
            while self.frame == self.atFrame_Sensor_Config_Source_MBTCPIP_Config_Type.name:
                self.atFrame_Sensor_Config_Source_MBTCPIP_Config_Type.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Source_MBTCPIP_Config_Address.name:
            self.atFrame_Sensor_Config_Source_MBTCPIP_Config_Address.set_pointer(
                self.atFrame_Sensor_Config_Source_MBTCPIP_Config_Address.pointer)
            while self.frame == self.atFrame_Sensor_Config_Source_MBTCPIP_Config_Address.name:
                self.atFrame_Sensor_Config_Source_MBTCPIP_Config_Address.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Source_MBRTU_Config_Port.name:
            self.atFrame_Sensor_Config_Source_MBRTU_Config_Port.set_pointer(
                self.atFrame_Sensor_Config_Source_MBRTU_Config_Port.pointer)
            while self.frame == self.atFrame_Sensor_Config_Source_MBRTU_Config_Port.name:
                self.atFrame_Sensor_Config_Source_MBRTU_Config_Port.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Source_MBRTU_Config_ID.name:
            self.atFrame_Sensor_Config_Source_MBRTU_Config_ID.set_pointer(
                self.atFrame_Sensor_Config_Source_MBRTU_Config_ID.pointer)
            while self.frame == self.atFrame_Sensor_Config_Source_MBRTU_Config_ID.name:
                self.atFrame_Sensor_Config_Source_MBRTU_Config_ID.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Source_MBRTU_Config_Type.name:
            self.atFrame_Sensor_Config_Source_MBRTU_Config_Type.set_pointer(
                self.atFrame_Sensor_Config_Source_MBRTU_Config_Type.pointer)
            while self.frame == self.atFrame_Sensor_Config_Source_MBRTU_Config_Type.name:
                self.atFrame_Sensor_Config_Source_MBRTU_Config_Type.polling_button()

        if self.frame == self.atFrame_Sensor_Config_Source_MBRTU_Config_Address.name:
            self.atFrame_Sensor_Config_Source_MBRTU_Config_Address.set_pointer(
                self.atFrame_Sensor_Config_Source_MBRTU_Config_Address.pointer)
            while self.frame == self.atFrame_Sensor_Config_Source_MBRTU_Config_Address.name:
                self.atFrame_Sensor_Config_Source_MBRTU_Config_Address.polling_button()

hmi= atHMI()
while True:
   hmi.polling_frame()