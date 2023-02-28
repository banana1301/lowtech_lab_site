from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/graphique")
def graphique():
    return  render_template("graphique.html")

@app.route("/connecter")
def connecter():
    return  render_template("connecter.html")

@app.route("/a_propos")
def a_propos():
    return  render_template("a_propos.html")

@app.route("/inscription")
def inscription():
    conn = sql.connect('database.db')
    print (conn)
    print("Connexion faite !!!")
    conn.execute('CREATE TABLE IF NOT EXISTS users(nom VARCHAR(255), prenom VARCHAR(255), email VARCHAR(255), mdp VARCHAR(255), date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP);')
    return  render_template("inscription.html")



@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nom = request.form['nom']
            prenom = request.form['prenom']
            email = request.form['email']
            mdp = request.form['mdp']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO users (nom,prenom,email,mdp) VALUES (?,?,?,?)",(nom,prenom,email,mdp) )
            
            con.commit()
            msg = "Enregistrement correctement envoyer"
        except:
            con.rollback()
            msg = "Erreur de l'enregistrement"
        finally:
            return render_template("graphique.html",msg = msg)
            con.close()




if __name__ == "__main__":
    app.run(debug=True)