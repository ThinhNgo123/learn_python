from PIL import Image, ImageDraw, ImageFont

# FONT = ImageFont.truetype("Font/inter/Inter-VariableFont_slnt,wght.ttf", 24)

FRAME_WIDTH = 480
FRAME_HEIGHT = 320
BASE_IMAGE_PATH = "Base_image.png"
BACKGROUND_COLOR = (0, 18, 25)
DEFAULT_COLOR = (255, 255, 255)

IP_FONT_SIZE = 24
IP_FONT_PATH = "Font/inter/Inter-VariableFont_slnt,wght.ttf"
IP_TEXT_POS_X = 171
IP_TEXT_POS_Y = 6
IP_TEXT_COLOR = (233, 216, 166)

TIME_FONT_SIZE = 24
TIME_FONT_PATH = "Font/inter/Inter-VariableFont_slnt,wght.ttf"
TIME_TEXT_POS_X = 469
TIME_TEXT_POS_Y = 6
TIME_TEXT_COLOR = (233, 216, 166)

MENU_FONT_PATH = "Font/inter/Inter-VariableFont_slnt,wght.ttf"
MENU_FONT_SIZE = 24
MENU_TEXT_POS_X = 4
MENU_TEXT_POS_Y = 290
MENU_TEXT_COLOR = (7, 59, 76)

HELP_FONT_PATH = "Font/inter/Inter-VariableFont_slnt,wght.ttf"
HELP_FONT_SIZE = 24
HELP_TEXT_POS_X = 475
HELP_TEXT_POS_Y = 290
HELP_TEXT_COLOR = (7, 59, 76)

CONTENT_FONT_PATH = "./Font/inter/Inter-VariableFont_slnt,wght.ttf"
CONTENT_FONT_SIZE = 24
CONTENT_TEXT_POS_Y = 292
CONTENT_TEXT_COLOR = (233, 216, 166) 

IMAGES = \
{
	"nest_remote_comfort_sensor": 
	{
		"path": "Image/nest_remote_comfort_sensor.png",
	 	"pos_x": 8,
	 	"pos_y": 0
	},
	"lan": 
	{
		"path": "Image/lan.png",
	 	"pos_x": 48,
	 	"pos_y": 0
	},
	"usb": 
	{
		"path": "Image/usb.png",
		"pos_x": 88,
		"pos_y": 0
	},
	"notification_important": 
	{
		"path": "Image/notification_important.png",
		"pos_x": 341,
		"pos_y": 0
	}
}

class BaseImage:

	def __init__(self):
		self.background = Image.new("RGB", (FRAME_WIDTH, FRAME_HEIGHT), color=BACKGROUND_COLOR)
		
		self.draw_object = ImageDraw.Draw(self.background)

		self.nest_remote_comfort_sensor = IMAGES["nest_remote_comfort_sensor"]
		self.lan = IMAGES["lan"]
		self.usb = IMAGES["usb"]
		self.notification_important = IMAGES["notification_important"]

		self.nest_remote_comfort_sensor_image = Image.open(self.nest_remote_comfort_sensor["path"])
		self.lan_image = Image.open(self.lan["path"])
		self.usb_image = Image.open(self.usb["path"])
		self.notification_important_image = Image.open(self.notification_important["path"])

		self.nest_remote_comfort_sensor_status = True
		self.lan_status = True
		self.usb_status = True
		self.notification_important_status = True

		self.ip_font = ImageFont.truetype(font=IP_FONT_PATH, size=IP_FONT_SIZE)
		self.time_font = ImageFont.truetype(font=TIME_FONT_PATH, size=TIME_FONT_SIZE)
		self.menu_font = ImageFont.truetype(font=MENU_FONT_PATH, size=MENU_FONT_SIZE)
		self.help_font = ImageFont.truetype(font=HELP_FONT_PATH, size=HELP_FONT_SIZE)
		self.content_font = ImageFont.truetype(font=CONTENT_FONT_PATH, size=CONTENT_FONT_SIZE)

		self.ip = "192.168.1.21"
		self.time = "21:20"
		self.content = ""
		self.left_control_text = "<-:Back"
		self.right_control_text = "0:Help"
	
	def draw_images(self):
		if self.nest_remote_comfort_sensor_status:
			self.background.paste(
				self.nest_remote_comfort_sensor_image, 
				box=(self.nest_remote_comfort_sensor["pos_x"], self.nest_remote_comfort_sensor["pos_y"]),
				mask=self.nest_remote_comfort_sensor_image)
		if self.lan_status:
			self.background.paste(
				self.lan_image, 
				box=(self.lan["pos_x"], self.lan["pos_y"]),
				mask=self.lan_image)
		if self.usb_status:
			self.background.paste(
				self.usb_image, 
				box=(self.usb["pos_x"], self.usb["pos_y"]),
				mask=self.usb_image)
		if self.notification_important_status:
			self.background.paste(
				self.notification_important_image, 
				box=(self.notification_important["pos_x"], self.notification_important["pos_y"]),
				mask=self.notification_important_image)
	
	def set_lan_status(self, status:bool):
		if status == True: 
			self.lan_status = True 
		else: 
			self.lan_status = False

	def set_usb_status(self, status:bool):
		if status == True: 
			self.usb_status = True 
		else: 
			self.usb_status = False

	def set_nest_remote_comfort_sensor_status(self, status:bool):
		if status == True: 
			self.nest_remote_comfort_sensor_status = True 
		else: 
			self.nest_remote_comfort_sensor_status = False
		
	def set_notification_important_status(self, status:bool):
		if status == True: 
			self.notification_important_status = True 
		else: 
			self.notification_important_status = False

	def draw_texts(self):
		pos_x = self.background.width // 2
		pos_y = CONTENT_TEXT_POS_Y
		self.get_draw().text((IP_TEXT_POS_X, IP_TEXT_POS_Y), self.ip, fill=IP_TEXT_COLOR, anchor="la", font=self.ip_font)
		self.get_draw().text((TIME_TEXT_POS_X, TIME_TEXT_POS_Y), self.time, fill=TIME_TEXT_COLOR, anchor="ra", font=self.time_font)
		self.get_draw().text((MENU_TEXT_POS_X, MENU_TEXT_POS_Y), self.left_control_text, fill=MENU_TEXT_COLOR, anchor="la", font=self.menu_font)
		self.get_draw().text((HELP_TEXT_POS_X, HELP_TEXT_POS_Y), self.right_control_text, fill=HELP_TEXT_COLOR, anchor="ra", font=self.help_font)
		self.get_draw().text((pos_x, pos_y), self.content, fill=CONTENT_TEXT_COLOR, anchor="ma", font=self.content_font)

	def set_left_control(self, text):
		self.left_control_text = text

	def set_right_control(self, text):
		self.right_control_text = text

	def draw_to_background(self):
		self.draw_images()
		self.draw_texts()

	def save(self, path=BASE_IMAGE_PATH):
		self.draw()
		self.background.save(path)

	def get_draw(self):
		return self.draw_object

	def set_ip(self, ip):
		self.ip = ip

	def set_time(self, time):
		self. time = time

	def set_content(self, content):
		self.content = content

	def add_text(self, xy, text, fill=DEFAULT_COLOR, font=None, anchor="la"):
		if xy and text and font:
			self.get_draw().text(xy, text, fill=fill, font=font, anchor=anchor)

	def add_image(self, image, x, y):
		if image:
			self.background.paste(im=image, box=(x, y), mask=image)

	def clear_background(self):
		self.get_draw().rectangle((0, 0, FRAME_WIDTH, FRAME_HEIGHT), fill=BACKGROUND_COLOR)

	def draw(self):
		self.clear_background()
		self.draw_to_background()

	def get_image(self):
		return self.background

	def load_data(self):
		pass

def main():
	from time import sleep, time
	# from  #import time
	image = BaseImage()
	image.set_ip("192.168.123")
	image.set_time(str(time())[-5:-1])
	image.set_content("hello world")
	image.set_lan_status(False)
	image.set_usb_status(False)
	image.set_nest_remote_comfort_sensor_status(False)
	image.set_notification_important_status(False)
	for i in range(5):
		image.set_time(str(time())[-5:-1])
		image.draw()
		image.get_image().show()
		sleep(1)

if __name__ == '__main__':
	main()