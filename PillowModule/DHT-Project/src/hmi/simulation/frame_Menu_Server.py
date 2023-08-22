from templates.Layout2 import Layout2
from templates.Column_chart import ColumnChart
from templates.Menu import Menu
from frame_Menu_Server_Edit import FrameMenuServerEdit
from frame_Help import FrameHelp

class FrameMenuServer:
    ACTION_UP = "up"
    ACTION_DOWN = "down"
    ACTION_BACK = "left"
    ACTION_HELP = "f2"
    ACTION_OK = "enter"

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = Layout2()
        self.column_chart = ColumnChart(self, title="Brief")
        self.menu = Menu(self, title="Server")

        #test
        self.add_column_chart(32, "C")
        self.add_column_chart(10, "E")
        self.add_column_chart(20, "D")
        self.add_menu_element("1.FTP 1")
        self.add_menu_element("2.FTP 2")

    def draw(self):
        element = self.menu.get_element()
        self.layout.set_content(element[element.find(".") + 1:])
        self.layout.draw()
        self.column_chart.draw()
        self.menu.draw()

    def event_handling(self, event):
        if event == FrameMenuServer.ACTION_UP:
            self.menu.event_handling(event)
        elif event == FrameMenuServer.ACTION_DOWN:
            self.menu.event_handling(event)
        elif event == FrameMenuServer.ACTION_OK:
            frame = FrameMenuServerEdit(self.hmi_screen)
            frame.set_title(self.menu.get_element())
            self.hmi_screen.push_frame(frame)
        elif event == FrameMenuServer.ACTION_HELP:
            frame = FrameHelp(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif event == FrameMenuServer.ACTION_BACK:
            self.back_event()

    def back_event(self):
        self.hmi_screen.pop_frame()

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
    frame = FrameMenuServer("hmi")
    frame.set_ip("192.168.1.21")
    frame.set_time("21:20")
    frame.add_column_chart(32, "C")
    frame.add_column_chart(10, "E")
    frame.add_column_chart(20, "D")
    frame.add_menu_element("1.FTP 1")
    frame.add_menu_element("2.FTP 2")
    frame.draw()
    frame.layout.background.show()

if __name__ == "__main__":
    main()