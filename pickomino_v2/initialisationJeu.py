def InitJoueur():
    '''None --> List
    retourne la liste des joueurs saisies au clavier'''

    liste_des_joueurs = []
    nombre_de_joueur = ""
    while not isinstance(nombre_de_joueur, int) or not 1<nombre_de_joueur<=6:
        try:
            nombre_de_joueur = int(input("Entrer le nombre de joueur : "))
        except ValueError:
            print("Vous devez saisir un entier")
            continue

    for i in range(nombre_de_joueur):
        nom_du_joueur = input(f"Nom du joueur {i+1} : ")
        liste_des_joueurs.append([nom_du_joueur, []])
    return liste_des_joueurs
    
jetons_en_jeu = [(21, 1), (22, 1), (23, 1), (24, 1), (25, 2), (26, 2), (27, 2), (28, 2), (29, 3), (30, 3), (31, 3), (32, 3), (33, 4), (34, 4), (35, 4), (36, 4)]
indice_joueur = 0
liste_des_joueurs = InitJoueur()

liste_jetons_retournes = []