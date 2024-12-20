import customtkinter as tk

class ToDoFrame(tk.CTkFrame):
    def __init__(self, master, x, y, todo):
        super().__init__(master, width=150, height=150)
        self.place(x=x, y=y)

        self.titel = tk.CTkLabel(self, text=todo, width=20, height=2)
        