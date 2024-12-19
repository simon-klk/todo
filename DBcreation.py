import sqlite3

connection = sqlite3.connect("Listen.db")
cursor = connection.cursor()

# Create Table that holds the ToDo-Lists
list_id = "list_ID INTEGER PRIMARY KEY AUTOINCREMENT"
list_name = "list_name varchar(20)"
list_elem = "list_elem int"
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

cursor.execute(items_string)

#Ausgaben
#cursor.execute("INSERT INTO items (item_text, item_beschreibung, item_datum, item_end_datum, list_ID) VALUES('Aufgabe 1', 'Beschreibung später machen', '2024-12-19', '2024-12-21', '1')")
#output = cursor.execute("SELECT * FROM items").fetchall()
#print(output)