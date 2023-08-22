from PIL import Image, ImageFont
try:
    from OptionEdit import OptionEdit, OptionSelection, OptionNone
except:
    from templates.OptionEdit import OptionEdit, OptionSelection, OptionNone

class Menu:
    TITLE_CENTER_X = 334.5
    TITLE_CENTER_Y = 45
    TITLE_FONT_SIZE = 24 
    # TITLE_FONT = ImageFont.truetype("Font/inter/Inter-VariableFont_slnt,wght.ttf", TITLE_FONT_SIZE)
    TITLE_FONT = ImageFont.truetype("Font/DejaVuSans/DejaVuSans.ttf", TITLE_FONT_SIZE)
    FIRST_ELEMENT_POS_X = 220
    FIRST_ELEMENT_POS_Y = 75
    ELEMENT_HEIGHT = 26
    TITLE_COLOR = (233, 216, 166)
    CURSOR_IMAGE = Image.open("Image/auto_fix.png")
    DISTANCE_BETWEEN_ELEMENTS = 0
    DISTANCE_BETWEEN_CURSOR_AND_ELEMENT = 5 
    MAX_ROW = 8
    ACTION_UP = "up"
    ACTION_DOWN = "down"
    ACTION_OK = "enter"

    def __init__(self, frame, title=None):
        self.frame = frame
        self.title = title
        self.title_center_x = Menu.TITLE_CENTER_X
        self.title_center_y = Menu.TITLE_CENTER_Y
        self.title_color = Menu.TITLE_COLOR
        self.element_color = Menu.TITLE_COLOR
        self.first_element_pos_x = Menu.FIRST_ELEMENT_POS_X
        self.first_element_pos_y = Menu.FIRST_ELEMENT_POS_Y
        self.element_height = Menu.ELEMENT_HEIGHT
        self.distance_between_cursor_and_element = Menu.DISTANCE_BETWEEN_CURSOR_AND_ELEMENT
        self.distance_between_elements = Menu.DISTANCE_BETWEEN_ELEMENTS
        self.cursor = 0
        self.cursor_status = True
        self.cursor_image = Menu.CURSOR_IMAGE
        self.cursor_image_width = self.cursor_image.width
        self.cursor_pos_x = self.calc_cursor_pos_x()
        self.cursor_pos_y = self.first_element_pos_y + 2
        self.pages = []
        self.page_current_number = 0
        self.max_row = Menu.MAX_ROW

    def set_element_height(self, height):
        self.element_height = height

    def set_title(self, title: str=None, center_x=None, center_y=None, color=None):
        if title:
            self.title = title
        if center_x:
            self.title_center_x = center_x
        if center_y:
            self.title_center_y = center_y
        if isinstance(color, tuple) and len(color) == 3:
            self.title_color = color

    def set_element_color(self, color):
        if isinstance(color, tuple) and len(color) == 3:
            self.element_color = color

    def set_first_element_position(self, pos_x=None, pos_y=None):
        if isinstance(pos_x, float) or isinstance(pos_x, int):
            self.first_element_pos_x = pos_x
            self.cursor_pos_x = self.calc_cursor_pos_x()
            # print("pos_x", self.cursor_pos_x)
        if isinstance(pos_y, float) or isinstance(pos_y, int):
            self.first_element_pos_y = pos_y
            self.cursor_pos_y = pos_y + 2

    def set_distance_between_cursor_and_element(self, distance):
        if isinstance(distance, float) or isinstance(distance, int):
            self.distance_between_cursor_and_element = distance
            self.cursor_pos_x = self.calc_cursor_pos_x()

    def set_distance_between_elements(self, distance):
        if isinstance(distance, float) or isinstance(distance, int):
            self.distance_between_elements = distance

    def set_max_row(self, max_row: int):
        self.max_row = max_row

    def set_cursor_image(self, image_path):
        self.cursor_image = Image.open(image_path)
        self.cursor_image_width = self.cursor_image.width
        self.cursor_pos_x = self.calc_cursor_pos_x()

    def calc_cursor_pos_x(self):
        return (self.first_element_pos_x - \
            self.distance_between_cursor_and_element - \
                self.cursor_image_width)

    def draw_text(self, pos_x, pos_y, text, fill, anchor):
        self.frame.layout.add_text(
            (pos_x, pos_y),
            text,
            fill,
            Menu.TITLE_FONT,
            anchor)

    def draw_title(self):
        self.draw_text(
            self.title_center_x, 
            self.title_center_y,
            text=self.title,
            fill=self.title_color,
            anchor="ma")

    def draw_elements(self):
        page = self.pages[self.page_current_number]
        for index in range(len(page)):
            pos_y = self.first_element_pos_y + (self.element_height + self.distance_between_elements) * index
            self.draw_text(
                self.first_element_pos_x,
                pos_y,
                text=page[index],
                fill=self.element_color,
                anchor="la")

    def hide_cursor(self):
        self.cursor_status = False

    def show_cursor(self):
        self.cursor_status = True

    def draw(self):
        self.draw_title()
        if len(self.pages) > 0:
            self.draw_cursor()
            self.draw_elements()

    def draw_cursor(self):
        if self.cursor_status:
            cursor_current_pos_y = self.cursor_pos_y + (self.element_height + self.distance_between_elements) * self.cursor
            # print(self.cursor_pos_x, cursor_current_pos_y)
            self.frame.layout.add_image(
                image=self.cursor_image,
                x=self.cursor_pos_x,
                y=cursor_current_pos_y)

    def add_element(self, element):
        if isinstance(element, str) or isinstance(element, float) or isinstance(element, int):
            if len(self.pages) == 0:
                self.pages.append([element])
            else:
                if len(self.pages[-1]) < self.max_row:
                    self.pages[-1].append(element)
                else:
                    self.pages.append([element])

    def event_handling(self, event):
        if len(self.pages) > 0:
            if event == Menu.ACTION_UP:
                self.up_event()
            elif event == Menu.ACTION_DOWN:
                self.down_event()
            elif event == Menu.ACTION_OK:
                self.ok_event()

    def up_event(self):
        self.cursor -= 1
        if self.cursor < 0:
            self.page_current_number -= 1
            if self.page_current_number < 0:
                self.page_current_number = len(self.pages) - 1
            self.cursor = len(self.pages[self.page_current_number]) - 1

    def down_event(self):
        self.cursor += 1
        if self.cursor >= len(self.pages[self.page_current_number]):
            self.cursor = 0
            self.page_current_number += 1
            if self.page_current_number >= len(self.pages):
                self.cursor = 0
                self.page_current_number = 0

    def ok_event(self):
        pass

    def get_element(self):
        if len(self.pages) > 0:
            return self.pages[self.page_current_number][self.cursor]
        else:
            return "No data"

    def clear_elements(self):
        self.pages = []

class MenuMonitoring(Menu):
    ACTION_DOWN = "down"
    ACTION_UP = "up"
    ACTION_CHANGE_STATUS = "enter"

    STATUS_STRING_TO_NUMBER = {"normal": 0, "calib": 1, "error": 2, "disable": 3}
    
    STATUS = {
        0: {
            "image": Image.open("./Image/check_circle_status.png"),
            "color": (6, 214, 160)
        },
        1: {
            "image": Image.open("./Image/compass_calibration_status.png"),
            "color": (202, 103, 2)
        },
        2: {
            "image": Image.open("./Image/error_status.png"),
            "color": (239, 71, 111)
        },
        3: {
            "image": Image.open("./Image/cancel_status.png"),
            "color": (7, 59, 76) 
        }
    }

    FIRST_STATUS_POS_X = 179
    FIRST_STATUS_POS_Y = 84
    FIRST_NAME_POS_X = 207
    FIRST_NAME_POS_Y = 81
    FIRST_VALUE_CENTER_POS_X = 413
    FIRST_VALUE_POS_Y = 81
    # FIRST_ELEMENT_CENTER_POS_X = 413
    # ELEMENT_COLOR = (6, 214, 160)

    TYPE_STATUS_AND_NAME = "status-name"
    TYPE_NAME_AND_VALUE = "name-value"
    TYPE_STATUS_NAME_VALUE = "status-name-value"

    def __init__(self, frame, type, title=None):
        super().__init__(frame, title)
        # self.first_element_pos_x = MenuMonitoringValue.FIRST_ELEMENT_CENTER_POS_X
        # self.element_color = MenuMonitoringValue.ELEMENT_COLOR
        # print(self.first_element_pos_y)
        self.is_show_status = False
        self.is_show_name = False
        self.is_show_value = False
        self.first_status_pos_x = MenuMonitoring.FIRST_ELEMENT_POS_X
        self.first_status_pos_y = MenuMonitoring.FIRST_ELEMENT_POS_Y
        self.first_name_pos_x = MenuMonitoring.FIRST_NAME_POS_X
        self.first_name_pos_y = MenuMonitoring.FIRST_NAME_POS_Y
        self.first_value_center_pos_x = MenuMonitoring.FIRST_VALUE_CENTER_POS_X
        self.first_value_pos_y = MenuMonitoring.FIRST_VALUE_POS_Y

        if type == MenuMonitoring.TYPE_NAME_AND_VALUE:
            self.is_show_name = True
            self.is_show_value = True
        elif type == MenuMonitoring.TYPE_STATUS_AND_NAME:
            self.is_show_status = True
            self.is_show_name = True
        elif type == MenuMonitoring.TYPE_STATUS_NAME_VALUE:
            self.is_show_status = True
            self.is_show_name = True
            self.is_show_value = True

    def set_first_status_position(self, pos_x=None, pos_y=None):
        if pos_x:
            self.first_status_pos_x = pos_x
        if pos_y:
            self.first_status_pos_y = pos_y

    def set_first_name_position(self, pos_x=None, pos_y=None):
        if pos_x:
            self.first_name_pos_x = pos_x
        if pos_y:
            self.first_name_pos_y = pos_y

    def set_first_value_position(self, center_x=None, pos_y=None):
        if center_x:
            self.first_value_center_pos_x = center_x
        if pos_y:
            self.first_value_pos_y = pos_y

    def add_element(self, status:str=None, name:str=None, value:str=None):
        element = []
        element.append(MenuMonitoring.STATUS_STRING_TO_NUMBER[status] if status else None)
        element.append(name if name else None)
        element.append(value if value else None)

        if len(self.pages) == 0:
            self.pages.append([element])
        else:
            if len(self.pages[-1]) < self.max_row:
                self.pages[-1].append(element)
            else:
                self.pages.append([element])
            
    def draw(self, anchor_value="ma"):
        self.draw_title()
        if len(self.pages) > 0:
            self.draw_cursor()
            self.draw_elements(anchor_value)

    def draw_elements(self, anchor):
        if len(self.pages) > 0:
            page = self.pages[self.page_current_number]
            if self.is_show_status:
                self.draw_status(page)
            if self.is_show_name:
                self.draw_names(page)
            if self.is_show_value:
                self.draw_values(page, anchor)

    def draw_status(self, page):
        for index in range(len(page)):
            pos_y = self.first_status_pos_y + (self.element_height + self.distance_between_elements) * index
            self.frame.layout.add_image(
                MenuMonitoring.STATUS[page[index][0]]["image"],
                self.first_status_pos_x,
                pos_y)

    def draw_names(self, page):
        for index in range(len(page)):
            pos_y = self.first_name_pos_y + (self.element_height + self.distance_between_elements) * index
            # print(self, MenuMonitoring.STATUS[page[index][0]]["color"])
            self.draw_text(
                self.first_name_pos_x,
                pos_y,
                text=page[index][1],
                fill=(255, 255, 255), #MenuMonitoring.STATUS[page[index][0]]["color"],
                anchor="la")

    def draw_values(self, page, anchor):
        for index in range(len(page)):
            pos_y = self.first_value_pos_y + (self.element_height + self.distance_between_elements) * index
            self.draw_text(
                self.first_value_center_pos_x,
                pos_y,
                text=page[index][2],
                fill=(255, 255, 255),#MenuMonitoring.STATUS[page[index][0]]["color"],
                anchor=anchor)

    def event_handling(self, event):
        if event == MenuMonitoring.ACTION_DOWN:
            self.down_event()
        elif event == MenuMonitoring.ACTION_UP:
            self.up_event()
        elif event == MenuMonitoring.ACTION_CHANGE_STATUS:
            self.change_status_event()

    def change_status_event(self):
        element = self.pages[self.page_current_number][self.cursor]
        if element[0] != MenuMonitoring.STATUS_STRING_TO_NUMBER["disable"]: #Check if the status is disabled or not
            element[0] = (element[0] + 1) % 3 

class MenuEdit(Menu):
    # ACTION_DOWN = "down"
    # ACTION_UP = "up"
    ACTION_ADD_LETTER = "add" 
    ACTION_DELETE_LETTER = "delete"
    ACTION_BACK = "left"
    ACTION_NEXT = "right"

    OPTION_EDIT = "edit"
    OPTION_SELECTION = "selection"
    OPTION_NONE = "none"

    POINTER_SPEED = 25
    FONT = ImageFont.truetype("./Font/inter/Inter-VariableFont_slnt,wght.ttf", 24)
    ELEMENT_COLOR = (148, 210, 189)
    ELEMENT_COLOR_SELECTION = (202, 103, 2)
    FIRST_ELEMENT_POS_X = 189
    FIRST_ELEMENT_POS_Y = 75

    MAX_CHAR = 100

    def __init__(self, frame):
        super().__init__(frame)
        self.hide_cursor()
        self.pointer_speed = MenuEdit.POINTER_SPEED
        self.pointer_counter = 0
        self.font = MenuEdit.FONT
        self.first_element_pos_x = MenuEdit.FIRST_ELEMENT_POS_X
        self.first_element_pos_y = MenuEdit.FIRST_ELEMENT_POS_Y
        self.element_color = MenuEdit.ELEMENT_COLOR
        self.element_color_selection = MenuEdit.ELEMENT_COLOR_SELECTION
        # self.pointer_status = 0
        # self.pointer = False
        self.edit_status = False
        self.max_char = MenuEdit.MAX_CHAR
        self.edit_position = 0 #the first position of string 

    def set_max_char(self, max_char:int):
        self.max_char = max_char
        for page in self.pages:
            for element_object in page:
                if isinstance(element_object, OptionEdit):
                    element_object.set_max_char(self.max_char)

    def set_edit_status(self, status:bool):
        self.edit_status = status
        self.edit_position = 0
        # if self.get_element().get_type() == "edit":
        #     if status:
        #         self.show_pointer()
        #     else:
        #         self.hide_pointer()

    def hide_pointer(self):
        self.pointer = False

    def show_pointer(self):
        self.pointer = True

    def set_pointer_speed(self, speed:int):
        if speed > 0:
            self.pointer_speed = speed

    def pointer_counter_increase(self):
        self.pointer_counter += 1
        if self.pointer_counter >= self.pointer_speed - 1:
            self.pointer_counter = 0
            self.pointer_status = (self.pointer_status + 1) % 2

    def draw_pointer(self):
        if self.pointer and self.pointer_status:
            pos_y = self.first_element_pos_y + (self.element_height + self.distance_between_elements) * self.cursor
            self.draw_text(
                self.first_element_pos_x + self.get_current_string_length() + 2,
                pos_y,
                text="|",
                fill=self.element_color,
                anchor="ma"
            )

    def get_current_string_length(self):
        return self.font.getlength(self.get_element().get_text())

    def event_handling(self, event):
        if event == MenuEdit.ACTION_UP:
            self.up_event()
        elif event == MenuEdit.ACTION_DOWN:
            self.down_event()
        elif event == MenuEdit.ACTION_BACK:
            self.back_event()
        elif event == MenuEdit.ACTION_NEXT:
            self.next_event()
        elif event == MenuEdit.ACTION_DELETE_LETTER:
            self.delete_letter()
        elif event == MenuEdit.ACTION_ADD_LETTER:
            self.add_letter()

    def up_event(self):
        if self.edit_status:
            element = self.get_element()
            if element.get_type() == "selection":
                element.event_handling("up")
            elif element.get_type() == "edit":
                self.set_up_char()
        else:
            if len(self.pages) > 0:
                super().up_event()

    def down_event(self):
        if self.edit_status:
            element = self.get_element()
            if element.get_type() == "selection":
                element.event_handling("down")
            elif element.get_type() == "edit":
                self.set_down_char()
        else:
            if len(self.pages) > 0:
                super().down_event()

    def next_event(self):
        if self.edit_status and isinstance(self.pages[self.page_current_number][self.cursor], OptionEdit):
            self.edit_position += 1
            length = len(self.get_element().get_text())
            if self.edit_position > length:
                self.edit_position = 0 

    def back_event(self):
        if self.edit_status and isinstance(self.pages[self.page_current_number][self.cursor], OptionEdit):
            self.edit_position -= 1
            if self.edit_position < 0:
                self.edit_position = len(self.pages[self.page_current_number][self.cursor].get_text())

    def set_up_char(self):
        element = self.get_element()
        text = element.get_text()
        if self.edit_position <= len(text) - 1:
            ascii_decimal = ord(text[self.edit_position]) - 1
            if ascii_decimal < 32:
                ascii_decimal = 126
            element.text = text[:self.edit_position] + chr(ascii_decimal) + text[self.edit_position + 1:]


    def set_down_char(self):
        print("down")
        element = self.get_element()
        text = element.get_text()
        if self.edit_position <= len(text) - 1:
            print("down")
            ascii_decimal = ord(text[self.edit_position]) + 1
            if ascii_decimal > 126:
                ascii_decimal = 32
            element.text = text[:self.edit_position] + chr(ascii_decimal) + text[self.edit_position + 1:]

    def add_letter(self):
        text_object = self.get_element()
        text = text_object.text
        length = len(text)
        if self.edit_position <= length - 1: 
            text_object.text = text[:self.edit_position] + "_" + text[self.edit_position:]
        elif self.edit_position == length:
            text_object.text = text + "_"

    def delete_letter(self):
        text_object = self.get_element()
        text = text_object.text
        length = len(text)
        if length > 1:
            if self.edit_position <= length - 2:
                text_object.text = text[:self.edit_position] + text[self.edit_position + 1:]
            elif self.edit_position == length - 1:
                text_object.text = text[:self.edit_position]
                self.edit_position = length - 2 

    def draw(self):
        # print("draw")
        super().draw()

    def add_element(self, type, *args):
        if type == MenuEdit.OPTION_NONE:
            element_object = OptionNone()
        elif type == MenuEdit.OPTION_EDIT:
            if isinstance(*args, str) or isinstance(*args, float) or isinstance(*args, int):
                element_object = OptionEdit(str(*args))
                element_object.set_max_char(self.max_char)
        elif type == MenuEdit.OPTION_SELECTION:
            if isinstance(args , tuple):
                element_object = OptionSelection(list(args))
        else:
            return
        if len(self.pages) == 0:
            self.pages.append([element_object])
        else:
            if len(self.pages[-1]) < self.max_row:
                self.pages[-1].append(element_object)
            else:
                self.pages.append([element_object])

    def draw_elements(self):
        page = self.pages[self.page_current_number]
        for index in range(len(page)):
            element = page[index]
            if not (element.get_type() == "none"):
                text = element.get_text()
                color = self.element_color
                pos_y = self.first_element_pos_y + (self.element_height + self.distance_between_elements) * index
                if self.edit_status and self.cursor == index:
                    if isinstance(element, OptionSelection):
                        color = self.element_color_selection
                    elif isinstance(element, OptionEdit):
                        if self.edit_position <= len(text) - 1:
                            text = text[:self.edit_position] + "[" + text[self.edit_position] + "]" + text[self.edit_position + 1:]
                            # print("text", text)
                        else:
                            text = text + "[]"
                            # print("text1", text)
                self.draw_text(
                    self.first_element_pos_x,
                    pos_y,
                    text=text,
                    fill=color,
                    anchor="la")

    def get_element(self):
        if len(self.pages) > 0:
            return self.pages[self.page_current_number][self.cursor]
        return None

if __name__ == "__main__":
    # test = Menu("frame")
    # for i in range(10):
    #     test.add_element(i+1)
    # test.cursor = 6
    # test.event_handling("down")
    # test.event_handling("down")
    # test.event_handling("down")
    # test.event_handling("down")


    # print(test.cursor)
    # test = MenuEdit("frame")
    # test.pages = [["hello", "hello", "hello"], ["hello", "hello", "hello"], ["hello", "hello"]]
    # test.page_current_number = 1
    # test.delete_letter()
    # test.delete_letter()
    # test.delete_letter()
    # test.delete_letter()
    # test.delete_letter()
    # test.delete_letter()
    # test.delete_letter()
    # test.delete_letter()
    # test.write_letter("a")
    # test.write_letter("a")
    # test.write_letter("a")
    # test.write_letter("a")
    # test.write_letter("a")
    # test.write_letter("a")
    # test.write_letter("a")
    # test.write_letter("a")
    # test.write_letter("a")
    # test.write_letter("a")
    # test.write_letter("a")
    # test.write_letter("a")
    # print(test.pages)

    test = MenuEdit("frame")
    test.add_element("edit", "kkk", "a", "b", "c")