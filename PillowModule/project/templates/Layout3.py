try:
	from templates.Base import BaseImage
except:
	from Base import BaseImage

RECT1_WIDTH = 169
RECT1_HEIGHT = 102
RECT1_TOP = 44
RECT1_LEFT = -14
RECT1_RADIUS = 10
RECT1_BORDER = 1
RECT1_BORDER_COLOR = (0, 95, 115)

RECT2_WIDTH = 169
RECT2_HEIGHT = 132
RECT2_TOP = 155
RECT2_LEFT = -13
RECT2_RADIUS = 10
RECT2_BORDER = 1
RECT2_BORDER_COLOR = (0, 95, 115)

RECT3_WIDTH = 329
RECT3_HEIGHT = 243
RECT3_TOP = 44
RECT3_LEFT = 165
RECT3_RADIUS = 10
RECT3_BORDER = 1
RECT3_BORDER_COLOR = (0, 95, 115)

class Layout3(BaseImage):
	def __init__(self):
		super().__init__()

	def draw_layout(self):
		self.get_draw().rounded_rectangle(((RECT1_LEFT, RECT1_TOP), (RECT1_LEFT + RECT1_WIDTH, RECT1_TOP + RECT1_HEIGHT)), radius=RECT1_RADIUS, outline=RECT1_BORDER_COLOR, width=RECT1_BORDER)
		self.get_draw().rounded_rectangle(((RECT2_LEFT, RECT2_TOP), (RECT2_LEFT + RECT2_WIDTH, RECT2_TOP + RECT2_HEIGHT)), radius=RECT2_RADIUS, outline=RECT2_BORDER_COLOR, width=RECT2_BORDER)
		self.get_draw().rounded_rectangle(((RECT3_LEFT, RECT3_TOP), (RECT3_LEFT + RECT3_WIDTH, RECT3_TOP + RECT3_HEIGHT)), radius=RECT3_RADIUS, outline=RECT3_BORDER_COLOR, width=RECT3_BORDER)

	def draw(self):
		super().draw()
		self.draw_layout()

def main():
	image = Layout3()
	image.set_ip("hfhhfhfh")
	image.set_time("10:00")
	image.set_content("eknofingosinvfin")
	image.draw()
	image.get_image().show()

if __name__ == '__main__':
	main()