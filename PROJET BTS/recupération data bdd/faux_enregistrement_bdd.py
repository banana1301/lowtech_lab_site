import sqlite3
import random
import time
import datetime


#chemin bdd
database_path = 'database.db'

#fonction generation des données
def generate_data():
    baterie = round(random.uniform(0, 100), 0)
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    return baterie, date


while True:
    print("ok")
    batterie, date = generate_data() #utilisattion fonction


#connection et enregistrement valeur dans la bdd
    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO VALEURS_CAPTEURS (date_jour, Pourcentage_BAT) VALUES (?, ?)", (date, batterie,))
        conn.commit()

#attente
    cursor.close()
    conn.close()
    time.sleep(5)



