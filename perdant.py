import pioche
from initialisationJeu import *

jetons_retournes = 0

RePlacerDomino = lambda : jetons_en_jeu.insert(pioche.RechercheP(jetons_en_jeu, liste_des_joueurs[indice_joueur][1][-1][0]), liste_des_joueurs[indice_joueur][1][-1])
#supprimer le dominos de la liste du joueur
def PartiePerdu(erreur):
    '''
    Str --> None
    replace le dernier pickomino de la pile d'un joueur et retourne(cacher) le dernier pickomino sur la table de jeu
    '''
    print(erreur)
    if liste_des_joueurs[indice_joueur][1] != []:
        RePlacerDomino()
    RetourneDomino()
    

def RetourneDomino():
    """list x int --> None
    Affiche le nombre de jeons retournes"""
    del jetons_en_jeu[-1]
    global jetons_retournes
    jetons_retournes += 1
    print("Le nombre de jetons retournes est de : ", jetons_retournes)







