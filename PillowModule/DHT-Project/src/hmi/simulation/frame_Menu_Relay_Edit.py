from templates.Layout1 import Layout1
from templates.Menu import Menu, MenuEdit
from frame_Menu_Relay_Input_Protocol_Detail import FrameMenuRelayInputProtocolDetail
from frame_Help import FrameHelp

class FrameMenuRelayEdit:
    ACTION_UP = "up"
    ACTION_DOWN = "down"
    ACTION_BACK = "left"
    ACTION_OK = "enter"
    ACTION_DELETE = "delete"
    ACTION_WRITE = "write"
    ACTION_HELP = "f2"

    TITLE_CENTER_X = 239
    TITLE_CENTER_Y = 44

    FIRST_FIELD_POS_X = 53
    FIRST_FIELD_POS_Y = 75

    FIRST_EDIT_POS_X = 253
    FIRST_EDIT_POS_Y = 75

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = Layout1()
        self.field = Menu(self)
        self.field.set_title(center_x=FrameMenuRelayEdit.TITLE_CENTER_X, center_y=FrameMenuRelayEdit.TITLE_CENTER_Y)
        self.field.set_first_element_position(FrameMenuRelayEdit.FIRST_FIELD_POS_X, FrameMenuRelayEdit.FIRST_FIELD_POS_Y)
        self.edit = MenuEdit(self)
        self.edit.set_first_element_position(FrameMenuRelayEdit.FIRST_EDIT_POS_X, FrameMenuRelayEdit.FIRST_EDIT_POS_Y)
        self.edit_status = False
        self.field_name = [
            "Name",
            "ID",
            "Status",
            "Value",
            "Input Protocol",
            "Input Protocol Detail",
            "Output Protocol",
        ]
        for field in self.field_name:
            self.field.add_element(field)
        
        #test
        self.edit.add_element("edit", "Pump")
        self.edit.add_element("edit", "1")
        self.edit.add_element("selection", "Normal", "Easy", "Medium", "Hard")
        self.edit.add_element("selection", "On", "Off")
        self.edit.add_element("edit", "MQTT")
        self.edit.add_element("none")
        self.edit.add_element("edit", "Digital Output 1")
        
    def set_title(self, title):
        self.field.set_title(title)

    def draw(self):
        element = self.field.get_element()
        self.layout.set_content(element[element.find(".") + 1:])
        self.layout.draw()
        self.field.draw()
        self.edit.draw()
        
    def event_handling(self, event):
        if event == FrameMenuRelayEdit.ACTION_HELP:
            frame = FrameHelp(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif event == FrameMenuRelayEdit.ACTION_UP:
            if not self.edit_status:
                self.field.event_handling("up")
            self.edit.event_handling("up")
        elif event == FrameMenuRelayEdit.ACTION_DOWN:
            if not self.edit_status:
                self.field.event_handling("down")
            self.edit.event_handling("down")
        elif event == FrameMenuRelayEdit.ACTION_BACK:
            if self.edit_status:
                self.edit.set_edit_status(False)
                self.edit_status = False
            else:
                self.hmi_screen.pop_frame()
        elif event == FrameMenuRelayEdit.ACTION_OK:
            if len(self.edit.pages):
                if self.edit.get_element().get_type() == "none":
                    frame = FrameMenuRelayInputProtocolDetail(self.hmi_screen)
                    frame.set_title(f"{self.field.title}.Input Protocol Detail")
                    self.hmi_screen.push_frame(frame)
                elif not self.edit_status:
                    self.edit_status = True
                    self.edit.set_edit_status(True)
        elif self.edit_status:
            if event == FrameMenuRelayEdit.ACTION_DELETE:
                self.edit.event_handling("delete")
            else:
                self.edit.event_handling(event)

    def get_image(self):
        self.draw()
        return self.layout.get_image()

def main():
    test = FrameMenuRelayEdit("hmi")
    test.draw()
    test.get_image().show()

if __name__ == "__main__":
    main()