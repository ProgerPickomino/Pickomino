def InitJoueur():
    liste_des_joueur = []
    nombre_de_joueur = ""
    while not isinstance(nombre_de_joueur, int) or not 1<nombre_de_joueur<=6:
        try:
            nombre_de_joueur = int(input("\nEntrez le nombre de joueur : "))
        except ValueError:
            print("La valeur doit etre un nombre entier")
            continue

    for i in range(nombre_de_joueur):
        nom_du_joueur = input(f"nom du joueur {i+1} : ")
        liste_des_joueur.append([nom_du_joueur, []])
    return liste_des_joueur


