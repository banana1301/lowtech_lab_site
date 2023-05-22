'''
1) Detection de l'arrive de fichiers dans un dossier particulier.
2) Si est une image le traitement pourra commencer. (.jpeg .jpg .SVG .AI .PNG) les autres formats ne seront pas pris en compte.
3) Dupliquer une image et rename par un diminutif [nom_fichier]_high _medium _low _down
4) Apres chaque duplication et rename faire le traitement sur l'image avant de passer au suivant.
'''

#import bibliothèque
import os
import shutil
import cv2
import time

#Chemin du dossier a surveiller
dossier_a_surveiller = r"C:\Users\gauti\OneDrive\Bureau\B\école\PROJET BTS"
#dossier_a_surveiller = r"/home/bts_sn_2a/GR/python/projet_bts_sn" #dossier d'enregistrement des images ubuntu
avant = dict ([(f, None) for f in os.listdir (dossier_a_surveiller)])


'''
creer un dictionnaire qui contient les noms de tous les fichiers dans le dossier a surveiller,
avec une valeur None associee a chaque nom de fichier.
Cela permet de stocker les noms des fichiers dans le dossier avant que le programme ne commence
a surveiller le dossier pour des modifications.
Cela nous permettra de comparer les fichiers dans le dossier avant et après l'attente,
pour detecter les fichiers qui ont ete ajoutes ou supprimes.
'''




while 1:

    time.sleep (10) #dort 10 secondes sera mit à 3600
    apres = dict ([(f, None) for f in os.listdir (dossier_a_surveiller)])
    ajoutes = [f for f in apres if not f in avant]
    supprimes = [f for f in avant if not f in apres]


    if ajoutes:
        print ("ajoutes : ", ", ".join (ajoutes))
        for fichier in ajoutes:
            if fichier.endswith(".jpg") or fichier.endswith(".jpeg") or fichier.endswith(".png"):
                print(f"Nouvelle image detectee : {fichier}")


                #######################
                ##########HIGH#########
                #######################

                #Renommer l'image en ajoutant "_high" a la fin du nom
                fichier_res_high = fichier.split(".")[0] + "_high." + fichier.split(".")[1]
                os.rename(os.path.join(dossier_a_surveiller, fichier), os.path.join(dossier_a_surveiller, fichier_res_high))

#high daltonien1
                fichier_res_high_dalto1 = fichier.split(".")[0] + "_high_dalto1." + fichier.split(".")[1]
                shutil.copy2(os.path.join(dossier_a_surveiller, fichier_res_high), os.path.join(dossier_a_surveiller, fichier_res_high_dalto1))
#high daltonien2
                fichier_res_high_dalto2 = fichier.split(".")[0] + "_high_dalto2." + fichier.split(".")[1]
                shutil.copy2(os.path.join(dossier_a_surveiller, fichier_res_high), os.path.join(dossier_a_surveiller, fichier_res_high_dalto2))


                #######################
                ##########MEDIUM#######
                #######################
                #Copier l'image et la renommer en "_medium"
                fichier_res_medium = fichier.split(".")[0] + "_medium." + fichier.split(".")[1]
                shutil.copy2(os.path.join(dossier_a_surveiller, fichier_res_high), os.path.join(dossier_a_surveiller, fichier_res_medium))


                '''Soucis dans resize'''
                #Redimensionner l'image moyenne à (800,600)
                image = cv2.imread(os.path.join(dossier_a_surveiller, fichier_res_medium))
                image = cv2.resize(image, dsize=(800, 600))


                '''soucis couleur image'''
                #Convertir l'image moyenne en noir et blanc
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(os.path.join(dossier_a_surveiller, fichier_res_medium), image)

#medium daltonien1
                fichier_res_medium_dalto1 = fichier.split(".")[0] + "_medium_dalto1." + fichier.split(".")[1]
                shutil.copy2(os.path.join(dossier_a_surveiller, fichier_res_high), os.path.join(dossier_a_surveiller, fichier_res_medium_dalto1))

#medium daltonien1
                fichier_res_medium_dalto2 = fichier.split(".")[0] + "_medium_dalto2." + fichier.split(".")[1]
                shutil.copy2(os.path.join(dossier_a_surveiller, fichier_res_high), os.path.join(dossier_a_surveiller, fichier_res_medium_dalto2))

                #######################
                ##########LOW##########
                #######################


                #Copier l'image et la renommer en "_low"
                fichier_res_low = fichier.split(".")[0] + "_low." + fichier.split(".")[1]
                shutil.copy2(os.path.join(dossier_a_surveiller, fichier_res_medium), os.path.join(dossier_a_surveiller, fichier_res_low))

                #Redimensionner l'image basse à (400, 300)
                image = cv2.imread(os.path.join(dossier_a_surveiller, fichier_res_low))
                image = cv2.resize(image, dsize=(400, 300))

                #Convertir l'image basse en noir et blanc
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(os.path.join(dossier_a_surveiller, fichier_res_low), image)


#low daltonien
                fichier_res_low_dalto1 = fichier.split(".")[0] + "_low_dalto1." + fichier.split(".")[1]
                shutil.copy2(os.path.join(dossier_a_surveiller, fichier_res_high), os.path.join(dossier_a_surveiller, fichier_res_low_dalto1))
#Un seul Low en Daltonien, car la version LOW sera une version noir et blanc. La version daltonien aura un Noir et blanc a plus fort contraste.

                #Ces deux lignes servent a eviter la duplication des fichiers qui viennet d'etre dupliques
                avant = dict ([(f, None) for f in os.listdir (dossier_a_surveiller)])
                time.sleep(1)


    if supprimes:
        print ("supprimes: ", ", ".join (supprimes))
        avant = apres
