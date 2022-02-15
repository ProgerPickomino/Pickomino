import random as rm

#cette fonction est faite de facon a lancer un seul des plusieurs fois et noter le nombre aui sort
def LenserDes(face_du_des, nombre_de_des):
    """
    list X int --> dict
    Fonction qui  renvoit une liste des valeurs affichees et leurs occurences apres le lance de des
    """
    #face des c'est les des disponibles
    #on ne peut pas mettre de valeurs par defauts parce que les des disponibles changent 
    dic_du_lancer = {}
    for f in range(nombre_de_des):
        chois_du_des = rm.choice(face_du_des) #prend une seule valeur
        dic_du_lancer[chois_du_des] = dic_du_lancer.get(chois_du_des ,0) + 1 #sauvegarde l'occurence des valeurs
    return dic_du_lancer

def PosibliterDeJeux(lancer, dic_des_retenu): # renvoit la liste des des que le joueur peut pendre, s'ils ne sont pas deja sorties
    """
    dic --> list
    """
    des_possible_a_recuper = []
    for i in lancer:
            if i not in dic_des_retenu:
                des_possible_a_recuper.append(i)
    return des_possible_a_recuper

def Recuperations(des_possible_a_recuper): #avec cette fonction on peut recuperer une seule valeur a la fois ? 

    """
    List -->  Str | Int
    """
    des_recuper = None
    while des_recuper not in des_possible_a_recuper:
        des_recuper = input("Quel dés souhaites-tu récuperer : ")
        if des_recuper != "veres":
            try:
                des_recuper = int(des_recuper)
            except ValueError:
                print("Tu dois entrer la valeur d'un dés.")
                continue
    return des_recuper

def ScoreJouer(dic_des_retenu):

    score = 0
    if "veres" in dic_des_retenu.keys():
        score = score + dic_des_retenu["veres"]*5
        del dic_des_retenu["veres"]
        for fac in dic_des_retenu:
            score = score + fac*dic_des_retenu[fac]
        return score
    return "Echec vous ne possedez pas de verres."

def Affiche_des(des_affiches):
    '''dic --> None'''
    for v in des_affiches:
        print(des_affiches['v'])

def TourDuJouer():
    """
    list X str --> None
    """
    continue_a_jouer = True
    nobre_de_des = 8
    fase_du_des = [1, 2, 3, 4, 5, "veres"]
    dic_des_retenu = {}
    while continue_a_jouer:
        lenser = LenserDes(fase_du_des, nobre_de_des)
        #aficher le lenser
        print("lancer : ", lenser) #temporere
        des_posible_a_recuper = PosibliterDeJeux(lenser, dic_des_retenu)
        #aficher les des que lons peux récuperer
        print("Des que je peux recuper : ", des_posible_a_recuper) #temporere
        if len(des_posible_a_recuper) == 0:
            return "tu n'as pas de simbole a récuperer c'est un echec"
        des_recuper = Recuperations(des_posible_a_recuper)
        dic_des_retenu[des_recuper] = lenser[des_recuper] #pour stocker l'occurence du des
        nobre_de_des -= lenser[des_recuper]
        veut_tu_continuer = ""
        while veut_tu_continuer not in ("oui", "non"):
            veut_tu_continuer = input("veut tu continuer a jouer [oui/non] : ")
        if veut_tu_continuer == "non":
            continue_a_jouer = False
    return ScoreJouer(dic_des_retenu)
#la on affiche les pickominos du plateau et ceux des autres joueurs puis on fait une fonction pour selectionner les pickominos
#fonction qui cache les pickominos sauf le dernier et fonction qui retourne le dernier pickomino
print(TourDuJouer())