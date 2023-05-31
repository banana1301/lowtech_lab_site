import sqlite3
connection = sqlite3.connect('database.db')
cur = connection.cursor()

# # cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
# #             ('First Post', 'Content for the first post')
# #             )

# # cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
# #             ('Second Post', 'Content for the second post')
# #             )

# # cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
# #             ('3éme Post', 'Content for the second post')
# #             )

# cur.execute("SELECT * FROM users WHERE email = 'a@a.com' ;")

# account=cur.fetchone()
# print(account)

# connection.commit()
# connection.close()

# from werkzeug.security import generate_password_hash,check_password_hash
# mdp="a"

# hmdp=(generate_password_hash(mdp, method='pbkdf2:sha1', salt_length=8))
# print(hmdp)

# print(check_password_hash(hmdp,"a"))


# import smtplib, ssl

# # on rentre les renseignements pris sur le site du fournisseur
# smtp_address = 'smtp.gmail.com'
# smtp_port = 465

# # on rentre les informations sur notre adresse e-mail
# email_address = 'mainguy701@gmail.com'
# email_password = 'mwrnqzkuwgalfdvf'

# # on rentre les informations sur le destinataire
# email_receiver = 'm.querquand@lacroixrouge-brest.fr'

# # on crée la connexion
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
#         # connexion au compte
#         server.login(email_address, email_password)
#         # envoi du mail
#         server.sendmail(email_address, email_receiver, 'Message automatique !!!!!')


# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')



# import sqlite3
# connection = sqlite3.connect('database.db')
# curseur = connection.cursor()

# curseur.execute('SELECT Pourcentage_BAT from VALEURS_CAPTEURS;')
# ligne1 = curseur.fetchall()
# print("ligne 1 -->",ligne1)

# liste = [x[0] for x in ligne1]
# print("liste -->", liste)

# import matplotlib.pyplot as plt
# import matplotlib
# from datetime import datetime
# matplotlib.use('Agg')

# dates = ['2023-05-1 15:19:30', '2023-05-2 15:19:25', '2023-05-3 15:19:20', '2023-04-4 12:52:09']
# parsed_dates = [datetime.strptime(date, '%Y-%m-%d %H:%M:%S') for date in dates]

# # parsed_dates=[1,2,3,4]

# # Données pour le premier graphique
# y1 = [10, 5, 20, 10]

# # Données pour le deuxième graphique
# y2 = [1, 8, 27, 64]

# # Création du premier graphique
# plt.figure()  # Créer une nouvelle figure
# plt.plot(parsed_dates, y1)
# plt.xlabel('Dates')
# plt.ylabel('Pourcentage')
# plt.title('Graphique 1')
# plt.savefig('static/ressource/graph/graph_bat.png')  # Enregistrer le graphique en tant qu'image

# # Création du deuxième graphique
# plt.figure()  # Créer une nouvelle figure
# plt.plot(parsed_dates, y2)
# plt.xlabel('Dates')
# plt.ylabel('Courant')
# plt.title('Graphique 2')
# plt.savefig('static/ressource/graph/graph_courant.png')  # Enregistrer le graphique en tant qu'image


import matplotlib
import matplotlib.pyplot as plt


matplotlib.use('Agg')

# Dates stockées dans une liste
dates = ['2023-05-01 15:19:30', '2023-05-02 15:19:25', '2023-05-03 15:19:20', '2023-04-04 12:52:09']
# parsed_dates = [datetime.strptime(date, '%Y-%m-%d %H:%M:%S') for date in dates]

# Données pour le premier graphique
y1 = [10, 5, 20, 10]

# Données pour le deuxième graphique
y2 = [1, 8, 27, 64]

# Création du premier graphique
fig, ax1 = plt.subplots()
ax1.plot(dates, y1)
ax1.set_xlabel('Dates')
ax1.set_ylabel('Pourcentage')
ax1.set_title('Graphique 1')

# Configurer le format de l'axe x pour afficher les dates
# date_fmt = mdates.DateFormatter('%Y-%m-%d')
# ax1.xaxis.set_major_formatter(date_fmt)
fig.autofmt_xdate()  # Ajuster automatiquement la rotation des étiquettes de date

# Enregistrer le premier graphique en tant qu'image
plt.savefig('static/ressource/graph/graph_bat.png')

# Création du deuxième graphique
fig, ax2 = plt.subplots()
ax2.plot(dates, y2)
ax2.set_xlabel('Dates')
ax2.set_ylabel('Courant')
ax2.set_title('Graphique 2')

# Configurer le format de l'axe x pour afficher les dates
# ax2.xaxis.set_major_formatter(date_fmt)
fig.autofmt_xdate()  # Ajuster automatiquement la rotation des étiquettes de date

# Enregistrer le deuxième graphique en tant qu'image
plt.savefig('static/ressource/graph/graph_courant.png')