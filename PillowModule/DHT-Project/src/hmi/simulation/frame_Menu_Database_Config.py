from templates.Layout1 import Layout1
from templates.Menu import Menu, MenuEdit
from frame_Help import FrameHelp

class FrameMenuDatabaseConfig:
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

    FIRST_EDIT_POS_X = 182
    FIRST_EDIT_POS_Y = 75

    MAX_CHAR = 19

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = Layout1()
        self.field = Menu(self)
        self.field.set_title(center_x=FrameMenuDatabaseConfig.TITLE_CENTER_X, center_y=FrameMenuDatabaseConfig.TITLE_CENTER_Y)
        self.field.set_first_element_position(FrameMenuDatabaseConfig.FIRST_FIELD_POS_X, FrameMenuDatabaseConfig.FIRST_FIELD_POS_Y)
        self.edit = MenuEdit(self)
        # self.edit.set_max_char(FrameMenuDatabaseConfig.MAX_CHAR)
        self.edit.set_first_element_position(FrameMenuDatabaseConfig.FIRST_EDIT_POS_X, FrameMenuDatabaseConfig.FIRST_EDIT_POS_Y)
        self.edit_status = False
        self.field_name = [
            "url",
            "user",
            "password",
            "org",
            "bucker",
            "token",
        ]
        for field in self.field_name:
            self.field.add_element(field)
        
        #test
        self.edit.add_element("edit", "http://localhost:8086")
        self.edit.add_element("edit", "mtg")
        self.edit.add_element("edit", "abc123123")
        self.edit.add_element("edit", "mtg")
        self.edit.add_element("edit", "mtg")
        self.edit.add_element("edit", "asd" * 18)
        self.edit.pages[0][5].set_max_char(FrameMenuDatabaseConfig.MAX_CHAR)
        
    def set_title(self, title):
        self.field.set_title(title)

    def draw(self):
        element = self.field.get_element()
        self.layout.set_content(element[element.find(".") + 1:])
        self.layout.draw()
        self.field.draw()
        self.edit.draw()
        
    def event_handling(self, event):
        if event == FrameMenuDatabaseConfig.ACTION_HELP:
            frame = FrameHelp(self.hmi_screen)
            self.hmi_screen.push_frame(frame) 
        elif event == FrameMenuDatabaseConfig.ACTION_UP:
            if not self.edit_status:
                self.field.event_handling("up")
            self.edit.event_handling("up")
        elif event == FrameMenuDatabaseConfig.ACTION_DOWN:
            if not self.edit_status:
                self.field.event_handling("down")
            self.edit.event_handling("down")
        elif event == FrameMenuDatabaseConfig.ACTION_BACK:
            if self.edit_status:
                self.edit.set_edit_status(False)
                self.edit_status = False
            else:
                self.hmi_screen.pop_frame()
        elif event == FrameMenuDatabaseConfig.ACTION_OK:
            if len(self.edit.pages):
                if self.edit.get_element().get_type() == "none":
                    print("coming soon")
                elif not self.edit_status:
                    self.edit_status = True
                    self.edit.set_edit_status(True)
        elif self.edit_status:
            if event == FrameMenuDatabaseConfig.ACTION_DELETE:
                self.edit.event_handling("delete")
            else:
                self.edit.event_handling(event)

    def get_image(self):
        self.draw()
        return self.layout.get_image()

def main():
    test = FrameMenuDatabaseConfig("hmi")
    test.get_image().show()

if __name__ == "__main__":
    main()