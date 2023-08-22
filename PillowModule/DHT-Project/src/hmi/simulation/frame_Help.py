from PIL import ImageFont
from templates.Base import BaseImage

RECT_WIDTH = 461
RECT_HEIGHT = 243
RECT_TOP = 44
RECT_LEFT = 10
RECT_RADIUS = 10
RECT_BORDER = 1
RECT_BORDER_COLOR = (0, 95, 115)

class FrameHelp:
    ACTION_BACK = "left"
    ACTION_UP = "up"
    ACTION_DOWN = "down"

    MAX_NUMBER_ROW_OF_PAGE = 9
    LENGTH_OF_ROW = 438
    POS_X = 22
    POS_Y = 54

    FONT = ImageFont.truetype("./Font/inter/Inter-VariableFont_slnt,wght.ttf", 24)
    LENGTH_SPACE = FONT.getlength(" ")

    TEXT_COLOR = (233, 216, 166)
    TEXT_HEIGHT = 25

    def __init__(self, hmi_screen) -> None:
        self.hmi_screen = hmi_screen
        self.layout = BaseImage()
        self.layout.set_right_control("")
        self.pages = None
        self.page_current_number = 0 #first page

        #test
        self.add_text("This is the tutorial for user F1, F2, F3, F4 is flex function button, to get string input please use T9 keyboard to type." * 10)

    def add_text(self, text:str):
        if len(text) != 0:
            rows = []
            text = text.split(" ")
            pixel = 0
            texts = [text[0]]
            pixel += self.get_length_text(text[0])
            for index in range(1, len(text)):
                pixel += self.get_length_text(text[index]) + FrameHelp.LENGTH_SPACE
                if pixel <= FrameHelp.LENGTH_OF_ROW:
                    texts.append(text[index])
                else:
                    rows.append(" ".join(texts))
                    texts = [text[index]]
                    pixel = 0
                    pixel += self.get_length_text(text[index]) + FrameHelp.LENGTH_SPACE
            rows.append(" ".join(texts))
            pages = []
            for index in range(0, len(rows), FrameHelp.MAX_NUMBER_ROW_OF_PAGE):
                pages.append(rows[index:index + FrameHelp.MAX_NUMBER_ROW_OF_PAGE])
            self.pages = pages

    def get_length_text(self, text:str):
        return FrameHelp.FONT.getlength(text)

    def event_handling(self, event):
        if event == FrameHelp.ACTION_BACK:
            self.hmi_screen.pop_frame()
        elif event == FrameHelp.ACTION_DOWN:
            self.down_event()
        elif event == FrameHelp.ACTION_UP:
            self.up_event()

    def get_image(self):
        self.draw()
        return self.layout.get_image()

    def draw(self):
        self.layout.draw()
        self.layout.get_draw().rounded_rectangle(
            (RECT_LEFT, RECT_TOP, RECT_LEFT + RECT_WIDTH, RECT_TOP + RECT_HEIGHT),
            radius=RECT_RADIUS,
            outline=RECT_BORDER_COLOR,
            width=RECT_BORDER
        )
        self.draw_text()

    def draw_text(self):
        page = self.pages[self.page_current_number]
        count = 0
        for row_text in page:
            self.layout.add_text(
                (FrameHelp.POS_X, FrameHelp.POS_Y + FrameHelp.TEXT_HEIGHT * count),
                text=row_text,
                fill=FrameHelp.TEXT_COLOR,
                font=FrameHelp.FONT,
                anchor="la"
            )
            count += 1

    def up_event(self):
        self.page_current_number -= 1
        if self.page_current_number < 0:
            self.page_current_number = len(self.pages) - 1

    def down_event(self):
        self.page_current_number += 1
        if self.page_current_number >= len(self.pages):
            self.page_current_number = 0

def main():
    frame = FrameHelp("hmi")
    frame.add_text(" ".join(["thinh"] * 26))
    print(frame.pages)
    frame.get_image().show()

if __name__ == "__main__":
    main()