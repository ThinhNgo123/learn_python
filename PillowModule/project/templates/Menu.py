from PIL import Image, ImageFont
try:
    from OptionEdit import OptionEdit, OptionSelection, OptionNone
except:
    from templates.OptionEdit import OptionEdit, OptionSelection, OptionNone

class Menu:
    TITLE_CENTER_X = 334.5
    TITLE_CENTER_Y = 45
    TITLE_FONT_SIZE = 24 
    TITLE_FONT = ImageFont.truetype("Font/inter/Inter-VariableFont_slnt,wght.ttf", TITLE_FONT_SIZE)
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

class MenuMonitoringValue(Menu):
    FIRST_ELEMENT_CENTER_POS_X = 413
    ELEMENT_COLOR = (6, 214, 160)

    def __init__(self, frame, title):
        super().__init__(frame, title)
        self.first_element_pos_x = MenuMonitoringValue.FIRST_ELEMENT_CENTER_POS_X
        self.element_color = MenuMonitoringValue.ELEMENT_COLOR
        # print(self.first_element_pos_y)

    def draw_elements(self):
        page = self.pages[self.page_current_number]
        for index in range(len(page)):
            pos_y = self.first_element_pos_y + (self.element_height + self.distance_between_elements) * index
            self.draw_text(
                self.first_element_pos_x,
                pos_y,
                text=page[index],
                fill=self.element_color,
                anchor="ma")

class MenuEdit(Menu):
    ACTION_DOWN = "down"
    ACTION_UP = "up"
    ACTION_WRITE_LETTER = "write" 
    ACTION_DELETE_LETTER = "delete"
    ACTION_BACK = "left"

    OPTION_EDIT = "edit"
    OPTION_SELECTION = "selection"
    OPTION_NONE = "none"

    POINTER_SPEED = 25
    FONT = ImageFont.truetype("./Font/inter/Inter-VariableFont_slnt,wght.ttf", 24)
    ELEMENT_COLOR = (148, 210, 189)
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
        self.pointer_status = 0
        self.pointer = False
        self.edit_status = False
        self.max_char = MenuEdit.MAX_CHAR

    def set_max_char(self, max_char:int):
        self.max_char = max_char
        for page in self.pages:
            for element_object in page:
                if isinstance(element_object, OptionEdit):
                    element_object.set_max_char(self.max_char)

    def set_edit_status(self, status:bool):
        self.edit_status = status
        if self.get_element().get_type() == "edit":
            if status:
                self.show_pointer()
            else:
                self.hide_pointer()

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
            if self.edit_status:
                if self.get_element().get_type() == "selection":
                    self.get_element().event_handling("up")
            else:
                if len(self.pages) > 0:
                    self.up_event()
        elif event == MenuEdit.ACTION_DOWN:
            if self.edit_status:
                if self.get_element().get_type() == "selection":
                    self.get_element().event_handling("down")
            else:
                if len(self.pages) > 0:
                    self.down_event()
        elif event == MenuEdit.ACTION_DELETE_LETTER:
            if self.edit_status:
                if self.get_element().get_type() == "edit":
                    self.delete_letter()
        else:
            if self.edit_status:
                if self.get_element().get_type() == "edit":
                    self.write_letter(event)

    def write_letter(self, letter:str):
        text_object = self.get_element()
        text_object.text = text_object.text + letter

    def delete_letter(self):
        text_object = self.get_element()
        if len(text_object.text) > 0:
            text_object.text = text_object.text[:-1] 

    def draw(self):
        super().draw()
        element = self.get_element()
        if element:
            if element.get_type() == "edit" and self.pointer:
                self.pointer_counter_increase()
                self.draw_pointer()

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
            if not (page[index].get_type() == "none"):
                pos_y = self.first_element_pos_y + (self.element_height + self.distance_between_elements) * index
                self.draw_text(
                    self.first_element_pos_x,
                    pos_y,
                    text=page[index].get_text(),
                    fill=self.element_color,
                    anchor="la")

    def get_element(self):
        if len(self.pages) > 0:
            return self.pages[self.page_current_number][self.cursor]
        return None

def main():
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

if __name__ == "__main__":
    main()