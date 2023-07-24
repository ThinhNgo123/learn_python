from templates.Layout1 import Layout1
from templates.Menu import Menu, MenuEdit
from frame_Menu_Sensor_Protocol_Detail import FrameMenuSensorProtocolDetail

class FrameMenuSensorEdit:
    ACTION_UP = "up"
    ACTION_DOWN = "down"
    ACTION_BACK = "left"
    ACTION_OK = "enter"
    ACTION_DELETE = "delete"
    ACTION_WRITE = "write"

    TITLE_CENTER_X = 239
    TITLE_CENTER_Y = 44

    FIRST_FIELD_POS_X = 53
    FIRST_FIELD_POS_Y = 75

    FIRST_EDIT_POS_X = 283
    FIRST_EDIT_POS_Y = 75

    def __init__(self, hmi_screen):
        self.hmi_screen = hmi_screen
        self.layout = Layout1()
        self.field = Menu(self)
        self.field.set_title(center_x=FrameMenuSensorEdit.TITLE_CENTER_X, center_y=FrameMenuSensorEdit.TITLE_CENTER_Y)
        self.field.set_first_element_position(FrameMenuSensorEdit.FIRST_FIELD_POS_X, FrameMenuSensorEdit.FIRST_FIELD_POS_Y)
        self.edit = MenuEdit(self)
        self.edit.set_first_element_position(FrameMenuSensorEdit.FIRST_EDIT_POS_X, FrameMenuSensorEdit.FIRST_EDIT_POS_Y)
        self.edit_status = False
        self.field_name = [
            "Name",
            "ID",
            "Unit",
            "Status",
            "SPS",
            "Raw Value",
            "Calib Value",
            "Protocol",
            "Protocol detail",
            "Calib Function",
            "Calib Index A",
            "Calib Index B",
            "Calib Index C",
            "Calib Index D",
            "Alarm Status",
            "Alarm Activate",
            "Alarm Raw Lower",
            "Alarm Raw Upper",
            "Alarm Calib Lower",
            "Alarm Calib Upper",
            "Error Status",
            "Error Activate",
            "Error Raw Lower",
            "Error Raw Upper",
            "Error Calib Lower",
            "Error Calib Upper",
            "Limit Status",
            "Limit Activate",
            "Limit Calib Lower",
            "Limit Calib Upper"
        ]
        for field in self.field_name:
            self.field.add_element(field)
        
        #test
        self.edit.add_element("edit", "Temperature")
        self.edit.add_element("edit", "1")
        self.edit.add_element("edit", "oC")
        self.edit.add_element("edit", "Normal")
        self.edit.add_element("edit", "10 S/m")
        self.edit.add_element("edit", "4.23")
        self.edit.add_element("edit", "28.32")
        self.edit.add_element("edit", "Modbus RTU")
        self.edit.add_element("none")
        self.edit.add_element("edit", "Ax + B")
        self.edit.add_element("edit", "1")
        self.edit.add_element("edit", "1")
        self.edit.add_element("edit", "1")
        self.edit.add_element("edit", "1")
        self.edit.add_element("selection", "Off", "On")
        self.edit.add_element("selection", "Enable", "Disable")
        self.edit.add_element("edit", 4)
        self.edit.add_element("edit", 20)
        self.edit.add_element("edit", 4)
        self.edit.add_element("edit", 20)
        self.edit.add_element("selection", "Normal", "Easy", "Medium", "Hard")
        self.edit.add_element("selection", "Enable", "Disable")
        self.edit.add_element("edit", 4)
        self.edit.add_element("edit", 20)
        self.edit.add_element("edit", 4)
        self.edit.add_element("edit", 20)
        self.edit.add_element("selection", "Normal", "Easy", "Medium", "Hard")
        self.edit.add_element("selection", "Enable", "Disable")
        self.edit.add_element("edit", 0)
        self.edit.add_element("edit", 100)
        
    def set_title(self, title):
        self.field.set_title(title)

    def draw(self):
        element = self.field.get_element()
        self.layout.set_content(element[element.find(".") + 1:])
        self.layout.draw()
        self.field.draw()
        self.edit.draw()
        
    def event_handling(self, event):
        if event == FrameMenuSensorEdit.ACTION_UP:
            if not self.edit_status:
                self.field.event_handling("up")
            self.edit.event_handling("up")
        elif event == FrameMenuSensorEdit.ACTION_DOWN:
            if not self.edit_status:
                self.field.event_handling("down")
            self.edit.event_handling("down")
        elif event == FrameMenuSensorEdit.ACTION_BACK:
            if self.edit_status:
                self.edit.set_edit_status(False)
                self.edit_status = False
            else:
                self.hmi_screen.pop_frame()
        elif event == FrameMenuSensorEdit.ACTION_OK:
            if len(self.edit.pages):
                if self.edit.get_element().get_type() == "none":
                    frame = FrameMenuSensorProtocolDetail(self.hmi_screen)
                    frame.set_title(f"{self.field.title}.Protocol Detail")
                    self.hmi_screen.push_frame(frame)
                elif not self.edit_status:
                    self.edit_status = True
                    self.edit.set_edit_status(True)
        elif self.edit_status:
            if event == FrameMenuSensorEdit.ACTION_DELETE:
                self.edit.event_handling("delete")
            else:
                self.edit.event_handling(event)

    def get_image(self):
        self.draw()
        return self.layout.get_image()

def main():
    test = FrameMenuSensorEdit("hmi")
    test.draw()
    test.get_image().show()

if __name__ == "__main__":
    main()