from PIL import ImageFont
from templates.Layout_error import LayoutError
from templates.Menu import Menu
from frame_Help import FrameHelp

TITLE_POS_X = 239
TITLE_POS_Y = 44
SIZE = 24
FONT = ImageFont.truetype("./Font/inter/Inter-VariableFont_slnt,wght.ttf", SIZE)
COLOR = (233, 216, 166)

class FrameMenuError:
    ACTION_UP = "up"
    ACTION_DOWN = "down"
    ACTION_BACK = "left"
    ACTION_HELP = "f2"

    TITLE_CODE_CENTER_X = 83.5
    TITLE_CODE_CENTER_Y = 72

    TITLE_CONTENT_CENTER_X = 252#126.5
    TITLE_CONTENT_CENTER_Y = 72

    TITLE_DATE_CENTER_X = 427#221.5
    TITLE_DATE_CENTER_Y = 72

    FIRST_CODE_POS_X = 51
    FIRST_CODE_POS_Y = 105

    FIRST_CONTENT_POS_X = 122
    FIRST_CONTENT_POS_Y = 105

    FIRST_DATE_POS_X = 398
    FIRST_DATE_POS_Y = 105

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = LayoutError()
        self.title = "Errors"
        self.title_pos_x = TITLE_POS_X
        self.title_pos_y = TITLE_POS_Y
        self.code = Menu(self)
        self.content = Menu(self)
        self.date = Menu(self)
        self.init()

        #test
        self.add_error("1001", "FTP time out", "23/6")
        self.add_error("1002", "FTP time out", "24/6")
        self.add_error("1003", "FTP time out", "25/6")
        self.add_error("1004", "FTP time out", "26/6")
        self.add_error("1005", "FTP time out", "27/6")
        self.add_error("1006", "FTP time out", "28/6")
        self.add_error("1007", "FTP time out", "29/6")
        self.add_error("1008", "FTP time out", "30/6")
        self.add_error("1009", "FTP time out", "1/2")
        self.add_error("1010", "FTP time out", "2/12")
        self.add_error("1011", "FTP time out", "23/12")
        self.add_error("1012", "FTP time out", "1/12")

    def init(self):
        self.code.set_title("Code", center_x=FrameMenuError.TITLE_CODE_CENTER_X, center_y=FrameMenuError.TITLE_CODE_CENTER_Y)
        self.content.set_title("Content", center_x=FrameMenuError.TITLE_CONTENT_CENTER_X, center_y=FrameMenuError.TITLE_CONTENT_CENTER_Y)
        self.date.set_title("Date", center_x=FrameMenuError.TITLE_DATE_CENTER_X, center_y=FrameMenuError.TITLE_DATE_CENTER_Y)
        self.code.set_first_element_position(FrameMenuError.FIRST_CODE_POS_X, FrameMenuError.FIRST_CODE_POS_Y)
        self.content.set_first_element_position(FrameMenuError.FIRST_CONTENT_POS_X, FrameMenuError.FIRST_CONTENT_POS_Y)
        self.date.set_first_element_position(FrameMenuError.FIRST_DATE_POS_X, FrameMenuError.FIRST_DATE_POS_Y)
        self.content.hide_cursor()
        self.date.hide_cursor()
        self.code.set_max_row(7)
        self.content.set_max_row(7)
        self.date.set_max_row(7)

    def draw_title(self):    
        self.layout.add_text(
            (self.title_pos_x, self.title_pos_y),
            text=self.title,
            fill=COLOR,
            font=FONT,
            anchor="ma"
        )

    def set_title(self, title):
        if isinstance(title, str) or isinstance(title, int) or isinstance(title, float):
            self.title = str(title)

    def draw(self):
        element = self.code.get_element()
        self.layout.set_content(element[element.find(".") + 1:])
        self.layout.draw()
        self.draw_title()
        self.code.draw()
        self.content.draw()
        self.date.draw()
        
    def event_handling(self, event):
        if event == FrameMenuError.ACTION_UP:
            self.code.event_handling("up")
            self.content.event_handling("up")
            self.date.event_handling("up")
        elif event == FrameMenuError.ACTION_DOWN:
            self.code.event_handling("down")
            self.content.event_handling("down")
            self.date.event_handling("down")
        elif event == FrameMenuError.ACTION_BACK:
            self.hmi_screen.pop_frame()
        elif event == FrameMenuError.ACTION_HELP:
            frame = FrameHelp(self.hmi_screen)
            self.hmi_screen.push_frame(frame)

    def get_image(self):
        self.draw()
        return self.layout.get_image()

    def add_error(self, code="None", content="None", date="None"):
        self.code.add_element(code)
        self.content.add_element(content)
        self.date.add_element(date)

def main():
    test = FrameMenuError("hmi")
    test.get_image().show()

if __name__ == "__main__":
    main()