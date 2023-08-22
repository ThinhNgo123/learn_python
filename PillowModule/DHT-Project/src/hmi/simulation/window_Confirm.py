from PIL import ImageFont
from threading import Thread

RECT_WIDTH = 280
RECT_HEIGHT = 120
RECT_COLOR = (52, 102, 103)
RECT_BORDER_RADIUS = 10

BUTTON_WIDTH = 85
BUTTON_HEIGHT = 29
BUTTON_BORDER_RADIUS = 5
BUTTON_COLOR_ON = (202, 103, 2)
BUTTON_COLOR_OFF = (0, 18, 25)
BUTTON_COLOR = (BUTTON_COLOR_OFF, BUTTON_COLOR_ON)

ACCEPT_BUTTON = "Yes"
ACCEPT_BUTTON_PADX = 45
ACCEPT_BUTTON_PADY = 77

REFUSE_BUTTON = "No"
REFUSE_BUTTON_PADX = 150
REFUSE_BUTTON_PADY = 77

TEXT_COLOR = (233, 216, 166)
TEXT_SIZE = 24
FONT = ImageFont.truetype("./Font/inter/Inter-VariableFont_slnt,wght.ttf", TEXT_SIZE)

class WindowConfirm:
    ACTION_OK = "enter"
    ACTION_LEFT = "left"
    ACTION_RIGHT = "right"

    SELECT_DEFAULT = 0

    MAX_NUMBER_ROW = 2
    MAX_LENGTH_TEXT = 270
    LENGTH_SPACE = FONT.getlength(" ")
    TEXT_HEIGHT = 25
    # X_MARGIN = 5
    Y_MARGIN = 14

    def __init__(self, frame, text=""):
        self.frame = frame
        self.rows = None
        self.show_status = False
        self.select = WindowConfirm.SELECT_DEFAULT
        self.callback = self.callback_default
        if text:
            self.set_text(text)

    def callback_default(self):
        print("callback default")

    def set_callback(self, callback, *args):
        self.callback = callback
        if args:
            self.callback_args = args

    def set_text(self, text:str):
        self.set_rows(text)

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
            self.draw_information(center_x, rect_pos_y)
            self.draw_button(
                rect_pos_x + ACCEPT_BUTTON_PADX, 
                rect_pos_y + ACCEPT_BUTTON_PADY, 
                ACCEPT_BUTTON, 
                BUTTON_COLOR[self.select == WindowConfirm.SELECT_DEFAULT])
            self.draw_button(
                rect_pos_x + REFUSE_BUTTON_PADX, 
                rect_pos_y + REFUSE_BUTTON_PADY, 
                REFUSE_BUTTON,
                BUTTON_COLOR[self.select == (WindowConfirm.SELECT_DEFAULT + 1)])

    def draw_button(self, rect_pos_x, rect_pos_y, text:str, color):
        self.frame.layout.get_draw().rounded_rectangle(
            (rect_pos_x, rect_pos_y, rect_pos_x + BUTTON_WIDTH, rect_pos_y + BUTTON_HEIGHT),
            radius=BUTTON_BORDER_RADIUS,
            fill=color
        )
        self.frame.layout.add_text(
            (rect_pos_x + BUTTON_WIDTH / 2, rect_pos_y),
            text=text,
            fill=TEXT_COLOR,
            font=FONT,
            anchor="ma"
        )

    def draw_information(self, center_x, rect_pos_y):
        count = 0
        for row_text in self.rows:
            self.frame.layout.add_text(
                (center_x, rect_pos_y + WindowConfirm.Y_MARGIN + WindowConfirm.TEXT_HEIGHT * count),
                text=row_text,
                fill=TEXT_COLOR,
                font=FONT,
                anchor="ma"
            )
            count += 1

    def event_handling(self, event):
        if self.show_status:
            if event == WindowConfirm.ACTION_OK:
                if self.select == WindowConfirm.SELECT_DEFAULT:
                    if hasattr(self, "callback_args"):
                        Thread(target=self.callback, args=self.callback_args).start()
                    else:
                        Thread(target=self.callback).start()
                self.show_status = False
            elif event == WindowConfirm.ACTION_LEFT:
                self.select -= 1
                if self.select < 0:
                    self.select = 1
            elif event == WindowConfirm.ACTION_RIGHT:
                self.select += 1
                if self.select > 1:
                    self.select = 0

    def show(self):
        self.show_status = True

    def get_show_status(self):
        return self.show_status

    def set_rows(self, text:str):
        if len(text) != 0:
            rows = []
            text = text.split(" ")
            pixel = 0
            texts = [text[0]]
            pixel += self.get_length_text(text[0])
            for index in range(1, len(text)):
                pixel += self.get_length_text(text[index]) + WindowConfirm.LENGTH_SPACE
                if pixel <= WindowConfirm.MAX_LENGTH_TEXT:
                    texts.append(text[index])
                else:
                    rows.append(" ".join(texts))
                    texts = [text[index]]
                    pixel = 0
                    pixel += self.get_length_text(text[index]) + WindowConfirm.LENGTH_SPACE
            rows.append(" ".join(texts))
            self.rows = rows

    def get_length_text(self, text:str):
        return FONT.getlength(text)

def main():
    alert = WindowConfirm("frame")
    alert.set_text("The upper limit is lower than the lower limit")

if __name__ == "__main__":
    main()