# programme qui permet de créer la BDD avec les tables
import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())
    
connection.commit()
connection.close()