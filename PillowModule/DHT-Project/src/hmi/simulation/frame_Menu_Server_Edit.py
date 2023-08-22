from templates.Layout1 import Layout1
from templates.Menu import Menu, MenuEdit
from frame_Help import FrameHelp

class FrameMenuServerEdit:
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

    FIRST_EDIT_POS_X = 207
    FIRST_EDIT_POS_Y = 75

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = Layout1()
        self.field = Menu(self)
        self.field.set_title(center_x=FrameMenuServerEdit.TITLE_CENTER_X, center_y=FrameMenuServerEdit.TITLE_CENTER_Y)
        self.field.set_first_element_position(FrameMenuServerEdit.FIRST_FIELD_POS_X, FrameMenuServerEdit.FIRST_FIELD_POS_Y)
        self.edit = MenuEdit(self)
        self.edit.set_first_element_position(FrameMenuServerEdit.FIRST_EDIT_POS_X, FrameMenuServerEdit.FIRST_EDIT_POS_Y)
        self.edit_status = False

        self.field_name = [
            "Name",
            "Status",
            "Type",
            "IP",
            "Port",
            "ID",
            "User",
            "Password",
            "Folder",
            "Send Time",
            "Check Time",
            "File Name",
            "Time Out"
        ]
        for field in self.field_name:
            self.field.add_element(field)

        #test
        self.edit.add_element("edit", "FTP 1")
        self.edit.add_element("edit", "1")
        self.edit.add_element("edit", "Connecting")
        self.edit.add_element("edit", "FTP Server")
        self.edit.add_element("edit", "103.140.42.141")
        self.edit.add_element("edit", "23")
        self.edit.add_element("edit", "test")
        self.edit.add_element("edit", "qttd@123^")
        self.edit.add_element("edit", "/FTP_TEST/BAO_TEST")
        self.edit.add_element("edit", "5 minutes")
        self.edit.add_element("edit", "24 hours")
        self.edit.add_element("edit", "filename")
        self.edit.add_element("edit", "1 seconds")

    def set_title(self, title):
        self.field.set_title(title)

    def draw(self):
        element = self.field.get_element()
        self.layout.set_content(element[element.find(".") + 1:])
        self.layout.draw()
        self.field.draw()
        self.edit.draw()

    def event_handling(self, event):
        if event == FrameMenuServerEdit.ACTION_HELP:
            frame = FrameHelp(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif event == FrameMenuServerEdit.ACTION_UP:
            if not self.edit_status:
                self.field.event_handling("up")
                self.edit.event_handling("up")
        elif event == FrameMenuServerEdit.ACTION_DOWN:
            if not self.edit_status:
                self.field.event_handling("down")
                self.edit.event_handling("down")
        elif event == FrameMenuServerEdit.ACTION_BACK:
            if self.edit_status:
                self.edit.set_edit_status(False)
                self.edit_status = False
            else:
                self.hmi_screen.pop_frame()
        elif event == FrameMenuServerEdit.ACTION_OK:
            if not self.edit_status:
                self.edit_status = True
                self.edit.set_edit_status(True)
        elif self.edit_status:
            if event == FrameMenuServerEdit.ACTION_DELETE:
                self.edit.event_handling("delete")
            else:
                self.edit.event_handling(event)
        

    def get_image(self):
        self.draw()
        return self.layout.get_image()

def main():
    test = FrameMenuServerEdit("hmi")
    test.get_image().show()

if __name__ == "__main__":
    main()