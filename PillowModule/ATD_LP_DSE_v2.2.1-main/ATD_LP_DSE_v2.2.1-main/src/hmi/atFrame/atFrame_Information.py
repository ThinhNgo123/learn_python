#!/usr/bin/env python3
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
sys.path.insert(0, 'driver')
from atST7789 import atST7789
from time import sleep
from atKeyboard import atKeyboard
sys.path.insert(0, 'json')
from atJsonData import atData
class atFrame_Information():
    pointer = 0
    notification = "Notification"
    name = "Editing Object "
    detail ="editing object detail"
    image_url = "image/ATLab_QR_180x180.jpg"
    pointer = 0
    tutorial = "Tutorial, Up to increase, down to decrease, OK to next or add new letter"


    font_header = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 25)
    font_detail = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)

    #  config for notification
    notification_area = (0,0,240,25)
    notification_area_color = (0,0,0)
    notification_area_outline_color = (0,0,0)
    notification_position = (0, 0)
    notification_color = (200,200,200)

    # config for line 1
    line_1_area = (0,26,240,26)
    line_1_area_color = (200,200,200)
    line_1_width = 1

    # config for name
    name_area = (0,27, 240,70)
    name_area_color = (0,0,0)
    name_area_outline_color = (0,0,0)
    name_position = (0,30)
    name_color = (167, 201, 87)
    
    #  config for detail
    # _editing_mode = "Number" #
    _editing_mode = "String" #
    _editing_detail = detail
    _number_letter_per_line = 14
    detail_area                 = (0,71,240,240)
    detail_area_color           = (50,50,50)
    detail_area_outline_color   = (100,100,100)
    detail_position             = (5,70)
    detail_color                = (255,255,255)
    detail_outline_color        = (0,0,0)

    image_position = (15,30)

    # function 
    _BACK_FUNCTION  = None
    _UP_FUNCTION    = None
    _DOWN_FUNCTION  = None
    _OK_FUNCTION    = None
    _F1_FUNCTION    = None
    _F3_FUNCTION    = None
    _F2_FUNCTION    = None
    _F4_FUNCTION    = None

    # Create ST7789 LCD display class.
    disp = atST7789(
        width= 240,
        height= 240,
        port=1,
        cs=24,
        dc=18,
        )
    # create a keyboard 

    keyboard = atKeyboard()
    keyboard_long_press_time = 2 #second
    # Initialize display.
    disp.begin()
    img = Image.new('RGB', (disp._width, disp._height), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    def __init__(self, name, detail =None,image_url=None) -> None:
        self.name = name
        self.detail = detail
        self.image_url = image_url

        # # draw notification
        # self.draw.text(
        #     self.notification_position, 
        #     self.notification, 
        #     font=self.font_detail,
        #     fill= self.notification_color
        #     )
        
        # # draw the line
        # self.draw.line(
        #     self.line_1_area, 
        #     width= self.line_1_width,
        #     fill=self.line_1_area_color
        # )

        # # draw name of editing object name
        # self.draw.text(
        #     xy  = self.name_position,    
        #     text= self.name,
        #     fill= self.name_color,
        #     font= self.font_header)

        # # draw editing pointer detail
        # if detail != None:
        #     self.draw.text(
        #         xy  =self.detail_position, 
        #         text=self.detail, 
        #         font=self.font_detail,
        #         fill=self.detail_color
        #     )

        # if image_url != None:
        #     image_QR = Image.open(self.image_url)
        #     self.img.paste(image_QR,self.image_position)

        #  init event for keyboard
        self._UP_FUNCTION = self._back_callback_default
        self._DOWN_FUNCTION = self._back_callback_default
        self._BACK_FUNCTION = self._back_callback_default
        self._OK_FUNCTION   = self._ok_callback_default
        self._F1_FUNCTION   = self._f1_callback_default
        self._F2_FUNCTION   = self._f2_callback_default
        self._F3_FUNCTION   = self._f3_callback_default
        self._F4_FUNCTION   = self._f4_callback_default
        
        # self.update()

    def set_notification(self,notification):
        self.notification = notification
        self.draw.rectangle(
            self.notification_area, 
            # outline=(0, 0, 0), 
            fill=self.notification_area_color)
        self.draw.text(
            self.notification_position, 
            self.notification, 
            font=self.font_detail,
            fill= self.notification_color
            )
        self.draw.line(
            self.line_1_area, 
            width= self.line_1_width,
            fill=self.line_1_area_color
        )
        self.update()
        pass

    def get_notification(self):
        return self.notification
        
    def set_name(self,name):
        self.name = name
        self.draw.rectangle(
            xy      =self.name_area, 
            outline =self.name_area_outline_color, 
            fill    =self.name_area_color
        )
        self.draw.text(
            xy  =self.name_position, 
            text=self.name, 
            font=self.font_header,
            fill=self.name_color
            )
        self.update()

    def set_information(self,detail= None, image_url= None):
        self.detail = detail
        self.image_url = image_url
        # delete the old information
        self.draw.rectangle(
            xy      =self.detail_area, 
            outline =self.detail_area_outline_color, 
            fill    =self.detail_area_color
        )
        if detail != None:
            self.draw.text(
                xy  =self.detail_position, 
                text=self.detail, 
                font=self.font_detail,
                fill=self.detail_color
            )
        if image_url != None:
            image_QR = Image.open(self.image_url)
            self.img.paste(image_QR,self.image_position)
            
        # self.update()

    def get_pointer(self):
        return self.pointer

    def set_pointer(self,position):
        # for detail information
        if self.detail != None:
            self.set_information(detail=self.detail)
            self.set_notification(self.notification)
            self.set_name(self.name)
        # for image information
        if self.image_url != None:
            self.set_information(image_url=self.image_url)
        # draw to lcd
        self.set_notification(self.notification)

    def update(self):
        self.disp.display(self.img)
        
    # callback function for keyboard
    def button_Up_callback(self):
        print("[Event]: frame " + self.name + ": button Up function executed")
        self._UP_FUNCTION()

    def button_Down_callback(self):
        print("[Event]: frame " + self.name + ": button Down function executed")
        self._DOWN_FUNCTION()

    def button_Back_callback(self):
        print("[Event]: frame " + self.name + ": button Back function executed")
        self._BACK_FUNCTION()
    
    def button_OK_callback(self):
        print("[Event]: frame " + self.name + ": button OK function executed")
        self._OK_FUNCTION()
    
    def button_F1_callback(self):
        print("[Event]: frame " + self.name + ": button F1 function executed")
        self._F1_FUNCTION()
    
    def button_F2_callback(self):
        print("[Event]: frame " + self.name + ": button F2 function executed")
        self._F2_FUNCTION()
    
    def button_F3_callback(self):
        print("[Event]: frame " + self.name + ": button F3 function executed")
        self._F3_FUNCTION()
    
    def button_F4_callback(self):
        print("[Event]: frame " + self.name + ": button F4 function executed")
        self._F4_FUNCTION()

    # default callback functions
    def _back_callback_default(self):
        print("[Event]: frame " + self.name + ": button BACK default callback function executed")
    def _ok_callback_default(self):
        print("[Event]: frame " + self.name + ": button OK default callback function executed")
    def _f1_callback_default(self):
        print("[Event]: frame " + self.name + ": button F1 default callback function executed")
    def _f2_callback_default(self):
        print("[Event]: frame " + self.name + ": button F2 default callback function executed")
    def _f3_callback_default(self):
        print("[Event]: frame " + self.name + ": button F3 default callback function executed")
    def _f4_callback_default(self):
        print("[Event]: frame " + self.name + ": button F4 default callback function executed")
    
    # set callback functions
    def set_F1_callback(self, callback_function):
        '''
        set the callback function will be call when the F1 button is pushed
        - callback_function : name of the function
        '''
        self._F1_FUNCTION = callback_function
    def set_F2_callback(self, callback_function):
        '''
        set the callback function will be call when the F2 button is pushed
        - callback_function : name of the function
        '''
        self._F2_FUNCTION = callback_function
    def set_F3_callback(self, callback_function):
        '''
        set the callback function will be call when the F3 button is pushed
        - callback_function : name of the function
        '''
        self._F3_FUNCTION = callback_function
    def set_F4_callback(self, callback_function):
        '''
        set the callback function will be call when the F4 button is pushed
        - callback_function : name of the function
        '''
        self._F4_FUNCTION = callback_function
    def set_Up_callback(self, callback_function):
        '''
        set the callback function will be call when the F4 button is pushed
        - callback_function : name of the function
        '''
        self._UP_FUNCTION = callback_function
    def set_Down_callback(self, callback_function):
        '''
        set the callback function will be call when the F4 button is pushed
        - callback_function : name of the function
        '''
        self._DOWN_FUNCTION = callback_function
    def set_Back_callback(self, callback_function):
        '''
        set the callback function will be call when the F4 button is pushed
        - callback_function : name of the function
        '''
        self._BACK_FUNCTION = callback_function
    def set_OK_callback(self, callback_function):
        '''
        set the callback function will be call when the F4 button is pushed
        - callback_function : name of the function
        '''
        self._OK_FUNCTION = callback_function

    def polling_button(self):
        '''
        call this frequently to poll button and execute event
        '''
        # F1 button
        if  self.keyboard.get_SW(self.keyboard.BT_SW1) == False :                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
            count = 0
            long_press = None
            self.button_F1_callback()
            while self.keyboard.get_SW(self.keyboard.BT_SW1)== False:
                sleep(0.01)
                count += 0.01
                if count > self.keyboard_long_press_time:
                    long_press = True
                    break
            if long_press :
                while self.keyboard.get_SW(self.keyboard.BT_SW1)== False:
                    self.button_F1_callback()
        # F2 button
        if  self.keyboard.get_SW(self.keyboard.BT_SW2) == False :
            self.button_F2_callback()
            while self.keyboard.get_SW(self.keyboard.BT_SW2)== False:
                pass
        # F3 button
        if  self.keyboard.get_SW(self.keyboard.BT_SW3) == False :
            self.button_F3_callback()
            while self.keyboard.get_SW(self.keyboard.BT_SW3)== False:
                pass
        # F4 button
        if  self.keyboard.get_SW(self.keyboard.BT_SW4) == False :
            count = 0
            long_press = None
            self.button_F4_callback()    
            while self.keyboard.get_SW(self.keyboard.BT_SW4)== False:
                sleep(0.01)
                count += 0.01
                if count > self.keyboard_long_press_time:
                    long_press = True
                    break
            if long_press :
                while self.keyboard.get_SW(self.keyboard.BT_SW4)== False:
                    self.button_F4_callback()
        # back button
        if  self.keyboard.get_SW(self.keyboard.BT_SW_Back) == False :
            count = 0
            long_press = None
            self.button_Back_callback()
            while self.keyboard.get_SW(self.keyboard.BT_SW_Back)== False:
                sleep(0.01)
                count += 0.01
                if count > self.keyboard_long_press_time:
                    long_press = True
                    break
            if long_press :
                while self.keyboard.get_SW(self.keyboard.BT_SW_Back)== False:
                    self.button_Back_callback()
        # ok button
        if  self.keyboard.get_SW(self.keyboard.BT_SW_OK) == False :
            count = 0
            long_press = None
            self.button_OK_callback()
            while self.keyboard.get_SW(self.keyboard.BT_SW_OK)== False:
                sleep(0.01)
                count += 0.01
                if count > self.keyboard_long_press_time:
                    long_press = True
                    break
            if long_press :
                while self.keyboard.get_SW(self.keyboard.BT_SW_OK)== False:
                    self.button_OK_callback()
        #  up button
        if  self.keyboard.get_SW(self.keyboard.BT_SW_Up) == False :
            count = 0
            long_press = None
            self.button_Up_callback()
            while self.keyboard.get_SW(self.keyboard.BT_SW_Up)== False:
                sleep(0.01)
                count += 0.01
                if count > self.keyboard_long_press_time:
                    long_press = True
                    break
            if long_press :
                while self.keyboard.get_SW(self.keyboard.BT_SW_Up)== False:
                    self.button_Up_callback()
        # down button
        if  self.keyboard.get_SW(self.keyboard.BT_SW_Down) == False :
            count = 0
            long_press = None
            self.button_Down_callback()
            while self.keyboard.get_SW(self.keyboard.BT_SW_Down)== False:
                sleep(0.01)
                count += 0.01
                if count > self.keyboard_long_press_time:
                    long_press = True
                    break

            if long_press :
                while self.keyboard.get_SW(self.keyboard.BT_SW_Down)== False:
                    self.button_Down_callback()
        
        # update notification
        if atData.data["Notification"]["Update"] == 1:
            self.set_notification(str(atData.data["Notification"]["Info"]))
            atData.data["Notification"]["Update"] = 0
            sleep(1)
        else:
            self.notification = str(atData.data["Notification"]["Info"])
    


if __name__ == "__main__":
    # class atFrame_Detail
    frame = atFrame_Information(
        name="About",
        image_url="image/ATLab_QR_240x240.jpg"
    )
    