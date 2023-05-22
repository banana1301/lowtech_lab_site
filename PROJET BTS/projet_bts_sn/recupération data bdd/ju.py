#!/usr/bin/python3
from pijuice import PiJuice
import time
pijuice = PiJuice(1, 0x14)
from datetime import datetime
import sqlite3

#La boucle va permettre de relever en tant réel les informations toutes les 5 secondes
while True: 
#Appel des valeurs tension, courant et pourcentage batterie
	tension = pijuice.status.GetBatteryVoltage()
	courant = pijuice.status.GetBatteryCurrent()
	pourcentage_batterie = (pijuice.status.GetChargeLevel())

#Conversion  tension (mV -> V) et courant (mA -> A)
	conver_t = tension['data'] /1000
	conver_c = courant['data'] /1000

#Récupération de la valeur du pourcentage batterie
	print (f"La batterie est chargée à {pourcentage_batterie['data']} %")
	print ('------->',type(pourcentage_batterie['data']))
#Récupération de la valeur de la tension
	print (f"La tension de la batterie est de {conver_t} V")

#Récupération de la valeur du courant
	print (f"Le courant est de {conver_c} A")

#Récupération de la valeur puissance
#Calcul de P=U*I
	puissance = conver_t*conver_c
	print (f"La puissance du système est {puissance} W")
	time.sleep (5)

#BDD
	connexion = sqlite3.connect("database.db")
#Vérification de la connexion à la base de données
	print ((f"Connexion OK {connexion}"))

	curseur = connexion.cursor()
#Evite de créer de nouveau une table à chaque redémarrage de la raspberry
	curseur.execute("""
	create table if not exists VALEURS_CAPTEURS
	(
		date_jour DATETIME,
		Tension float,
		Courant float,
		Puissance float,
		Pourcentage_BAT int
	);
	""")

	valeurs  = {"date" : datetime.now(), "Tension" : conver_t, "Courant" : conver_c, "Puissance" : puissance, "Pourcentage_BAT" : pourcentage_batterie['data']}
	curseur.execute ("INSERT INTO VALEURS_CAPTEURS values (:date,:Tension,:Courant,:Puissance,:Pourcentage_BAT)", valeurs)
	connexion.commit()
	curseur.execute("SELECT*FROM VALEURS_CAPTEURS")

	donnees = curseur.fetchall()
	print (donnees)
	for ligne in donnees:
		print(ligne[0])

	connexion.close()
	time.sleep (5)
