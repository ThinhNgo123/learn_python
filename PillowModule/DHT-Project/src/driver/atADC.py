import os

try:
    import smbus
except:
    os.system("pip install smbus")
    import smbus

try:
    from MCP342x import MCP342x
except:
    os.system("pip install MCP342x")
    from MCP342x import MCP342x


class atADC():
    i2c_bus = smbus.SMBus(5)

    AI1 = MCP342x(i2c_bus, 0x68, channel=3, resolution=18)
    AI2 = MCP342x(i2c_bus, 0x68, channel=2, resolution=18)
    AI3 = MCP342x(i2c_bus, 0x68, channel=1, resolution=18)
    AI4 = MCP342x(i2c_bus, 0x68, channel=0, resolution=18)

    AI5 = MCP342x(i2c_bus, 0x6c, channel=3, resolution=18)
    AI6 = MCP342x(i2c_bus, 0x6c, channel=2, resolution=18)
    AI7 = MCP342x(i2c_bus, 0x6c, channel=1, resolution=18)
    AI8 = MCP342x(i2c_bus, 0x6c, channel=0, resolution=18)

    def __init__(self) -> None:
        pass

    def read_AI_1(self):
        voltage_ADC = self.AI1.convert_and_read()
        voltage_in = voltage_ADC / 2.2*(2.2+3.3)
        current_in = voltage_in / 200 * 1000
        return current_in
    def read_AI_2(self):
        voltage_ADC = self.AI2.convert_and_read()
        voltage_in = voltage_ADC / 2.2*(2.2+3.3)
        current_in = voltage_in / 200 * 1000
        return current_in
    def read_AI_3(self):
        voltage_ADC = self.AI3.convert_and_read()
        voltage_in = voltage_ADC / 2.2*(2.2+3.3)
        current_in = voltage_in / 200 * 1000
        return current_in
    def read_AI_4(self):
        voltage_ADC = self.AI4.convert_and_read()
        voltage_in = voltage_ADC / 2.2*(2.2+3.3)
        current_in = voltage_in / 200 * 1000
        return current_in
    def read_AI_5(self):
        voltage_ADC = self.AI5.convert_and_read()
        voltage_in = voltage_ADC / 2.2*(2.2+3.3)
        current_in = voltage_in / 200 * 1000
        return current_in
    def read_AI_6(self):
        voltage_ADC = self.AI6.convert_and_read()
        voltage_in = voltage_ADC / 2.2*(2.2+3.3)
        current_in = voltage_in / 200 * 1000
        return current_in
    def read_AI_7(self):
        voltage_ADC = self.AI7.convert_and_read()
        voltage_in = voltage_ADC / 2.2*(2.2+3.3)
        current_in = voltage_in / 200 * 1000
        return current_in
    def read_AI_8(self):
        voltage_ADC = self.AI8.convert_and_read()
        voltage_in = voltage_ADC / 2.2*(2.2+3.3)
        current_in = voltage_in / 200 * 1000
        return current_in

    def read(self, channel_list, samples):
        """
        Read list of port at the same time, and samples
        - channel_list : [self.AI1, self.AI2]
        - samples : sample number for each channel
        """

        return  MCP342x.convert_and_read_many(channel_list, samples)

at4_20mAs = atADC()
if __name__ == "__main__":
    
    print("channel 1 :" + str(at4_20mAs.read_AI_1()) + " mA")
    print("channel 2 :" + str(at4_20mAs.read_AI_2()) + " mA")
    print("channel 3 :" + str(at4_20mAs.read_AI_3()) + " mA")
    print("channel 4 :" + str(at4_20mAs.read_AI_4()) + " mA")
    print("channel 5 :" + str(at4_20mAs.read_AI_5()) + " mA")
    print("channel 6 :" + str(at4_20mAs.read_AI_6()) + " mA")
    print("channel 7 :" + str(at4_20mAs.read_AI_7()) + " mA")
    print("channel 8 :" + str(at4_20mAs.read_AI_8()) + " mA")
