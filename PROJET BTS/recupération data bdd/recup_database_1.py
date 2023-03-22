import sqlite3
import time

database_path = 'database.db'
battery_status_element = 'battery-status'

while True:
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute('SELECT Pourcentage_BAT FROM VALEURS_CAPTEURS ORDER BY date_jour DESC LIMIT 1')
    row = cursor.fetchone()

    if row is not None:
        pourcent = row[0]
        print(pourcent)
        if pourcent >= 80. 
            print('La batterie est chargée à plus de 80%.')
        elif pourcent >= 40 and pourcent < 79:
            print('La batterie est chargée entre 40% et 79%.')
        else:
            print('La batterie est chargée à moins de 40%.')

    cursor.close()
    conn.close()
    time.sleep(5)
