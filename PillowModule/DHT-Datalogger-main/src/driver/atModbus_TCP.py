#!/usr/bin/env python3
import os 
try:    
    from pyModbusTCP.client import ModbusClient
    
except:
    os.system("sudo pip install pyModbusTCP")
from pyModbusTCP.client import ModbusClient

import sys
sys.path.insert(0,"func/tool")
from Convert_Engine import convert_engine
import struct
class atModbus_TCP_Class():

    host = "192.168.1.3"
    port = 502
    unit_id = 1
    timeout = 30
    debug = False
    auto_open=True,
    auto_close=True

    client = ModbusClient(
        host= host,
        port= port,
        unit_id= unit_id,
        timeout= timeout,
        auto_open= auto_open,
        auto_close= auto_close
    )
    
    def __init__(self) -> None:
        pass

    def read(self, 
        IP = "192.168.1.11", 
        port = 502,
        ID = 1, 
        type = "holding", 
        time_out = 30,
        address = 1, 
        datatype = "int16"):

        result = None
        self.client = ModbusClient(
            host= IP,
            port= port,
            unit_id= ID,
            timeout= time_out,
            auto_open= self.auto_open,
            auto_close= self.auto_close
        )
        registers = []
        if (datatype == "bool"):
            reg_number = 1
            if type == "discrete":
                registers = self.client.read_discrete_inputs(address, reg_number)
            elif type == "input":
                registers = self.client.read_input_registers(address, reg_number)
            elif type == "coil":
                registers = self.client.read_coils(address, reg_number)
            elif type == "holding":
                registers = self.client.read_holding_registers(address, reg_number)

            if self.auto_close == False :
                self.client.close()
            result = 1 if registers[0] != 0 else 0

        if (datatype == "uint8"):
            reg_number = 1
            if type == "discrete":
                registers = self.client.read_discrete_inputs(address, reg_number)
            elif type == "input":
                registers = self.client.read_input_registers(address, reg_number)
            elif type == "coil":
                registers = self.client.read_coils(address, reg_number)
            elif type == "holding":
                registers = self.client.read_holding_registers(address, reg_number)

            if self.auto_close == False :
                self.client.close()
            result = registers[0] % 256


        if (datatype == "int8"):
            reg_number = 1
            if type == "discrete":
                registers = self.client.read_discrete_inputs(address, reg_number)
            elif type == "input":
                registers = self.client.read_input_registers(address, reg_number)
            elif type == "coil":
                registers = self.client.read_coils(address, reg_number)
            elif type == "holding":
                registers = self.client.read_holding_registers(address, reg_number)

            if self.auto_close == False :
                self.client.close()
            result = registers[0] % 256


        if (datatype == "uint16"):
            reg_number = 1
            if type == "discrete":
                registers = self.client.read_discrete_inputs(address, reg_number)
            elif type == "input":
                registers = self.client.read_input_registers(address, reg_number)
            elif type == "coil":
                registers = self.client.read_coils(address, reg_number)
            elif type == "holding":
                registers = self.client.read_holding_registers(address, reg_number)

            if self.auto_close == False :
                self.client.close()
            result = registers[0]

        if (datatype == "int16"):
            reg_number = 1
            if type == "discrete":
                registers = self.client.read_discrete_inputs(address, reg_number)
            elif type == "input":
                registers = self.client.read_input_registers(address, reg_number)
            elif type == "coil":
                registers = self.client.read_coils(address, reg_number)
            elif type == "holding":
                registers = self.client.read_holding_registers(address, reg_number)

            if self.auto_close == False :
                self.client.close()
            result = registers[0]

        if (datatype == "uint32"):
            reg_number = 2
            if type == "discrete":
                registers = self.client.read_discrete_inputs(address, reg_number)
            elif type == "input":
                registers = self.client.read_input_registers(address, reg_number)
            elif type == "coil":
                registers = self.client.read_coils(address, reg_number)
            elif type == "holding":
                registers = self.client.read_holding_registers(address, reg_number)

            if self.auto_close == False :
                self.client.close()

            result = registers[0]*256 + registers[1]

        if (datatype == "int32"):
            reg_number = 2
            if type == "discrete":
                registers = self.client.read_discrete_inputs(address, reg_number)
            elif type == "input":
                registers = self.client.read_input_registers(address, reg_number)
            elif type == "coil":
                registers = self.client.read_coils(address, reg_number)
            elif type == "holding":
                registers = self.client.read_holding_registers(address, reg_number)

            if self.auto_close == False :
                self.client.close()

            result = registers[0]*256 + registers[1]

        if (datatype == "uint32-Swapped"):
            reg_number = 2
            if type == "discrete":
                registers = self.client.read_discrete_inputs(address, reg_number)
            elif type == "input":
                registers = self.client.read_input_registers(address, reg_number)
            elif type == "coil":
                registers = self.client.read_coils(address, reg_number)
            elif type == "holding":
                registers = self.client.read_holding_registers(address, reg_number)

            if self.auto_close == False :
                self.client.close()

            result = registers[1]*35565 + registers[0]

        if (datatype == "int32-Swapped"):
            reg_number = 2
            if type == "discrete":
                registers = self.client.read_discrete_inputs(address, reg_number)
            elif type == "input":
                registers = self.client.read_input_registers(address, reg_number)
            elif type == "coil":
                registers = self.client.read_coils(address, reg_number)
            elif type == "holding":
                registers = self.client.read_holding_registers(address, reg_number)

            if self.auto_close == False :
                self.client.close()

            result = registers[1]*35565 + registers[0]


        if (datatype == "float32"):
            reg_number = 2
            if type == "discrete":
                registers = self.client.read_discrete_inputs(address, reg_number)
            elif type == "input":
                registers = self.client.read_input_registers(address, reg_number)
            elif type == "coil":
                registers = self.client.read_coils(address, reg_number)
            elif type == "holding":
                registers = self.client.read_holding_registers(address, reg_number)
            
            if self.auto_close == False :
                self.client.close()
            result = convert_engine.convert_to_real(registers[1],registers[0])

        if (datatype == "float32-Swapped"):
            reg_number = 2
            if type == "discrete":
                registers = self.client.read_discrete_inputs(address, reg_number)
            elif type == "input":
                registers = self.client.read_input_registers(address, reg_number)
            elif type == "coil":
                registers = self.client.read_coils(address, reg_number)
            elif type == "holding":
                registers = self.client.read_holding_registers(address, reg_number)
            
            if self.auto_close == False :
                self.client.close()
            result = convert_engine.convert_to_real(registers[1],registers[0])

        if (datatype == "float64"):
            reg_number = 4
            if type == "discrete":
                registers = self.client.read_discrete_inputs(address, reg_number)
            elif type == "input":
                registers = self.client.read_input_registers(address, reg_number)
            elif type == "coil":
                registers = self.client.read_coils(address, reg_number)
            elif type == "holding":
                registers = self.client.read_holding_registers(address, reg_number)

            if self.auto_close == False :
                self.client.close()

            
            result = convert_engine.convert_to_real64(registers)

        if (datatype == "float64-Swapped"):
            reg_number = 4
            if type == "discrete":
                registers = self.client.read_discrete_inputs(address, reg_number)
            elif type == "input":
                registers = self.client.read_input_registers(address, reg_number)
            elif type == "coil":
                registers = self.client.read_coils(address, reg_number)
            elif type == "holding":
                registers = self.client.read_holding_registers(address, reg_number)

            if self.auto_close == False :
                self.client.close()

            numb_str = f'{registers[3]:x}{registers[2]:x}{registers[1]:x}{registers[0]:x}'
            print("numb_str",numb_str)
            result = struct.unpack('!f', bytes.fromhex(numb_str))[0]
        

        # return result
        return result
        

atModbus_TCP = atModbus_TCP_Class()

if __name__ == "__main__":
    result = atModbus_TCP.read(
        IP= "192.168.1.11",
        type= "holding",
        address= 1,
    )
    print(result)