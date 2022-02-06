import initialisationJeu as ij  
from affichage import *
def JeuPlusieurJoueur():
    jetons_en_jeux = [(21, 1), (22, 1), (23, 1), (24, 1), (25, 2), (26, 2), (27, 2), (28, 2), (29, 3), (30, 3), (31, 3), (32, 3), (33, 4), (34, 4), (35, 4), (36, 4)]
    affichage_dominos(jetons_en_jeux)
    jetons_retourner = 0
    liste_des_joueur = ij.InitJoueur()
    AfficheJoueur(liste_des_joueur)
    

JeuPlusieurJoueur()
