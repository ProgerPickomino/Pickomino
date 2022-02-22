from initialisationJeu import *
def AfficheJoueur(liste_des_joueur):
    for i in range(len(liste_des_joueur)):
        print(liste_des_joueur[i])
        
        print(liste_des_joueur[i][0], ":", end = "")
        if len(liste_des_joueur[i][1]) == 0:
            print("Le joueur n'a pas de jetons")
        else:
            print("Son jetons le plus haut et :", liste_des_joueur[i][1][-1], "sons nombre de jetons et de", len(liste_des_joueur[i][1]))

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

def affiche_des(lance_de_des):
    list_des = []
    """ 
    Dic --> None
    """
    for des in lance_de_des :
        for i in range(lance_de_des[des]):
            list_des.append(des)
    print(list_des) 

def dominos_caches(list_dominos, dernier_visible = True):
    '''
    List x Bool --> List
    masque tous les dominos du joueur sauf le dernier
    '''
    if dernier_visible:
        nb_dominos_caches = len(list_dominos)-1
        dernier_dominos = list_dominos[-1]
    else :
        nb_dominos_caches = len(list_dominos)
        dernier_dominos = ('#','#')
    
    l_dominos_caches = [('# ', '#') for i in range(nb_dominos_caches)]
    l_dominos_caches.append(dernier_dominos)
    return l_dominos_caches

#affichage_dominos(dominos_caches([(29, 3), (30, 3), (31, 3), (32, 3), (33, 4), (34, 4), (35, 4), (36, 4)]))


#fonction qui affiche les dominos retournes