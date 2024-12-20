import todo as td
import customtkinter as tk
from datetime import datetime
from tkcalendar import Calendar, DateEntry
from DBcreation import *
import sqlite3



db = sqliteDB(sqlite3.connect("Listen.db"))

class TaskWindow:
    def __init__(self, list_id, refresh_callback=None):
        self.root = tk.CTkToplevel()  # Changed from CTk to CTkToplevel
        self.root.title("Aufgabe hinzufügen")
        self.root.geometry("350x450+100+100")
        self.root.attributes('-topmost', True)
        self.list_id = list_id
        self.refresh_callback = refresh_callback
        

        self.task_text = tk.CTkEntry(self.root, placeholder_text="Aufgabe")
        self.task_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        self.task_description = tk.CTkEntry(self.root, placeholder_text="Beschreibung")
        self.task_description.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.task_date = tk.CTkEntry(self.root, placeholder_text="Datum")
        self.task_date.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.task_date.insert(0, datetime.now().strftime("%Y-%m-%d"))

        self.task_end_date = DateEntry(self.root, date_pattern='yyyy-mm-dd', show_calendar=True, width=20)
        self.task_end_date.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.add_task_button = tk.CTkButton(self.root, text="Aufgabe hinzufügen", command=self.add_task)
        self.add_task_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        self.tasks = []

    def add_task(self):
        text = self.task_text.get()
        beschreibung = self.task_description.get()
        datum = self.task_date.get()
        end_datum = self.task_end_date.get()
        liste = self.list_id
        new_task = td.ToDo(text, beschreibung, end_datum, liste)
        self.root.destroy()
        if self.refresh_callback:
            self.refresh_callback()
