from templates.Layout1 import Layout1
from templates.Menu import Menu
from frame_Help import FrameHelp
from window_Confirm import WindowConfirm

class FrameMenuPower:
    ACTION_OK = "enter"
    ACTION_BACK = "left"
    ACTION_HELP = "f2"
    ACTION_UP = "up"
    ACTION_DOWN = "down"
    TITLE_CENTER_X = 239
    TITLE_CENTER_Y = 44
    FIRST_ELEMENT_POS_X = 54
    FIRST_ELEMENT_POS_Y = 75
    ELEMENT_HEIGHT = 29
    DISTANCE_BETWEEN_ELEMENTS = 1
    DISTANCE_BETWEEN_CURSOR_AND_ELEMENT = 11

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = Layout1()
        self.menu = Menu(self, title="Power")
        self.init()
        self.confirm = WindowConfirm(self)

    def init(self):
        self.menu.set_title(
            center_x=FrameMenuPower.TITLE_CENTER_X,
            center_y=FrameMenuPower.TITLE_CENTER_Y)
        self.menu.set_distance_between_cursor_and_element(FrameMenuPower.DISTANCE_BETWEEN_CURSOR_AND_ELEMENT)
        self.menu.set_distance_between_elements(FrameMenuPower.DISTANCE_BETWEEN_ELEMENTS)
        self.menu.set_first_element_position(
            pos_x=FrameMenuPower.FIRST_ELEMENT_POS_X,
            pos_y=FrameMenuPower.FIRST_ELEMENT_POS_Y)
        self.menu.set_element_height(FrameMenuPower.ELEMENT_HEIGHT)
        self.add_menu_element("Reboot device")
        self.add_menu_element("Shut down")

    def event_handling(self, event):
        if not self.confirm.get_show_status():
            if event == FrameMenuPower.ACTION_BACK:
                self.hmi_screen.pop_frame()
            elif event == FrameMenuPower.ACTION_UP:
                self.menu.event_handling(event)
            elif event == FrameMenuPower.ACTION_DOWN:
                self.menu.event_handling(event)
            elif event == FrameMenuPower.ACTION_HELP:
                frame = FrameHelp(self.hmi_screen)
                self.hmi_screen.push_frame(frame)
            elif event == FrameMenuPower.ACTION_OK:
                element = self.menu.get_element()
                if element == "Reboot device":
                    self.confirm.set_text("Do you want to this thing ?")
                    self.confirm.set_callback(self.reboot_device, ".", ".", ".")
                    self.confirm.show()
                elif element == "Shut down":
                    self.confirm.set_text("Shut down ?")
                    self.confirm.set_callback(self.shut_down)
                    self.confirm.show()
        else:
            self.confirm.event_handling(event)

    def draw(self):
        element = self.menu.get_element()
        self.layout.set_content(element[element.find(".") + 1:])
        self.layout.draw()
        self.menu.draw()
        #test
        self.confirm.draw(480//2, 320//2)

    def get_image(self):
        self.draw()
        return self.layout.get_image()

    def set_menu_title(self, title):
        self.menu.set_title(title)

    def set_ip(self, ip):
        self.layout.set_ip(ip)

    def set_time(self, time):
        self.layout.set_time(time)

    def add_menu_element(self, element):
        self.menu.add_element(element)

    #test
    def reboot_device(self, arg1, arg2, arg3):
        print("Rebooting device" + arg1 + arg2 + arg3)

    def shut_down(self):
        print("Shutting down...")

def main():
    frame = FrameMenuPower("hmi")
    frame.set_ip("192.168.1.21")
    frame.set_time("21:20")
    frame.get_image().show()

if __name__ == "__main__":
    main()