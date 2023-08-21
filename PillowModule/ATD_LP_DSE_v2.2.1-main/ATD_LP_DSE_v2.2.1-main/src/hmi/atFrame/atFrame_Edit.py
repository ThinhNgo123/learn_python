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
class atFrame_Edit():
    pointer = 0
    notification = "Notification"
    name = "Editing Object "
    detail ="editing object detail"
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

    def __init__(self, name, detail = None,edit_mode = "String") -> None:
        '''
        - edit_mode : in the liter ["String","Number"]
        '''
        self.name = name
        self.detail = detail
        self._editing_mode = edit_mode
        
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
        # self.draw.text(
        #     xy  = self.detail_position,
        #     text= self.detail,
        #     fill= self.detail_color,
        #     font= self.font_detail
        # )
        
        #  init event for keyboard
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
        # self.update()

    def set_detail(self,detail):
        self.detail = detail
        self.draw.rectangle(
            xy      =self.detail_area, 
            outline =self.detail_area_outline_color, 
            fill    =self.detail_area_color
        )
        self.draw.text(
            xy  =self.detail_position, 
            text=self.detail, 
            font=self.font_detail,
            fill=self.detail_color
            )
        self.update()

    def get_pointer(self):
        return self.pointer

    def set_pointer(self,position = 1):
        # update pointer
        self.pointer = position
        # rend new editing detail
        self._editing_detail = ""\
            + self.detail[:self.pointer] \
            + "{" \
            + self.detail[self.pointer] \
            + "}" \
            + self.detail[self.pointer+1 :] 
        
        # auto line down
        if len(self._editing_detail) > self._number_letter_per_line:
            for count in range (1,len(self._editing_detail) // self._number_letter_per_line +1):
                self._editing_detail = "" \
                    + self._editing_detail[:count*self._number_letter_per_line]\
                    + "\n"\
                    + self._editing_detail[count*self._number_letter_per_line:]\
            
        # delete the old name
        self.set_name(self.name)
        # delete old detail

        self.draw.rectangle(
            xy      =self.detail_area, 
            outline =self.detail_area_outline_color, 
            fill    =self.detail_area_color
        )

        self.draw.rectangle
        # draw editing pointer detail
        self.draw.text(
            xy  = self.detail_position,
            text= self._editing_detail,
            fill= self.detail_color,
            font= self.font_detail
        )

        self.set_notification(self.notification)
        
    def get_pointer(self):
        return self.pointer

    def update(self):
        self.disp.display(self.img)
        
    # callback function for keyboard
    def button_Up_callback(self):
        print("[Event]: frame " + self.name + ": button Up function executed")
        if self._editing_mode == "Number":
            number = 0
            number_str = self.detail[self.pointer]
            if number_str ==".":
                number = 10
            elif number_str =="-":
                number = 11
            else:
                try :
                    number = int(number_str)
                except:
                    number = 0

            number +=1
            if number >11:
                number = 0
            
            if number == 10:
                number_str = "."
            elif  number == 11:
                number_str = "-"
            else:
                number_str = str(number)
        # String mode
        if self._editing_mode == "String":
            number_str = self.detail[self.pointer]

            number = ord(number_str) + 1
    
            if number >ord("~"):
                number = ord(" ")
            number_str = chr(number)
        self.detail = ""\
            + self.detail[:self.pointer] \
            + number_str \
            + self.detail[self.pointer+1 :]

        print(self.detail)
        self.set_pointer(self.pointer)
        # update screen
        self.update()
    
    def button_Down_callback(self):
        print("[Event]: frame " + self.name + ": button Down function executed")
        # Number mode
        if self._editing_mode == "Number":
            number = 0
            number_str = self.detail[self.pointer]
            if number_str ==".":
                number = 10
            elif number_str =="-":
                number = 11
            else:
                try :
                    number = int(number_str)
                except:
                    number = 0

            number -=1
            if number <0:
                number = 11
            
            if number == 10:
                number_str = "."
            elif  number == 11:
                number_str = "-"
            else:
                number_str = str(number)
        # String mode
        if self._editing_mode == "String":
            number_str = self.detail[self.pointer]

            number = ord(number_str) -1
    
            if number <ord(" "):
                number = ord("~")
            number_str = chr(number)

        self.detail = ""\
            + self.detail[:self.pointer] \
            + number_str \
            + self.detail[self.pointer+1 :]

        self.set_pointer(self.pointer)
        print(self.detail)

    def button_Back_callback(self):
        print("[Event]: frame " + self.name + ": button Back function executed")
        print(self._editing_detail)
        pointer = self.get_pointer()
        pointer -= 1
        if pointer < 0:
            pointer = len(self.detail) - 1
        self.set_pointer(pointer)
        self.update()
        pass
    
    def button_OK_callback(self):
        print("[Event]: frame " + self.name + ": button OK function executed")
        pointer = self.get_pointer()
        pointer += 1
        if pointer == len(self.detail):
            pointer = 0
        self.set_pointer(pointer)
        self.update()
        pass
    
    def button_F1_callback(self):
        print("[Event]: frame " + self.name + ": button F1 function executed")
        self._F1_FUNCTION()
        
        
    
    def button_F2_callback(self):
        print("[Event]: frame " + self.name + ": button F2 function executed")
        if len(self.detail) != self.pointer+1 :
            self.detail = \
                self.detail[:self.pointer] + \
                "_" + \
                self.detail[self.pointer:]
            self.set_pointer(self.pointer)
        else :
            self.detail += "_"
            self.set_pointer(len(self.detail)-1)

        self.set_pointer(self.pointer)
    
    def button_F3_callback(self):
        print("[Event]: frame " + self.name + ": button F3 function executed")
        
        if len(self.detail) > 1:
            if len(self.detail) != self.pointer+1 :
                self.detail = \
                    self.detail[:self.pointer] + \
                    self.detail[self.pointer+1:]
                self.set_pointer(self.pointer)
            else :
                self.detail = \
                    self.detail[:len(self.detail) - 1] 
                self.set_pointer(self.pointer-1)
    
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
            # else:
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
            pass
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
    frame = atFrame_Edit(
        name="Number",
        detail="0",
        edit_mode="Number"
    )
    
    frame.set_pointer(frame.pointer)
    while True:
        frame.polling_button()