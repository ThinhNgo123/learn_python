from PIL import Image, ImageDraw, ImageFont
from templates.Layout3 import Layout3
from templates.Menu import Menu, MenuMonitoringValue
from frame_Menu import FrameMenu


DARK_GREEN = (148, 210, 189)
LIGHT_GREEN = (6, 214, 160)
PINK = (239, 71, 111, 1)
ORANGE = (202, 103, 2, 1)

ON_COLOR = LIGHT_GREEN
OFF_COLOR = DARK_GREEN

FONT = ImageFont.truetype("Font/inter/Inter-VariableFont_slnt,wght.ttf", 24)

SERVER_TEXT = "Servers"
SERVERS_TEXT_POS_X = 52
SERVERS_TEXT_POS_Y = 46
SERVERS_TEXT_COLOR = (148, 210, 189)

SERVER_IMAGE_PATH = "templates/Image/backup.png"
SERVER_IMAGE_POS_X = 16
SERVER_IMAGE_POS_Y = 48

RELAY_TEXT = "Relays"
RELAY_TEXT_POS_X = 52
RELAY_TEXT_POS_Y = 155
RELAY_TEXT_COLOR = (148, 210, 189)

RELAY_IMAGE_PATH = "templates/Image/toggle_off.png"
RELAY_IMAGE_POS_X = 17
RELAY_IMAGE_POS_Y = 160

SENSOR_IMAGE_PATH = "templates/Image/sensors.png" 
SENSOR_IMAGE_POS_X = 172
SENSOR_IMAGE_POS_Y = 44

CHECK_IMAGE_PATH = "templates/Image/check_circle.png"
ERROR_IMAGE_PATH = "templates/Image/error.png"
COMPASS_IMAGE_PATH = "templates/Image/compass_calibration.png"

class FrameMonitoring:
	ACTION_OK = "enter"
	ACTION_HELP = "0"
	ACTION_DOWN = "down"
	ACTION_UP = "up"
	ACTION_RIGHT = "right"

	FIRST_ELEMENT_SERVER_POS_X = 46
	FIRST_ELEMENT_SERVER_POS_Y = 76

	FIRST_ELEMENT_RELAY_POS_X = 8
	FIRST_ELEMENT_RELAY_POS_Y = 190

	TITLE_SENSOR_POS_X = 294
	TITLE_SENSOR_POS_Y = 48
	
	FIRST_ELEMENT_SENSOR_POS_X = 207
	FIRST_ELEMENT_SENSOR_POS_Y = 81

	TITLE_SENSOR_VALUE_POS_X = 413
	TITLE_SENSOR_VALUE_POS_Y = 48

	FIRST_ELEMENT_SENSOR_VALUE_POS_Y = 81

	TEXT_COLOR = (6, 214, 160)

	def __init__(self, hmi_screen):
		self.hmi_screen = hmi_screen
		self.layout = Layout3()
		self.layout.set_left_control("OK:Menu")

		self.server_image = Image.open(SERVER_IMAGE_PATH)
		self.relay_image = Image.open(RELAY_IMAGE_PATH)
		self.sensor_image = Image.open(SENSOR_IMAGE_PATH)

		self.menu_list = {
			"server": Menu(self),
			"relay": Menu(self),
			"sensor": Menu(self, title="Sensor"),
			"sensor_value": MenuMonitoringValue(self, title="Value")
		}

		self.menu_list["server"].set_first_element_position(self.FIRST_ELEMENT_SERVER_POS_X, self.FIRST_ELEMENT_SERVER_POS_Y)
		self.menu_list["relay"].set_first_element_position(self.FIRST_ELEMENT_RELAY_POS_X, self.FIRST_ELEMENT_RELAY_POS_Y)
		self.menu_list["sensor"].set_first_element_position(self.FIRST_ELEMENT_SENSOR_POS_X, self.FIRST_ELEMENT_SENSOR_POS_Y)
		self.menu_list["sensor_value"].set_first_element_position(pos_y=self.FIRST_ELEMENT_SENSOR_VALUE_POS_Y)
		self.menu_list["relay"].cursor_pos_x = 96
		self.menu_list["sensor_value"].set_title(
			center_x=self.TITLE_SENSOR_VALUE_POS_X,
			center_y=self.TITLE_SENSOR_VALUE_POS_Y,
			color=RELAY_TEXT_COLOR
		)
		self.menu_list["sensor"].set_title(
			center_x=self.TITLE_SENSOR_POS_X,
			center_y=self.TITLE_SENSOR_POS_Y,
			color=RELAY_TEXT_COLOR
		)
		self.menu_list["server"].set_max_row(2)
		self.menu_list["server"].hide_cursor()
		self.menu_list["relay"].set_max_row(3)
		self.menu_list["relay"].hide_cursor()
		self.menu_list["sensor"].set_max_row(7)
		self.menu_list["sensor_value"].set_max_row(7)
		self.menu_list["sensor_value"].hide_cursor()
		# print(self.menu_list["server"].cursor_pos_x)
		# print(self.menu_list["relay"].cursor_pos_x)

		for value in self.menu_list.values():
			value.set_element_color(self.TEXT_COLOR)

		#test
		self.add_server("FTP 1")
		self.add_server("FTP 2")
		self.add_server("FTP 3")
		self.add_server("FTP 4")
		self.add_server("FTP 5")
		self.add_relay("Pump")
		self.add_relay("Fan")
		self.add_relay("Pump 2")
		self.add_relay("Pump 3")
		self.add_relay("Pump 4")
		self.add_relay("Pump 5")
		self.add_sensor("Temperature", "109.32oC")
		self.add_sensor("CO2", "700ppm")
		self.add_sensor("Flow", "10m3/h")
		self.add_sensor("Flow2", "1m3/h")
		self.add_sensor("Humidity", "87%")
		self.add_sensor("NH4", "20ppm")
		self.add_sensor("Dirty", "20mg/m3")
		self.add_sensor("Temperature", "109.32oC")
		self.add_sensor("Temperature", "109.32oC")
		self.add_sensor("Temperature", "109.32oC")
		self.add_sensor("Temperature", "109.32oC")
		self.index = 0
		self.list = ["sensor", "server", "relay"]

	def draw(self):
		element = self.menu_list[self.list[self.index]].get_element()
		self.layout.set_content(element[element.find(".") + 1:])
		self.layout.draw()
		self.layout.add_image(self.server_image, SERVER_IMAGE_POS_X, SERVER_IMAGE_POS_Y)
		self.layout.add_image(self.relay_image, RELAY_IMAGE_POS_X, RELAY_IMAGE_POS_Y)
		self.layout.add_image(self.sensor_image, SENSOR_IMAGE_POS_X, SENSOR_IMAGE_POS_Y)

		self.layout.add_text((SERVERS_TEXT_POS_X, SERVERS_TEXT_POS_Y), SERVER_TEXT, fill=SERVERS_TEXT_COLOR, font=FONT, anchor="la")
		self.layout.add_text((RELAY_TEXT_POS_X, RELAY_TEXT_POS_Y), RELAY_TEXT, fill=RELAY_TEXT_COLOR, font=FONT, anchor="la")

		for value in self.menu_list.values():
			value.draw()

	def add_server(self, server):
		self.menu_list["server"].add_element(server)

	def add_relay(self, relay):
		self.menu_list["relay"].add_element(relay)
	
	def add_sensor(self, sensor=None, value=None):
		self.menu_list["sensor"].add_element(sensor)
		self.menu_list["sensor_value"].add_element(value)

	def event_handling(self, event):
		if event == FrameMonitoring.ACTION_OK:
			# print("monitoring")
			frame = FrameMenu(self.hmi_screen)
			self.hmi_screen.push_frame(frame)
		elif event == FrameMonitoring.ACTION_HELP:
			print("help")
		elif event == FrameMonitoring.ACTION_DOWN:
			self.menu_list[self.list[self.index]].event_handling(event)
			if self.list[self.index] == "sensor":
				self.menu_list["sensor_value"].event_handling(event)
		elif event == FrameMonitoring.ACTION_UP:
			self.menu_list[self.list[self.index]].event_handling(event)
			if self.list[self.index] == "sensor":
				self.menu_list["sensor_value"].event_handling(event)
		elif event == FrameMonitoring.ACTION_RIGHT:
			self.index = (self.index + 1) % 3
			for index in range(len(self.list)):
				if index == self.index:
					self.menu_list[self.list[index]].show_cursor()
				else:
					self.menu_list[self.list[index]].hide_cursor()
			
	def get_image(self):
		self.draw()
		return self.layout.get_image()

def main():
	image = FrameMonitoring("hmi")
	image.draw()
	image.get_image().show()

if __name__ == '__main__':
	main()