import pioche
from initialisationJeu import *


RePlacerDomino = lambda domi_remettre : jetons_en_jeu.insert(pioche.RechercheP(jetons_en_jeu, domi_remettre[0]), domi_remettre)
#supprimer le dominos de la liste du joueur
def insertion(elem):
    """ ListxElem --> None . Ins`ere elem dans la liste tri´ee"""
    pos = len(jetons_en_jeu)
    jetons_en_jeu.append(elem)
    while pos>0 and jetons_en_jeu[pos-1][0] > elem[0] :
        jetons_en_jeu[pos] = jetons_en_jeu[pos - 1]
        pos = pos - 1 #pas besoin du si car ´e valuation paresseuse
    jetons_en_jeu[pos] = elem

def PartiePerdu(erreur, indice):
    '''
    Str --> None
    replace le dernier pickomino de la pile d'un joueur et retourne(cacher) le dernier pickomino sur la table de jeu
    '''
    print(erreur)
    #print('HEREEEEEEEEEEEEEEE', indice_joueur)
    if liste_des_joueurs[indice][1] != []:
        insertion(liste_des_joueurs[indice][1].pop())
        #RePlacerDomino(liste_des_joueurs[indice_joueur][1].pop())
    RetourneDomino()
    

def RetourneDomino():
    """list x int --> None
    Affiche le nombre de jeons retournes"""
    del jetons_en_jeu[-1]
    liste_jetons_retournes.append(('# ','# '))
    print("Le nombre de jetons retournes est de : ", len(liste_jetons_retournes))




