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

def PiquerPckomino(liste_p, score, indice_joueur):
    """ List x Int --> List
    Renvoie la liste des pickominos qu'un joueur peut prendre"""
    jetons_du_joueur = liste_des_joueurs[indice_joueur][1]
    nv_liste_p = [e for e in liste_p if e not in jetons_du_joueur]
    #liste_des_joueurs
    for i in liste_des_joueurs:
        if len(i[1]) != 0 and i[1][-1][0] == score :
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
    for i in range(len(liste_des_joueurs)):
        if liste_des_joueurs[i][1] != [] and selections == liste_des_joueurs[i][1][-1][0]:
            liste_des_joueurs[indice_joueur][1].append(liste_des_joueurs[i][1].pop())
            break
    if selections in liste_des_valeur_possible:
        indice_s = jetons_en_jeu.pop(RechercheP(jetons_en_jeu, selections))
        liste_des_joueurs[indice_joueur][1].append(indice_s)








