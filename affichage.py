
def AfficheJoueur(liste_des_joueur):
    for i in range(len(liste_des_joueur)):
        print(liste_des_joueur[i][0], ": ", end = "")
        if len(liste_des_joueur[i][1]) == 0:
            print("Le joueur n'a pas de jetons")
        else:
            print("Son jetons le plus haut et :", liste_des_joueur[i][1][-1])

def affichage_dominos(Liste):
    """List --> None 
    affiche les dominos
    """
    if len(Liste)==0:
        print("Toues les dominos ont ete joues")
    print(' -----  '*len(Liste))
    for i in range(len(Liste)):
        print(' |',Liste[i][0],'| ', end = '')
    print(' ')
    print(' -----  '*len(Liste), end='') 
    print(' ')  
    for i in range(len(Liste)):
        print(' |',Liste[i][1],'|  ', end = '')  
    print(' ')
    print(' -----  '*len(Liste), end='') 
