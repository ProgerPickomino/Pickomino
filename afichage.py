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

def aficher_ganiens(liste_des_joueurs):
    indice_max = [0]
    for i in range(1, len(liste_des_joueurs)):
        if liste_des_joueurs[i][2] == liste_des_joueurs[indice_max[0]][2]:
            indice_max.append(i)
        if liste_des_joueurs[i][2] > liste_des_joueurs[indice_max[0]][2]:
            indice_max = [i]
    
    if len(indice_max) == 1:
        indice = indice_max[0]
        print(f"le ganient et {liste_des_joueurs[indice][0]} et sons score et de {liste_des_joueurs[indice][2]}")
    else:
        les_ganinent = "les ganient sons : \n"
        for j in indice_max:
            les_ganinent += f"{liste_des_joueurs[j][0]} et sons score et de {liste_des_joueurs[j][2]},\n"
        print(les_ganinent[:-2])
    
     

