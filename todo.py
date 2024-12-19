# Hier kommen die ToDos rein

class ToDo:
    def __init__(self, text, beschreibung, datum, end_datum, liste):
        self.text = text
        self.done = False


    def mark_as_done(self):
        self.done = True

    def mark_as_undone(self):
        self.done = False

class Liste:
    def __init__(self, name):
        self.name = name
        self.todos = []