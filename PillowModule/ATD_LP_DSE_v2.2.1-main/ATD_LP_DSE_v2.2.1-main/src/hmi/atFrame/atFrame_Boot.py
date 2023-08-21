#!/usr/bin/env python3
import sys
import os
from time import sleep
try:
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont
except:
    os.system("sudo pip install Pillow")
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont

sys.path.insert(0, 'driver')
from atST7789 import atST7789
from atKeyboard import atKeyboard

class atFrame_Boot():
    logo_path = "image/Wallpaper_Orangepi_Datalogger_2.jpg"
    name = "Booting frame"
    version_info = "Version information"
    company_name = "ATLab"
    loading_percent = 50 # unit %%
    loading_info = "Installing ..."

    #  version info config
    version_info_area = (0,0,240,25)
    version_info_area_color = (0,0,0)
    version_info_area_outline_color = (0,0,0)
    version_info_position = (0, 0)
    version_info_color = (150,150,150)

    #  company name config
    company_name_area = (0,130,244,209)
    company_name_area_color = (0,0,0)
    company_name_area_outline_color = (0,0,0)
    company_name_position = (55, 140)
    company_name_color = (167, 201, 87)

    # config for loading percentage line
    loading_percent_line_area = (9,199,231,202 )
    loading_percent_line_area_color = (0,0,0)
    loading_percent_line_area_outline_color = (0,0,0)
    loading_percent_line_color = (255,255,255)
    loading_percent_line_width = 5

    #  loading config
    
    loading_info_area = (0,210,240,240)
    loading_info_area_color = (0,0,0)
    loading_info_area_outline_color = (0,0,0)
    loading_info_position = (0, 210)
    loading_info_color = (255,255,255)

    font_header = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 35)
    font_detail = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)

    # Create ST7789 LCD display class.
    disp = atST7789(
        width= 240,
        height= 240,
        port=1,
        cs=24,
        dc=18,
        )
    # Initialize display.
    disp.begin()

    img = Image.open(logo_path)
    draw = ImageDraw.Draw(img)
    # img = img.resize(disp._width,disp._height)

    def __init__(self, name) -> None:
        self.name = name
        # draw version_info
        self.draw.text(
            self.version_info_position, 
            self.version_info, 
            font=self.font_detail,
            fill= self.version_info_color
        )
        # draw company name
        self.draw.text(
            self.company_name_position, 
            self.company_name, 
            font=self.font_header,
            fill= self.company_name_color
        )
        # draw loading_info
        self.draw.text(
            self.loading_info_position, 
            self.loading_info, 
            font=self.font_detail,
            fill= self.loading_info_color,
            align="center"
        )

        self.disp.display(self.img)
        pass

    def set_loading_percent(self, percentage):
        '''
        set the line percentage of loading modules
        '''
        # rebound
        if percentage > 100:
            percentage = 100
        if percentage < 0:
            percentage = 0
            
        # calculate the line length
        self.loading_percent = percentage
        loading_percent_line_area = (
            10,
            200,
            10+ (self.loading_percent*220)//100,
            200 
        )

        # delete the old line
        self.draw.rectangle(
            self.loading_percent_line_area, 
            outline=self.loading_percent_line_area_outline_color, 
            fill=self.loading_percent_line_area_color)

        #  draw the new line
        self.draw.line(
            loading_percent_line_area, 
            width= self.loading_percent_line_width,
            fill=self.loading_percent_line_color
        )

        # update draw to screen
        self.update()

    def set_loading_info(self, loading_information):
        '''
        set the loading information on boot frame
        '''
        self.loading_info = loading_information
        # delete the old loading info
        self.draw.rectangle(
            self.loading_info_area, 
            # outline=(0, 0, 0), 
            fill=self.loading_info_area_color)
        #  draw the new loading info
        self.draw.text(
            self.loading_info_position, 
            self.loading_info, 
            font=self.font_detail,
            fill= self.loading_info_color,
            align="center"
            )
        # update draw to screen
        self.update()
        pass

    def set_version_info(self, version_information):
        '''
        set the version information on boot frame
        '''
        self.version_info = version_information
        # delete the old loading info
        self.draw.rectangle(
            self.version_info_area, 
            # outline=(0, 0, 0), 
            fill=self.version_info_area_color)
        #  draw the new loading info
        self.draw.text(
            self.version_info_position, 
            self.version_info, 
            font=self.font_detail,
            fill= self.version_info_color
            )
        # update draw to screen
        self.update()
        pass

    def update(self):
        self.disp.display(self.img)
        pass

if __name__ == "__main__":
    frame = atFrame_Boot(
        name= "Boot",
    )
    count = 1
    while True:
        count +=1
        frame.set_loading_percent(count)
        frame.set_loading_info(str(count) + "...")
        frame.set_version_info("DOPZ2V2.1")
        sleep(0.05)
    # frame.update()
