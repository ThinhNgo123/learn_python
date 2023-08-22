from threading import Thread
from PIL import ImageFont
from time import sleep

RECT_WIDTH = 280
RECT_HEIGHT = 120
RECT_COLOR = (52, 102, 103)
RECT_BORDER_RADIUS = 10

TEXT_COLOR = (233, 216, 166)
TEXT_SIZE = 24
FONT = ImageFont.truetype("./Font/inter/Inter-VariableFont_slnt,wght.ttf", TEXT_SIZE)

class WindowInformation:
    MAX_LENGTH_TEXT = 270
    DELAY_TIME = 2

    def __init__(self, frame, text=""):
        self.frame = frame
        self.text = text
        self.show_status = False

    def set_text(self, text:str):
        self.text = text

    def draw_rect(self, rect_pos_x, rect_pos_y):
        self.frame.layout.get_draw().rounded_rectangle(
            (rect_pos_x, rect_pos_y, rect_pos_x + RECT_WIDTH, rect_pos_y + RECT_HEIGHT),
            radius=RECT_BORDER_RADIUS,
            fill=RECT_COLOR,
        )

    def draw(self, center_x, center_y):
        if self.show_status:
            rect_pos_x = center_x - RECT_WIDTH / 2
            rect_pos_y = center_y - RECT_HEIGHT / 2
            self.draw_rect(rect_pos_x, rect_pos_y)
            self.draw_text(center_x, center_y)

    def draw_text(self, center_x, center_y):
        self.frame.layout.add_text(
            (center_x, center_y),
            text=self.text,
            fill=TEXT_COLOR,
            font=FONT,
            anchor="mm"
        )

    def delay(self, time):
        self.show_status = True
        sleep(time)
        self.show_status = False

    def show(self):
        Thread(target=self.delay, args=(WindowInformation.DELAY_TIME,)).start()

    def get_show_status(self):
        return self.show_status