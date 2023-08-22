from frame_Boosting import FrameBoosting

class HMIScreen:
    LAST_FRAME_INDEX = -1

    def __init__(self):
        self.frame_stack = []
        self.current_frame = HMIScreen.LAST_FRAME_INDEX
        self.init()

    def init(self):
        self.frame_stack.append(FrameBoosting(self))

    def push_frame(self, frame):
        self.frame_stack.append(frame)
        # print(self.frame_stack)

    def pop_frame(self):
        if len(self.frame_stack) >= 1:
            self.frame_stack.pop()
        # print(self.frame_stack)

    def event_handling(self, event):
        self.frame_stack[self.current_frame].event_handling(event)

    def update(self):
        pass

    def get_screen(self):
        return self.frame_stack[self.current_frame].get_image()

if __name__ == "__main__":
    pass