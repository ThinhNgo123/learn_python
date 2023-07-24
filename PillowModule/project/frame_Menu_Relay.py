from templates.Layout2 import Layout2
from templates.Column_chart import ColumnChart
from templates.Menu import Menu
from frame_Menu_Relay_Edit import FrameMenuRelayEdit

class FrameMenuRelay:
    ACTION_UP = "up"
    ACTION_DOWN = "down"
    ACTION_BACK = "left"
    ACTION_HELP = "0"
    ACTION_OK = "enter"

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = Layout2()
        self.column_chart = ColumnChart(self, title="Brief")
        self.menu = Menu(self, title="Relay")
        self.add_menu_element("1.Pump")
        self.add_menu_element("2.Fan")
        self.add_menu_element("3.Fan-2")
        self.add_column_chart(32, "N")
        self.add_column_chart(10, "E")
        self.add_column_chart(20, "D")

    def draw(self):
        element = self.menu.get_element()
        self.layout.set_content(element[element.find(".") + 1:])
        self.layout.draw()
        self.column_chart.draw()
        self.menu.draw()

    def event_handling(self, event):
        if event == FrameMenuRelay.ACTION_UP:
            self.menu.event_handling(event)
        elif event == FrameMenuRelay.ACTION_DOWN:
            self.menu.event_handling(event)
        elif event == FrameMenuRelay.ACTION_OK:
            frame = FrameMenuRelayEdit(self.hmi_screen)
            frame.set_title(self.menu.get_element())
            self.hmi_screen.push_frame(frame)
        elif event == FrameMenuRelay.ACTION_HELP:
            self.help_event()
        elif event == FrameMenuRelay.ACTION_BACK:
            self.hmi_screen.pop_frame()

    def help_event(self):
        pass

    def get_image(self):
        self.draw()
        return self.layout.get_image()

    def add_column_chart(self, number: int, text: str):
        self.column_chart.add_column(number, text)

    def add_menu_element(self, element: str):
        self.menu.add_element(element)

    def set_ip(self, ip):
        self.layout.set_ip(ip)

    def set_time(self, time):
        self.layout.set_time(time)

    def set_menu_title(self, title):
        self.menu.set_title(title)

    def set_column_chart_title(self, title):
        self.column_chart.set_title(title)

def main():
    frame = FrameMenuRelay("hmi")
    frame.set_ip("192.168.1.21")
    frame.set_time("21:20")
    frame.add_column_chart(32, "N")
    frame.add_column_chart(10, "E")
    frame.add_column_chart(20, "D")
    frame.add_menu_element("1.Pump")
    frame.add_menu_element("2.Fan")
    frame.add_menu_element("3.Fan-2")
    frame.draw()
    frame.layout.background.show()

if __name__ == "__main__":
    main()