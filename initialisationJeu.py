

def InitJoueur():
    '''None --> List
    retourne la liste des joueurs saisies au clavier'''

    liste_des_joueurs = []
    nombre_de_joueur = ""
    type_partie = ""
    nombre_de_joueur = 0
    global nombre_de_joueurs_aleatoire 
    nombre_de_joueurs_aleatoire = 0
    while not 1<nombre_de_joueur<=6 or (type_partie not in {'h', 'a'}):
        try:
            type_partie = input("Voulez-vous jouer une partie humains VS humains ou humains VS artificielles {h/a} : ")
            if type_partie not in {'h', 'a'}:
                print('Veuillez choisir h/a : ')
            else :
                nombre_de_joueur = int(input("Entrer le nombre de joueurs : "))
        except ValueError:
            print("Vous devez saisir un entier")
            continue

    if type_partie == "a":
        while  not 1<=nombre_de_joueurs_aleatoire<=nombre_de_joueur :
            try :
                nombre_de_joueurs_aleatoire = int(input("Entrez le nombre de joueurs aleatoires : "))
            except ValueError :
                print("Vous devez saisir un entier")
                continue

    nombre_de_joueur_humains = nombre_de_joueur - nombre_de_joueurs_aleatoire 

    for i in range(nombre_de_joueur):
        if i < nombre_de_joueurs_aleatoire :
            nom_du_joueur = input(f"Nom du joueur aleatoire {i+1} : ")
        else :
            nom_du_joueur = input(f"Nom du joueur humain {i+1} : ")

        liste_des_joueurs.append([nom_du_joueur, [], 0])

    return liste_des_joueurs
  
    
jetons_en_jeu = [(21, 1), (22, 1), (23, 1), (24, 1), (25, 2), (26, 2), (27, 2), (28, 2), (29, 3), (30, 3), (31, 3), (32, 3), (33, 4), (34, 4), (35, 4), (36, 4)]
indice_joueur = 0
liste_des_joueurs = InitJoueur()
liste_jetons_retournes = []
