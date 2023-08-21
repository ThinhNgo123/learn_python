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
class atFrame_Menu():
    pointer = 0
    notification = "Notification"
    name = "Menu name"
    menu_list =["option 1",
                "option 2",
                "option 3",
                "option 4",
                "option 5",
                "option 6",
                "option 7",
                "option 8",
                "option 9",
                "option 10",
                "option 11",
                "option 12",
                "option 13",
                "option 14",
                "option 15"]

    font_header = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 25)
    font_detail = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)

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
    name_position = (0,30)
    name_color = (167, 201, 87)
    menu_list_position = (40,68)
    submenu_between_margin = 30
    submenu_max_per_page = 6

    # config pointer
    pointer_area = (5,72,30,93)
    pointer_active_color    = (255,57,70)
    pointer_inactive_color  = (50,50,50)
    pointer_outline_color   = (1,1,1)


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

    def __init__(self, name, list=None) -> None:
        # init context
        self.name = name
        self.menu_list = list

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

        # # draw name of menu
        # self.draw.text(
        #     xy  =self.name_position,    
        #     text=self.name,
        #     fill=self.name_color,
        #     font=self.font_header)

        # # draw options
        # count = 0
        # for option in self.menu_list:
        #     self.draw.text(
        #         (   
        #             self.menu_list_position[0], 
        #             count*self.submenu_between_margin + self.menu_list_position[1]
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

    def set_menu(self,name = None,list=None):
        if not name == None:
            self.name = name
        if not list == None:
            self.menu_list = list
        self.set_pointer(self.pointer)

    def _set_display_menu(self):
        # clear the old menu
        self.draw.rectangle(self.menu_area, outline=(0, 0, 0), fill=self.menu_area_color)
        # draw name of menu
        self.draw.text(
            xy  =self.name_position,    
            text=self.name,
            fill=self.name_color,
            font=self.font_header)
        # draw options
        page_of_display_menu = self.pointer // self.submenu_max_per_page
        for submenu_index in range (page_of_display_menu * self.submenu_max_per_page , self.get_menu_length()):
            # break if end of menu list
            if submenu_index == self.get_menu_length() :
                break
            # break if end of page
            if submenu_index == (page_of_display_menu +1)*self.submenu_max_per_page:
                break
            try:
                self.draw.text(
                    (   
                        self.menu_list_position[0], 
                        (submenu_index % self.submenu_max_per_page)*self.submenu_between_margin + self.menu_list_position[1]
                    ), 
                    self.menu_list[submenu_index], 
                    font=self.font_detail
                )
            except Exception as error:
                print(error)
        pass
        
    def get_chosen_submenu(self):
        return self.menu_list[self.pointer]

    def get_menu_length(self):
        return len(self.menu_list)

    def get_menu(self):
        menu = {"name":self.name,
                "list":self.menu_list}
        return menu

    def  set_pointer(self,position = 1):
        self.pointer = position
        # go to page of pointer
        self._set_display_menu()
        # go to pointer
        page_of_display_menu = self.pointer // self.submenu_max_per_page
        for pointer in range(page_of_display_menu * self.submenu_max_per_page , self.get_menu_length()):
            # break if end of menu list
            if pointer == self.get_menu_length() :
                break
            # break if end of page
            if pointer == (page_of_display_menu +1)*self.submenu_max_per_page:
                break
            if  pointer == position:
                self.draw.rectangle(
                    (
                        self.pointer_area[0], 
                        (pointer % self.submenu_max_per_page)*self.submenu_between_margin + self.pointer_area[1] , 
                        self.pointer_area[2], 
                        (pointer % self.submenu_max_per_page)*self.submenu_between_margin + self.pointer_area[3]
                    ), 
                    outline= self.pointer_outline_color, 
                    fill=    self.pointer_active_color)
            else:
                self.draw.rectangle(
                    (
                        self.pointer_area[0], 
                        (pointer % self.submenu_max_per_page)*self.submenu_between_margin + self.pointer_area[1] , 
                        self.pointer_area[2], 
                        (pointer % self.submenu_max_per_page)*self.submenu_between_margin + self.pointer_area[3]
                    ), 
                    outline=self.pointer_outline_color, 
                    fill=   self.pointer_inactive_color)
        self.set_notification(self.notification)
        # self.update() 
        

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
            pointer = self.get_menu_length() - 1
        self.set_pointer(pointer)
        self.update()    
    def button_Down_callback(self):
        print("[Event]: frame " + self.name + ": button Down function executed")
        pointer = self.get_pointer()
        pointer += 1
        if pointer >= self.get_menu_length():
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
            self.button_F1_callback()
            while self.keyboard.get_SW(self.keyboard.BT_SW1) == False:
                pass

        if  self.keyboard.get_SW(self.keyboard.BT_SW2) == False :
            self.button_F2_callback()
            while self.keyboard.get_SW(self.keyboard.BT_SW2)== False:
                pass

        if  self.keyboard.get_SW(self.keyboard.BT_SW3) == False :
            self.button_F3_callback()
            while self.keyboard.get_SW(self.keyboard.BT_SW3)== False:
                pass

        if  self.keyboard.get_SW(self.keyboard.BT_SW4) == False :
            self.button_F4_callback()
            while self.keyboard.get_SW(self.keyboard.BT_SW4)== False:
                pass

        if  self.keyboard.get_SW(self.keyboard.BT_SW_Back) == False :
            self.button_Back_callback()
            while self.keyboard.get_SW(self.keyboard.BT_SW_Back)== False:
                pass

        if  self.keyboard.get_SW(self.keyboard.BT_SW_OK) == False :
            self.button_OK_callback()
            while self.keyboard.get_SW(self.keyboard.BT_SW_OK)== False:
                pass

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
    frame = atFrame_Menu(
        "Menu",
        [   
            "Option 1",
            "Option 2",
            "Option 3",
            "Option 4",
            "Option 5",
            "Option 6",
            "Option 7",
            "Option 8",
            "Option 9",
            "Option 10",
        ]
    )

    def F1():
        print("F1")
    def F2():
        print("F2")
    def F3():
        print("F3")
    def F4():
        print("F4")
    def Back():
        print("Back")
    def OK():
        print("OK")

    frame.set_Back_callback(Back)
    frame.set_OK_callback(OK)
    frame.set_F1_callback(F1)
    frame.set_F2_callback(F2)
    frame.set_F3_callback(F3)
    frame.set_F4_callback(F4)

    frame.set_notification("No thing to see")
    print(frame.get_menu())

    count = 1
    frame.set_pointer(0)
    while True:
        frame.polling_button()
        sleep(0.01)