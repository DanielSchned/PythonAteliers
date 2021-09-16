import re

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
        lst_mot ([type]): [description]
        n ([type]): [description]
    """
    lst_mot_n = []
    
    for i in range(len(lst_mot)):
        if len(lst_mot[i]) == n:
            lst_mot_n.append(lst_mot[i])

    return(print(lst_mot_n))

mots_Nlettres(["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", 
"finir", "aimer"], 5)

def commence_par(mot, prefixe): 
    
    if prefixe in mot:
        booleen = True
    else:
        booleen  = False

    return(print(booleen))

commence_par("incompréhensible", "in")

