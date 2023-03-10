
#!/usr/bin/python3
from pijuice import PiJuice
import time
pijuice = PiJuice(1, 0x14)
while True: 
	print (pijuice.status.GetStatus())
	print (pijuice.status.GetChargeLevel())
#récupération des valeurs tension et courant  
	tension = pijuice.status.GetBatteryVoltage()
	courant =pijuice.status.GetBatteryCurrent()
	
	conver_t = tension['data'] /1000
	conver_c = courant['data'] /1000
#Récupération de la valeur du pourcentage batterie
	pourcentage_batterie = (pijuice.status.GetChargeLevel['data']) 


#Récupération de la valeur puissance	
	puissance = conver_t*conver_c
	print (f"La puissance du système est {puissance}")

#Récupération de la valeur tension
	
	time.sleep (5)

