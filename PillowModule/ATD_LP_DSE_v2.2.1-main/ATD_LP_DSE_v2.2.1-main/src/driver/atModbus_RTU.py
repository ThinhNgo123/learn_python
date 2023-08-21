
#!/usr/bin/env python3
import os 
try:    
    import minimalmodbus
    import serial
except:
    os.system("pip3 install -U minimalmodbus")
    import minimalmodbus
    import serial

PORT = {"RS485-1" : '/dev/ttyS5'}

class atModbus_RTU_Driver(minimalmodbus.Instrument):
    
    def __init__(self, port: str, slaveaddress: int, mode: str = ..., close_port_after_each_call: bool = False, debug: bool = False) -> None:
        super().__init__(port, slaveaddress, mode, close_port_after_each_call, debug)

        self.mode = "rtu"
        self.close_port_after_each_call = True
        self.debug = False
        self.serial.port = PORT["RS485-1"] # this is the serial port name
        self.serial.baudrate = 9600         # Baud
        self.serial.bytesize = 8
        self.serial.parity   = serial.PARITY_EVEN
        self.serial.stopbits = 1
        self.serial.timeout  = 1          # seconds
        self.address = 4
    
    def read(
        self, 
        mode: str = "rtu",
        debug = False,
        port: str = PORT["RS485-1"],
        baudrate: int = 9600,
        bytesize: int = 8,
        stopbits: int= 1,
        parity : str = serial.PARITY_EVEN,
        timeout : int = 1,
        address : int = 1,
        type : str = "holding",
        register_address : int = 1,
        register_number : int = 1,
        number_of_decimals: int = 0,
        datatype='int16'
        ):
        # update new parameter for modbus 
        self.mode = mode
        self.debug = debug
        self.serial.port = port 
        self.serial.baudrate = baudrate         
        self.serial.bytesize = bytesize
        self.serial.parity   = parity
        self.serial.stopbits = stopbits
        self.serial.timeout  = timeout  # seconds
        self.address = address

        # print(self)
        if register_number < 0:
            return "register_number must the greater than 0"
        if register_number == 1:
            if type == "holding":
                return self.read_register(
                    registeraddress= register_address,
                    number_of_decimals= number_of_decimals,
                    functioncode= 3)

            elif type == "input":
                return self.read_register(
                    registeraddress= register_address,
                    number_of_decimals= number_of_decimals,
                    functioncode= 4)

            elif type == "discrete":
                return self.read_bit(
                    registeraddress= register_address,
                    functioncode= 2)

            elif type == "coil":
                return self.read_bit(
                    registeraddress= register_address,
                    functioncode= 1)

        # read many register or bit
        if register_number > 1:

            if type == "holding":
                try:
                    return self.read_registers(
                        registeraddress= register_address,
                        number_of_registers= register_number,
                        functioncode= 3)
                except :
                    return False

            if type == "input":
                try:
                    return self.read_registers(
                        registeraddress= register_address,
                        number_of_registers= register_number,
                        functioncode= 4
                        )
                except :
                    return False

            if type == "discrete":
                try:
                    return self.read_bits(
                        registeraddress= register_address,
                        number_of_bits= register_number,
                        functioncode= 2
                        )
                except :
                    return False

            if type == "coil":
                try:
                    return self.read_bits(
                        registeraddress= register_address,
                        number_of_bits= register_number,
                        functioncode= 1
                        )
                except :
                    return False

atModbus_RTU  = atModbus_RTU_Driver(
    port= PORT["RS485-1"],
    slaveaddress= 1
)

if __name__ == "__main__":
    values = atModbus_RTU.read(
                type= "holding",
                address= 4,
                register_address= 0X3000-1,
                # register_number= 10
            )
    print(values)
    values = atModbus_RTU.read(
                type= "holding",
                address= 4,
                register_address= 0X3000-1,
                register_number= 10
            )
    print(values)