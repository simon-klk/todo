# Hier kommen die ToDos rein

class ToDo:
    def __init__(self, text, beschreibung, datum, end_datum):
        self.text = text
        self.done = False


    def mark_as_done(self):
        self.done = True

    def mark_as_undone(self):
        self.done = False
