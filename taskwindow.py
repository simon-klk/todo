import todo as td
import customtkinter as tk
from datetime import datetime

class TaskWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Aufgabe hinzufügen")
        self.root.geometry("350x450")

        self.task_text = tk.CTkEntry(self.root, placeholder_text="Aufgabe")
        self.task_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        self.task_description = tk.CTkEntry(self.root, placeholder_text="Beschreibung")
        self.task_description.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.task_date = tk.CTkEntry(self.root, placeholder_text="Datum")
        self.task_date.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.task_date.insert(0, datetime.now().strftime("%Y-%m-%d"))

        self.task_end_date = tk.CTkEntry(self.root, placeholder_text="Enddatum")
        self.task_end_date.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.add_task_button = tk.CTkButton(self.root, text="Aufgabe hinzufügen", command=self.add_task)
        self.add_task_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        self.tasks = []

    def add_task(self):
        text = self.task_text.get()
        beschreibung = self.task_description.get()
        datum = self.task_date.get()
        end_datum = self.task_end_date.get()

        new_task = td.ToDo(text, beschreibung, datum, end_datum)
        self.tasks.append(new_task)
        print(f"Aufgabe hinzugefügt: {new_task.text}")

if __name__ == "__main__":
    tk.set_appearance_mode("dark")
    tk.set_default_color_theme("blue")

    main = tk.CTk()
    app = TaskWindow(main)
    main.mainloop()