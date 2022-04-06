from initialisationJeu import *
from perdant import *

def AfficheJoueur(liste_des_joueurs):
    for i in range(len(liste_des_joueurs)):
        print(liste_des_joueurs[i][0], ":", end = "")
        if len(liste_des_joueurs[i][1]) == 0:
            print("Le joueur n'a pas de jetons")
        else:
            print("\nVous avez ", len(liste_des_joueurs[i][1]),' jetons',"Le jeton en haut de la pile est :", liste_des_joueurs[i][1][-1])
            affichage_dominos(liste_des_joueurs[i][1])
            print('\n')
      
def affichage_dominos(Liste):
    """
    List --> None 
    affiche les dominos
    """
    if len(Liste)==0:
        print("\nTous les dominos ont été joués")
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

def affiche_des(lance_de_des):
    list_des = []
    """ 
    Dic --> None
    """
    for des in lance_de_des :
        for i in range(lance_de_des[des]):
            list_des.append(des)
    print(list_des) 

     

