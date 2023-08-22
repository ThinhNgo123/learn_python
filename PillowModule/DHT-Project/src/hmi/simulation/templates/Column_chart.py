from PIL import ImageFont

class ColumnChart:
    GREEN = (6, 214, 160)
    ORANGE = (202, 103, 2)
    PINK = (239, 71, 111)
    BLUE = (7, 59, 76)
    YELLOW = (255, 255, 0)
    TITLE_COLOR = (233, 216, 166)
    COLORS = (GREEN, ORANGE, PINK, BLUE, YELLOW)
    MAX_COLUMN = len(COLORS)
    GAPSIZE1_DEFAULT = 5 #distance between title and column
    GAPSIZE2_DEFAULT = 5 #distance between column and text 
    GAPSIZE3_DEFAULT = 10 #distance between columns
    BOX_WIDTH_DEFAULT = 168
    BOX_HEIGHT_DEFAULT = 243
    BOX_POS_X = 0
    FONT_SIZE_DEFAULT = 24
    FONT_DEFAULT = ImageFont.truetype("Font/inter/Inter-VariableFont_slnt,wght.ttf", FONT_SIZE_DEFAULT)
    TITLE_POS_CENTER_X = 76.5
    TITLE_POS_CENTER_Y = 45
    MAX_COLUMN_HEIGHT = 128
    COLUMN_WIDTH = 28
    COLUMN_BORDER_RADIUS = 5
    MAX_COLUMN_POS_Y = 114

    def __init__(self, frame, title=None):
        self.frame = frame
        self.title = title
        self.title_pos_center_x = ColumnChart.TITLE_POS_CENTER_X
        self.title_pos_center_y = ColumnChart.TITLE_POS_CENTER_Y
        self.gap_size1 = ColumnChart.GAPSIZE1_DEFAULT
        self.gap_size2 = ColumnChart.GAPSIZE2_DEFAULT
        self.box_width = ColumnChart.BOX_WIDTH_DEFAULT
        self.box_height = ColumnChart.BOX_HEIGHT_DEFAULT
        self.box_pos_x = ColumnChart.BOX_POS_X
        self.font = ColumnChart.FONT_DEFAULT
        self.font_size = ColumnChart.FONT_SIZE_DEFAULT
        self.text_color = ColumnChart.TITLE_COLOR
        self.column = []
        self.gap_size3 = None
        self.max_column_pos_y = ColumnChart.MAX_COLUMN_POS_Y

    def set_title(self, title, center_x=None, center_y=None):
        self.title = title
        if isinstance(center_x, float):
            self.title_pos_center_x = center_x
        if isinstance(center_y, float):
            self.title_pos_center_y = center_y

    def set_distance_1(self, distance):
        if isinstance(distance, float):
            self.gap_size1 = distance

    def set_distance_2(self, distance):
        if isinstance(distance, float):
            self.gap_size2 = distance

    def set_box_width(self, width):
        if isinstance(width, float):
            self.box_width = width

    def set_box_height(self, height):
        if isinstance(height, float):
            self.box_height = height

    def set_box_pos_x(self, pos_x):
        if isinstance(pos_x, float):
            self.box_pos_x = pos_x

    def set_text_color(self, color):
        if isinstance(color, tuple) and len(color) == 3:
            self.text_color = color

    def calc_gapsize3(self):
        length = len(self.column)
        gap_size3 = (self.box_width - length * ColumnChart.COLUMN_WIDTH) / (length + 1)
        if gap_size3 > 0:
            self.gap_size3 = gap_size3
        else:
            self.gap_size3 = 0

    def draw_title(self):
        if isinstance(self.title, str):
            self.frame.layout.add_text(
                (self.title_pos_center_x, self.title_pos_center_y), 
                text=self.title, 
                fill=self.text_color, 
                font=self.font, 
                anchor="ma")

    def add_column(self, number: int, text: str):
        if len(self.column) < ColumnChart.MAX_COLUMN:
            self.column.append([number, text])

    def draw_column(self, x, y, height, color):
        self.frame.layout.get_draw().rounded_rectangle(
            ((x, y), (x + ColumnChart.COLUMN_WIDTH, y + height)),
            radius=ColumnChart.COLUMN_BORDER_RADIUS,
            fill=color)

    def draw_text(self, pos_x, pos_y, text, anchor="ma"):
        self.frame.layout.add_text(
            (pos_x, pos_y), 
            text, 
            self.text_color, 
            self.font, 
            anchor)

    def draw(self):
        self.draw_title()
        if len(self.column) > 0:
            self.calc_gapsize3()
            self.draw_column_group()

    def draw_column_group(self):
        numbers = [column[0] for column in self.column]
        max_number = max(numbers)
        for index in range(len(self.column)):
            column_pos_x = self.box_pos_x + (self.gap_size3 * (index + 1)) + (ColumnChart.COLUMN_WIDTH * index)
            if numbers[index] == max_number:
                column_height = ColumnChart.MAX_COLUMN_HEIGHT
                column_pos_y = self.max_column_pos_y
            else:
                column_height ,column_pos_y = self.calc_column_pos_y(max_number, numbers[index])
            text_center_x = column_pos_x + (ColumnChart.COLUMN_WIDTH // 2) 
            number_pos_y_bottom = column_pos_y - self.gap_size1
            text_pos_y = column_pos_y + column_height + self.gap_size2

            self.draw_text(
                text_center_x, 
                number_pos_y_bottom, 
                str(numbers[index]), 
                anchor="mb")
            self.draw_column(
                column_pos_x, 
                column_pos_y, 
                column_height, 
                color=ColumnChart.COLORS[index])
            self.draw_text(
                text_center_x, 
                text_pos_y, 
                text=self.column[index][1],
                anchor="ma")

    def calc_column_pos_y(self, max_number,number):
        column_height = ColumnChart.MAX_COLUMN_HEIGHT / (max_number / number)
        return column_height, (self.max_column_pos_y + (ColumnChart.MAX_COLUMN_HEIGHT - column_height))

def main():
    chart = ColumnChart("frame")

if __name__ == "__main__":
    main()