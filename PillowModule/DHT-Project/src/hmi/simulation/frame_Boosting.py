from frame_Monitoring import FrameMonitoring
from PIL import Image, ImageDraw, ImageFont
from time import sleep
from threading import Thread

FONT_PATH = "./Font/Source Sans Pro/SourceSansPro-Black.ttf"
# FONT_PATH = "./Font/DejaVuSans/DejaVuSans-Bold.ttf"
FONT_SIZE_16 = 16
FONT_SIZE_24 = 24

FRAME_WIDTH = 480
FRAME_HEIGHT = 320
BACKGROUND_COLOR = (0, 18, 25)
LOGO_IMAGE_PATH = "./Image/Logo 1.png"
LOGO_POS_X = 146
LOGO_POS_Y = 103

VERSION = "Version 1.0.0"
VERSION_POS_X = 0
VERSION_POS_Y = 0 
VERSION_COLOR = (0, 95, 115)

LOADING = "Loading..."
LOADING_POS_X = 183
LOADING_POS_Y = 272
LOADING_COLOR = (233, 216, 166)

class FrameBoosting:
	ACTION_OK = "enter"

	def __init__(self, hmi_screen):
		self.hmi_screen = hmi_screen
		#create font
		self.font_16 = ImageFont.truetype(FONT_PATH, FONT_SIZE_16)
		self.font_24 = ImageFont.truetype(FONT_PATH, FONT_SIZE_24)

		#create background image
		self.background = Image.new("RGB", size=(FRAME_WIDTH, FRAME_HEIGHT), color=BACKGROUND_COLOR)
		 
		self.logo_image = Image.open(LOGO_IMAGE_PATH)
		self.logo_box = (LOGO_POS_X, LOGO_POS_Y)

		self.version = VERSION
		self.loading = LOADING

		self.image_draw = ImageDraw.Draw(self.background)

		Thread(target=self.next_frame).start()

	def get_draw(self):
		return self.image_draw

	def clear_background(self):
		self.get_draw().rectangle((0, 0, FRAME_WIDTH, FRAME_HEIGHT), fill=BACKGROUND_COLOR)

	def draw(self):
		self.clear_background()
		self.background.paste(
			self.logo_image, 
			box=self.logo_box, 
			mask=self.logo_image)
		self.image_draw.text(
			(VERSION_POS_X, VERSION_POS_Y), 
			text=self.version, 
			fill=VERSION_COLOR, 
			font=self.font_16,
			anchor="la") 
		self.image_draw.text(
			(LOADING_POS_X, LOADING_POS_Y), 
			text=self.loading, 
			fill=LOADING_COLOR, 
			font=self.font_24,
			anchor="la") 

	def set_version(self, version):
		if isinstance(version, str):
			self.version = version

	def set_loading(self, loading):
		if isinstance(loading, str):
			self.loading = loading

	def next_frame(self):
		sleep(2)
		self.hmi_screen.push_frame(FrameMonitoring(self.hmi_screen))

	def event_handling(self, event):
		pass

	def save(self):
		self.background.save("background.png")

	def get_image(self):
		self.draw()
		return self.background
	
if __name__ == "__main__":
	frame = FrameBoosting("hmi")
	frame.get_image().show()
	frame.save()
