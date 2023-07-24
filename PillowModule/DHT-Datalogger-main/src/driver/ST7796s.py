#!/usr/bin/env python
import os
import numbers
import time
try:
    import numpy as np
except:
    os.system("pip install numpy")
    import numpy as np

try:
    import spidev
except: 
    os.system("sudo pip install spidev")
    import spidev
try:
    from OPi import GPIO
except:
    os.system("sudo pip install OPi.GPIO")
    from OPi import GPIO

__version__ = '0.0.1'
BOARD = {
    3:    47,    # SDA.5      / RXD.1     / GPIO1_B7
    5:    46,    # SCL.5      / TXD.1     / GPIO1_B6
    7:    54,    # PWM15                  / GPIO1_C6
    8:    131,   # RXD.0                  / GPIO4_A3
    10:   132,   # TXD.0                  / GPIO4_A4
    11:   138,   # CAN1_RX                / GPIO4_B2
    12:   29,    # CAN2_TX                / GPIO0_D5
    13:   139,   # CAN1_TX                / GPIO4_B3
    15:   28,    # CAN2_RX                / GPIO3_A6
    16:   59,    # SDA.1      / RXD.4     / GPIO1_D3
    18:   58,    # SCL.1      /TXD.4      /GPIO1_D2
    19:   49,    # SPI4_MOSI  /TXD.3      /GPIO1_C1
    21:   48,    # SPI4_MISO  /RXD.3      /GPIO1_C0
    22:   92,    # GPIO2_D4   /PowerOn_Low
    23:   50,    # SPI4_CLK               /GPIO1_C2
    24:   52,    # SPI4_CS1               /GPIO1_C4
    26:   35,    # PWM1                   /GPIO1_A3
}
BG_SPI_CS_BACK = 0
BG_SPI_CS_FRONT = 1

SPI_CLOCK_HZ = 16000000

ST7796S_TFTWIDTH = 320  # ST7796S max TFT width
ST7796S_TFTHEIGHT = 480 # ST7796S max TFT height

ST7796S_NOP = 0x00     # No-op register
ST7796S_SWRESET = 0x01 # Software reset register
ST7796S_RDDID = 0x04   # Read display identification information
ST7796S_RDDST = 0x09   # Read Display Status

ST7796S_SLPIN = 0x10  # Enter Sleep Mode
ST7796S_SLPOUT = 0x11 # Sleep Out
ST7796S_PTLON = 0x12  # Partial Mode ON
ST7796S_NORON = 0x13  # Normal Display Mode ON

ST7796S_RDMODE = 0x0A     # Read Display Power Mode
ST7796S_RDMADCTL = 0x0B   # Read Display MADCTL
ST7796S_RDPIXFMT = 0x0C   # Read Display Pixel Format
ST7796S_RDIMGFMT = 0x0D   # Read Display Image Format
ST7796S_RDSELFDIAG = 0x0F # Read Display Self-Diagnostic Result

ST7796S_INVOFF = 0x20   # Display Inversion OFF
ST7796S_INVON = 0x21    # Display Inversion ON
ST7796S_GAMMASET = 0x26 # Gamma Set
ST7796S_DISPOFF = 0x28  # Display OFF
ST7796S_DISPON = 0x29   # Display ON

ST7796S_CASET = 0x2A # Column Address Set
ST7796S_PASET = 0x2B # Page Address Set
ST7796S_RAMWR = 0x2C # Memory Write
ST7796S_RAMRD = 0x2E # Memory Read

ST7796S_PTLAR = 0x30    # Partial Area
ST7796S_VSCRDEF = 0x33  # Vertical Scrolling Definition
ST7796S_MADCTL = 0x36   # Memory Access Control
ST7796S_VSCRSADD = 0x37 # Vertical Scrolling Start Address
ST7796S_COLMOD = 0x3A   # COLMOD: Pixel Format Set



ST7796S_IFMODE  = 0xB0
ST7796S_FRMCTR1 = 0xB1
ST7796S_FRMCTR2 = 0xB2
ST7796S_FRMCTR3 = 0xB3
ST7796S_INVCTR = 0xB4
ST7796S_BPC = 0xB5
ST7796S_DFC = 0xB6
ST7796S_EM = 0xB6

ST7796S_GCTRL = 0xB7
ST7796S_GTADJ = 0xB8
ST7796S_VCOMS = 0xBB


ST7796S_PWR1 = 0xC0
ST7796S_PWR2 = 0xC1
ST7796S_PWR3 = 0xC2
ST7796S_VRHS = 0xC3
ST7796S_VDVS = 0xC4
ST7796S_VCMPCTL = 0xC5
ST7796S_VCM_Offset = 0xC6

ST7796S_RDID1 = 0xDA
ST7796S_RDID2 = 0xDB
ST7796S_RDID3 = 0xDC
ST7796S_RDID4 = 0xDD

ST7796S_GMCTRP1 = 0xE0
ST7796S_GMCTRN1 = 0xE1
ST7796S_DGC1 = 0xE2
ST7796S_DGC2 = 0xE3
ST7796S_DOCA = 0xE8

ST7796S_CSCON = 0xF0

ST7796S_PWCTR6 = 0xFC


#Color definitions
ST7796S_BLACK = 0x0000       #   0,   0,   0
ST7796S_NAVY = 0x000F        #   0,   0, 123
ST7796S_DARKGREEN = 0x03E0   #   0, 125,   0
ST7796S_DARKCYAN = 0x03EF    #   0, 125, 123
ST7796S_MAROON = 0x7800      # 123,   0,   0
ST7796S_PURPLE = 0x780F      # 123,   0, 123
ST7796S_OLIVE = 0x7BE0       # 123, 125,   0
ST7796S_LIGHTGREY = 0xC618   # 198, 195, 198
ST7796S_DARKGREY = 0x7BEF    # 123, 125, 123
ST7796S_BLUE = 0x001F        #   0,   0, 255
ST7796S_GREEN = 0x07E0       #   0, 255,   0
ST7796S_CYAN = 0x07FF        #   0, 255, 255
ST7796S_RED = 0xF800         # 255,   0,   0
ST7796S_MAGENTA = 0xF81F     # 255,   0, 255
ST7796S_YELLOW = 0xFFE0      # 255, 255,   0
ST7796S_WHITE = 0xFFFF       # 255, 255, 255
ST7796S_ORANGE = 0xFD20      # 255, 165,   0
ST7796S_GREENYELLOW = 0xAFE5 # 173, 255,  41
ST7796S_PINK = 0xFC18        # 255, 130, 198

# //-----------------------------------------------------------------------------
ST7796S_MAD_RGB        =0x08
ST7796S_MAD_BGR        =0x00

ST7796S_MAD_VERTICAL   =0x20
ST7796S_MAD_X_LEFT     =0x00
ST7796S_MAD_X_RIGHT    =0x40
ST7796S_MAD_Y_UP       =0x80
ST7796S_MAD_Y_DOWN     =0x00

ST7796S_COLORMODE = 0

if ST7796S_COLORMODE == 0:
  ST7796S_MAD_COLORMODE = ST7796S_MAD_RGB
else:
  ST7796S_MAD_COLORMODE = ST7796S_MAD_BGR

ST7796S_ORIENTATION = 3
if (ST7796S_ORIENTATION == 0):
  # ST7796S_SIZE_X                   =  ST7796S_LCD_PIXEL_WIDTH
  # ST7796S_SIZE_Y                   =  ST7796S_LCD_PIXEL_HEIGHT
  ST7796S_MAD_DATA_RIGHT_THEN_UP   =  ST7796S_MAD_COLORMODE | ST7796S_MAD_X_RIGHT | ST7796S_MAD_Y_UP
  ST7796S_MAD_DATA_RIGHT_THEN_DOWN =  ST7796S_MAD_COLORMODE | ST7796S_MAD_X_RIGHT | ST7796S_MAD_Y_DOWN
  ST7796S_MAD_DATA_RGBMODE         =  ST7796S_MAD_COLORMODE | ST7796S_MAD_X_LEFT  | ST7796S_MAD_Y_DOWN
elif (ST7796S_ORIENTATION == 1):
  # ST7796S_SIZE_X                   =  ST7796S_LCD_PIXEL_HEIGHT
  # ST7796S_SIZE_Y                   =  ST7796S_LCD_PIXEL_WIDTH
  ST7796S_MAD_DATA_RIGHT_THEN_UP   =  ST7796S_MAD_COLORMODE | ST7796S_MAD_X_RIGHT | ST7796S_MAD_Y_DOWN | ST7796S_MAD_VERTICAL
  ST7796S_MAD_DATA_RIGHT_THEN_DOWN =  ST7796S_MAD_COLORMODE | ST7796S_MAD_X_LEFT  | ST7796S_MAD_Y_DOWN | ST7796S_MAD_VERTICAL
  ST7796S_MAD_DATA_RGBMODE         =  ST7796S_MAD_COLORMODE | ST7796S_MAD_X_RIGHT | ST7796S_MAD_Y_DOWN
elif (ST7796S_ORIENTATION == 2):
  # ST7796S_SIZE_X                   =  ST7796S_LCD_PIXEL_WIDTH
  # ST7796S_SIZE_Y                   =  ST7796S_LCD_PIXEL_HEIGHT
  ST7796S_MAD_DATA_RIGHT_THEN_UP   =  ST7796S_MAD_COLORMODE | ST7796S_MAD_X_LEFT  | ST7796S_MAD_Y_DOWN
  ST7796S_MAD_DATA_RIGHT_THEN_DOWN =  ST7796S_MAD_COLORMODE | ST7796S_MAD_X_LEFT  | ST7796S_MAD_Y_UP
  ST7796S_MAD_DATA_RGBMODE         =  ST7796S_MAD_COLORMODE | ST7796S_MAD_X_RIGHT | ST7796S_MAD_Y_UP
elif (ST7796S_ORIENTATION == 3):
  # ST7796S_SIZE_X                   =  ST7796S_LCD_PIXEL_HEIGHT
  # ST7796S_SIZE_Y                   =  ST7796S_LCD_PIXEL_WIDTH
  ST7796S_MAD_DATA_RIGHT_THEN_UP   =  ST7796S_MAD_COLORMODE | ST7796S_MAD_X_LEFT  | ST7796S_MAD_Y_UP   | ST7796S_MAD_VERTICAL
  ST7796S_MAD_DATA_RIGHT_THEN_DOWN =  ST7796S_MAD_COLORMODE | ST7796S_MAD_X_RIGHT | ST7796S_MAD_Y_UP   | ST7796S_MAD_VERTICAL
  ST7796S_MAD_DATA_RGBMODE         =  ST7796S_MAD_COLORMODE | ST7796S_MAD_X_LEFT  | ST7796S_MAD_Y_UP

class atST7796S(object):
    """Representation of an ST7796S TFT LCD."""

    def __init__(self, port, cs, dc, backlight=None, rst=None, width=320,
                 height=480, rotation=90, invert=True, spi_speed_hz=40000000,
                 offset_left=0,
                 offset_top=0):
        """Create an instance of the display using SPI communication.

        Must provide the GPIO pin number for the D/C pin and the SPI driver.

        Can optionally provide the GPIO pin number for the reset pin as the rst parameter.

        :param port: SPI port number
        :param cs: SPI chip-select number (0 or 1 for BCM
        :param backlight: Pin for controlling backlight
        :param rst: Reset pin for ST7796S
        :param width: Width of display connected to ST7796S
        :param height: Height of display connected to ST7796S
        :param rotation: Rotation of display connected to ST7796S
        :param invert: Invert display
        :param spi_speed_hz: SPI speed (in Hz)

        """
        if rotation not in [0, 90, 180, 270]:
            raise ValueError("Invalid rotation {}".format(rotation))

        if width != height and rotation in [90, 270]:
            raise ValueError("Invalid rotation {} for {}x{} resolution".format(rotation, width, height))

        GPIO.setmode(BOARD)
        GPIO.setwarnings(False)

        self._spi = spidev.SpiDev(port,1)
        # self._spi.open(1, 0)
        self._spi.mode = 0
        self._spi.lsbfirst = False
        self._spi.max_speed_hz = spi_speed_hz

        self._cs = cs
        self._dc = dc
        self._rst = rst
        self._width = width
        self._height = height
        self._rotation = rotation
        self._invert = invert

        self._offset_left = offset_left
        self._offset_top = offset_top
        # Set DC as output.
        try:
            GPIO.setup(dc, GPIO.OUT)
        except:
            pass

        # Setup backlight as output (if provided).
        self._backlight = backlight
        if backlight is not None:
            try: 
                GPIO.setup(backlight, GPIO.OUT)
                GPIO.output(backlight, GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(backlight, GPIO.HIGH)
            except:
                pass

        # Setup reset as output (if provided).
        if rst is not None:
            try:
                GPIO.setup(rst, GPIO.OUT)
            except:
                pass

        # if cs is not None:
        #     GPIO.setup(cs, GPIO.OUT)

        self.reset()
        self._init()

    def send(self, data, is_data=True, chunk_size=4096):
        """Write a byte or array of bytes to the display. Is_data parameter
        controls if byte should be interpreted as display data (True) or command
        data (False).  Chunk_size is an optional size of bytes to write in a
        single SPI transaction, with a default of 4096.
        """
        # Set DC low for command, high for data.
        GPIO.output(self._dc, is_data)
        # Convert scalar argument to list so either can be passed as parameter.
        if isinstance(data, numbers.Number):
            data = [data & 0xFF]
        # Write data a chunk at a time.
        for start in range(0, len(data), chunk_size):
            end = min(start + chunk_size, len(data))
            self._spi.xfer(data[start:end])

    def set_backlight(self, value):
        """Set the backlight on/off."""
        if self._backlight is not None:
            GPIO.output(self._backlight, value)

    @property
    def width(self):
        return self._width if self._rotation == 0 or self._rotation == 180 else self._height

    @property
    def height(self):
        return self._height if self._rotation == 0 or self._rotation == 180 else self._width

    def command(self, data):
        """Write a byte or array of bytes to the display as command data."""
        self.send(data, False)

    def data(self, data):
        """Write a byte or array of bytes to the display as display data."""
        self.send(data, True)

    def reset(self):
        """Reset the display, if reset pin is connected."""
        if self._rst is not None:
            GPIO.output(self._rst, 1)
            time.sleep(0.500)
            GPIO.output(self._rst, 0)
            time.sleep(0.500)
            GPIO.output(self._rst, 1)
            time.sleep(0.500)
    
    def _init(self):
      # Initialize the display.

      self.command(ST7796S_SWRESET)  # Software reset
      time.sleep(0.150)              # delay 150 ms

      
      self.command(ST7796S_CSCON)
      self.data(0xC3)
      self.command(ST7796S_CSCON)
      self.data(0x96)

      self.command(ST7796S_MADCTL)
      self.data(0x68)
      
      self.command(ST7796S_COLMOD)
      self.data(0x05)

      self.command(ST7796S_IFMODE)
      self.data(0x80)

      self.command(ST7796S_DFC)  
      self.data(0x20)
      self.data(0x20)

      self.command(ST7796S_BPC)  
      self.data(0x02)
      self.data(0x03)
      self.data(0x00)
      self.data(0x04)

      self.command(ST7796S_FRMCTR1)  
      self.data(0x80)
      self.data(0x10)

      self.command(ST7796S_FRMCTR1)  
      self.data(0x80)
      
      self.command(ST7796S_INVCTR)
      self.data(0x00)

      self.command(ST7796S_EM)
      self.data(0xC6)

      self.command(ST7796S_VCMPCTL)
      self.data(0x24)

      self.command(ST7796S_DOCA)
      self.data(0x40)
      self.data(0x8A)
      self.data(0x00)
      self.data(0x00)
      self.data(0x29)
      self.data(0x19)
      self.data(0xA5)
      self.data(0x33)

      self.command(ST7796S_GMCTRP1)
      self.data(0xF0)
      self.data(0x09)
      self.data(0x13)
      self.data(0x12)
      self.data(0x12)
      self.data(0x2B)
      self.data(0x3C)
      self.data(0x44)
      self.data(0x4B)
      self.data(0x1B)
      self.data(0x18)
      self.data(0x17)
      self.data(0x1D)
      self.data(0x21)

      self.command(ST7796S_GMCTRN1)
      self.data(0xF0)
      self.data(0x09)
      self.data(0x13)
      self.data(0x0C)
      self.data(0x0D)
      self.data(0x27)
      self.data(0x3B)
      self.data(0x44)
      self.data(0x4D)
      self.data(0x0B)
      self.data(0x17)
      self.data(0x17)
      self.data(0x1D)
      self.data(0x21)

      # self.command(ST7796S_MADCTL)
      self.data(ST7796S_MAD_DATA_RIGHT_THEN_DOWN)

      self.command(ST7796S_CSCON)
      self.data(0xC3)
      self.command(ST7796S_CSCON)
      self.data(0x96)

      if self._invert:
          self.command(ST7796S_INVON)   # Invert display
      else:
          self.command(ST7796S_INVOFF)  # Don't invert display

      self.command(ST7796S_SLPOUT)
      time.sleep(0.200)               # 100 ms

      self.command(ST7796S_DISPON)     # Display on
      time.sleep(0.100)               # 100 ms

    def begin(self):
        """Set up the display

        Deprecated. Included in __init__.

        """
        pass

    def set_window(self, x0=0, y0=0, x1=None, y1=None):
        """Set the pixel address window for proceeding drawing commands. x0 and
        x1 should define the minimum and maximum x pixel bounds.  y0 and y1
        should define the minimum and maximum y pixel bound.  If no parameters
        are specified the default will be to update the entire display from 0,0
        to width-1,height-1.
        """
        if x1 is None:
            x1 = self._width - 1

        if y1 is None:
            y1 = self._height - 1

        y0 += self._offset_top
        y1 += self._offset_top

        x0 += self._offset_left
        x1 += self._offset_left

        self.command(ST7796S_CASET)       # Column addr set
        self.data(x0 >> 8)
        self.data(x0 & 0xFF)             # XSTART
        self.data(x1 >> 8)
        self.data(x1 & 0xFF)             # XEND
        self.command(ST7796S_PASET)       # Row addr set
        self.data(y0 >> 8)
        self.data(y0 & 0xFF)             # YSTART
        self.data(y1 >> 8)
        self.data(y1 & 0xFF)             # YEND
        self.command(ST7796S_RAMWR)       # write to RAM

    def display(self, image):
        """Write the provided image to the hardware.

        :param image: Should be RGB format and the same dimensions as the display hardware.

        """
        # Set address bounds to entire display.
        self.set_window()

        # Convert image to 16bit RGB565 format and
        # flatten into bytes.
        pixelbytes = self.image_to_data(image, self._rotation)

        # Write data to hardware.
        for i in range(0, len(pixelbytes), 4096):
            self.data(pixelbytes[i:i + 4096])

    def image_to_data(self, image, rotation=0):
        if not isinstance(image, np.ndarray):
            image = np.array(image.convert('RGB'))

        # Rotate the image
        pb = np.rot90(image, rotation // 90).astype('uint16')

        # Mask and shift the 888 RGB into 565 RGB
        red   = (pb[..., [0]] & 0xf8) << 8
        green = (pb[..., [1]] & 0xfc) << 3
        blue  = (pb[..., [2]] & 0xf8) >> 3

        # Stick 'em together
        result = red | green | blue

        # Output the raw bytes
        return result.byteswap().tobytes()

if __name__ == "__main__":
  import sys
  import os
  try:
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont
  except:
    os.system("sudo pip install Pillow")
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont
  MESSAGE = "You are my sunshine, my only "
  print("""
  scrolling-test.py - Display scrolling text.

  You r using test driver testing firm
  """)
  disp = atST7796S(
      width=480,
      height=320,
      rotation=180,
      port=4,
      cs=1,
      dc=22,
      spi_speed_hz=20 * 1000 * 1000,
      invert=False,
      offset_left=0,
      offset_top=0
   )
  # Initialize display.
  disp.begin()

  WIDTH = disp.width
  HEIGHT = disp.height

  image_file = "../image/deployrainbows.gif"
  # Load an image.
  print('Loading gif: {}...'.format(image_file))
  image = Image.open(image_file)

  print('Drawing gif, press Ctrl+C to exit!')

  frame = 0

  while True:
      try:
          image.seek(frame)
          disp.display(image.resize((WIDTH, HEIGHT)))
          frame += 1
          # time.sleep(0.01)

      except EOFError:
          frame = 0