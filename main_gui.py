from todo import *
from new_list import *
from todo_frame import *
# from taskwindow import *
import customtkinter as tk

listes = ["Arbeit", "Privat", "Einkaufen", "Schule", "Sonstiges"]
todos = ["Schuhe putzen", "Rainer telefonieren", "Banane"]

# Set the appearance mode to dark
tk.set_appearance_mode("dark")
tk.set_default_color_theme("blue")

# Create the main window
main = tk.CTk()
main.title("To-Do List")
main.geometry("900x600")
main.resizable(False, False)

# Create the font after initializing the main window
myfont = tk.CTkFont(family="Arial", size=16)

"""Buttons - oben"""
# Open List Button

def open_list(list_id):
    todo_list = ToDoList(main, listes[list_id])
    todo_list.import_todo()


# Frame für die Auswahl der Liste
top_frame = tk.CTkFrame(main, width=892, height=60)
top_frame.place(x=5, y=5)

# Button für die Erstellung einer neuen Liste
new_list_button = tk.CTkButton(top_frame, text="Neue Liste", width=90, height=40)
new_list_button.place(x=790, y=10)

# Listen anzeigen
def show_list():
    def on_click(list_name):
        open_list(listes.index(list_name))

    list_buttons = []
    i = 10
    for list_name in listes:    
        list_button = tk.CTkButton(top_frame, text=list_name, width=90, height=40, command=lambda name=list_name: on_click(name))
        list_button.place(x=i, y=10)
        list_buttons.append(list_button)
        i += 100

    
"""Liste der ToDos - Mitte"""
class ToDoList:
    def __init__(self, master, name):
        self.master = master
        self.frame = tk.CTkFrame(self.master, width=892, height=400)
        self.frame.place(x=5, y=70)
        self.label = tk.CTkLabel(self.frame, text=name, font=myfont, width=100, height=40)
        self.label.place(x=0, y=0)

    
    def import_todo(self):
        new_x = 5
        new_y = 50
        i = 1
        for todo in todos: 
            print(todo, new_x, new_y)
            ToDoFrame(master=self.frame, x=new_x, y=new_y, todo=todo)
            new_y += 50
            i += 1
            if i % 5 == 0:
                new_x = 5
                new_y = 50

        

show_list()
main.mainloop()