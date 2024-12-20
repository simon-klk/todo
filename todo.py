# Hier kommen die ToDos rein

import datetime
import sqlite3
from DBcreation import *


db = sqliteDB(sqlite3.connect("Listen.db"))



class ToDo:
    def __init__(self, text, beschreibung, end_datum, liste):
        self.text = text
        self.done = False
        self.datum = str(datetime.datetime.now().strftime("%Y-%m-%d"))
        self.beschreibung = beschreibung
        self.end_datum = end_datum  
        self.liste = liste
        
        db.cursor.execute("""
                          INSERT INTO items 
                          (item_text, list_ID, item_beschreibung, item_datum, item_end_datum) VALUES 
                          (?, ?, ?, ?, ?);
                          """, (self.text, self.liste, self.beschreibung, self.datum, self.end_datum))
        db.commit()
        

    def mark_as_done(self):
        self.done = True

    def mark_as_undone(self):
        self.done = False

class Liste:
    def __init__(self, name):
        self.name = name
        self.todos = []