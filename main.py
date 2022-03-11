from initialisationJeu import *
import pioche
import perdant
import gameplay as g
from afichage import *
import time
import os

def JeuPlusieursJoueur():
    nombre_de_toure = 0
    
    while jetons_en_jeu != []:
        indice_joueur = nombre_de_toure%len(liste_des_joueurs)
        print("Tour du joueur", liste_des_joueurs[indice_joueur][0])

        AfficheJoueur()
        affichage_dominos(jetons_en_jeu, jetons_retournes)

        print("")
        score = g.TourDuJoueur()
        
        if isinstance(score, str):
            perdant.PartiePerdu(score)
        else:
            indice_p = pioche.RechercheP(jetons_en_jeu, score)
            if isinstance(indice_p, str):
                perdant.PartiePerdu(indice_p)
        if not isinstance(score, str) and not isinstance(indice_p, str):
            print('ici indice_p', indice_p+1)

            if score < jetons_en_jeu[0][0]:
                liste_p = []

            if score >= 21:
                liste_p = jetons_en_jeu[:indice_p + 1]

            liste_possibliliter = pioche.PiquerPckomino(liste_p, score, indice_joueur)

            if not isinstance(liste_possibliliter, str):
                affichage_dominos(liste_possibliliter, 0)
                pioche.RecupePickomino(indice_joueur, liste_possibliliter)
            else:
                print('Votre score est de :',score)
                print(liste_possibliliter)

        nombre_de_toure +=1
        print('Nombre de jetons retournes ' ,jetons_retournes)
        #time.sleep(5)
        #os.system('cls')
        #rajouter du temps
JeuPlusieursJoueur()
