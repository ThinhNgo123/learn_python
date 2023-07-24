from templates.Layout1 import Layout1
from templates.Menu import Menu, MenuEdit

class FrameMenuSensorProtocolDetail:
    ACTION_UP = "up"
    ACTION_DOWN = "down"
    ACTION_BACK = "left"
    ACTION_OK = "enter"
    ACTION_DELETE = "delete"
    ACTION_WRITE = "write"

    TITLE_CENTER_X = 239
    TITLE_CENTER_Y = 44

    FIRST_FIELD_POS_X = 53
    FIRST_FIELD_POS_Y = 75

    FIRST_EDIT_POS_X = 283
    FIRST_EDIT_POS_Y = 75

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = Layout1()
        self.field = Menu(self)
        self.field.set_title(center_x=FrameMenuSensorProtocolDetail.TITLE_CENTER_X, center_y=FrameMenuSensorProtocolDetail.TITLE_CENTER_Y)
        self.field.set_first_element_position(FrameMenuSensorProtocolDetail.FIRST_FIELD_POS_X, FrameMenuSensorProtocolDetail.FIRST_FIELD_POS_Y)
        self.edit = MenuEdit(self)
        self.edit.set_first_element_position(FrameMenuSensorProtocolDetail.FIRST_EDIT_POS_X, FrameMenuSensorProtocolDetail.FIRST_EDIT_POS_Y)
        self.edit_status = False
        self.field_name = [
            "Protocol",
            "Port",
            "Baud rate",
            "Data bits",
            "Stop bit",
            "Parity",
            "ID",
            "Type",
            "Address"
        ]
        for field in self.field_name:
            self.field.add_element(field)
        
        #test
        self.edit.add_element("edit", "Modbus RTU")
        self.edit.add_element("edit", "RS485-1")
        self.edit.add_element("edit", "8")
        self.edit.add_element("edit", "1")
        self.edit.add_element("edit", "even")
        self.edit.add_element("edit", "1")
        self.edit.add_element("edit", "holding")
        self.edit.add_element("edit", "1")
        
    def set_title(self, title):
        self.field.set_title(title)

    def draw(self):
        element = self.field.get_element()
        self.layout.set_content(element[element.find(".") + 1:])
        self.layout.draw()
        self.field.draw()
        self.edit.draw()
        
    def event_handling(self, event):
        if event == FrameMenuSensorProtocolDetail.ACTION_UP:
            if not self.edit_status:
                self.field.event_handling("up")
            self.edit.event_handling("up")
        elif event == FrameMenuSensorProtocolDetail.ACTION_DOWN:
            if not self.edit_status:
                self.field.event_handling("down")
            self.edit.event_handling("down")
        elif event == FrameMenuSensorProtocolDetail.ACTION_BACK:
            if self.edit_status:
                self.edit.set_edit_status(False)
                self.edit_status = False
            else:
                self.hmi_screen.pop_frame()
        elif event == FrameMenuSensorProtocolDetail.ACTION_OK:
            if len(self.edit.pages):
                if self.edit.get_element().get_type() == "none":
                    print("frame menu sensor protocol detail")
                elif not self.edit_status:
                    self.edit_status = True
                    self.edit.set_edit_status(True)
        elif self.edit_status:
            if event == FrameMenuSensorProtocolDetail.ACTION_DELETE:
                self.edit.event_handling("delete")
            else:
                self.edit.event_handling(event)

    def get_image(self):
        self.draw()
        return self.layout.get_image()

def main():
    test = FrameMenuSensorProtocolDetail("hmi")
    test.draw()
    test.get_image().show()

if __name__ == "__main__":
    main()