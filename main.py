from initialisationJeu import *
import pioche
import perdant
import gameplay as g
from afichage import *
import time
import os
import random 
import randomplayer

def JeuPlusieursJoueur():
    nombre_de_toure = 0
    while jetons_en_jeu != []:
        indice_joueur = nombre_de_toure%len(liste_des_joueurs)
        print("Tour du joueur", liste_des_joueurs[indice_joueur][0], indice_joueur)

        AfficheJoueur(liste_des_joueurs)
        affichage_dominos(jetons_en_jeu+liste_jetons_retournes)

        print("")
        score = g.TourDuJoueur() #pour la recuperation des des 
        
        if isinstance(score, str):
            jetons_retournes = perdant.PartiePerdu(score, indice_joueur)
        else:
            indice_p = pioche.RechercheP(jetons_en_jeu, score)
            if isinstance(indice_p, str):
                jetons_retournes = perdant.PartiePerdu(indice_p, indice_joueur)
        if not isinstance(score, str) and not isinstance(indice_p, str):

            if score < jetons_en_jeu[0][0]:
                jetons_retournes = perdant.PartiePerdu(score, indice_joueur)
                liste_p = []

            else :
                liste_p = [e for e in jetons_en_jeu if e[0] <= score ]
                #jetons_en_jeu[:indice_p + 1]

            liste_possibliliter = pioche.PiquerPckomino(liste_p, score, indice_joueur) #rajouter le pickomino du joueur qui est egal au score 

            if not isinstance(liste_possibliliter, str):
                affichage_dominos(liste_possibliliter)
                pioche.RecupePickomino(indice_joueur, liste_possibliliter)
            else:
                print('Votre score est de :',score)
                print(liste_possibliliter)
        totale_de_vers_joueur = sum(e[1] for e in liste_des_joueurs[indice_joueur][1])
        liste_des_joueurs[indice_joueur][2] = totale_de_vers_joueur
        print(f"le joueur {liste_des_joueurs[indice_joueur][0]}, posede {totale_de_vers_joueur} vers")
        nombre_de_toure +=1
        print('Nombre de jetons retournes ' ,len(liste_jetons_retournes))
        #time.sleep(5)
        #os.system('cls')
        #rajouter du temps
        aficher_ganiens()
def Joueuraleatoire():
    nombre_de_toure = 0

    while jetons_en_jeu != []:
        indice_joueur = nombre_de_toure%len(liste_des_joueurs)
        print("Tour du joueur", liste_des_joueurs[indice_joueur][0], indice_joueur) 
        AfficheJoueur(liste_des_joueurs)
        affichage_dominos(jetons_en_jeu)
        if indice_joueur < nombre_de_joueurs_aleatoire :
            print('\n')
            score = randomplayer.TourDuJoueurAleatoire()
        else :
            print('\n')
            score = g.TourDuJoueurHumain(indice_joueur)
        
        indice_p = pioche.RechercheP(jetons_en_jeu, score) 
        if isinstance(indice_p, str):
            perdant.PartiePerdu(indice_p, indice_joueur) #print l'erreur et incremente le nombre de jetons reoturnes
        if not isinstance(score, str) and not isinstance(indice_p, str):
            if score < jetons_en_jeu[0][0]:
                perdant.PartiePerdu(score, indice_joueur)
                liste_p = []

            else :
                liste_p = [e for e in jetons_en_jeu if e[0] <= score ]
                #jetons_en_jeu[:indice_p + 1]

            liste_possibliliter = pioche.PiquerPckomino(liste_p, score, indice_joueur) 

            if not isinstance(liste_possibliliter, str):
                affichage_dominos(liste_possibliliter)
                if indice_joueur < nombre_de_joueurs_aleatoire :
                    #time.sleep(1)
                    randomplayer.SelectionRandom(liste_possibliliter, liste_des_joueurs)
                else :
                    pioche.RecupePickomino(indice_joueur, liste_possibliliter)
            else:
                print('Votre score est de :',score)
        totale_de_vers_joueur = sum(e[1] for e in liste_des_joueurs[indice_joueur][1])
        liste_des_joueurs[indice_joueur][2] = totale_de_vers_joueur
        print(f"le joueur {liste_des_joueurs[indice_joueur][0]}, posede {totale_de_vers_joueur} vers")
        nombre_de_toure +=1
        print('\nNombre de jetons retournes ' ,len(liste_jetons_retournes))
        #time.sleep(3)
        os.system('cls')
    aficher_ganiens()

#random.seed(3)
Joueuraleatoire()

