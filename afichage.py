
def aficheJoueur(liste_des_joueur):
    for i in range(len(liste_des_joueur)):
        print(liste_des_joueur[i][0], ": ", end = "")
        if len(liste_des_joueur[i][1]) == 0:
            print("le joueur na pas de jetons")
        else:
            print("sons jetons le plus haut et :", liste_des_joueur[i][1][-1])