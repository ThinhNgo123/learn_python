from templates.Layout1 import Layout1
from templates.Menu import Menu
from frame_Help import FrameHelp
from window_Information import WindowInformation

class FrameMenuBackup:
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
    DISTANCE_BETWEEN_ELEMENTS = 0
    DISTANCE_BETWEEN_CURSOR_AND_ELEMENT = 11

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = Layout1()
        self.menu = Menu(self, title="Back Up")
        self.init()
        self.add_menu_element("Save \"Setting\" to USB")
        self.add_menu_element("Save \"Data\" to USB")
        self.window_information = WindowInformation(self)

    def init(self):
        self.menu.set_title(
            center_x=FrameMenuBackup.TITLE_CENTER_X,
            center_y=FrameMenuBackup.TITLE_CENTER_Y)
        self.menu.set_distance_between_cursor_and_element(FrameMenuBackup.DISTANCE_BETWEEN_CURSOR_AND_ELEMENT)
        self.menu.set_distance_between_elements(FrameMenuBackup.DISTANCE_BETWEEN_ELEMENTS)
        self.menu.set_first_element_position(
            pos_x=FrameMenuBackup.FIRST_ELEMENT_POS_X,
            pos_y=FrameMenuBackup.FIRST_ELEMENT_POS_Y)
        self.menu.set_element_height(FrameMenuBackup.ELEMENT_HEIGHT)

    def event_handling(self, event):
        if event == FrameMenuBackup.ACTION_BACK:
            self.hmi_screen.pop_frame()
        elif event == FrameMenuBackup.ACTION_UP:
            self.menu.event_handling(event)
        elif event == FrameMenuBackup.ACTION_DOWN:
            self.menu.event_handling(event)
        elif event == FrameMenuBackup.ACTION_HELP:
            frame = FrameHelp(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif event == FrameMenuBackup.ACTION_OK:
            element = self.menu.get_element()
            if element == "Save \"Setting\" to USB":
                self.window_information.set_text("Saved setting")
                self.window_information.show()
            elif element == "Save \"Data\" to USB":
                self.window_information.set_text("Saved data")
                self.window_information.show()

    def draw(self):
        element = self.menu.get_element()
        self.layout.set_content(element[element.find(".") + 1:])
        self.layout.draw()
        self.menu.draw()
        #test
        self.window_information.draw(480 // 2, 320 // 2)

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
    frame = FrameMenuBackup("hmi")
    frame.set_ip("192.168.1.21")
    frame.set_time("21:20")
    frame.get_image().show()
    frame.event_handling("enter")
    frame.menu.cursor = 1
    frame.event_handling("enter")

if __name__ == "__main__":
    main()