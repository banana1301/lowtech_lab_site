# import sqlite3

# connection = sqlite3.connect('database.db')

# cur = connection.cursor()

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


import smtplib, ssl

# on rentre les renseignements pris sur le site du fournisseur
smtp_address = 'smtp.gmail.com'
smtp_port = 465

# on rentre les informations sur notre adresse e-mail
email_address = 'mainguy701@gmail.com'
email_password = 'mwrnqzkuwgalfdvf'

# on rentre les informations sur le destinataire
email_receiver = 'm.querquand@lacroixrouge-brest.fr'

# on crée la connexion
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
        # connexion au compte
        server.login(email_address, email_password)
        # envoi du mail
        server.sendmail(email_address, email_receiver, 'Message automatique !!!!!')




#mwrn qzku wgal fdvf