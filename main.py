from initialisationJeu import *
import pioche
import perdant
import gameplay as g
from afichage import *

def JeuPlusieurJourer():
    nombre_de_toure = 0
    
    while jetons_en_jeux != []:
        indix_jouer = nombre_de_toure%len(liste_des_joueur)
        print("au tour du joueur", liste_des_joueur[indix_jouer][0])
        AfficheJoueur()
        affichage_dominos(jetons_en_jeux)
        print("")
        score = g.TourDuJouer()
        if isinstance(score, str):
            perdant.PartiePerdu(score)
        else:
            indice_p = pioche.RechercheP(jetons_en_jeux, score)
            if isinstance(indice_p, str):
                perdant.PartiePerdu(indice_p)
        if not isinstance(score, str) and not isinstance(indice_p, str):
            print(indice_p+1)
            liste_p = jetons_en_jeux[:indice_p]
            liste_posibliliter = pioche.PiquerPckomino(liste_p, score)
            if not isinstance(liste_posibliliter, str):
                print(liste_posibliliter)
                pioche.RecupePickomino(indix_jouer, liste_posibliliter)
            else:
                print(score)
                print(liste_posibliliter)

        nombre_de_toure +=1
JeuPlusieurJourer()
