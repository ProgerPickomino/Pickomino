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
def MeilleurScore(lancer_des):
    '''
    Dict --> Int | Str
    '''
    
    dictionnaire_score = dict()
    for face in lancer_des :
        if face == "vers":
            dictionnaire_score[face] = lancer_des[face]*5
        else :
            dictionnaire_score[face] = lancer_des[face]*face
    m = random.choice(tuple(dictionnaire_score.keys()))
    for c in dictionnaire_score:
        if dictionnaire_score[m] < dictionnaire_score[c]:
            m = c
        if 5 in dictionnaire_score.keys() and 'vers' in dictionnaire_score.keys() :
            if dictionnaire_score['vers'] == dictionnaire_score[5]:
                m = 'vers'
    return m 
print(MeilleurScore({1:6, 5:6, 'vers':5}))
def TourDuJoueurGlouton():
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
        des_possible_a_recuperer = DesPossiblesaRecuperer(lancer, dic_des_retenu)
        print("Des que j'ai recupere :", des_du_joueur)

        if len(des_possible_a_recuperer) == 0:
            return "Tu n'as pas de dés a récuperer c'est un echec"
        time.sleep(2)
        des_recupere = MeilleurScore(des_possible_a_recuperer)

        des_du_joueur.append(des_recupere)

        dic_des_retenu[des_recupere] = lancer[des_recupere]
        print('Votre score est de :',ScoreJoueur(dic_des_retenu))
        nombre_de_des -= lancer[des_recupere]
        if nombre_de_des == 0 or ScoreJoueur(dic_des_retenu) >  jetons_en_jeu[0][0]:
            continue_a_jouer = False
            break
    return ScoreJoueurFinale(dic_des_retenu)