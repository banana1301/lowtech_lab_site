from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    database_path = 'database.db'
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute('SELECT Pourcentage_BAT FROM VALEURS_CAPTEURS ORDER BY date_jour DESC LIMIT 1')
    row = cursor.fetchone()

    pourcent = 0

    if row is not None:
        pourcent = row[0]
        print(pourcent)

    cursor.close()
    conn.close()

    return render_template('modif.html', pourcent_battery_recupere=pourcent)

if __name__ == '__main__':
    app.debug = True
    app.run()
