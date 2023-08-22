from PIL import ImageFont
from threading import Thread

RECT_WIDTH = 280
RECT_HEIGHT = 120
RECT_COLOR = (52, 102, 103)
RECT_BORDER_RADIUS = 10

OK_BUTTON = "OK"
OK_BUTTON_WIDTH = 85
OK_BUTTON_HEIGHT = 29
OK_BUTTON_COLOR = (0, 18, 25)
OK_BUTTON_BORDER_RADIUS = 5
OK_BUTTON_PADX = 97.5
OK_BUTTON_PADY = 77

TEXT_COLOR = (233, 216, 166)
TEXT_SIZE = 24
FONT = ImageFont.truetype("./Font/inter/Inter-VariableFont_slnt,wght.ttf", TEXT_SIZE)

class WindowAlert:
    ACTION_OK = "enter"

    MAX_NUMBER_ROW = 2
    MAX_LENGTH_TEXT = 270
    LENGTH_SPACE = FONT.getlength(" ")
    TEXT_HEIGHT = 25
    X_MARGIN = 5
    Y_MARGIN = 14

    def __init__(self, frame, text=""):
        self.frame = frame
        self.rows = None
        self.show_status = False
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
            self.draw_information(rect_pos_x, rect_pos_y)
            self.draw_button(rect_pos_x + OK_BUTTON_PADX, rect_pos_y + OK_BUTTON_PADY)

    def draw_button(self, rect_pos_x, rect_pos_y):
        self.frame.layout.get_draw().rounded_rectangle(
            (rect_pos_x, rect_pos_y, rect_pos_x + OK_BUTTON_WIDTH, rect_pos_y + OK_BUTTON_HEIGHT),
            radius=OK_BUTTON_BORDER_RADIUS,
            fill=OK_BUTTON_COLOR
        )
        self.frame.layout.add_text(
            (rect_pos_x + OK_BUTTON_WIDTH / 2, rect_pos_y),
            text=OK_BUTTON,
            fill=TEXT_COLOR,
            font=FONT,
            anchor="ma"
        )

    def draw_information(self, rect_pos_x, rect_pos_y):
        count = 0
        for row_text in self.rows:
            self.frame.layout.add_text(
                (rect_pos_x + WindowAlert.X_MARGIN, 
                rect_pos_y + WindowAlert.Y_MARGIN + WindowAlert.TEXT_HEIGHT * count),
                text=row_text,
                fill=TEXT_COLOR,
                font=FONT,
                anchor="la"
            )
            count += 1

    def event_handling(self, event):
        if event == WindowAlert.ACTION_OK:
            if self.show_status:
                self.show_status = False
                if hasattr(self, "callback_args"):
                    Thread(target=self.callback, args=self.callback_args).start()
                else:
                    Thread(target=self.callback).start()

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
                pixel += self.get_length_text(text[index]) + WindowAlert.LENGTH_SPACE
                if pixel <= WindowAlert.MAX_LENGTH_TEXT:
                    texts.append(text[index])
                else:
                    rows.append(" ".join(texts))
                    texts = [text[index]]
                    pixel = 0
                    pixel += self.get_length_text(text[index]) + WindowAlert.LENGTH_SPACE
            rows.append(" ".join(texts))
            self.rows = rows

    def get_length_text(self, text:str):
        return FONT.getlength(text)

def main():
    alert = WindowAlert("frame")
    alert.set_text("The upper limit is lower than the lower limit")

if __name__ == "__main__":
    main()