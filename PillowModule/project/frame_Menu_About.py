from PIL import Image, ImageFont
from templates.Base import BaseImage

RECT_WIDTH = 456
RECT_HEIGHT = 243
RECT_TOP = 44
RECT_LEFT = 13
RECT_RADIUS = 10
RECT_BORDER = 1
RECT_BORDER_COLOR = (0, 95, 115)

FONT_PATH = "Font/inter/Inter-VariableFont_slnt,wght.ttf"
FONT_SIZE = 24
TEXT_COLOR = (233, 216, 166)

WEBSITE = "mtgroup.tech"
WEBSITE_POS_X = 241
WEBSITE_POS_Y = 104

PHONE_NUMBER = "+84-963189981"
PHONE_NUMBER_POS_X = 315
PHONE_NUMBER_POS_Y = 136

EMAIL = "quantrac.mtg@gmail.com"
EMAIL_POS_X = 316
EMAIL_POS_Y = 167

MST = "MST: 2301052220"
MST_POS_X = 316
MST_POS_Y = 198

LOGO_PATH = "Image/Logo 1 Rotate.png"
LOGO_POS_X = 41
LOGO_POS_Y = 65

class FrameMenuAbout:
    ACTION_BACK = "left"
    ACTION_HELP = "0"

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = BaseImage()
        self.font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        self.website = WEBSITE
        self.website_pos_x = WEBSITE_POS_X
        self.website_pos_y = WEBSITE_POS_Y
        self.phone_number = PHONE_NUMBER
        self.phone_number_pos_x = PHONE_NUMBER_POS_X
        self.phone_number_pos_y = PHONE_NUMBER_POS_Y
        self.email = EMAIL
        self.email_pos_x = EMAIL_POS_X
        self.email_pos_y = EMAIL_POS_Y
        self.mst = MST
        self.mst_pos_x = MST_POS_X
        self.mst_pos_y = MST_POS_Y
        self.logo_image = Image.open(LOGO_PATH)
        self.logo_pos_x = LOGO_POS_X
        self.logo_pos_y = LOGO_POS_Y
        self.layout.set_left_control("<-:Back")

    def set_website(self, website):
        if isinstance(website, str):
            self.website = website

    def set_phone_number(self, phone_number):
        if isinstance(phone_number, str):
            self.phone_number = phone_number

    def set_email(self, email):
        if isinstance(email, str):
            self.email = email

    def set_mst(self, mst):
        if isinstance(mst, str):
            self.mst = mst

    def draw_image(self):
        self.layout.add_image(self.logo_image, self.logo_pos_x, self.logo_pos_y)

    def draw_information(self):
        draw_text = self.layout.add_text
        draw_text(
            (self.website_pos_x, self.website_pos_y),
            text=self.website,
            fill=TEXT_COLOR,
            font=self.font,
            anchor="la")
        draw_text(
            (self.phone_number_pos_x, self.phone_number_pos_y),
            text=self.phone_number,
            fill=TEXT_COLOR,
            font=self.font,
            anchor="ma")
        draw_text(
            (self.email_pos_x, self.email_pos_y),
            text=self.email,
            fill=TEXT_COLOR,
            font=self.font,
            anchor="ma")
        draw_text(
            (self.mst_pos_x, self.mst_pos_y),
            text=self.mst,
            fill=TEXT_COLOR,
            font=self.font,
            anchor="ma")

    def draw(self):
        self.layout.draw()
        self.draw_rect()
        self.draw_image()
        self.draw_information()

    def event_handling(self, event):
        if event == FrameMenuAbout.ACTION_BACK:
            self.hmi_screen.pop_frame()
        elif event == FrameMenuAbout.ACTION_HELP:
            pass

    def get_image(self):
        self.draw()
        return self.layout.get_image()

    def draw_rect(self):
        self.layout.get_draw().rounded_rectangle(((RECT_LEFT, RECT_TOP), (RECT_LEFT + RECT_WIDTH, RECT_TOP + RECT_HEIGHT)), radius=RECT_RADIUS, outline=RECT_BORDER_COLOR, width=RECT_BORDER)

def main():
    frame = FrameMenuAbout("hmi")
    frame.get_image().show()

if __name__ == "__main__":
    main()