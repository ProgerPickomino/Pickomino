from initialisationJeu import *
from pioche import *
from gameplay import *
import time
import random

def SelectionGlouton(L_pickomino ,liste_des_joueurs, indice_joueur):
    """ 
    list x list -->  None
    """
    pickomino_autre_joueur = []

    selections = L_pickomino[-1]
    for i in range(len(liste_des_joueurs)):
        if liste_des_joueurs[i][1] != [] and selections == liste_des_joueurs[i][1][-1]:
            pickomino_autre_joueur.append(liste_des_joueurs[i][1][-1])
            liste_des_joueurs[indice_joueur][1].append(liste_des_joueurs[i][1].pop())

    if  selections not in pickomino_autre_joueur:
        pickomino = jetons_en_jeu.pop(RechercheP(jetons_en_jeu, selections[0]))
        liste_des_joueurs[indice_joueur][1].append(pickomino)

def TourDuJoueurGlouton():
    """
    list X str --> int | str
    """
    continue_a_jouer = True
    nombre_de_des = 8
    face_du_des = [1, 2, 3, 4, 5, "vers"]
    dic_des_retenu = {}
    des_du_joueur = []
    dic_scores = dict()
    
    while continue_a_jouer:
        lancer = LanceDes(face_du_des, nombre_de_des)
        affiche_des(lancer)
        des_possible_a_recuperer = DesPossiblesaRecuperer(lancer, dic_des_retenu)
        print("Des que j'ai recupere :", des_du_joueur)

        if len(des_possible_a_recuperer) == 0:
            return "Tu n'as pas de dés a récuperer c'est un echec"
        time.sleep(2)

        for face in des_possible_a_recuperer:
            if face == "vers":
                dic_scores[face] = des_possible_a_recuperer[face]*5
            else :
                dic_scores[face] = des_possible_a_recuperer[face]*face

        cle_max = random.choice(tuple(dic_scores.keys()))

        print(tuple(dic_scores.keys()))
        for face in dic_scores:
            if dic_scores[cle_max] < dic_scores[face]:
                cle_max = face
            if 5 in dic_scores and 'vers' in dic_scores:
                if dic_scores[5] == dic_scores["vers"]:
                    cle_max = "vers"

        des_du_joueur.append(cle_max)
        print('\ndes possibles a recuperer ',des_possible_a_recuperer)
        print('\ndictionnaire de scores ', dic_scores, 'caleur de cle max',cle_max)

        dic_des_retenu[cle_max] = lancer[cle_max]
        print('\ndictoinnaire des retnues : ', dic_des_retenu)
        print('Votre score est de :',ScoreJoueur(dic_des_retenu))

        nombre_de_des -= lancer[cle_max]
        if nombre_de_des == 0 or ScoreJoueur(dic_des_retenu) >  jetons_en_jeu[0][0]:
            continue_a_jouer = False
            break
    return ScoreJoueurFinale(dic_des_retenu)
TourDuJoueurGlouton()