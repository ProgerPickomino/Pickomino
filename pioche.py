from initialisationJeu import *
def RechercheP(liste_p, score):
    """ 
    List x Elem --> Bool
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
    return sup

def PiquerPckomino(liste_p, score):
    nv_liste_p = liste_p[:]
    for i in liste_des_joueur:
        if len(i[1]) != 0 and i[1][-1][0] == score:
            nv_liste_p.append(i[1][-1])
    if nv_liste_p == []:
        return "vous naver pas un score sufisans"
    return nv_liste_p

def RecupePickomino(indice_joureur, pickomino_disponible):
    """ list x int x list x list --> None"""
    liste_des_valeur_posible = [i[0] for i in pickomino_disponible]
    selections = ""
    while not isinstance(selections, int) and selections not in liste_des_valeur_posible:
        try:
            selections = int(input("ransénier le pickomino que vous souéter prandre : "))
        except ValueError:
            print("La valeur doit etre un nombre entier")
            continue
        if selections not in liste_des_valeur_posible:
            print("la valeur dois etre dans les posibiliter")
    for i in range(len(liste_des_joueur)):
        if liste_des_joueur[i][1] != [] and selections == liste_des_joueur[i][1][-1][0]:
            liste_des_joueur[indice_joureur][1].append(liste_des_joueur[i][1].pop())
            break
    if selections in liste_des_valeur_posible:
        indice_s = jetons_en_jeux.pop(RechercheP(jetons_en_jeux, selections))
        liste_des_joueur[indice_joureur][1].append(indice_s)









