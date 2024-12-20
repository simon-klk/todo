import sqlite3

class sqliteDB:

    def __init__(self, connection):     #connection = sqlite3.connect("Listen.db")
        self.connection = connection  
        self.cursor = self.connection.cursor()  

    def create_DB_and_Tables(self):

        # Create Table that holds the ToDo-Lists
        list_id = "list_ID INTEGER PRIMARY KEY AUTOINCREMENT"
        list_name = "list_name varchar(20)"
        list_elem = "list_elem int"     #Number of items inside LISTE
        list_beschreibung = "list_beschreibung varchar(200)"
        list_erstelldatum = "list_erstelldatum date"


        lists_string = f"""
                CREATE TABLE IF NOT EXISTS listen(  
                {list_id},
                {list_name},
                {list_elem},
                {list_beschreibung},
                {list_erstelldatum}  
                );
                """



        # Create Table that holds the Lists' items
        item_id = "item_ID INTEGER PRIMARY KEY AUTOINCREMENT"
        list_id = "list_ID INTEGER, FOREIGN KEY(list_ID) REFERENCES listen(list_ID)"
        item_text = "item_text varchar(20)"
        item_beschreibung = "item_beschreibung varchar(200)"
        item_datum = "item_datum date"
        item_enddatum = "item_end_datum date" 


        items_string = f"""
                CREATE TABLE IF NOT EXISTS items(
                {item_id},
                {item_text},
                {item_beschreibung},
                {item_datum},
                {item_enddatum},
                {list_id}
                );
                """

        self.cursor.execute(items_string)

    # Benutze Commit nach jeder Änderung (Update, Insert into, Delete)
    def commit(self):
        self.connection.commit()

    # Benutze Rollback um Änderungen rückgängig zu machen       (NOCH NICHT GETESTET)
    def rollback(self):
        self.connection.rollback()

    def close(self):
        self.cursor.close()
        self.connection.close()
        



