class screen():
    name = "screen name"
    def __init__(self) -> None:
        pass
    def set_name(self,name):
        self.name = name
        print("Change the current screen to " + self.name + " screen")
        
Current_Screen = screen()