
#!/usr/bin/python3
from pijuice import PiJuice
import time
# Import des modules nécessaires pour la base de données
from datetime import datetime
import sqlite3
# Import des modules nécessaires pour communiquer avec un 
#dispositif I2C et contrôler les broches GPIO du Raspberry Pi
import smbus  
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
pijuice = PiJuice(1, 0x14)

#La boucle va permettre de relever en tant réel les informations
#toutes les 5 secondes
while True:
	print (f"{GPIO.input(21)}") 
#Appel des valeurs tension, courant et pourcentage batterie  
	tension = pijuice.status.GetBatteryVoltage()
	courant = pijuice.status.GetBatteryCurrent()
	pourcentage_batterie = pijuice.status.GetChargeLevel()

#Conversion  tension (mV -> V) et courant (mA -> A)
	conver_t = tension['data'] /1000
	conver_c = courant['data'] /1000

#Récupération de la valeur puissance
#Calcul de P=U*I	
	puissance = conver_t*conver_c


#BDD

	connexion = sqlite3.connect("./database.db")
#Vérification de la connexion à la base de données
	print ((f"Connexion OK {connexion}"))

	curseur = connexion.cursor()
#Evite de créer de nouveau une table à chaque redémarrage de la raspberry


	# Déclaration des champs de la base de données
	valeurs  = {"date" : datetime.now(), "Tension" : conver_t, "Courant" : conver_c,"Pourcentage_BAT" : pourcentage_batterie['data'],  "Luminosite" : GPIO.input(21)}
	
	# Permet d'insérer les valeurs dans la base de données en utilisant les requêtes SQL
	curseur.execute ("INSERT INTO VALEURS_CAPTEURS values (:date,:Tension,:Courant,:Pourcentage_BAT,:Luminosite)", valeurs)

	# Execite la requête SQL précédente
	connexion.commit()

	# Permet de montrer les champs de la table 
	curseur.execute("SELECT*FROM VALEURS_CAPTEURS")

	# Fonction qui permet de récupérer les données de la base de données
	donnees = curseur.fetchall()

	# Extinction de la base de donnée
	connexion.close()
	

# Capteur de luminosité

#      j'utilise la bibliothèque GPIO pour détecter l'état du port 21 (0 ou 1)
	if GPIO.input(21) == 1:
#      je traduis en luxmètre à quoi correspond le 1 et 0
		luminosité = 130
		print (f"La luminosité est infèrieur à {luminosité} lux") 

	else :
		luminosité = 200
		print (f"La luminosité est supérieur à {luminosité} lux")
#
		
	time.sleep(5)
