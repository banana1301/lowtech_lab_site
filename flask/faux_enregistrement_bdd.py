import sqlite3
import random
import time
import datetime
#ce programme simule un enregistrement de valer aléatoir dans la base de donné en vu de faire des tests

#chemin bdd
database_path = 'database.db'

#fonction generation des données
def generate_data():
    baterie = round(random.uniform(0, 100), 0) #valeur aléatoire entre 0 et 100
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') #date comprte la date au format year month day hour minute seconde
    return baterie, date #retourne les valeurs


while True:
    print("ok")
    batterie, date = generate_data() #utilisation fonction de génération des donnés

    #connection et enregistrement valeur dans la bdd
    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO VALEURS_CAPTEURS (date_jour, Pourcentage_BAT) VALUES (?, ?)", (date, batterie,)) #requete sql d'enregistrement dans la bdd
        conn.commit() #sauvegarde de l'enregistrement

    cursor.close()
    conn.close()
    #attente
    time.sleep(20)



