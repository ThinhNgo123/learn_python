import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Layout intro")
window.geometry("600x400")

label1 = ttk.Label(window, text = "Label 1", background = "red")
label2 = ttk.Label(window, text = "Label 2", background = "blue")

#pack
# label1.pack(side = "left", expand = True, fill = "y")
# label2.pack(side= "right", expand = True, fill = "y")

#grid
# window.columnconfigure(0, weight = 1)
# window.columnconfigure(1, weight = 1)
# window.columnconfigure(2, weight = 2)
# window.rowconfigure(0, weight = 1)
# window.rowconfigure(1, weight = 1)

# label1.grid(row = 0, column = 1, sticky = "nesw")
# label2.grid(row = 1, column = 0, columnspan = 3, sticky = "nesw")

#place
label1.place(x = 100, y = 150, width = 200, height = 200)
label2.place(relx = 0.5, rely = 0.5, relwidth = 1, anchor = "sw")

window.mainloop()