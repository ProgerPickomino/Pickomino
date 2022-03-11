from initialisationJeu import *

def RechercheP(liste_p, score):
    """ 
    List x Elem --> Int
    Retourne l'indice du pickomino inferieur ou egal au score
    """
    if isinstance(score, str):
        return score
    appartient = False
    inf , sup = 0, len ( liste_p ) - 1
    while inf <= sup and not ( appartient ) :
        med = ( inf + sup )//2
        if liste_p [med][0] == score :
            appartient = True
        elif liste_p [med][0] > score :
            sup = med - 1
        else :
            inf = med + 1
    return med

def PiquerPckomino(liste_p, score):
    """ List x Int --> List
    Renvoie la liste des pickominos qu'un joueur peut prendre"""
    nv_liste_p = liste_p[:]
    for i in liste_des_joueur:
        if len(i[1]) != 0 and i[1][-1][0] == score:
            nv_liste_p.append(i[1][-1])
    if nv_liste_p == []:
        return "\nVotre score est insuffisant"
    return nv_liste_p


def RecupePickomino(indice_joueur, pickomino_disponible):
    """ list x int -->  None"""
    liste_des_valeur_possible = [i[0] for i in pickomino_disponible]
    selections = ""
    while not isinstance(selections, int) and selections not in liste_des_valeur_possible:
        try:
            selections = int(input("\nQuel pickomino voulez-vous prendre : "))
        except ValueError:
            print("\nLa valeur doit etre un nombre entier")
            continue
        if selections not in liste_des_valeur_possible:
            print("\nLa valeur dois etre dans les posibilites")
    for i in range(len(liste_des_joueur)):
        if liste_des_joueur[i][1] != [] and selections == liste_des_joueur[i][1][-1][0]:
            liste_des_joueur[indice_joueur][1].append(liste_des_joueur[i][1].pop())
            break
    if selections in liste_des_valeur_possible:
        indice_s = jetons_en_jeux.pop(RechercheP(jetons_en_jeux, selections))
        liste_des_joueur[indice_joueur][1].append(indice_s)









