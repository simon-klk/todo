# Hier kommen die ToDos rein

import datetime


class ToDo:
    def __init__(self, text, beschreibung, end_datum, liste):
        self.text = text
        self.done = False
        self.datum = str(datetime.datetime.now().strftime("%d.%m.%Y"))
        self.beschreibung = beschreibung
        self.end_datum = end_datum  
        self.liste = liste

    def mark_as_done(self):
        self.done = True

    def mark_as_undone(self):
        self.done = False

class Liste:
    def __init__(self, name):
        self.name = name
        self.todos = []