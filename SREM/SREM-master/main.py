import pygame
import assets
import player
import tests
import iso
import gui
import world
import interface
from tkinter import *

# The main game class that is intantiated on startup.
class Game:

    def __init__(self, w, h):
        pygame.init()
        self.width = w
        self.height = h
        self.window = None  # The pygame window Surface
        self.input = None
        self.view = None
        self.gui = None
        self.test = None
        self.done = False  # A flag for the game loop indicating if the game is done playing.
        self.player = None
        self.world = None
        self.interface = None

    def run(self):
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("SREM")
        pygame.display.set_icon(assets.load_image("icon.png"))

        self.view = iso.View(self.window)
        self.gui = gui.Gui(self.window)

        self.onInit()

        self.test = tests.TestIso(self)
        if self.test is not None:
            self.test.onInit()

        clock = pygame.time.Clock()

        while not self.done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                else:
                    self.gui.on_event(event)

            self.update(clock)
            self.draw()

            pygame.display.flip()
            clock.tick(60)

    def update(self, clock):
        self.world.update(clock)
        self.interface.update(clock)

    def draw(self):
        self.window.fill((0, 0, 0))
        self.view.draw()
        self.gui.draw()

    def onInit(self):
        self.player = player.Player(self)
        self.world = world.World(self)
        self.interface = interface.Interface(self)
        self.world.create()
        self.interface.display()



def display_screen_size_dropdown():
    tk = Tk()
    tk.title("SREM")
    tk.geometry("300x120")
    tk.wm_iconphoto(False, PhotoImage(file="assets/pixel/icon.png"))

    label = Label(tk, text="Select window size:")
    label.pack()

    selected = StringVar()
    selected.set("600x800")

    def start():
        size_str = selected.get()
        w = int(size_str.split("x")[0])
        h = int(size_str.split("x")[1])
        tk.withdraw()
        tk.quit()
        game = Game(w, h)
        game.run()

    options = [
        "600x600",
        "600x700",
        "600x800"
    ]

    dropdown = OptionMenu(tk, selected, *options)
    dropdown.pack()
    ok_button = Button(tk, text="OK", command=start)
    ok_button.pack()
    tk.mainloop()


if __name__ == "__main__":
    display_screen_size_dropdown()
