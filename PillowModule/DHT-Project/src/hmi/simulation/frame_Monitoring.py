from PIL import Image, ImageDraw, ImageFont
from templates.Layout3 import Layout3
from templates.Menu import Menu, MenuMonitoring
from frame_Login import FrameLogin
from frame_Help import FrameHelp

FONT = ImageFont.truetype("Font/inter/Inter-VariableFont_slnt,wght.ttf", 24)
TITLE_COLOR = (148, 210, 189)

TITLE_SERVERS_POS_X = 52
TITLE_SERVERS_POS_Y = 46

SERVER_IMAGE_PATH = "Image/backup.png"
SERVER_IMAGE_POS_X = 16
SERVER_IMAGE_POS_Y = 48

TITLE_RELAY_POS_X = 52
TITLE_RELAY_POS_Y = 155

RELAY_IMAGE_PATH = "Image/toggle_off.png"
RELAY_IMAGE_POS_X = 17
RELAY_IMAGE_POS_Y = 160

SENSOR_IMAGE_PATH = "Image/sensors.png" 
SENSOR_IMAGE_POS_X = 172
SENSOR_IMAGE_POS_Y = 44

TITLE_SENSOR_POS_X = 294
TITLE_SENSOR_POS_Y = 48

TITLE_SENSOR_VALUE_POS_X = 413
TITLE_SENSOR_VALUE_POS_Y = 48

class FrameMonitoring:
	ACTION_CHANGE_STATUS = "enter"
	ACTION_UP = "up"
	ACTION_DOWN = "down"
	ACTION_RIGHT = "right"
	ACTION_LEFT = "left"
	ACTION_NEXT_FRAME = "f1"
	ACTION_HELP = "f2"

	FIRST_STATUS_SERVER_POS_X = 16
	FIRST_STATUS_SERVER_POS_Y = 79

	FIRST_NAME_SERVER_POS_X = 46
	FIRST_NAME_SERVER_POS_Y = 76

	FIRST_NAME_RELAY_POS_X = 8
	FIRST_NAME_RELAY_POS_Y = 190

	FIRST_VALUE_RELAY_POS_X = 102
	FIRST_VALUE_RELAY_POS_Y = 190
	
	# FIRST_ELEMENT_SENSOR_POS_X = 207
	# FIRST_ELEMENT_SENSOR_POS_Y = 81

	# TITLE_SENSOR_VALUE_POS_X = 413
	# TITLE_SENSOR_VALUE_POS_Y = 48

	# FIRST_ELEMENT_SENSOR_VALUE_POS_Y = 81

	TEXT_COLOR = (6, 214, 160)

	def __init__(self, hmi_screen):
		self.hmi_screen = hmi_screen
		self.layout = Layout3()
		self.layout.set_left_control("F1:Login")
		self.server_image = Image.open(SERVER_IMAGE_PATH)
		self.relay_image = Image.open(RELAY_IMAGE_PATH)
		self.sensor_image = Image.open(SENSOR_IMAGE_PATH)

		self.menus = {
			"servers": MenuMonitoring(self, MenuMonitoring.TYPE_STATUS_AND_NAME),
			"relays": MenuMonitoring(self, MenuMonitoring.TYPE_NAME_AND_VALUE),
			"sensors": MenuMonitoring(self, MenuMonitoring.TYPE_STATUS_NAME_VALUE)}
		self.index = 0
		self.list = ["sensors", "servers", "relays"]
		

		#test
		self.add_server("normal", "FTP 1")
		self.add_server("normal", "FTP 2")
		self.add_server("normal", "FTP 3")
		self.add_server("normal", "FTP 4")
		self.add_server("normal", "FTP 5")
		self.add_relay("Pump", "On")
		self.add_relay("Fan", "Off")
		self.add_relay("Pump 2", "Off")
		self.add_relay("Pump 3", "Off")
		self.add_relay("Pump 4", "Off")
		self.add_relay("Pump 5", "Off")
		self.add_sensor("Temperature", "109.32oC", "error")
		self.add_sensor("CO2", "700ppm", "disable")
		self.add_sensor("Flow", "10m3/h", "normal")
		self.add_sensor("Flow2", "1m3/h", "calib")
		self.add_sensor("Humidity", "87%", "calib")
		self.add_sensor("NH4", "20ppm", "error")
		self.add_sensor("Dirty", "20mg/m3", "normal")
		self.add_sensor("Temperature", "109.32oC", "disable")
		self.add_sensor("Temperature", "109.32oC", "disable")
		self.add_sensor("Temperature", "109.32oC", "disable")
		self.add_sensor("Temperature", "109.32oC", "disable")
		for i in range(10000):
			self.add_sensor(f"{i}.Temperature", "109.32oC", "disable")
		for i in range(10000):
			self.add_server("normal" ,f"FTP {i+1}")
		for i in range(10000):
			self.add_relay(f"Fan {i+1}", "Off")

	def init(self):
		self.menus["sensors"].set_title(
			title="Sensor",
			center_x=self.TITLE_SENSOR_POS_X,
			center_y=self.TITLE_SENSOR_POS_Y,
			color=TITLE_COLOR
		)

		self.menus["servers"].cursor_pos_x = 16
		self.menus["relays"].cursor_pos_x = 8

		self.menus["servers"].set_first_status_position(self.FIRST_STATUS_SERVER_POS_X, self.FIRST_STATUS_SERVER_POS_Y)
		self.menus["servers"].set_first_name_position(self.FIRST_NAME_SERVER_POS_X, self.FIRST_NAME_SERVER_POS_Y)
		self.menus["relays"].set_first_name_position(self.FIRST_NAME_RELAY_POS_X, self.FIRST_NAME_RELAY_POS_Y)
		self.menus["relays"].set_first_value_position(self.FIRST_VALUE_RELAY_POS_X, self.FIRST_VALUE_RELAY_POS_Y)

		self.menus["servers"].set_max_row(2)
		self.menus["servers"].hide_cursor()
		self.menus["relays"].set_max_row(3)
		self.menus["relays"].hide_cursor()
		self.menus["sensors"].set_max_row(7)

		# for value in self.menu_list.values():
		# 	value.set_element_color(self.TEXT_COLOR)

	def draw(self):
		#test
		# self.clear_sensors()
		# self.clear_relays()
		# self.clear_servers()
		#
		element = self.menus[self.list[self.index]].get_element()[1]
		self.layout.set_content(element[element.find(".") + 1:])
		self.layout.draw()
		self.layout.add_image(self.server_image, SERVER_IMAGE_POS_X, SERVER_IMAGE_POS_Y)
		self.layout.add_image(self.relay_image, RELAY_IMAGE_POS_X, RELAY_IMAGE_POS_Y)
		self.layout.add_image(self.sensor_image, SENSOR_IMAGE_POS_X, SENSOR_IMAGE_POS_Y)
		self.layout.add_text((TITLE_SERVERS_POS_X, TITLE_SERVERS_POS_Y), "Servers", fill=TITLE_COLOR, font=FONT, anchor="la")
		self.layout.add_text((TITLE_RELAY_POS_X, TITLE_RELAY_POS_Y), "Relays", fill=TITLE_COLOR, font=FONT, anchor="la")
		self.layout.add_text((TITLE_SENSOR_VALUE_POS_X, TITLE_SENSOR_VALUE_POS_Y), "Value", fill=TITLE_COLOR, anchor="ma")
		
		self.menus["servers"].draw()
		self.menus["relays"].draw(anchor_value="la")
		self.menus["sensors"].draw()
		# for value in self.menu_list.values():
		# 	value.draw()

	def add_server(self, status, name):
		self.menus["servers"].add_element(status, name)

	def add_relay(self, name, value):
		self.menus["relays"].add_element(name=name, value=value)
	
	def add_sensor(self, name, value, status):
		self.menus["sensors"].add_element(status, name, value)

	# def clear_sensors(self):
	# 	self.menu_list["sensor"].clear_elements()
	# 	self.menu_list["sensor_value"].clear_elements()
	# 	self.menu_list["sensor_status"].clear_elements()

	# def clear_relays(self):
	# 	self.menu_list["relay"].clear_elements()

	# def clear_servers(self):
	# 	self.menu_list["server"].clear_elements()

	def event_handling(self, event):
		if event == FrameMonitoring.ACTION_NEXT_FRAME:
			frame = FrameLogin(self.hmi_screen)
			self.hmi_screen.push_frame(frame)
		elif event == FrameMonitoring.ACTION_HELP:
			frame = FrameHelp(self.hmi_screen)
			self.hmi_screen.push_frame(frame)
		elif event == FrameMonitoring.ACTION_DOWN:
			self.menus[self.list[self.index]].event_handling(event)
		elif event == FrameMonitoring.ACTION_UP:
			self.menus[self.list[self.index]].event_handling(event)
		elif event == FrameMonitoring.ACTION_RIGHT:
			self.index = (self.index + 1) % 3
			for index in range(len(self.list)):
				if index == self.index:
					self.menus[self.list[index]].show_cursor()
				else:
					self.menus[self.list[index]].hide_cursor()
		elif event == FrameMonitoring.ACTION_LEFT:
			pass
		elif event == FrameMonitoring.ACTION_CHANGE_STATUS:
			self.menus[self.list[self.index]].event_handling("f1")
			
	def get_image(self):
		self.draw()
		return self.layout.get_image()

if __name__ == '__main__':
	image = FrameMonitoring("hmi")
	image.draw()
	image.get_image().show()