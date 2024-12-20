from todo import *
from new_list import *
from todo_frame import *
from taskwindow import *
import customtkinter as tk
from DBcreation import *
import sqlite3



db = sqliteDB(sqlite3.connect("Listen.db"))

db.create_DB_and_Tables()
db.commit()

# db.cursor.execute("INSERT INTO items (item_text, list_ID, item_beschreibung, item_datum, item_end_datum) VALUES ('name',2, 'beschreibung', '2021-1-1', '2021-1-1')")
# db.commit()

# db.cursor.execute("SELECT list_name FROM listen")
# list_names = db.cursor.fetchall()

# db.cursor.execute("SELECT list_ID FROM listen")
# list_IDs = db.cursor.fetchall()

db.cursor.execute("SELECT * FROM listen")
lists = db.cursor.fetchall()






# todos = ["Schuhe putzen", "Rainer telefonieren", "Banane", "test1", "test2", "test3", ]




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

def open_list(list_name):
    todo_list = ToDoList(main, list_name)
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
        open_list(list_name)
        

    list_buttons = []
    i = 10
    for list in lists:    
        list_button = tk.CTkButton(top_frame, text=list[1], width=90, height=40, command=lambda name=list: on_click(name))
        list_button.place(x=i, y=10)
        list_buttons.append(list_button)
        i += 100

    
"""Liste der ToDos - Mitte"""
class ToDoList:
    def __init__(self, master, list):
        self.master = master
        self.frame = tk.CTkFrame(self.master, width=892, height=420)
        self.frame.place(x=5, y=70)
        self.label = tk.CTkLabel(self.frame, text=list[1], font=myfont, width=100, height=40)
        self.label.place(x=0, y=0)
        
        self.list_ID = list[0]
        """Button NEW TASK"""  
        new_task_button = tk.CTkButton(self.frame, text="Neue Aufgabe", width=90, height=40, command=lambda: TaskWindow(self.list_ID, self.refresh_todos)) #Welche Liste
        new_task_button.place(x=790, y=375)  
        
    def refresh_todos(self):
        # Clear existing todo frames
        for widget in self.frame.winfo_children():
            if isinstance(widget, ToDoFrame):
                widget.destroy()
        # Re-import todos
        self.import_todo()
    
    def import_todo(self):
        new_x = 5
        new_y = 50
        i = 0
        db.cursor.execute("SELECT * FROM items WHERE list_ID = ?", (self.list_ID,))
        todos = db.cursor.fetchall()
        for todo in todos: 
            

            ToDoFrame(master=self.frame, x=new_x, y=new_y, todo=todo)
            new_x += 180
            i += 1
            if i % 5 == 0:
                new_x = 5
                new_y = 220



show_list()
main.mainloop()