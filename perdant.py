import pioche
from initialisationJeu import *
RePlacerDomino = lambda : jetons_en_jeux.insert(pioche.RechercheP(jetons_en_jeux, liste_des_joueur[indix_jouer][1][-1][0]), liste_des_joueur[indix_jouer][1][-1])
def PartiePerdu(ereure):
    print(ereure)
    if liste_des_joueur[indix_jouer][1] != []:
        RePlacerDomino(indix_jouer)
    RetourneDomino()
    

def RetourneDomino():
    """list x int --> None"""
    del jetons_en_jeux[-1]
    global jetons_retourner
    jetons_retourner += 1
    print("le nobre de jetons retourner et de : ", jetons_retourner)






