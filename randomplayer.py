from initialisationJeu import *
import random
from pioche import *
from gameplay import *
import time

def SelectionRandom(L ,liste_des_joueurs, indice_joueur):
    """ list x List -->  None"""
    pickomino_autre_joueur = []
    selections = random.choice(L)
    for i in range(len(liste_des_joueurs)):
        if liste_des_joueurs[i][1] != [] and selections == liste_des_joueurs[i][1][-1]:
            pickomino_autre_joueur.append(liste_des_joueurs[i][1][-1])
            liste_des_joueurs[indice_joueur][1].append(liste_des_joueurs[i][1].pop())

    if selections in L and (selections not in pickomino_autre_joueur):
        pickomino = jetons_en_jeu.pop(RechercheP(jetons_en_jeu, selections[0]))
        liste_des_joueurs[indice_joueur][1].append(pickomino)

def TourDuJoueurAleatoire():
    """
    list X str --> int | str
    """
    continue_a_jouer = True
    nombre_de_des = 8
    face_du_des = [1, 2, 3, 4, 5, "vers"]
    dic_des_retenu = {}
    des_du_joueur = []
    while continue_a_jouer:
        lancer = LanceDes(face_du_des, nombre_de_des)
        affiche_des(lancer)
        des_possible_a_recuperer = PossibliterDeJeux(lancer, dic_des_retenu)
        print("Des que j'ai recupere :", des_du_joueur)

        if len(des_possible_a_recuperer) == 0:
            return "Tu n'as pas de dés a récuperer c'est un echec"
        time.sleep(2)
        des_recupere = random.choice(des_possible_a_recuperer)
        des_du_joueur.append(des_recupere)
        dic_des_retenu[des_recupere] = lancer[des_recupere]
        print('Votre score est de :',ScoreJoueur(dic_des_retenu))
        nombre_de_des -= lancer[des_recupere]
        if nombre_de_des == 0 or ScoreJoueur(dic_des_retenu) >  jetons_en_jeu[0][0]:
            continue_a_jouer = False
            break
    return ScoreJoueurFinale(dic_des_retenu)
