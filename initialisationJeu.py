def InitJoueur():
    liste_des_joueur = []
    nombre_de_joueur = ""
    while not isinstance(nombre_de_joueur, int) or not 1<nombre_de_joueur<=6:
        try:
            nombre_de_joueur = int(input("entre le nobre de joueur : "))
        except ValueError:
            print("La valeur doit etre un nombre entier")
            continue

    for i in range(nombre_de_joueur):
        nom_du_joueur = input(f"nom du joueur {i+1} : ")
        liste_des_joueur.append([nom_du_joueur, []])
    return liste_des_joueur
jetons_en_jeux = [(21, 1), (22, 1), (23, 1), (24, 1), (25, 2), (26, 2), (27, 2), (28, 2), (29, 3), (30, 3), (31, 3), (32, 3), (33, 4), (34, 4), (35, 4), (36, 4)]
jetons_retourner = 0
liste_des_joueur = InitJoueur()
indix_jouer = 0