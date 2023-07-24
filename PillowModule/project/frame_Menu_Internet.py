from templates.Layout1 import Layout1
from templates.Menu import Menu
from frame_Menu_Internet_4GLTE import FrameMenuInternet4GLTE
from frame_Menu_Internet_Ethernet import FrameMenuInternetEthernet
from frame_Menu_Internet_OpenVPN import FrameMenuInternetOpenVPN
from frame_Menu_Internet_Wifi import FrameMenuInternetWifi

class FrameMenuInternet:
    ACTION_OK = "enter"
    ACTION_BACK = "left"
    ACTION_HELP = "0"
    ACTION_UP = "up"
    ACTION_DOWN = "down"

    INTERNET_4GLTE = 0
    INTERNET_ETHERNET = 1
    INTERNET_OPENVPN = 2
    INTERNET_WIFI = 3

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
        self.menu = Menu(self, title="Internet")
        self.init()

    def init(self):
        self.menu.set_title(
            center_x=FrameMenuInternet.TITLE_CENTER_X,
            center_y=FrameMenuInternet.TITLE_CENTER_Y)
        self.menu.set_distance_between_cursor_and_element(FrameMenuInternet.DISTANCE_BETWEEN_CURSOR_AND_ELEMENT)
        self.menu.set_distance_between_elements(FrameMenuInternet.DISTANCE_BETWEEN_ELEMENTS)
        self.menu.set_first_element_position(
            pos_x=FrameMenuInternet.FIRST_ELEMENT_POS_X,
            pos_y=FrameMenuInternet.FIRST_ELEMENT_POS_Y)
        self.menu.set_element_height(FrameMenuInternet.ELEMENT_HEIGHT)
        self.add_menu_element("Ethernet")
        self.add_menu_element("Wifi")
        self.add_menu_element("OpenVPN")
        self.add_menu_element("4g LTE")

    def event_handling(self, event):
        if event == FrameMenuInternet.ACTION_BACK:
            self.hmi_screen.pop_frame()
        elif event == FrameMenuInternet.ACTION_UP:
            self.menu.event_handling(event)
        elif event == FrameMenuInternet.ACTION_DOWN:
            self.menu.event_handling(event)
        elif event == FrameMenuInternet.ACTION_HELP:
            pass
        elif event == FrameMenuInternet.ACTION_OK:
            self.ok_event()

    def ok_event(self):
        if self.menu.cursor == FrameMenuInternet.INTERNET_4GLTE:
            frame = FrameMenuInternet4GLTE(self.hmi_screen)
        elif self.menu.cursor == FrameMenuInternet.INTERNET_ETHERNET:
            frame = FrameMenuInternetEthernet(self.hmi_screen)
        elif self.menu.cursor == FrameMenuInternet.INTERNET_OPENVPN:
            frame = FrameMenuInternetOpenVPN(self.hmi_screen)
        elif self.menu.cursor == FrameMenuInternet.INTERNET_WIFI:
            frame = FrameMenuInternetWifi(self.hmi_screen)
        try:
            frame.set_title(f"Internet.{str(self.menu.get_element())}")
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

    def set_menu_title(self, title):
        self.menu.set_title(title)

    def set_ip(self, ip):
        self.layout.set_ip(ip)

    def set_time(self, time):
        self.layout.set_time(time)

    def add_menu_element(self, element):
        self.menu.add_element(element)

def main():
    frame = FrameMenuInternet("hmi")
    frame.set_ip("192.168.1.21")
    frame.set_time("21:20")
    frame.get_image().show()

if __name__ == "__main__":
    main()