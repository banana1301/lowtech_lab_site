#////////////////////////////IMPORTATION//////////////////////////////////
from flask import Flask, render_template, url_for, redirect, request, session
import re
import sqlite3
#//////////////////////////////////////////////////////////////////////////
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = '7z3V98deMEiYRfF2x4i9'
#////////////////////////////////////CONNECTION BDD////////////////////////
connection = sqlite3.connect('database.db',check_same_thread=False)
curseur = connection.cursor()
#//////////////////////////////////////////////////////////////////////////

@app.route('/login',methods=['GET','POST'])
def login():
    # créer une variable pour stocker les erreur dedans par la suite
    msg=''
    # verifie que les champs sont remplie
    if request.method == 'POST' and 'email' in request.form and 'mdp' in request.form:
        # pour récupérer plus simplement 
        email = request.form['email']
        mdp = request.form['mdp']
        hmdp=hash(mdp)
        #chercher si le compte existe
        curseur.execute("SELECT * FROM users WHERE email = '{}' AND mdp = '{}' ".format(email,hmdp))
        # retourner les valeurs
        account= curseur.fetchone()
        print(account)
        # SI le compte existe
        if account:
            # creer une session
            session['loggedin'] = True
            session['id'] = account [0]
            session ['username'] = account [3]
            return 'Connection réussi'
        else: 
            #Compte n'existe pas ou mdp pas correct
            msg='Email ou Mot de passe INCORRECT'
    return render_template('connecter.html',msg=msg)

@app.route('/register', methods=['GET','POST'])
def register():
    msg=''
    if request.method == 'POST' and 'email' in request.form and 'nom' in request.form and 'prenom' in request.form and 'mdp' in request.form:
        email = request.form['email']
        nom = request.form['nom']
        prenom = request.form['prenom']
        mdp = request.form['mdp']
        hmdp=hash(mdp)
        curseur.execute("SELECT * FROM users WHERE email = '{}' ".format(email))
        account= curseur.fetchone()
        if account:
            msg = 'Le compte existe déjà'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Email invalide'
        elif not nom or not prenom or not mdp or not email:
            msg = 'Remplir le forulaire !'
        else:
            # Si le compte n'existe pas 
            curseur.execute("INSERT INTO users VALUES (NULL,'{}','{}','{}','{}')".format(nom,prenom,email,hmdp))
            connection.commit()
            msg='Compte enregistrer'
    elif request.method == 'POST':
        #si le formulaire est vide
        msg= "Remplir tous les champs !"
    return render_template('inscription.html', msg=msg)

@app.route('/logout')
def logout():
    #supprimer les données de sessions
    session.pop('loggedin',None)
    session.pop('id',None)
    session.pop('username',None)
    return redirect(url_for('login'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/graphique')
def graphique():
    return render_template('graphique.html')

@app.route('/a_propos')
def a_propos():
    return render_template('a_propos.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
