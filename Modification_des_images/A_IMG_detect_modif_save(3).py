#import bibliothèque
import os
import shutil
import time
from PIL import Image, ImageFilter


#Chemin du dossier a surveiller
dossier_a_surveiller = r"static/photos" #dossier d'enregistrement des images
avant = dict ([(f, None) for f in os.listdir (dossier_a_surveiller)])


while 1:
    print("programme de modification d'image python : ok")

    time.sleep (3600) #dort 1 heure
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


                fichier_res_high = fichier.split(".")[0] + "_high." + fichier.split(".")[1] #Renommer l'image en ajoutant "_high" a la fin du nom
                os.rename(os.path.join(dossier_a_surveiller, fichier), os.path.join(dossier_a_surveiller, fichier_res_high))





            #   _
            #  | |
            #  | | _____      __
            #  | |/ _ \ \ /\ / /
            #  | | (_) \ V  V / , basse qualité d'image
            #  |_|\___/ \_/\_/




                fichier_res_low = fichier.split(".")[0] + "_low." + fichier.split(".")[1] #Copier l'image et la renommer en "_low"
                shutil.copy2(os.path.join(dossier_a_surveiller, fichier_res_high), os.path.join(dossier_a_surveiller, fichier_res_low)) #enregistrement du fichier

                time.sleep(0.1)#temps tampon

                #charger l'image à transformer
                img = Image.open(os.path.join(dossier_a_surveiller, fichier_res_low))
                #appliquer un filtre de dithering
                img = img.convert(mode='1', dither=Image.FLOYDSTEINBERG)
                #enregistrer l'image transformée avec une qualité de 50 et une compression optimisée
                img.save(os.path.join(dossier_a_surveiller, fichier_res_low),optimize=True, quality=1)

            #   ___  __ ___   _____
            #  / __|/ _` \ \ / / _ \
            #  \__ \ (_| |\ V /  __/ , sauvegarde du répertoire
            #  |___/\__,_| \_/ \___|


                #Ne pas supprimer la ligne du dessous, cette ligne sert à ne pas dupliquer les images nouvellement crée par l'utilisateur
                avant = dict ([(f, None) for f in os.listdir (dossier_a_surveiller)])
                time.sleep(1) #dort 1 seconde
            avant = dict ([(f, None) for f in os.listdir (dossier_a_surveiller)])



    if supprimes:
        print ("supprimes: ", ", ".join (supprimes))
        avant = apres