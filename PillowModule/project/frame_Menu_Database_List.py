from templates.Layout1 import Layout1
from templates.Menu import Menu

class FrameMenuDatabaseList:
    ACTION_OK = "enter"
    ACTION_BACK = "left"
    ACTION_HELP = "0"
    ACTION_UP = "up"
    ACTION_DOWN = "down"
    TITLE_CENTER_X = 239
    TITLE_CENTER_Y = 44
    FIRST_ELEMENT_POS_X = 54
    FIRST_ELEMENT_POS_Y = 75
    ELEMENT_HEIGHT = 26
    DISTANCE_BETWEEN_ELEMENTS = 0
    DISTANCE_BETWEEN_CURSOR_AND_ELEMENT = 7

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = Layout1()
        self.menu = Menu(self, title="Database.Data List")
        self.init()

        #test
        self.add_menu_element("1.Temperature")
        self.add_menu_element("2.CO2")
        self.add_menu_element("3.Flow")
        self.add_menu_element('4.Flow2')
        self.add_menu_element("5.Humidity")
        self.add_menu_element("6.Humidity")
        self.add_menu_element("7.NH4")
        self.add_menu_element("8.Dirty")
        self.add_menu_element("9.Dirty")
        self.add_menu_element("10.Dirty")
        self.add_menu_element("11.Dirty")
        self.add_menu_element("12.Dirty")

    def init(self):
        self.menu.set_title(
            center_x=FrameMenuDatabaseList.TITLE_CENTER_X,
            center_y=FrameMenuDatabaseList.TITLE_CENTER_Y)
        self.menu.set_distance_between_cursor_and_element(FrameMenuDatabaseList.DISTANCE_BETWEEN_CURSOR_AND_ELEMENT)
        self.menu.set_distance_between_elements(FrameMenuDatabaseList.DISTANCE_BETWEEN_ELEMENTS)
        self.menu.set_first_element_position(
            pos_x=FrameMenuDatabaseList.FIRST_ELEMENT_POS_X,
            pos_y=FrameMenuDatabaseList.FIRST_ELEMENT_POS_Y)
        self.menu.set_element_height(FrameMenuDatabaseList.ELEMENT_HEIGHT)

    def event_handling(self, event):
        if event == FrameMenuDatabaseList.ACTION_BACK:
            self.hmi_screen.pop_frame()
        elif event == FrameMenuDatabaseList.ACTION_UP:
            self.menu.event_handling(event)
        elif event == FrameMenuDatabaseList.ACTION_DOWN:
            self.menu.event_handling(event)
        elif event == FrameMenuDatabaseList.ACTION_HELP:
            pass
        elif event == FrameMenuDatabaseList.ACTION_OK:
            pass

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
    frame = FrameMenuDatabaseList("hmi")
    frame.set_ip("192.168.1.21")
    frame.set_time("21:20")
    frame.get_image().show()

if __name__ == "__main__":
    main()