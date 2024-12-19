import sqlite3

connection = sqlite3.connect("Listen.db")
cursor = connection.cursor()

# Create Table that holds the ToDo-Lists

list_id = "list_ID int NOT NULL AUTO_INCREMENT"
list_name = "list_name varchar(20)"
list_elem = "list_elem int"
list_beschreibung = "list_beschreibung varchar(200)"
list_erstelldatum = "list_erstelldatum date"
list_setPrimary = "PRIMARY KEY (list_ID)"

lists_string = f"CREATE TABLE IF NOT EXISTS listen(  {list_id},{list_name},{list_elem},{list_beschreibung},{list_erstelldatum},{list_setPrimary}  );"
cursor.execute(lists_string)
