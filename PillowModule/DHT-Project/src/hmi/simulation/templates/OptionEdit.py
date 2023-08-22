class OptionEdit:
    TYPE = "edit"

    MAX_CHAR = 100

    def __init__(self, text:str=None):
        if text:
            self.text = text
        else:
            self.text = ""
        self.max_char = OptionEdit.MAX_CHAR

    def set_max_char(self, max_char:int):
        self.max_char = max_char

    def get_text(self):
        if len(self.text) > self.max_char: 
            return self.text[:self.max_char] + "..."
        else:
            return self.text

    def get_type(self):
        return OptionEdit.TYPE

class OptionSelection:
    TYPE = "selection"

    ACTION_UP = "up"
    ACTION_DOWN = "down"

    def __init__(self, selection):
        self.selection_list = selection
        self.index = 0

    def event_handling(self, event):
        if event == OptionSelection.ACTION_UP:
            self.index = (self.index + 1) % len(self.selection_list)
        elif event == OptionSelection.ACTION_DOWN:
            self.index -= 1
            if self.index <= -1:
                self.index = len(self.selection_list) - 1

    def get_text(self):
        return self.selection_list[self.index]

    def get_type(self):
        return OptionSelection.TYPE

class OptionNone:
    TYPE = "none"

    def __init__(self):
        pass

    def get_type(self):
        return OptionNone.TYPE
