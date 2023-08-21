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

class atFrame_Monitor():
    pointer = 0
    notification = "Notification"
    name = "Menu name"
    conclusion = "Normal"
    objects = {}
    object_info_list =[]

    object_status_list = []
    
    
    font_header = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
    font_detail = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)

    normal_status_color  = (42, 157, 143)
    calib_status_color  = (233, 196, 106)
    error_status_color  = (231, 111, 81)

    #  config for notification
    notification_area = (0,0,240,25)
    notification_area_color = (0,0,0)
    notification_area_outline_color = (0,0,0)
    notification_position = (0, 0)
    notification_color = (200,200,200)

    # config for line 1
    line_1_area = (0,notification_area[3] + 1,240,notification_area[3]+1)
    line_1_area_color = (200,200,200)
    line_1_width = 1

    # config for menu
    menu_area = (0,line_1_area[3] + 1, 240,240)
    menu_area_color = (0,0,0)
    
    # conclusion
    conclusion_position = (0,30)
    conclusion_color = normal_status_color

    object_info_list_position = (40,68)
    submenu_between_margin = 30
    submenu_max_per_page = 6

    # config pointer
    pointer_area = (5,72,30,93)
    pointer_active_color    = (255,57,70)
    pointer_inactive_color  = (50,50,50)
    pointer_outline_color   = (255,255,255)


    # function 
    _BACK_FUNCTION = None
    _OK_FUNCTION = None
    _F1_FUNCTION = None
    _F3_FUNCTION = None
    _F2_FUNCTION = None
    _F4_FUNCTION = None

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

    def __init__(self, name, object_dict) -> None:
        # init context
        self.name = name
        self.objects = object_dict
        self._import_object_dict()

        # # draw notification
        # self.draw.text(
        #     self.notification_position, 
        #     self.notification, 
        #     font=self.font_detail,
        #     fill= self.notification_color
        #     )
        # self.draw.line(
        #     self.line_1_area, 
        #     width= self.line_1_width,
        #     fill=self.line_1_area_color
        # )

        # # # draw conclusion of menu
        # self.draw.text(
        #     xy  =self.conclusion_position,    
        #     text=self.conclusion,
        #     fill=self.conclusion_color,
        #     font=self.font_header)

        # # draw options
        # count = 0
        # for option in self.object_info_list:
        #     self.draw.text(
        #         (   
        #             self.object_info_list_position[0], 
        #             count*self.submenu_between_margin + self.object_info_list_position[1]
        #         ), 
        #         option, 
        #         font=self.font_detail
        #     )
        #     count +=1
        
        #  init event for keyboard
        self._BACK_FUNCTION = self._back_callback_default
        self._OK_FUNCTION   = self._ok_callback_default
        self._F1_FUNCTION   = self._f1_callback_default
        self._F2_FUNCTION   = self._f2_callback_default
        self._F3_FUNCTION   = self._f3_callback_default
        self._F4_FUNCTION   = self._f4_callback_default
        
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

    def _import_object_dict(self) :
        # print(object_dict)
        # generate object list
        self.object_info_list = []
        for object in self.objects:
            object_infor = str(object)[:4] + " : " + self.objects[object]["Infor"]
            self.object_info_list.append(object_infor)            
        # print(self.object_info_list)
        # generate status list
        self.object_status_list = []
        for object in self.objects:
            object_status = self.objects[object]["Status"]
            self.object_status_list.append(object_status)
        # print(self.object_status_list)

    def set_objects(self, objects = None):
        
        if not objects == None:
            self.objects = objects
            self._import_object_dict
            self.set_pointer(self.pointer)
    
    def _set_conclusion(self, conclusion):
        self.conclusion = conclusion
        if self.conclusion == "Normal":
            self.conclusion_color = self.normal_status_color
        if self.conclusion == "Calib":
            self.conclusion_color = self.calib_status_color
        if self.conclusion == "Error":
            self.conclusion_color = self.error_status_color
        # self._set_display_objects()
        self.update()

    def _update_conclusion(self):
        # check if error
        for object in self.objects:
            if self.objects[object]["Status"] == "Error":
                self._set_conclusion("Error")
                return
        #  check if calib
        for object in self.objects:
            if self.objects[object]["Status"] == "Calib":
                self._set_conclusion("Calib")
                return

        self._set_conclusion("Normal")
        
    def _set_display_objects(self):
        # clear the old menu
        self.draw.rectangle(self.menu_area, outline=(0, 0, 0), fill=self.menu_area_color)
        # draw conclusion
        self.draw.text(
            xy  =self.conclusion_position,    
            text=self.conclusion,
            fill=self.conclusion_color,
            font=self.font_header)
        # draw options
        page_of_display_objects = self.pointer // self.submenu_max_per_page
        for submenu_index in range (page_of_display_objects * self.submenu_max_per_page , self.get_objects_length()):
            # break if end of menu list
            if submenu_index == self.get_objects_length() :
                break
            # break if end of page
            if submenu_index == (page_of_display_objects +1)*self.submenu_max_per_page:
                break
            self.draw.text(
                (   
                    self.object_info_list_position[0], 
                    (submenu_index % self.submenu_max_per_page)*self.submenu_between_margin + self.object_info_list_position[1]
                ), 
                self.object_info_list[submenu_index], 
                font=self.font_detail
            )
        pass
        
    def get_chosen_submenu(self):
        return self.object_info_list[self.pointer]

    def get_objects_length(self):
        return len(self.object_info_list)

    def get_objects(self):
        return self.objects

    def set_pointer(self,position = 1):
        self.pointer = position
        # go to page of pointer
        self._update_conclusion()
        self._set_display_objects()
        # go to pointer
        page_of_display_objects = self.pointer // self.submenu_max_per_page

        for pointer in range(page_of_display_objects * self.submenu_max_per_page , self.get_objects_length()):
            # break if end of menu list
            if pointer == self.get_objects_length() :
                break
            # break if end of page
            if pointer == (page_of_display_objects +1)*self.submenu_max_per_page:
                break
            if  pointer == position:
                if self.object_status_list[pointer] == "Normal":
                    self.pointer_active_color = self.normal_status_color
                if self.object_status_list[pointer] == "Calib":
                    self.pointer_active_color = self.calib_status_color
                if self.object_status_list[pointer] == "Error":
                    self.pointer_active_color = self.error_status_color

                self.draw.rectangle(
                    (
                        self.pointer_area[0], 
                        (pointer % self.submenu_max_per_page)*self.submenu_between_margin + self.pointer_area[1] , 
                        self.pointer_area[2], 
                        (pointer % self.submenu_max_per_page)*self.submenu_between_margin + self.pointer_area[3]
                    ), 
                    outline= self.pointer_outline_color, 
                    fill=    self.pointer_active_color
                )
            else:
                if self.object_status_list[pointer] == "Normal":
                    self.pointer_inactive_color = self.normal_status_color
                if self.object_status_list[pointer] == "Calib":
                    self.pointer_inactive_color = self.calib_status_color
                if self.object_status_list[pointer] == "Error":
                    self.pointer_inactive_color = self.error_status_color
                self.draw.rectangle(
                    (
                        self.pointer_area[0], 
                        (pointer % self.submenu_max_per_page)*self.submenu_between_margin + self.pointer_area[1] , 
                        self.pointer_area[2], 
                        (pointer % self.submenu_max_per_page)*self.submenu_between_margin + self.pointer_area[3]
                    ), 
                    # outline=self.pointer_outline_color, 
                    fill=   self.pointer_inactive_color)
        
        self.set_notification(self.notification)
        
        
    def get_pointer(self):
        return self.pointer

    def update(self):
        self.disp.display(self.img)
        
    # callback function for keyboard
    def button_Up_callback(self):
        print("[Event]: frame " + self.name + ": button Up function executed")
        pointer = self.get_pointer()
        pointer -= 1
        if pointer < 0:
            pointer = self.get_objects_length() - 1
        self.set_pointer(pointer)
        self.update()    
    def button_Down_callback(self):
        print("[Event]: frame " + self.name + ": button Down function executed")
        pointer = self.get_pointer()
        pointer += 1
        if pointer == self.get_objects_length():
            pointer = 0
        self.set_pointer(pointer)
        self.update()
    def button_Back_callback(self):
        print("[Event]: frame " + self.name + ": button Back function executed")
        
        self._BACK_FUNCTION()
        pass
    def button_OK_callback(self):
        print("[Event]: frame " + self.name + ": button OK function executed")
        self._OK_FUNCTION()
        pass
    def button_F1_callback(self):
        print("[Event]: frame " + self.name + ": button F1 function executed")
        self._F1_FUNCTION()
        pass
    def button_F2_callback(self):
        print("[Event]: frame " + self.name + ": button F2 function executed")
        self._F2_FUNCTION()
        pass
    def button_F3_callback(self):
        print("[Event]: frame " + self.name + ": button F3 function executed")
        self._F3_FUNCTION()
        pass
    def button_F4_callback(self):
        print("[Event]: frame " + self.name + ": button F4 function executed")
        self._F4_FUNCTION()
        pass

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
    def set_Back_callback(self, callback_function):
        '''
        set the callback function will be call when the Back button is pushed
        - callback_function : name of the function
        '''
        self._BACK_FUNCTION = callback_function
    def set_OK_callback(self, callback_function):
        '''
        set the callback function will be call when the OK button is pushed
        - callback_function : name of the function
        '''
        self._OK_FUNCTION = callback_function
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
        if  self.keyboard.get_SW(self.keyboard.BT_SW1) == False :
            while self.keyboard.get_SW(self.keyboard.BT_SW1) == False:
                pass
            self.button_F1_callback()

        if  self.keyboard.get_SW(self.keyboard.BT_SW2) == False :
            while self.keyboard.get_SW(self.keyboard.BT_SW2)== False:
                pass
            self.button_F2_callback()

        if  self.keyboard.get_SW(self.keyboard.BT_SW3) == False :
            while self.keyboard.get_SW(self.keyboard.BT_SW3)== False:
                pass
            self.button_F3_callback()

        if  self.keyboard.get_SW(self.keyboard.BT_SW4) == False :
            while self.keyboard.get_SW(self.keyboard.BT_SW4)== False:
                pass
            self.button_F4_callback()

        if  self.keyboard.get_SW(self.keyboard.BT_SW_Back) == False :
            while self.keyboard.get_SW(self.keyboard.BT_SW_Back)== False:
                pass
            self.button_Back_callback()

        if  self.keyboard.get_SW(self.keyboard.BT_SW_OK) == False :
            while self.keyboard.get_SW(self.keyboard.BT_SW_OK)== False:
                pass
            self.button_OK_callback()

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
            # else:
                

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
            # else:
                
        # update notification
        if atData.data["Notification"]["Update"] == 1:
            self.set_notification(str(atData.data["Notification"]["Info"]))
            atData.data["Notification"]["Update"] = 0
            sleep(1)
        else:
            self.notification = str(atData.data["Notification"]["Info"])


if __name__ == "__main__":
    # class atFrame_Detail
    objects = {
        "FTP": {
            "Status" : "Normal",
            "Infor" : "Connecting"
        },
        "Temperature": {
            "Status" : "Normal",
            "Infor" : "37.5 oC"
        },
        "Pressure": {
            "Status" : "Calib",
            "Infor" : "1.2 atm"
        },
        "H2S": {
            "Status" : "Error",
            "Infor" : "100 ppm"
        },
        "CH4": {
            "Status" : "Normal",
            "Infor" : "20%"
        },
        "Flow": {
            "Status" : "Normal",
            "Infor" : "20 m3/h"
        },
        "Volt": {
            "Status" : "Normal",
            "Infor" : "220 V"
        },
        "Curr": {
            "Status" : "Normal",
            "Infor" : "1200 A"
        },   
    }
    frame = atFrame_Monitor(
        "Menu",
        objects
    )

    frame.set_notification("No thing to see")

    count = 1
    frame.set_pointer(0)
    frame.set_objects(objects=objects)
    while True:
        frame.polling_button()
        sleep(0.01)