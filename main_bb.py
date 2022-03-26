from initialisationJeu import *
import pioche
import perdant
import gameplay as g
from afichage import *
import time
import os

def JeuPlusieurJourer():
    nombre_de_toure = 0
    
    while jetons_en_jeux != []:
        indix_jouer = nombre_de_toure%len(liste_des_joueur)
        print("Tour du joueur", liste_des_joueur[indix_jouer][0])

        AfficheJoueur()
        affichage_dominos(jetons_en_jeux + jetons_retourner)

        print("")
        score = g.TourDuJouer()
        
        if isinstance(score, str):
            perdant.PartiePerdu(score)
        else:
            indice_p = pioche.RechercheP(jetons_en_jeux, score)
            if isinstance(indice_p, str):
                perdant.PartiePerdu(indice_p)
        if not isinstance(score, str) and not isinstance(indice_p, str):
            print('ici indice_p', indice_p+1)

            if score < jetons_en_jeux[0][0]:
                liste_p = []

            if score >= 21:
                liste_p = jetons_en_jeux[:indice_p + 1]

            liste_posibliliter = pioche.PiquerPckomino(liste_p, score)

            if not isinstance(liste_posibliliter, str):
                affichage_dominos(liste_posibliliter)
                pioche.RecupePickomino(indix_jouer, liste_posibliliter)
            else:
                print('Votre score est de :',score)
                print(liste_posibliliter)

        nombre_de_toure +=1
        print('Nombre de jetons retourne ' ,len(jetons_retourner))
        #time.sleep(5)
        #os.system('cls')
        #rajouter du temps

## BB 28 fevrier 2022
import random
# random.seed(1)
random.seed(1)
JeuPlusieurJourer()
