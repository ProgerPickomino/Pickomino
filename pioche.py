from initialisationJeu import *

def RechercheP(liste_p, score):
    """ 
    List x Elem --> Int
    Retourne l'indice du pickomino inferieur ou egal au score
    """
    if isinstance(score, str):
        return score
    appartient = False
    pos = len(liste_p)
    while pos >= 0 and not appartient:
        pos -= 1
        if liste_p[pos][0] == score :
            appartient = True
    return pos
print(
    RechercheP([(21, 1), (22, 1), (23, 1), (24, 1), (25, 2), (26, 2), (27, 2)] , 24))

def PiquerPckomino(liste_p, score, indice):
    """ 
    List x Int --> List | Str
    Renvoie la liste des pickominos qu'un joueur peut prendre
    """
    jetons_du_joueur = liste_des_joueurs[indice][1]
    nv_liste_p = [e for e in liste_p if e not in jetons_du_joueur]
    #liste_des_joueurs
    for i in range(len(liste_des_joueurs)):
        if i!= indice and len(liste_des_joueurs[i][1]) != 0 and liste_des_joueurs[i][1][-1][0] == score :
            nv_liste_p.append(liste_des_joueurs[i][1][-1])
    if nv_liste_p == []:
        return "\nVotre score est insuffisant"
    return nv_liste_p 

def RecupePickomino(indice_joueur, pickomino_disponible):
    """ list x int -->  None"""
    liste_des_valeur_possible = [i[0] for i in pickomino_disponible]
    pickomino_autre_joueur = []
    selections = ""
    while  selections not in liste_des_valeur_possible:
        try:
            selections = int(input("\nQuel pickomino voulez-vous prendre : "))
        except ValueError:
            print("\nLa valeur doit etre un nombre entier")
            continue
        if selections not in liste_des_valeur_possible:
            print("\nLa valeur dois etre dans les possibilites")

    for i in range(len(liste_des_joueurs)):
        if liste_des_joueurs[i][1] != [] and selections == liste_des_joueurs[i][1][-1][0]:
            pickomino_autre_joueur.append(liste_des_joueurs[i][1][-1][0])
            liste_des_joueurs[indice_joueur][1].append(liste_des_joueurs[i][1].pop())
            
            break
    if selections in liste_des_valeur_possible and (selections not in pickomino_autre_joueur):
        indice_s = jetons_en_jeu.pop(RechercheP(jetons_en_jeu, selections))
        liste_des_joueurs[indice_joueur][1].append(indice_s)










