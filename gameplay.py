import random as rm
from afichage import *

def LanceDes(face_du_des, nombre_de_des):
    """
    list X dic X int --> dict
    Retourne le resultat du lancer de des
    """
    dic_du_lancer = {}
    for f in range(nombre_de_des):
        chois_du_des = rm.choice(face_du_des)
        dic_du_lancer[chois_du_des] = dic_du_lancer.get(chois_du_des ,0) + 1
    return dic_du_lancer

def PossibliterDeJeux(lenser, dic_des_retenu):
    """
    dic --> list
    retourne la liste des des qu'un joueur peux recuperer
    """
    des_possible_a_recuperer = []
    for i in lenser:
            if i not in dic_des_retenu:
                des_possible_a_recuperer.append(i)
    return des_possible_a_recuperer

def Recuperations(des_possible_a_recuperer):
    """
    list --> int
    retourne le des que le joueur veut recuperer 
    """
    des_recupere = None
    while des_recupere not in des_possible_a_recuperer:
        des_recupere = input("Quel dés souhaites tu récuperer : ")
        if des_recupere != "vers":
            try:
                des_recupere = int(des_recupere)
            except ValueError:
                print("Tu dois entrer la valeur d'un dés.")
                continue
    return des_recupere

def ScoreJoueurFinale(dic_des_retenu):
    '''
    Dict --> None | Int
    retourne le score du joueur si celui-ci est compris entre 21 et 36, une erreur sinon
    '''
    score = 0
    if "vers" in dic_des_retenu.keys():
        score = score + dic_des_retenu["vers"]*5
        del dic_des_retenu["vers"]
        for fac in dic_des_retenu:
            score = score + fac*dic_des_retenu[fac]
        return score
    return "Echec vous ne possedez pas de verres."

def ScoreJoueur(dic_des_retenu):
    '''
    Dict --> Int
    Retourne le score du joueur apres chaque lqnce de des
    '''
    score = 0
    if "vers" in dic_des_retenu.keys():
        score = score + dic_des_retenu["vers"]*5
    for fac in dic_des_retenu:
        if fac != "vers":
            score = score + fac*dic_des_retenu[fac]
    return score

def TourDuJoueur():
    """
    list X str --> int | str
    """
    continue_a_jouer = True
    nombre_de_des = 8
    face_du_des = [1, 2, 3, 4, 5, "vers"]
    dic_des_retenu = {}
    while continue_a_jouer:
        lancer = LanceDes(face_du_des, nombre_de_des)
        #aficher le lancer
        affiche_des(lancer) #temporére
        des_possible_a_recuperer = PossibliterDeJeux(lancer, dic_des_retenu)
        #aficher les des que lons peux récuperer
        print("des que je peux recuper : ", des_possible_a_recuperer) #temporére
        if len(des_possible_a_recuperer) == 0:
            return "tu n'as pas de dés a récuperer c'est un echec"
        des_recupere = Recuperations(des_possible_a_recuperer)
        dic_des_retenu[des_recupere] = lancer[des_recupere]
        print('Votre score est de :',ScoreJoueur(dic_des_retenu))
        nombre_de_des -= lancer[des_recupere]
        if nombre_de_des == 0:
            continue_a_jouer = False
            break
        veux_tu_continuer = ""
        while veux_tu_continuer not in ("oui", "non"):
            veux_tu_continuer = input("veux tu continuer a jouer [oui/non] : ")
        if veux_tu_continuer == "non":
            continue_a_jouer = False
    return ScoreJoueurFinale(dic_des_retenu)

