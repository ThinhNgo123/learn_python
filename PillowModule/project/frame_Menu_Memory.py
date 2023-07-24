from templates.Layout1 import Layout1
from templates.Menu import Menu, MenuEdit

class FrameMenuMemory:
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

    FIRST_EDIT_POS_X = 164
    FIRST_EDIT_POS_Y = 75

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = Layout1()
        self.field = Menu(self)
        self.field.set_title(title="Memory" ,center_x=FrameMenuMemory.TITLE_CENTER_X, center_y=FrameMenuMemory.TITLE_CENTER_Y)
        self.field.set_first_element_position(FrameMenuMemory.FIRST_FIELD_POS_X, FrameMenuMemory.FIRST_FIELD_POS_Y)
        self.edit = MenuEdit(self)
        self.edit.set_first_element_position(FrameMenuMemory.FIRST_EDIT_POS_X, FrameMenuMemory.FIRST_EDIT_POS_Y)
        self.edit_status = False
        self.field_name = [
            "Disk",
            "USB1",
            "USB2",
            "USB3",
            "USB4",
            "USB5"
        ]
        for field in self.field_name:
            self.field.add_element(field)
        
        #test
        self.edit.add_element("edit", "5.21 GiB / 64 GiB")
        self.edit.add_element("edit", "None")
        self.edit.add_element("edit", "None")
        self.edit.add_element("edit", "None")
        self.edit.add_element("edit", "None")
        self.edit.add_element("edit", "None")
        
    def set_title(self, title):
        self.field.set_title(title)

    def draw(self):
        element = self.field.get_element()
        self.layout.set_content(element[element.find(".") + 1:])
        self.layout.draw()
        self.field.draw()
        self.edit.draw()
        
    def event_handling(self, event):
        if event == FrameMenuMemory.ACTION_UP:
            if not self.edit_status:
                self.field.event_handling("up")
            self.edit.event_handling("up")
        elif event == FrameMenuMemory.ACTION_DOWN:
            if not self.edit_status:
                self.field.event_handling("down")
            self.edit.event_handling("down")
        elif event == FrameMenuMemory.ACTION_BACK:
            if self.edit_status:
                self.edit.set_edit_status(False)
                self.edit_status = False
            else:
                self.hmi_screen.pop_frame()
        elif event == FrameMenuMemory.ACTION_OK:
            if len(self.edit.pages):
                if self.edit.get_element().get_type() == "none":
                    print("frame menu sensor protocol detail")
                elif not self.edit_status:
                    self.edit_status = True
                    self.edit.set_edit_status(True)
        elif self.edit_status:
            if event == FrameMenuMemory.ACTION_DELETE:
                self.edit.event_handling("delete")
            else:
                self.edit.event_handling(event)

    def get_image(self):
        self.draw()
        return self.layout.get_image()

def main():
    test = FrameMenuMemory("hmi")
    test.draw()
    test.get_image().show()

if __name__ == "__main__":
    main()