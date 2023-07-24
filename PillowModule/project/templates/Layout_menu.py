try:
	from templates.Base import BaseImage
except:
	from Base import BaseImage

RECT_WIDTH = 461
RECT_HEIGHT = 243
RECT_TOP = 44
RECT_LEFT = 10
RECT_RADIUS = 10
RECT_BORDER = 1
RECT_BORDER_COLOR = (0, 95, 115)

LINE_WIDTH = 440
LINE_TOP_1 = 129.5
LINE_TOP_2 = 207.5
LINE_TOP_3 = 280.5
LINE_LEFT = 18
LINE_BORDER = 1
LINE_COLOR = (148, 210, 189)

class LayoutMenu(BaseImage):
	def __init__(self):
		super().__init__()

	def draw_layout(self):
		self.get_draw().rounded_rectangle(((RECT_LEFT, RECT_TOP), (RECT_LEFT + RECT_WIDTH, RECT_TOP + RECT_HEIGHT)), radius=RECT_RADIUS, outline=RECT_BORDER_COLOR, width=RECT_BORDER)
		self.get_draw().line(((LINE_LEFT, LINE_TOP_1), (LINE_LEFT + LINE_WIDTH, LINE_TOP_1)), fill=LINE_COLOR, width=LINE_BORDER)
		self.get_draw().line(((LINE_LEFT, LINE_TOP_2), (LINE_LEFT + LINE_WIDTH, LINE_TOP_2)), fill=LINE_COLOR, width=LINE_BORDER)
		self.get_draw().line(((LINE_LEFT, LINE_TOP_3), (LINE_LEFT + LINE_WIDTH, LINE_TOP_3)), fill=LINE_COLOR, width=LINE_BORDER)

	def draw(self):
		super().draw()
		self.draw_layout()

def main():
	image = LayoutMenu()
	image.set_ip("192.168.1.1")
	image.set_time("10:00")
	image.set_content("Layout menu")
	image.draw()
	image.get_image().show()

if __name__ == '__main__':
	main()