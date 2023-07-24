from PIL import Image, ImageFont
from templates.Layout_menu import LayoutMenu
from frame_Menu_Sensor import FrameMenuSensor
from frame_Menu_Server import FrameMenuServer
from frame_Menu_Relay import FrameMenuRelay
from frame_Menu_Error import FrameMenuError
from frame_Menu_Database import FrameMenuDatabase
from frame_Menu_Internet import FrameMenuInternet
from frame_Menu_Memory import FrameMenuMemory
from frame_Menu_Restore import FrameMenuRestore
from frame_Menu_Backup import FrameMenuBackup
from frame_Menu_User import FrameMenuUser
from frame_Menu_Develop import FrameMenuDevelop
from frame_Menu_About import FrameMenuAbout
from frame_Menu_Power import FrameMenuPower

ICON_PATH = {
    "Sensor": {"light": "Image/sensors_light.png", "dark": "Image/sensors_dark.png"},
    "Server": {"light": "Image/server_light.png", "dark": "Image/server_dark.png"},
    "Relay": {"light": "Image/relay_light.png", "dark": "Image/relay_dark.png"},
    "Error": {"light": "Image/error_light.png", "dark": "Image/error_dark.png"},
    "Data": {"light": "Image/data_light.png", "dark": "Image/data_dark.png"},
    "Internet": {"light": "Image/internet_light.png", "dark": "Image/internet_dark.png"},
    "Memory": {"light": "Image/memory_light.png", "dark": "Image/memory_dark.png"},
    "Restore": {"light": "Image/restore_light.png", "dark": "Image/restore_dark.png"},
    "Backup": {"light": "Image/backup_light.png", "dark": "Image/backup_dark.png"},
    "User": {"light": "Image/user_light.png", "dark": "Image/user_dark.png"},
    "Develop": {"light": "Image/develop_light.png", "dark": "Image/develop_dark.png"},
    "About": {"light": "Image/about_light.png", "dark": "Image/about_dark.png"},
    "Power": {"light": "Image/power_light.png", "dark": "Image/power_dark.png"}
}

SENSOR_IMAGE_POS_X = 18
SENSOR_IMAGE_POS_Y = 56

SENSOR_TEXT_POS_X = 25
SENSOR_TEXT_POS_Y = 111
SENSOR_TEXT_SIZE = 14
SENSOR_TEXT_FONT_PATH = "Font/inter/Inter-VariableFont_slnt,wght.ttf"
SENSOR_TEXT_COLOR = (233, 216, 166)

SERVERS_POS_X = 84
SERVERS_POS_Y = 51

RELAY_POS_X = 148
RELAY_POS_Y = 58

ERRORS_POS_X = 216
ERRORS_POS_Y = 61

DATA_POS_X = 271
DATA_POS_Y = 56

INTERNET_POS_X = 335
INTERNET_POS_Y = 58

MEMORY_POS_X = 398
MEMORY_POS_Y = 57

RESTORE_POS_X = 21
RESTORE_POS_Y = 141

BACKUP_POS_X = 83
BACKUP_POS_Y = 139

USER_POS_X = 152
USER_POS_Y = 139

DEVELOP_POS_X = 215
DEVELOP_POS_Y = 139

ABOUT_POS_X = 277
ABOUT_POS_Y = 138

POWER_POS_X = 339
POWER_POS_Y = 136

POSITION_ICON = (
    (SENSOR_IMAGE_POS_X, SENSOR_IMAGE_POS_Y),
    (SERVERS_POS_X, SERVERS_POS_Y),
    (RELAY_POS_X, RELAY_POS_Y),
    (ERRORS_POS_X, ERRORS_POS_Y),
    (DATA_POS_X, DATA_POS_Y),
    (INTERNET_POS_X, INTERNET_POS_Y),
    (MEMORY_POS_X, MEMORY_POS_Y),
    (RESTORE_POS_X, RESTORE_POS_Y),
    (BACKUP_POS_X, BACKUP_POS_Y),
    (USER_POS_X, USER_POS_Y),
    (DEVELOP_POS_X, DEVELOP_POS_Y),
    (ABOUT_POS_X, ABOUT_POS_Y),
    (POWER_POS_X, POWER_POS_Y))

class FrameMenu:
    POINTER_DEFAULT = 0
    ACTION_BACK = "left"
    ACTION_OK = "enter"
    ACTION_NEXT = "right"
    ACTION_HELP = "0" 
    SENSOR = 0
    SERVER = 1
    RELAY = 2
    ERROR = 3
    DATA = 4
    INTERNET = 5
    MEMORY = 6
    RESTORE = 7
    BACKUP = 8
    USER = 9
    DEVELOP = 10
    ABOUT = 11
    POWER = 12
    CONTENTS = ("Sensor", "Servers", "Relay", "Errors", "Data", "Internet", "Memory", "Restore", "Back up", "User", "Develop", "About", "Power")

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = LayoutMenu()
        self.sensor = {
            "light": Image.open(ICON_PATH["Sensor"]["light"]),
            "dark": Image.open(ICON_PATH["Sensor"]["dark"])}
        self.sensor_text_font = ImageFont.truetype(SENSOR_TEXT_FONT_PATH, SENSOR_TEXT_SIZE)
        self.server = {
            "light": Image.open(ICON_PATH["Server"]["light"]),
            "dark": Image.open(ICON_PATH["Server"]["dark"])}
        self.relay = {
            "light": Image.open(ICON_PATH["Relay"]["light"]),
            "dark": Image.open(ICON_PATH["Relay"]["dark"])}
        self.errors = {
            "light": Image.open(ICON_PATH["Error"]["light"]),
            "dark": Image.open(ICON_PATH["Error"]["dark"])}
        self.data = {
            "light": Image.open(ICON_PATH["Data"]["light"]),
            "dark": Image.open(ICON_PATH["Data"]["dark"])}
        self.internet = {
            "light": Image.open(ICON_PATH["Internet"]["light"]),
            "dark": Image.open(ICON_PATH["Internet"]["dark"])}
        self.memory = {
            "light": Image.open(ICON_PATH["Memory"]["light"]),
            "dark": Image.open(ICON_PATH["Memory"]["dark"])}
        self.restore = {
            "light": Image.open(ICON_PATH["Restore"]["light"]),
            "dark": Image.open(ICON_PATH["Restore"]["dark"])}
        self.backup = {
            "light": Image.open(ICON_PATH["Backup"]["light"]),
            "dark": Image.open(ICON_PATH["Backup"]["dark"])}
        self.user = {
            "light": Image.open(ICON_PATH["User"]["light"]),
            "dark": Image.open(ICON_PATH["User"]["dark"])}
        self.develop = {
            "light": Image.open(ICON_PATH["Develop"]["light"]),
            "dark": Image.open(ICON_PATH["Develop"]["dark"])}
        self.about = {
            "light": Image.open(ICON_PATH["About"]["light"]),
            "dark": Image.open(ICON_PATH["About"]["dark"])}
        self.power = {
            "light": Image.open(ICON_PATH["Power"]["light"]),
            "dark": Image.open(ICON_PATH["Power"]["dark"])}
        self.icons = [self.sensor, self.server, self.relay, self.errors, self.data, self.internet, self.memory, self.restore, self.backup, self.user, self.develop, self.about, self.power]
        self.statuses = [True, *([False] * (len(self.icons) - 1))]
        self.pointer = FrameMenu.POINTER_DEFAULT
        self.layout.set_left_control("<-:Back")

    def draw(self):
        self.layout.draw()
        draw_image = self.layout.add_image
        draw_text = self.layout.add_text

        draw_text(
            (SENSOR_TEXT_POS_X, SENSOR_TEXT_POS_Y), 
            text="Sensor", 
            fill=SENSOR_TEXT_COLOR, 
            font=self.sensor_text_font)
        
        for index in range(len(self.icons)):
            if self.statuses[index]:
                draw_image(self.icons[index]["light"], POSITION_ICON[index][0], POSITION_ICON[index][1])
            else:
                draw_image(self.icons[index]["dark"], POSITION_ICON[index][0], POSITION_ICON[index][1])

    def set_content(self, content):
        self.layout.set_content(content=content)

    def show(self):
        self.draw()
        self.layout.background.show()

    def event_handling(self, event):
        if event == FrameMenu.ACTION_HELP:
            self.help_event()
        elif event == FrameMenu.ACTION_BACK:
            self.back_event()
        elif event == FrameMenu.ACTION_NEXT:
            self.next_event()
        elif event == FrameMenu.ACTION_OK:
            self.ok_event() 

    def help_event(self):
        print("help")
        pass

    def back_event(self):
        self.hmi_screen.pop_frame()

    def next_event(self):
        self.statuses[self.pointer] = False
        self.pointer += 1
        if self.pointer >= len(self.icons):
            self.pointer = FrameMenu.POINTER_DEFAULT
        self.statuses[self.pointer] = True
        self.layout.set_content(FrameMenu.CONTENTS[self.pointer])

    def ok_event(self):
        if self.pointer == FrameMenu.SENSOR:
            frame = FrameMenuSensor(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif self.pointer == FrameMenu.SERVER:
            frame = FrameMenuServer(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif self.pointer == FrameMenu.RELAY:
            frame = FrameMenuRelay(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif self.pointer == FrameMenu.ERROR:
            frame = FrameMenuError(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif self.pointer == FrameMenu.DATA:
            frame = FrameMenuDatabase(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif self.pointer == FrameMenu.INTERNET:
            frame = FrameMenuInternet(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif self.pointer == FrameMenu.MEMORY:
            frame = FrameMenuMemory(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif self.pointer == FrameMenu.RESTORE:
            frame = FrameMenuRestore(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif self.pointer == FrameMenu.BACKUP:
            frame = FrameMenuBackup(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif self.pointer == FrameMenu.USER:
            frame = FrameMenuUser(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif self.pointer == FrameMenu.DEVELOP:
            frame = FrameMenuDevelop(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif self.pointer == FrameMenu.ABOUT:
            frame = FrameMenuAbout(self.hmi_screen)
            self.hmi_screen.push_frame(frame)
        elif self.pointer == FrameMenu.POWER:
            frame = FrameMenuPower(self.hmi_screen)
            self.hmi_screen.push_frame(frame)

    def get_image(self):
        self.draw()
        return self.layout.get_image()

def main():
    frame = FrameMenu("hmi")
    frame.set_content("Sensor")
    frame.draw()
    frame.layout.background.show()
    # frame.show()

if __name__ == "__main__":
    main()