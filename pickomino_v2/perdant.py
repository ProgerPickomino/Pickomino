import pioche
from initialisationJeu import *


RePlacerDomino = lambda domi_remettre : jetons_en_jeu.insert(pioche.RechercheP(jetons_en_jeu, domi_remettre[0])+1, domi_remettre)
#supprimer le dominos de la liste du joueur
def PartiePerdu(erreur):
    '''
    Str --> None
    replace le dernier pickomino de la pile d'un joueur et retourne(cacher) le dernier pickomino sur la table de jeu
    '''
    print(erreur)
    if liste_des_joueurs[indice_joueur][1] != []:
        RePlacerDomino(liste_des_joueurs[indice_joueur][1][-1])
        liste_des_joueurs[indice_joueur][1].pop()
        
    nombre_jetons_retourner = RetourneDomino()
    

def RetourneDomino():
    """list x int --> None
    Affiche le nombre de jeons retournes"""
    del jetons_en_jeu[-1]
    liste_jetons_retournes.append(('#','#'))
    print("Le nombre de jetons retournes est de : ", len(liste_jetons_retournes))







