import tkinter as tk

class ImageButton(tk.Button):
    def __init__(self, master=None, image=None, **kwargs):
        super().__init__(master, **kwargs)
        self.image = tk.PhotoImage(file=image)
        self.configure(image=self.image)

root = tk.Tk()
button = ImageButton(root, image='bird1.png')
button.pack()
root.mainloop()