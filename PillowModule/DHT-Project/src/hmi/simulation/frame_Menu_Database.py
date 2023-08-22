from templates.Layout1 import Layout1
from templates.Menu import Menu
from frame_Menu_Database_List import FrameMenuDatabaseList
from frame_Menu_Database_Config import FrameMenuDatabaseConfig
from frame_Help import FrameHelp

class FrameMenuDatabase:
    ACTION_OK = "enter"
    ACTION_BACK = "left"
    ACTION_HELP = "f2"
    ACTION_UP = "up"
    ACTION_DOWN = "down"
    DATA_LIST = 0
    CONFIG = 1
    TITLE_CENTER_X = 239
    TITLE_CENTER_Y = 44
    FIRST_ELEMENT_POS_X = 50
    FIRST_ELEMENT_POS_Y = 74
    ELEMENT_HEIGHT = 29
    DISTANCE_BETWEEN_ELEMENTS = 1
    DISTANCE_BETWEEN_CURSOR_AND_ELEMENT = 7

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = Layout1()
        self.menu = Menu(self, title="Database")
        self.init()

    def init(self):
        self.menu.set_title(
            center_x=FrameMenuDatabase.TITLE_CENTER_X,
            center_y=FrameMenuDatabase.TITLE_CENTER_Y)
        self.menu.set_distance_between_cursor_and_element(FrameMenuDatabase.DISTANCE_BETWEEN_CURSOR_AND_ELEMENT)
        self.menu.set_distance_between_elements(FrameMenuDatabase.DISTANCE_BETWEEN_ELEMENTS)
        self.menu.set_first_element_position(
            pos_x=FrameMenuDatabase.FIRST_ELEMENT_POS_X,
            pos_y=FrameMenuDatabase.FIRST_ELEMENT_POS_Y)
        self.menu.set_element_height(FrameMenuDatabase.ELEMENT_HEIGHT)
        self.menu.add_element("Data list")
        self.menu.add_element("Config")

    def event_handling(self, event):
        if event == FrameMenuDatabase.ACTION_BACK:
            self.hmi_screen.pop_frame()
        elif event == FrameMenuDatabase.ACTION_UP:
            self.menu.event_handling(event)
        elif event == FrameMenuDatabase.ACTION_DOWN:
            self.menu.event_handling(event)
        elif event == FrameMenuDatabase.ACTION_HELP:
            frame = FrameHelp(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif event == FrameMenuDatabase.ACTION_OK:
            self.ok_event()

    def ok_event(self):
        if self.menu.cursor == FrameMenuDatabase.DATA_LIST:
            frame = FrameMenuDatabaseList(self.hmi_screen)
        elif self.menu.cursor == FrameMenuDatabase.CONFIG:
            frame = FrameMenuDatabaseConfig(self.hmi_screen)
        try:
            frame.set_title(f"Database.{str(self.menu.get_element())}")
            self.hmi_screen.push_frame(frame)
        except:
            print("error")

    def draw(self):
        element = self.menu.get_element()
        self.layout.set_content(element[element.find(".") + 1:])
        self.layout.draw()
        self.menu.draw()

    def get_image(self):
        self.draw()
        return self.layout.get_image()

    def set_title(self, title):
        self.menu.set_title(title)

    def set_ip(self, ip):
        self.layout.set_ip(ip)

    def set_time(self, time):
        self.layout.set_time(time)

    def add_menu_element(self, element):
        self.menu.add_element(element)

def main():
    frame = FrameMenuDatabase("hmi")
    frame.set_ip("192.168.1.21")
    frame.set_time("21:20")
    frame.get_image().show()

if __name__ == "__main__":
    main()