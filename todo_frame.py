import customtkinter as tk

class ToDoFrame(tk.CTkFrame):
    def __init__(self, master, x, y, todo):
        super().__init__(master, width=150, height=150)
        self.place(x=5, y=70)
        self.label = tk.CTkLabel(self, text=todo, width=100, height=40)
        self.label.place(x=x, y=y)
        