from frame_Boosting import FrameBoosting

class HMIScreen:

    def __init__(self):
        self.frame_stack = []
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
        self.frame_stack[-1].event_handling(event)

    def update(self):
        pass

    def get_screen(self):
        return self.frame_stack[-1].get_image()

def main():
    pass

if __name__ == "__main__":
    main()