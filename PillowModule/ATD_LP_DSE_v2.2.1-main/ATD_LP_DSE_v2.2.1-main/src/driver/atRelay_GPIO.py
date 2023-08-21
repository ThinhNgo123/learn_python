import os
BOARD = {
    3:    229,   # PH5/I2C3_SDA
    5:    228,   # PH4/I2C3_SCK
    7:    73,    # PC9
    8:    226,   # PH2/UART5_TX
    10:   227,   # PH3/UART5_RX
    11:   70,    # PC6
    12:   75,    # PC11
    13:   69,    # PC5
    15:   72,    # PC8
    16:   79,    # PC15
    18:   78,    # PC14
    19:   231,   # PH7,SPI1_MOSI
    21:   232,   # PH8,SPI1_MISO
    22:   71,    # PC7
    23:   230,   # PH6,SPI1_CLK
    24:   233,   # PH9,SPI1_CS
    26:   74,    # PC10
}
try:
    from OPi import GPIO
except:
    os.system("pip install OPi.GPIO")
    from OPi import GPIO

from time import sleep


class atRelay_GPIO_Class():
    PC9 = 7
    PC6 = 11
    PC11 = 12
    PC5 = 13
    PC8 = 15
    PC15 = 16
    PC14 = 18
    PC7 = 22
    PC10 = 26
    def __init__(self) -> None:
        GPIO.setmode(BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(7, GPIO.OUT)

    def turnOn(self):
        GPIO.output(self.PC9,GPIO.HIGH)

    def turnOff(self):
        GPIO.output(self.PC9,GPIO.LOW)

atRelay_GPIO = atRelay_GPIO_Class()
