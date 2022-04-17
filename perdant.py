import pioche
from initialisationJeu import *


RePlacerDomino = lambda domi_remettre : jetons_en_jeu.insert(pioche.RechercheP(jetons_en_jeu, domi_remettre[0]), domi_remettre)
#supprimer le dominos de la liste du joueur

def insertion(elem, liste_jetons):
    """ 
    Elem x List --> None . 
    Insere elem dans la liste triee
    """
    pos = len(liste_jetons)
    liste_jetons.append(elem)
    while pos>0 and liste_jetons[pos-1][0] > elem[0] :
        liste_jetons[pos] = liste_jetons[pos - 1]
        pos = pos - 1 
    liste_jetons[pos] = elem
    return liste_jetons

def PartiePerdu(erreur, indice):
    '''
    Str --> None
    replace le dernier pickomino de la pile d'un joueur et retourne(cache) le dernier pickomino sur la table de jeu
    '''
    print(erreur)
    if liste_des_joueurs[indice][1] != []:
        insertion(liste_des_joueurs[indice][1].pop(), jetons_en_jeu)
    RetourneDomino()
    

def RetourneDomino():
    """list x int --> None
    Affiche le nombre de jeons retournes"""
    del jetons_en_jeu[-1]
    liste_jetons_retournes.append(('# ','# '))
    print("Le nombre de jetons retournes est de : ", len(liste_jetons_retournes))




