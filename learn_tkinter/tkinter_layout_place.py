import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Layout use place")
window.geometry("400x600+100+0")

label1 = ttk.Label(window, text = "Label 1", background = "red")
label2 = ttk.Label(window, text = "Label 2", background = "blue")
label3 = ttk.Label(window, text = "Label 3", background = "green")
button = ttk.Button(window, text = "Button")

label1.place(x = 100, y = 200)

window.mainloop()