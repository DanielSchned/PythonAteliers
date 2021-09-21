import re
import random

def full_name(nom):
    lst = nom.split(" ")
    print(str(lst[0].upper()) + " " + str(lst[1].capitalize()))



def is_mail(str_arg:str):
    tuple = [1, 0]
    if "@" not in str_arg:
        tuple = [0,2]
        print("il manque l'@", tuple)
        
    else:
        lst_mail = str_arg.split("@")
        print(lst_mail)
        print(len(lst_mail))
        if lst_mail[0] == "":
            tuple = [0, 1]
            print("le corp n'est pas valide", tuple)
        elif "gmail" not in lst_mail[1]:
            tuple = [0, 3]
            print("le domaine n'est pas valide", tuple)
        elif "." not in str_arg:
            tuple=[0,4]
            print("il manque le .", tuple)


    # for i in range(len(point)):
    #     if point[i] == "@":
    #         tuple = [1, 0]
        
    #     if point[i] == 
    

# is_mail("danielschneider2a@gmail.com")
# is_mail("danielschneider2agmail.com")
# is_mail("danielschneider2a@gmél.com")
# is_mail("danielschneider2a@gmailcom")
# is_mail("@gmail.com")

#-----------------------------------------------------------------------------------------------------------------------------------

def mots_Nlettres(lst_mot, n):
    """[summary]

    Args:
        lst_mot ([list]): [description]
        n ([int]): [description]
    """
    lst_mot_n = []
    
    for i in range(len(lst_mot)):
        if len(lst_mot[i]) == n:
            lst_mot_n.append(lst_mot[i])

    return(lst_mot_n)

# mots_Nlettres(["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", 
# "finir", "aimer"], 5)

def commence_par(mot:str, prefixe:str): 
    
    booleen = mot.endswith(prefixe,0,len(prefixe))
    return(booleen)

#commence_par("incompréhensible", "in")

def commence_par_list(mot, prefixe):
    booleen = True
    for i in range(len(prefixe)):
        if mot[i] != prefixe[i]:
            booleen = False
    return(booleen)

# commence_par_list("incompréhensible", "in")

def finit_par(mot, suffixe):
    booleen = False
    if mot[len(mot) - len(suffixe):len(mot)] == suffixe:
        booleen = True
    return(booleen)

#finit_par("probablement", "ment")

def finissent_par(lst_mot, suffixe):
    lst = []
    for i in range(len(lst_mot)):
        mot = lst_mot[i]
        if finit_par(mot, suffixe) == True:
            lst.append(mot)
    return lst
# finissent_par(["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", 
#  "finir", "aimer"], "er")

def commencent_par(lst_mot, prefixe):
    lst = []
    for i in range(len(lst_mot)):
        mot = lst_mot[i]
        if commence_par(mot, prefixe):
            lst.append(mot)
    return lst

# commencent_par(["jouer","bonjour", "aimez", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", 
#  "aimons", "aimer"], "ai")

def liste_mots(lst_mot, prefixe, suffixe, n):
    lst_f = finissent_par(lst_mot, suffixe)
    lst_c = commencent_par(lst_f, prefixe)
    lst_m = mots_Nlettres(lst_c, n)
    return(lst_m)

#liste_mots(["jouer","bonjour", "aimez", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour",  "aimons", "aimer"], "ai", "er", 5)

def dictionnaire(fichier):
    f = open(fichier, "r", 8)
    c = f.readline()
    lst_mot = []
    while c != "":
        c = f.readline().replace("\n", "")
        lst_mot.append(c)
    liste_mots(lst_mot, "ai", "er", 5)
    print("**fin**")
      
        
#dictionnaire("littre.txt")

#-----------------------------------------------------------------------------------------------------------------------

def places_lettres(ch:str, mot:str):
    j = 0
    lst_ch = []  
    for i in range(len(mot)):
        if mot[i] == ch:
            j = j + 1  
            lst_ch.append(i)
    print(lst_ch)            
            
    print(j)
#places_lettres("a", "bonjour")

def outputStr(mot, lpos):
    mot_r = "_" * len(mot)
    for e in lpos:
        for i, e1 in enumerate(mot):
            if i == e:
                mot_r = mot_r[:i] + e1 + mot_r[i + 1:]
    return(print(mot_r))

        

    
# outputStr("bonjour", [0,2])    
# outputStr("bonjour", [])
def build_list(fichier):
    file, content = open(fichier), []
    content.append(file.readline())
    while content[len(content)-1] != '':
        content.append(file.readline().replace('\n', '').lower())
    file.close()
    del content[len(content) - 1]
    return content


def runGame():
    
    #lst_mot = build_list(fichier)
    lst_m = ["jouer","bonjour", "aimez", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour",  "aimons", "aimer"]
    k = random.randrange(0, len(lst_m))
    mot = lst_m[k]
    nb_tentative = 8
    mot_r, compt, lst_i = outputStr(mot, []), 0, []
    lst_car_dess, dessin = ["\n|________"," \\", "\n|   / ", "\n|    T","\n|    O"], ""
    while len(lst_i) < len(mot_r) and compt < nb_tentative:
        lettre = input("Veuillez saisir une lettre\n")
        for e in places_lettres(lettre, mot):
            lst_i.append(e)

        print(outputStr(mot, lst_i))
        if not places_lettres(lettre, mot):
            dessin = lst_car_dess[0] + dessin
            lst_car_dess = lst_car_dess[1:]
        print(dessin)
        compt += 1
    if compt == nb_tentative:
        print("Perdu")
    else:
        print("Gagné")

#runGame("littre.txt")
    


#runGame()