try:
	from templates.Base import BaseImage
except:
	from Base import BaseImage

RECT1_WIDTH = 179
RECT1_HEIGHT = 243
RECT1_TOP = 44
RECT1_LEFT = -11
RECT1_RADIUS = 10
RECT1_BORDER = 1
RECT1_BORDER_COLOR = (0, 95, 115)

RECT2_WIDTH = 311
RECT2_HEIGHT = 243
RECT2_TOP = 44
RECT2_LEFT = 179
RECT2_RADIUS = 10
RECT2_BORDER = 1
RECT2_BORDER_COLOR = (0, 95, 115)

LINE1_WIDTH = 151
LINE1_TOP = 74.99
LINE1_LEFT = 7
LINE1_BORDER = 1
LINE1_COLOR = (0, 95, 115)

LINE2_WIDTH = 281.01
LINE2_TOP = 74.99
LINE2_LEFT = 191
LINE2_BORDER = 1
LINE2_COLOR = (0, 95, 115)

class Layout2(BaseImage):
	def __init__(self):
		super().__init__()

	def draw_layout(self):
		self.get_draw().rounded_rectangle(((RECT1_LEFT, RECT1_TOP), (RECT1_LEFT + RECT1_WIDTH, RECT1_TOP + RECT1_HEIGHT)), radius=RECT1_RADIUS, outline=RECT1_BORDER_COLOR, width=RECT1_BORDER)
		self.get_draw().rounded_rectangle(((RECT2_LEFT, RECT2_TOP), (RECT2_LEFT + RECT2_WIDTH, RECT2_TOP + RECT2_HEIGHT)), radius=RECT2_RADIUS, outline=RECT2_BORDER_COLOR, width=RECT2_BORDER)
		self.get_draw().line(((LINE1_LEFT, LINE1_TOP), (LINE1_LEFT + LINE1_WIDTH, LINE1_TOP)), fill=LINE1_COLOR, width=LINE1_BORDER)
		self.get_draw().line(((LINE2_LEFT, LINE2_TOP), (LINE2_LEFT + LINE2_WIDTH, LINE2_TOP)), fill=LINE2_COLOR, width=LINE2_BORDER)

	def draw(self):
		super().draw()
		self.draw_layout()

def main():
	image = Layout2()
	image.draw()
	image.get_image().show()

if __name__ == '__main__':
	main()