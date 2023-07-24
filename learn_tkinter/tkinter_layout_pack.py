import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Layout use pack")
window.geometry("400x600+100+0")

label1 = ttk.Label(window, text = "First label", background = "red")
label2 = ttk.Label(window, text = "Label 2", background = "blue")
label3 = ttk.Label(window, text = "Last of the label 3", background = "green")
button = ttk.Button(window, text = "Button")

label1.pack(side = "top", expand = True, padx = 10, fill = "both", pady = 10)
label2.pack(side = "left", expand = True, fill = "both")
label3.pack(side = "top", expand = True, fill = "both")
button.pack(side = "top", expand = True, fill = "both")

window.mainloop()