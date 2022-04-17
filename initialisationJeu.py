def InitJoueur():
    '''None --> List
    retourne la liste des joueurs saisies au clavier'''

    liste_des_joueurs = []
    nombre_de_joueur = ""
    nombre_de_joueur = 0
    while not 1<nombre_de_joueur<=6 :
        try:
            nombre_de_joueur = int(input("Entrer le nombre de joueurs : "))
        except ValueError:
            print("Vous devez saisir un entier")
            continue
    


    for i in range(nombre_de_joueur):
        type_du_joueur = ""
        nom_du_joueur = input(f"Nom du joueur {i+1} : ")
        while type_du_joueur not in {"a", "h", "g"}:
            type_du_joueur = input(f"voulez-vous que {nom_du_joueur} sois un jouer humain, aléatoire ou glouton (h/a/g) : ")
        liste_des_joueurs.append([nom_du_joueur, [], 0, type_du_joueur])
    print(liste_des_joueurs)
    return liste_des_joueurs
  
    
jetons_en_jeu = [(21, 1), (22, 1), (23, 1), (24, 1), (25, 2), (26, 2), (27, 2), (28, 2), (29, 3), (30, 3), (31, 3), (32, 3), (33, 4), (34, 4), (35, 4), (36, 4)]
indice_joueur = 0
liste_des_joueurs = InitJoueur()
liste_jetons_retournes = []
