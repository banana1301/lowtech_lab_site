@app.route('/')
def home():
    database_path = 'database.db' # chemin de la base de données
    conn = sqlite3.connect(database_path) # connexion à la base de données
    cursor = conn.cursor() # création du curseur
    cursor.execute('SELECT Pourcentage_BAT FROM VALEURS_CAPTEURS ORDER BY date_jour DESC LIMIT 1') # requête SQL d'acquisition des données de batterie en fonction de la date pour obtenir le plus récent
    row = cursor.fetchone()

    if row is not None:
        pourcent = row[0] # row[0] stoque désormais la valeur prise dans la bdd
    else:
        pourcent = 0

    cursor.close()
    conn.close()
    return render_template('index.html', pourcent_battery_recupere=pourcent)