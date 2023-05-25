#import bibliothèque
import os
import shutil
import time
from PIL import Image, ImageFilter


#Chemin du dossier a surveiller
dossier_a_surveiller = r"C:\Users\gauti\OneDrive\Bureau\B\école\PROJET BTS\site test\modification_image_degradation" #dossier d'enregistrement des images
avant = dict ([(f, None) for f in os.listdir (dossier_a_surveiller)])


while 1:
    print('ok')

    time.sleep (9) #dort 9 secondes sera mit à 3600
    apres = dict ([(f, None) for f in os.listdir (dossier_a_surveiller)])
    ajoutes = [f for f in apres if not f in avant]
    supprimes = [f for f in avant if not f in apres]


    if ajoutes:
        print ("ajoutes : ", ", ".join (ajoutes))

        for fichier in ajoutes:
            if fichier.endswith(".jpg") or fichier.endswith(".jpeg") or fichier.endswith(".png") :
                print(f"image modifiée : {fichier}")


            #   _     _       _
            #  | |   (_)     | |
            #  | |__  _  __ _| |__
            #  | '_ \| |/ _` | '_ \
            #  | | | | | (_| | | | |, haute qualité d'image
            #  |_| |_|_|\__, |_| |_|
            #            __/ |
            #           |___/

#high
                fichier_res_high = fichier.split(".")[0] + "_high." + fichier.split(".")[1] #Renommer l'image en ajoutant "_high" a la fin du nom
                os.rename(os.path.join(dossier_a_surveiller, fichier), os.path.join(dossier_a_surveiller, fichier_res_high))





            #   _
            #  | |
            #  | | _____      __
            #  | |/ _ \ \ /\ / /
            #  | | (_) \ V  V / , basse qualité d'image
            #  |_|\___/ \_/\_/



#low
                fichier_res_low = fichier.split(".")[0] + "_low." + fichier.split(".")[1] #Copier l'image et la renommer en "_low"
                shutil.copy2(os.path.join(dossier_a_surveiller, fichier_res_high), os.path.join(dossier_a_surveiller, fichier_res_low)) #enregistrement du fichier


                # Charger l'image à transformer
                img = Image.open(fichier_res_low)
                # Appliquer un filtre de dithering
                img = img.convert(mode='1', dither=Image.FLOYDSTEINBERG)
                # Enregistrer l'image transformée
                img.save("mon_image_journal.jpg")

            #   ___  __ ___   _____
            #  / __|/ _` \ \ / / _ \
            #  \__ \ (_| |\ V /  __/ , sauvegarde du répertoire
            #  |___/\__,_| \_/ \___|


                #Ne pas supprimer la ligne du dessous, cette ligne sert à ne pas dupliquer les images nouvellement crée par l'utilisateur
                avant = dict ([(f, None) for f in os.listdir (dossier_a_surveiller)])
                time.sleep(1) #dort 1 secondes sera mit à 3600
            avant = dict ([(f, None) for f in os.listdir (dossier_a_surveiller)])



    if supprimes:
        print ("supprimes: ", ", ".join (supprimes))
        avant = apres

