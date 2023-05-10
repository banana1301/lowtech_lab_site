# programme qui permet d'initialiser la BDD avec les tables

import sqlite3 # importation de la bibliothéque sqlite3

connection = sqlite3.connect('database.db') # connection a la base database.db

with open('schema.sql') as f: # lecture du fichier schema.sql
    connection.executescript(f.read()) # exécution des commandes
    
connection.commit()
connection.close()