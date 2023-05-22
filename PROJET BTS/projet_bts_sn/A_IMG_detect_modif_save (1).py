#import bibliothèque
import os
import shutil
import cv2
import time

#Chemin du dossier a surveiller
dossier_a_surveiller = r"/home/bts_sn_2a/GR/python/projet_bts_sn" #dossier d'enregistrement des images
avant = dict ([(f, None) for f in os.listdir (dossier_a_surveiller)])


while 1:

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


            #                      _ _
            #                     | (_)
            #   _ __ ___   ___  __| |_ _   _ _ __ ___
            #  | '_ ` _ \ / _ \/ _` | | | | | '_ ` _ \
            #  | | | | | |  __/ (_| | | |_| | | | | | |, moyenne qualité d'image
            #  |_| |_| |_|\___|\__,_|_|\__,_|_| |_| |_|


#medium
                fichier_res_medium = fichier.split(".")[0] + "_medium." + fichier.split(".")[1] #Copier l'image et la renommer en "_medium"
                shutil.copy2(os.path.join(dossier_a_surveiller, fichier_res_high), os.path.join(dossier_a_surveiller, fichier_res_medium)) #enregistrement du fichier


                #Redimensionner l'image moyenne
                image = cv2.imread(os.path.join(dossier_a_surveiller, fichier_res_medium)) #lecture image/mettre l'image à modifier dans "image"

                echelle_resize = 60 # pourcentage de l'echelle high
                largeur = int(image.shape[1] * echelle_resize / 100)
                hauteur = int(image.shape[0] * echelle_resize / 100) #shape est un tuple : (row (height), column (width), color (3))
                dim = (largeur, hauteur)

                image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) #modification image


                #appliquer un filtre de détorioration
                image = cv2.GaussianBlur(image,(5,5),0)#modification image
                cv2.imwrite(os.path.join(dossier_a_surveiller, fichier_res_medium), image) #enregistrement(ecriture) de l'image


            #   _
            #  | |
            #  | | _____      __
            #  | |/ _ \ \ /\ / /
            #  | | (_) \ V  V / , basse qualité d'image
            #  |_|\___/ \_/\_/



#low
                fichier_res_low = fichier.split(".")[0] + "_low." + fichier.split(".")[1] #Copier l'image et la renommer en "_low"
                shutil.copy2(os.path.join(dossier_a_surveiller, fichier_res_medium), os.path.join(dossier_a_surveiller, fichier_res_low)) #enregistrement du fichier

                echelle_resize = 35 # pourcentage de l'echelle high
                largeur = int(image.shape[1] * echelle_resize / 100)
                hauteur = int(image.shape[0] * echelle_resize / 100) #shape est un tuple : (row (height), column (width), color (3))
                dim = (largeur, hauteur)

                image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) #modification image


                #appliquer un filtre de détorioration
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #modification image
                cv2.imwrite(os.path.join(dossier_a_surveiller, fichier_res_low), image) #enregistrement(ecriture) de l'image


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
