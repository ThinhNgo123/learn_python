from templates.Layout1 import Layout1
from templates.Menu import Menu

class FrameMenuPower:
    ACTION_OK = "enter"
    ACTION_BACK = "left"
    ACTION_HELP = "0"
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
        if event == FrameMenuPower.ACTION_BACK:
            self.hmi_screen.pop_frame()
        elif event == FrameMenuPower.ACTION_UP:
            self.menu.event_handling(event)
        elif event == FrameMenuPower.ACTION_DOWN:
            self.menu.event_handling(event)
        elif event == FrameMenuPower.ACTION_HELP:
            pass
        elif event == FrameMenuPower.ACTION_OK:
            print(self.menu.get_element())

    def draw(self):
        element = self.menu.get_element()
        self.layout.set_content(element[element.find(".") + 1:])
        self.layout.draw()
        self.menu.draw()

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

def main():
    frame = FrameMenuPower("hmi")
    frame.set_ip("192.168.1.21")
    frame.set_time("21:20")
    frame.get_image().show()

if __name__ == "__main__":
    main()