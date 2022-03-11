import pioche
from initialisationJeu import *

jetons_retourner = 0

RePlacerDomino = lambda : jetons_en_jeux.insert(pioche.RechercheP(jetons_en_jeux, liste_des_joueur[indix_jouer][1][-1][0]), liste_des_joueur[indix_jouer][1][-1])
def PartiePerdu(ereure):
    '''
    Str --> None
    replace le dernier pickomino de la pile d'un joueur et retourne(cacher) le dernier pickomino sur la table de jeu
    '''
    print(ereure)
    if liste_des_joueur[indix_jouer][1] != []:
        RePlacerDomino()
    RetourneDomino()
    

def RetourneDomino():
    """list x int --> None
    Affiche le nombre de jeons retournes"""
    del jetons_en_jeux[-1]
    global jetons_retourner
    jetons_retourner += 1
    print("Le nombre de jetons retournes est de : ", jetons_retourner)







