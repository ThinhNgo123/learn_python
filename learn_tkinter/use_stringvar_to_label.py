# import tkinter as tk
# import tkinter.messagebox as msg

# class LabelText:
#     def __init__(self, label):
#         self.label = label
#         self.text = ""
        
#     def set(self, text):
#         self.text = text
#         self.label['text'] = self.text

# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
        
#         self.label = tk.Label(self)
#         self.label.pack()

#         self.label_text = LabelText(self.label)

#         self.button = tk.Button(self, text='hello', command=self.hello)
#         self.button.pack()

#     def hello(self):
#         self.label_text.set('game')
#         self.button['command'] = self.show

#     def show(self):
#         if msg.askyesno("Warning", "Chuong trinh dong sau 2 giay"):
#             self.label_text.set("Chuong trinh dong sau 2 giay")
#             self.after(2000, self.destroy)
        
# # help(msg.askyesno)
# app = App()
# app.mainloop()

import tkinter as tk
import tkinter.messagebox as msgbox

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        help(self.tk)
        self.title("Hello Tkinter")
        self.label_text = tk.StringVar()
        self.label_text.set("My Name Is: ")
        self.name_text = tk.StringVar()
        self.label = tk.Label(self, textvar=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=10)
        self.name_entry = tk.Entry(self, textvar=self.name_text)
        self.name_entry.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)
        hello_button = tk.Button(self, text="Say Hello", command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))
        goodbye_button = tk.Button(self, text="Say Goodbye", command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))

    def say_hello(self):
        message = "Hello there " + self.name_text.get()
        msgbox.showinfo("Hello", message)
    def say_goodbye(self):
        if msgbox.askyesno("Close Window?", "Would you like to close this window?"):
            message = "Window will close in 2 seconds - goodybye " + self.name_text.get()
            self.label_text.set(message)
            self.after(2000, self.destroy)
        else:
            msgbox.showinfo("Not Closing", "Great! This window will stay open.")

win = Window()
win.mainloop()