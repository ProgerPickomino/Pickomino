import random as rm

def LenserDes(fase_du_des, nobre_de_des):
    """
    list X dic X int --> dict
    """
    dic_du_lenser = {}
    for f in range(nobre_de_des):
        chois_du_des = rm.choice(fase_du_des)
        dic_du_lenser[chois_du_des] = dic_du_lenser.get(chois_du_des ,0) + 1
    return dic_du_lenser

def PosibliterDeJeux(lenser, dic_des_retenu):
    """
    dic --> list
    """
    des_posible_a_recuper = []
    for i in lenser:
            if i not in dic_des_retenu:
                des_posible_a_recuper.append(i)
    return des_posible_a_recuper

def Recuperations(des_posible_a_recuper):
    """
    list -->
    """
    des_recuper = None
    while des_recuper not in des_posible_a_recuper:
        des_recuper = input("Quelle dés souéte tu récuperer : ")
        if des_recuper != "veres":
            try:
                des_recuper = int(des_recuper)
            except ValueError:
                print("Tu dois entre la valeur d'un dés.")
                continue
    return des_recuper

def ScoreJouerFinale(dic_des_retenu):
    score = 0
    if "veres" in dic_des_retenu.keys():
        score = score + dic_des_retenu["veres"]*5
        del dic_des_retenu["veres"]
        for fac in dic_des_retenu:
            score = score + fac*dic_des_retenu[fac]
        return score
    return "Echeque vous ne posédéer pas de veres."

def ScoreJouer(dic_des_retenu):
    score = 0
    if "veres" in dic_des_retenu.keys():
        score = score + dic_des_retenu["veres"]*5
    for fac in dic_des_retenu:
        if fac != "veres":
            score = score + fac*dic_des_retenu[fac]
    return score

def TourDuJouer():
    """
    list X str --> int | str
    """
    continue_a_jouer = True
    nobre_de_des = 8
    fase_du_des = [1, 2, 3, 4, 5, "veres"]
    dic_des_retenu = {}
    while continue_a_jouer:
        lenser = LenserDes(fase_du_des, nobre_de_des)
        #aficher le lenser
        print("lenser : ", lenser) #temporére
        des_posible_a_recuper = PosibliterDeJeux(lenser, dic_des_retenu)
        #aficher les des que lons peux récuperer
        print("des que je peux recuper : ", des_posible_a_recuper) #temporére
        if len(des_posible_a_recuper) == 0:
            return "tu na pas de dés a récuperer sais un echerque"
        des_recuper = Recuperations(des_posible_a_recuper)
        dic_des_retenu[des_recuper] = lenser[des_recuper]
        print(ScoreJouer(dic_des_retenu))
        nobre_de_des -= lenser[des_recuper]
        if nobre_de_des == 0:
            continue_a_jouer = False
            break
        veut_tu_continuser = ""
        while veut_tu_continuser not in ("oui", "non"):
            veut_tu_continuser = input("veut tu continuer a jouer [oui/non] : ")
        if veut_tu_continuser == "non":
            continue_a_jouer = False
    return ScoreJouerFinale(dic_des_retenu)

