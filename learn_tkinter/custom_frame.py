import tkinter as tk

class DataTable(tk.Frame):
    def __init__(self, master=None, data=None):
        super().__init__(master)
        self.data = data
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[i])):
                label = tk.Label(self, text=str(self.data[i][j]))
                label.grid(row=i, column=j)
                row.append(label)
            self.data[i] = row

root = tk.Tk()
data = [['Name', 'Age', 'Gender'],
        ['John', '25', 'Male'],
        ['Jane', '30', 'Female'],
        ['Bob', '40', 'Male']]
table = DataTable(root, data=data)
table.data[0][0]["text"] = "name"
root.mainloop()
