try:
    from templates.Base import BaseImage
except:
    from Base import BaseImage

RECT_WIDTH = 456
RECT_HEIGHT = 243
RECT_TOP = 44
RECT_LEFT = 13
RECT_RADIUS = 10
RECT_BORDER = 1
RECT_BORDER_COLOR = (0, 95, 115)

LINE_WIDTH = 408
LINE_TOP_1 = 72.5
LINE_TOP_2 = 101.5
LINE_LEFT = 51
LINE_BORDER = 1
LINE_COLOR = (0, 95, 115)

LINE_HEIGHT = 202
LINE_LEFT_1 = 116.5
LINE_LEFT_2 = 393.5
LINE_TOP = 82
LINE_BORDER = 1
LINE_COLOR = (0, 95, 115)

class LayoutError(BaseImage):
    def __init__(self):
        super().__init__()

    def draw_layout(self):
        self.get_draw().rounded_rectangle(((RECT_LEFT, RECT_TOP), (RECT_LEFT + RECT_WIDTH, RECT_TOP + RECT_HEIGHT)), radius=RECT_RADIUS, outline=RECT_BORDER_COLOR, width=RECT_BORDER)
        self.get_draw().line(((LINE_LEFT, LINE_TOP_1), (LINE_LEFT + LINE_WIDTH, LINE_TOP_1)), fill=LINE_COLOR, width=LINE_BORDER)
        self.get_draw().line(((LINE_LEFT, LINE_TOP_2), (LINE_LEFT + LINE_WIDTH, LINE_TOP_2)), fill=LINE_COLOR, width=LINE_BORDER)
        self.get_draw().line(((LINE_LEFT_1, LINE_TOP), (LINE_LEFT_1, LINE_TOP + LINE_HEIGHT)), fill=LINE_COLOR, width=LINE_BORDER)
        self.get_draw().line(((LINE_LEFT_2, LINE_TOP), (LINE_LEFT_2, LINE_TOP + LINE_HEIGHT)), fill=LINE_COLOR, width=LINE_BORDER)


    def draw(self):
        super().draw()
        self.draw_layout()

def main():
    image = LayoutError()
    image.draw()
    image.get_image().show()

if __name__ == "__main__":
    main()