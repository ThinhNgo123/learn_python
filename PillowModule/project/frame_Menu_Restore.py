from templates.Layout1 import Layout1
from templates.Menu import Menu

class FrameMenuRestore:
    ACTION_OK = "enter"
    ACTION_BACK = "left"
    ACTION_HELP = "help"
    ACTION_UP = "up"
    ACTION_DOWN = "down"
    TITLE_CENTER_X = 239
    TITLE_CENTER_Y = 44
    FIRST_ELEMENT_POS_X = 54
    FIRST_ELEMENT_POS_Y = 75
    ELEMENT_HEIGHT = 29
    DISTANCE_BETWEEN_ELEMENTS = 0
    DISTANCE_BETWEEN_CURSOR_AND_ELEMENT = 11

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = Layout1()
        self.menu = Menu(self, title="Restore")
        self.init()

    def init(self):
        self.menu.set_title(
            center_x=FrameMenuRestore.TITLE_CENTER_X,
            center_y=FrameMenuRestore.TITLE_CENTER_Y)
        self.menu.set_distance_between_cursor_and_element(FrameMenuRestore.DISTANCE_BETWEEN_CURSOR_AND_ELEMENT)
        self.menu.set_distance_between_elements(FrameMenuRestore.DISTANCE_BETWEEN_ELEMENTS)
        self.menu.set_first_element_position(
            pos_x=FrameMenuRestore.FIRST_ELEMENT_POS_X,
            pos_y=FrameMenuRestore.FIRST_ELEMENT_POS_Y)
        self.menu.set_element_height(FrameMenuRestore.ELEMENT_HEIGHT)
        self.add_menu_element("Default Restore")
        self.add_menu_element("Restore Setting from USB")
        self.add_menu_element("Restore Database from USB")

    def event_handling(self, event):
        if event == FrameMenuRestore.ACTION_BACK:
            self.hmi_screen.pop_frame()
        elif event == FrameMenuRestore.ACTION_UP:
            self.menu.event_handling(event)
        elif event == FrameMenuRestore.ACTION_DOWN:
            self.menu.event_handling(event)
        elif event == FrameMenuRestore.ACTION_HELP:
            pass
        elif event == FrameMenuRestore.ACTION_OK:
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
    frame = FrameMenuRestore("hmi")
    frame.set_ip("192.168.1.21")
    frame.set_time("21:20")
    frame.get_image().show()

if __name__ == "__main__":
    main()