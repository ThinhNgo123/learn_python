# import tkinter as tk
# from tkinter import ttk

# window = tk.Tk()
# window.title("Layout use pack")
# window.geometry("400x600+100+0")

# label1 = ttk.Label(window, text = "First label", background = "red")
# label2 = ttk.Label(window, text = "Label 2", background = "blue")
# label3 = ttk.Label(window, text = "Label another", background = "green")
# label4 = ttk.Label(window, text = "A Button")
# label5 = ttk.Label(window, text = "Last of the labels", background = "orange")
# label6 = ttk.Label(window, text = "Another Button")
# button3 = ttk.Button(window, text = "Button 3")
# button4 = ttk.Button(window, text = "Button 4")
# button5 = ttk.Button(window, text = "Button 5")

# label1.pack(side = "top", expand = True, fill = "both")
# label2.pack(side = "top", expand = True, fill = "both")
# label3.pack(side = "top", expand = True, pady = 100)
# label4.pack(side = "left", expand = True, fill = "both")
# label5.pack(side = "left", expand = True, fill = "both")
# label6.pack(side = "left", expand = True, fill = "both")
# button3.pack(side = "top", expand = True, fill = "both")
# button4.pack(side = "top", expand = True, fill = "both")
# button5.pack(side = "top", expand = True, fill = "both")

# window.mainloop()

#use frame
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Layout use pack")
window.geometry("400x600+100+0")

#frame top
frame_top = ttk.Frame(window)
label1 = ttk.Label(frame_top, text = "First label", background = "red")
label2 = ttk.Label(frame_top, text = "Label 2", background = "blue")

label3 = ttk.Label(window, text = "Label another", background = "green")

#frame bottom
frame_bottom = ttk.Frame(window)
# frame_bottom_left = ttk.Frame(frame_bottom)
frame_bottom_right = ttk.Frame(frame_bottom)
label4 = ttk.Label(frame_bottom, text = "A Button", background = "white")
label5 = ttk.Label(frame_bottom, text = "Last of the labels", background = "orange")
label6 = ttk.Label(frame_bottom, text = "Another Button", background = "white")
button3 = ttk.Button(frame_bottom_right, text = "Button 3")
button4 = ttk.Button(frame_bottom_right, text = "Button 4")
button5 = ttk.Button(frame_bottom_right, text = "Button 5")

# layout top
frame_top.pack(expand = True, fill = "both")
label1.pack(expand = True, fill = "both")
label2.pack(expand = True, fill = "both")

label3.pack(expand = True)

#layout bottom
# frame_bottom_left.pack(side = "left", expand = True, fill = "both")
label4.pack(side = "left", expand = True, fill = "both")
label5.pack(side = "left", expand = True, fill = "both")
label6.pack(side = "left", expand = True, fill = "both")
frame_bottom_right.pack(side = "left", fill = "both")
button3.pack(expand = True, fill = "both")
button4.pack(expand = True, fill = "both")
button5.pack(expand = True, fill = "both")
frame_bottom.pack(expand = True, fill = "both", padx = 20, pady = 20)

window.mainloop()