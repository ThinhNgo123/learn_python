from templates.Layout1 import Layout1
from templates.Menu import Menu
from frame_Help import FrameHelp
from window_Alert import WindowAlert

class FrameMenuDevelop:
    ACTION_OK = "enter"
    ACTION_BACK = "left"
    ACTION_HELP = "f2"
    ACTION_UP = "up"
    ACTION_DOWN = "down"
    TITLE_CENTER_X = 239
    TITLE_CENTER_Y = 44
    FIRST_ELEMENT_POS_X = 52
    FIRST_ELEMENT_POS_Y = 75
    ELEMENT_HEIGHT = 29
    DISTANCE_BETWEEN_ELEMENTS = 0
    DISTANCE_BETWEEN_CURSOR_AND_ELEMENT = 9

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = Layout1()
        self.menu = Menu(self, title="Develop")
        self.init()
        self.alert = WindowAlert(self, text="The upper limit is lower than the lower limit")

    def init(self):
        self.menu.set_title(
            center_x=FrameMenuDevelop.TITLE_CENTER_X,
            center_y=FrameMenuDevelop.TITLE_CENTER_Y)
        self.menu.set_distance_between_cursor_and_element(FrameMenuDevelop.DISTANCE_BETWEEN_CURSOR_AND_ELEMENT)
        self.menu.set_distance_between_elements(FrameMenuDevelop.DISTANCE_BETWEEN_ELEMENTS)
        self.menu.set_first_element_position(
            pos_x=FrameMenuDevelop.FIRST_ELEMENT_POS_X,
            pos_y=FrameMenuDevelop.FIRST_ELEMENT_POS_Y)
        self.menu.set_element_height(FrameMenuDevelop.ELEMENT_HEIGHT)
        self.add_menu_element("This function is developping")


    def event_handling(self, event):
        if event == FrameMenuDevelop.ACTION_BACK:
            self.hmi_screen.pop_frame()
        elif event == FrameMenuDevelop.ACTION_UP:
            self.menu.event_handling(event)
        elif event == FrameMenuDevelop.ACTION_DOWN:
            self.menu.event_handling(event)
        elif event == FrameMenuDevelop.ACTION_HELP:
            frame = FrameHelp(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif event == FrameMenuDevelop.ACTION_OK:
            if self.alert.get_show_status():
                self.alert.event_handling(FrameMenuDevelop.ACTION_OK)
            else:
                self.alert.show()

    def draw(self):
        self.layout.draw()
        self.menu.draw()
        #test
        self.alert.draw(480//2,320//2)

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
    frame = FrameMenuDevelop("hmi")
    frame.set_ip("192.168.1.21")
    frame.set_time("21:20")
    frame.get_image().show()

if __name__ == "__main__":
    main()