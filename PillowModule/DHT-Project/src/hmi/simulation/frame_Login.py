from PIL import Image, ImageFont
from templates.Base import BaseImage
from templates.Menu import MenuEdit
from frame_Menu import FrameMenu

RECT_WIDTH = 461
RECT_HEIGHT = 243
RECT_TOP = 44
RECT_LEFT = 10
RECT_RADIUS = 10
RECT_BORDER = 1
RECT_BORDER_COLOR = (0, 95, 115)

LOGO_IMAGE_PATH = "./Image/Logo 1.png"
LOGO_POS_X = 151
LOGO_POS_Y = 56

USERNAME_RECT_LEFT = 65
USERNAME_RECT_TOP = 181
USERNAME_RECT_WIDTH = 362
USERNAME_RECT_HEIGHT = 35
USERNAME_RECT_BORDER_RADIUS = 5
USERNAME_RECT_COLOR = (233, 216, 166)

PASSWORD_RECT_LEFT = 65
PASSWORD_RECT_TOP = 228
PASSWORD_RECT_WIDTH = 362
PASSWORD_RECT_HEIGHT = 35
PASSWORD_RECT_BORDER_RADIUS = 5
PASSWORD_RECT_COLOR = (233, 216, 166)

class FrameLogin:
    ACTION_UP = "up"
    ACTION_DOWN = "down"
    ACTION_LEFT = "left"
    ACTION_RIGHT = "right"
    ACTION_BACK = "f1"
    ACTION_LOGIN = "f2"
    ACTION_ADD_LETTER = "f3"
    ACTION_DELETE_LETTER = "f4"
    ACTION_OK = "enter"
    
    FONT = ImageFont.truetype("./Font/inter/Inter-VariableFont_slnt,wght.ttf", 24)

    SELECTION_DEFAULT = "User name"

    POINTER_POS_X_DEFAULT = 80
    POINTER_POS_Y = (198.5, 245.5)

    COLOR1 = (0, 18, 25)
    COLOR2 = (128, 128, 128)

    USERNAME_POS_X = 220
    USERNAME_POS_Y = 184
    DISTANCE_BETWEEN_ELEMENT = 18

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = BaseImage()
        self.logo_image = Image.open(LOGO_IMAGE_PATH)
        self.selection = FrameLogin.SELECTION_DEFAULT
        self.font = FrameLogin.FONT
        self.login = MenuEdit(self)
        self.init()

    def init(self):
        self.layout.set_left_control("F1:Back")
        self.layout.set_right_control("F2:Login")
        
        self.login.element_color = FrameLogin.COLOR1
        self.login.set_first_element_position(FrameLogin.USERNAME_POS_X, FrameLogin.USERNAME_POS_Y) #184 228
        self.login.set_distance_between_elements(FrameLogin.DISTANCE_BETWEEN_ELEMENT)
        self.login.set_max_row(2)
        self.login.add_element("edit", "_")
        self.login.add_element("edit", "_")
        self.login.set_edit_status(True)

    # def get_current_string_length(self):
    #     if self.selection == "User name":
    #         text = self.login_info["User name"]
    #         if text == "":
    #             return -8 #pointer pos x = (pointer pos x default - 8 / 2) so that the cursor does not stick to the text
    #         else:
    #             return self.font.getlength(text)
    #     elif self.selection == "Password":
    #         text = self.login_info["Password"]
    #         if text == "":
    #             return -8 #pointer pos x = (pointer pos x default - 8 / 2) so that the cursor does not stick to the text
    #         else:
    #             return self.font.getlength("*" * len(text))

    def event_handling(self, event):
        if event == FrameLogin.ACTION_UP:
            self.login.set_up_char()
        elif event == FrameLogin.ACTION_DOWN:
            self.login.set_down_char()
        elif event == FrameLogin.ACTION_BACK:
            self.hmi_screen.pop_frame()
        elif event == FrameLogin.ACTION_RIGHT:
            self.login.next_event()
        elif event == FrameLogin.ACTION_LEFT:
            self.login.back_event()
        elif event == FrameLogin.ACTION_LOGIN:
            if self.get_user_and_pass() == ("admin", "a"):
                frame = FrameMenu(self.hmi_screen)
                self.hmi_screen.push_frame(frame)
        elif event == FrameLogin.ACTION_DELETE_LETTER:
            self.login.delete_letter()
        elif event == FrameLogin.ACTION_ADD_LETTER:
            self.login.add_letter()
        elif event == FrameLogin.ACTION_OK:
            if self.selection == "User name":
                self.selection = "Password"
                self.login.cursor = 1
                self.login.edit_position = 0
            elif self.selection == "Password":
                self.selection = "User name"
                self.login.cursor = 0
                self.login.edit_position = 0

    def get_user_and_pass(self):
        return self.login.pages[0][0].get_text(), self.login.pages[0][1].get_text()

    def delete_letter(self):
        text_object = self.login_info[self.selection]
        text = text_object.text
        length = len(text)
        if length > 1:
            if self.edit_position <= length - 2:
                text_object.text = text[:self.edit_position] + text[self.edit_position + 1:]
            elif self.edit_position == length - 1:
                text_object.text = text[:self.edit_position]
                self.edit_position = length - 2 

    def add_letter(self):
        text_object = self.login_info[self.selection]
        text = text_object.text
        length = len(text)
        if self.edit_position <= length - 2: 
            text_object.text = text[:self.edit_position] + "_" + text[self.edit_position:]
        elif self.edit_position == length:
            text_object.text = text + "_"

    def get_image(self):
        self.draw()
        return self.layout.get_image()

    def draw(self):
        self.layout.set_content(self.selection)
        self.layout.draw()
        self.layout.get_draw().rounded_rectangle(
            (RECT_LEFT, RECT_TOP, RECT_LEFT + RECT_WIDTH, RECT_TOP + RECT_HEIGHT),
            radius=RECT_RADIUS,
            outline=RECT_BORDER_COLOR,
            width=RECT_BORDER
        )
        self.layout.get_draw().rounded_rectangle(
            (USERNAME_RECT_LEFT, USERNAME_RECT_TOP, USERNAME_RECT_LEFT + USERNAME_RECT_WIDTH, USERNAME_RECT_TOP + USERNAME_RECT_HEIGHT),
            radius=USERNAME_RECT_BORDER_RADIUS,
            fill=USERNAME_RECT_COLOR,
        )
        self.layout.get_draw().rounded_rectangle(
            (PASSWORD_RECT_LEFT, PASSWORD_RECT_TOP, PASSWORD_RECT_LEFT + PASSWORD_RECT_WIDTH, PASSWORD_RECT_TOP + PASSWORD_RECT_HEIGHT),
            radius=PASSWORD_RECT_BORDER_RADIUS,
            fill=PASSWORD_RECT_COLOR
        )
        self.layout.add_image(
            self.logo_image,
            LOGO_POS_X,
            LOGO_POS_Y
        )
        self.layout.get_draw().text(
            (FrameLogin.POINTER_POS_X_DEFAULT, FrameLogin.POINTER_POS_Y[0]),
            text="User name:",
            fill=FrameLogin.COLOR1,
            font=self.font,
            anchor="lm"
        )
        self.layout.get_draw().text(
            (FrameLogin.POINTER_POS_X_DEFAULT + 11, FrameLogin.POINTER_POS_Y[1]),
            text="Password:",
            fill=FrameLogin.COLOR1,
            font=self.font,
            anchor="lm"
        )
        self.login.draw()
    
    def next_event(self):
        if self.edit_status and isinstance(self.pages[self.page_current_number][self.cursor], OptionEdit):
            self.edit_position += 1
            length = len(self.get_element().get_text())
            if self.edit_position > length:
                self.edit_position = length 

    def back_event(self):
        if self.edit_status and isinstance(self.pages[self.page_current_number][self.cursor], OptionEdit):
            self.edit_position -= 1
            if self.edit_position < 0:
                self.edit_position = 0

if __name__ == "__main__":
    frame = FrameLogin("hmi")
    frame.get_image().show()