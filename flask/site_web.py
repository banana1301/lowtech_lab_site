#////////////////////////////IMPORTATION//////////////////////////////////
from flask import Flask, render_template, url_for, redirect, request, session,flash
import re
import sqlite3
from werkzeug.exceptions import abort
from waitress import serve
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

@app.route('/blog')
def blog():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('blog.html', posts=posts)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',(title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('blog'))
    return render_template('create.html')

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('blog'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('blog'))

if __name__ == "__main__":
    # app.run(host="0.0.0.0", debug=True)
    print("Adresse du site: http://127.0.0.0:5000")
    print("Le site et accessible depuis son ip local aussi.")
    print("En cours d'exécution...")
    serve(app, host='0.0.0.0', port= 5000)