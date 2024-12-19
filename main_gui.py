from todo import *
import customtkinter as tk

# Set the appearance mode to dark
tk.set_appearance_mode("dark")
tk.set_default_color_theme("blue")

main = tk.CTk()
main.title("To-Do List")
main.geometry("900x600")
main.resizable(False, False)


"""Leiste auswahl liste - oben"""

# Erstellen der Leiste oben
top_frame = tk.CTkFrame(main, width=892, height=60)
top_frame.place(x=5, y=5)

# Rechter Button für neue Liste


main.mainloop()