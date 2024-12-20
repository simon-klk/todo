import customtkinter as tk

class ToDoFrame(tk.CTkFrame):
    def __init__(self, master, x, y, todo):
        super().__init__(master, width=150, height=150)
        self.place(x=x, y=y)

        self.titel = tk.CTkLabel(self, text=todo[1], font=("Arial", 16), width=20, height=2)
        self.titel.place(x=10, y=10)
        self.beschreibung = tk.CTkLabel(self, text=todo[2], font=("Arial", 12), width=20, height=2)
        self.beschreibung.place(x=10, y=35)
        
        self.end_date = tk.CTkLabel(self, text=todo[4], font=("Arial", 14), width=20, height=2)
        self.end_date.place(x=10, y=120)
        
        self.edit_button = tk.CTkButton(self, text="B",font=("Arial", 16, "bold"), width=10, height=10)
        self.edit_button.place(x=120, y=120)
