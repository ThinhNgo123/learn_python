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
class atFrame_Login():
    pointer = 0
    notification = "Notification"
    name = "Login"

    editing_object = "User name"
    
    password ="editing object password"
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
    name_area = (0,27, 240,69)
    name_area_color = (0,0,0)
    name_area_outline_color = (0,0,0)
    name_position = (0,30)
    name_color = (167, 201, 87)

    # config for user name header
    user_name_header = "User Name :"
    user_name_header_area = (0,70, 240,99)
    user_name_header_area_color = (0,0,0)
    user_name_header_area_outline_color = (0,0,0)
    user_name_header_position = (0,70)
    user_name_header_color = (233, 196, 106)

    # config for user name
    user_name = "User1"
    user_name_area = (0,100, 240,150)
    user_name_area_color = (50,50,50)
    user_name_area_outline_color = (0,0,0)
    user_name_position = (0,100)
    user_name_color = (255, 255, 255)

    # config for password header
    password_header = "Password :"
    password_header_area = (0,150, 240,180)
    password_header_area_color = (0,0,0)
    password_header_area_outline_color = (0,0,0)
    password_header_position = (0,150)
    password_header_color = (233, 196, 106)

    
    #  config for password

    password = "Password"
    password_area                 = (0,180,240,240)
    password_area_color           = (50,50,50)
    password_area_outline_color   = (100,100,100)
    password_position             = (5,180)
    password_color                = (255,255,255)
    password_outline_color        = (0,0,0)

    # _editing_mode = "Number" #
    _editing_mode = "String" #
    _editing_pointer = "User Name"
    editing_object = None
    _editing_object = None
    _number_letter_per_line = 14


    # function 
    _BACK_FUNCTION  = None
    _BACK_LONG_PRESS_FUNCTION    = None
    _UP_FUNCTION    = None
    _DOWN_FUNCTION  = None
    _OK_FUNCTION    = None
    _OK_LONG_PRESS_FUNCTION    = None
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

    def __init__(self, name, user_name ,password,edit_mode = "String") -> None:
        '''
        - edit_mode : in the liter ["String","Number]
        '''
        self.name = name
        self.password = password
        self.user_name = user_name
        self._editing_mode = edit_mode

        self.editing_object = self.user_name

        # draw notification
        self.draw.text(
            self.notification_position, 
            self.notification, 
            font=self.font_detail,
            fill= self.notification_color
            )
        
        # draw the line
        self.draw.line(
            self.line_1_area, 
            width= self.line_1_width,
            fill=self.line_1_area_color
        )

        # draw name of editing object name
        self.draw.text(
            xy  = self.name_position,    
            text= self.name,
            fill= self.name_color,
            font= self.font_header)

        # draw user name header:
        self.draw.text(
            xy  = self.user_name_header_position,    
            text= self.user_name_header,
            fill= self.user_name_header_color,
            font= self.font_detail)

        # draw user name:
        self.draw.text(
            xy  = self.user_name_position,    
            text= self.user_name,
            fill= self.user_name_color,
            font= self.font_detail)

        # draw password header:
        self.draw.text(
            xy  = self.password_header_position,    
            text= self.password_header,
            fill= self.password_header_color,
            font= self.font_detail)
        
        # draw password:
        self.draw.text(
            xy  = self.password_position,    
            text= self.password,
            fill= self.password_color,
            font= self.font_detail)

        # draw editing pointer password
        self.draw.text(
            xy  = self.password_position,
            text= self.password,
            fill= self.password_color,
            font= self.font_detail
        )
        
        #  init event for keyboard
        self._F4_FUNCTION   = self._f4_callback_default
        self._OK_LONG_PRESS_FUNCTION = self._ok_long_press_callback_default
        self._BACK_LONG_PRESS_FUNCTION = self._back_long_press_callback_default
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
        
    def set_user_name_header(self):
        # draw user name header:
        self.draw.rectangle(
            xy      =self.user_name_header_area, 
            outline =self.user_name_header_area_outline_color, 
            fill    =self.user_name_header_area_color
        )
        self.draw.text(
            xy  = self.user_name_header_position,    
            text= self.user_name_header,
            fill= self.user_name_header_color,
            font= self.font_detail)

    def set_user_name(self,user_name):
        self.user_name = user_name
        self.draw.rectangle(
            xy      =self.user_name_area, 
            outline =self.user_name_area_outline_color, 
            fill    =self.user_name_area_color
        )
        self.draw.text(
            xy  =self.user_name_position, 
            text=self.user_name, 
            font=self.font_detail,
            fill=self.user_name_color
            )

    def set_password_header(self):
        # draw password header:
        self.draw.rectangle(
            xy      =self.password_header_area, 
            outline =self.password_header_area_outline_color, 
            fill    =self.password_header_area_color
        )
        self.draw.text(
            xy  = self.password_header_position,    
            text= self.password_header,
            fill= self.password_header_color,
            font= self.font_detail)
        
    def set_password(self,password):
        self.password = password
        self.draw.rectangle(
            xy      =self.password_area, 
            outline =self.password_area_outline_color, 
            fill    =self.password_area_color
        )
        self.draw.text(
            xy  =self.password_position, 
            text=self.password, 
            font=self.font_detail,
            fill=self.password_color
            )

    def get_pointer(self):
        return self.pointer

    def set_pointer(self,position = 1):
        # update pointer
        self.pointer = position
        # rend new editing password
        self._editing_object = ""\
            + self.editing_object[:self.pointer] \
            + "{" \
            + self.editing_object[self.pointer] \
            + "}" \
            + self.editing_object[self.pointer+1 :] 
        
        # auto line down
        if len(self._editing_object) > self._number_letter_per_line:
            for count in range (1,len(self._editing_object) // self._number_letter_per_line +1):
                self._editing_object = "" \
                    + self._editing_object[:count*self._number_letter_per_line]\
                    + "\n"\
                    + self._editing_object[count*self._number_letter_per_line:]\

        if self._editing_pointer == "Password":
            self.password = self._editing_object

        if self._editing_pointer == "User Name":
            self.user_name = self._editing_object
        

        # delete the old name
        self.set_name(self.name)
        # delete the old user name header
        self.set_user_name_header()
        self.set_user_name(self.user_name)
        self.set_password_header()
        self.set_password(self.password)

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
            number_str = self.editing_object[self.pointer]
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
            number_str = self.editing_object[self.pointer]

            number = ord(number_str) + 1
    
            if number >ord("~"):
                number = ord(" ")
            number_str = chr(number)

        self.editing_object = ""\
            + self.editing_object[:self.pointer] \
            + number_str \
            + self.editing_object[self.pointer+1 :]

        print(self.password)
        self.set_pointer(self.pointer)
        # update screen
        self.update()
    
    def button_Down_callback(self):
        print("[Event]: frame " + self.name + ": button Down function executed")
        # Number mode
        if self._editing_mode == "Number":
            number = 0
            number_str = self.editing_object[self.pointer]
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
            number_str = self.editing_object[self.pointer]

            number = ord(number_str) -1
    
            if number <ord(" "):
                number = ord("~")
            number_str = chr(number)

        self.editing_object = ""\
            + self.editing_object[:self.pointer] \
            + number_str \
            + self.editing_object[self.pointer+1 :]

        self.set_pointer(self.pointer)
        print(self.editing_object)

    def button_Back_callback(self):
        print("[Event]: frame " + self.name + ": button Back function executed")
        print(self._editing_object)
        pointer = self.get_pointer()
        pointer -= 1
        if pointer < 0:
            pointer = len(self.editing_object) - 1
        self.set_pointer(pointer)
        self.update()
        pass
    
    def button_OK_callback(self):
        print("[Event]: frame " + self.name + ": button OK function executed")
        pointer = self.get_pointer()
        pointer += 1
        if pointer == len(self.editing_object):
            pointer = 0
        self.set_pointer(pointer)
        self.update()
        pass

    def button_OK_long_press_callback(self):
        print("[Event]: frame " + self.name + ": button OK long press function executed")
        self.set_pointer(self.pointer)
        self.pointer = 0

        if self._editing_pointer == "User Name":
            # save user name
            self.user_name = self.editing_object

        elif self._editing_pointer == "Password":
            # save password
            self.password = self.editing_object

        print("Save infor and login with user/password: " +  self.user_name + "/" + self.password)  

        self._OK_LONG_PRESS_FUNCTION()
        pass
    
    def button_F1_callback(self):
        print("[Event]: frame " + self.name + ": button F1 function executed")
        if self._editing_pointer == "User Name":
            self._editing_pointer = "Password"
            # save user name
            self.user_name = self.editing_object
            # load password to editing object
            self.editing_object = self.password

        elif self._editing_pointer == "Password":
            self._editing_pointer = "User Name"
            # save password
            self.password = self.editing_object
            # load user name to editing object
            self.editing_object = self.user_name

        self.pointer = 0
        print("Set editing pointer to " + self._editing_pointer)
        self.set_pointer(self.pointer)

    def button_F2_callback(self):
        print("[Event]: frame " + self.name + ": button F2 function executed")
        if len(self.editing_object) != self.pointer+1 :
            self.editing_object = \
                self.editing_object[:self.pointer] + \
                "_" + \
                self.editing_object[self.pointer:]
            self.set_pointer(self.pointer)
        else :
            self.editing_object += "_"
            self.set_pointer(len(self.editing_object)-1)

        self.set_pointer(self.pointer)
    
    def button_F3_callback(self):
        print("[Event]: frame " + self.name + ": button F3 function executed")
        
        if len(self.editing_object) > 1:
            if len(self.editing_object) != self.pointer+1 :
                self.editing_object = \
                    self.editing_object[:self.pointer] + \
                    self.editing_object[self.pointer+1:]
                self.set_pointer(self.pointer)
            else :
                self.editing_object = \
                    self.editing_object[:len(self.editing_object) - 1] 
                self.set_pointer(self.pointer-1)
    
    def button_F4_callback(self):
        print("[Event]: frame " + self.name + ": button F4 function executed")
        self._F4_FUNCTION()

    def button_BACK_long_press_callback(self):
        print("[Event]: frame " + self.name + ": button F4 function executed")
        self._BACK_LONG_PRESS_FUNCTION()

    # default callback functions
    def _ok_long_press_callback_default(self):
        print("[Event]: frame " + self.name + ": button OK long press default callback function executed")
    def _back_long_press_callback_default(self):
        print("[Event]: frame " + self.name + ": button Back long press default callback function executed")
    def _f4_callback_default(self):
        print("[Event]: frame " + self.name + ": button F4 default callback function executed")

    # set callback functions
    def set_F4_callback(self, callback_function):
        '''
        set the callback function will be call when the F4 button is pushed
        - callback_function : name of the function
        '''
        self._F4_FUNCTION = callback_function
    def set_OK_long_press_callback(self, callback_function):
        '''
        set the callback function will be call when the F4 button is pushed
        - callback_function : name of the function
        '''
        self._OK_LONG_PRESS_FUNCTION = callback_function
    def set_BACK_long_press_callback(self, callback_function):
        '''
        set the callback function will be call when the F4 button is pushed
        - callback_function : name of the function
        '''
        self._BACK_LONG_PRESS_FUNCTION = callback_function
    

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
                self.button_BACK_long_press_callback()
                while self.keyboard.get_SW(self.keyboard.BT_SW_Back)== False:
                    pass
            
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
                self.button_OK_long_press_callback()
                while self.keyboard.get_SW(self.keyboard.BT_SW_OK)== False:
                    pass
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
    # class atFrame_password
    frame = atFrame_Login(
        name="Login",
        user_name="_User2_",
        password="_Password2_",
        edit_mode="String"
    )
    def exit():
        print("F4 function")
    def login():
        print("log in with user name:" + frame.user_name + "   password:" + frame.password)
    frame.set_F4_callback(
        lambda: exit()
    )
    frame.set_OK_long_press_callback(
        lambda: login()
    )
    frame.set_pointer(frame.pointer)
    while True:
        frame.polling_button()