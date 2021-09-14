
def somme1(L:list):
    """Calcul de la somme des nombre d'une liste avec for in range"""
    somme = 0
    for i in range(len(L)):
        somme = somme + L[i]
    return(somme)


#somme1([1,2,3,4])

def somme2(L:list):
    """Calcul de la somme des nombre d'une liste avec for in"""
    i, somme = 0, 0
    while i < len(L):
        
        somme = somme + L[i]
        i = i + 1

    return(somme)

#somme2([1,2,3,4])

def somme3(L:list):
    """Calcul de la somme des nombre d'une liste avec la boucle while"""
    somme = 0
    for c in L:
        somme = somme + c
    return(somme)

#somme3([1,2,3,4])

def test_exercice1 (): 
  print("TEST SOMME") 
  #test liste vide 
  print("Test liste vide -> 1 : "+ str(somme1([]))+ " 2 : "+ str(somme2([]))+ " 3 : "+ str(somme3([]))) 
  #test somme 11111 
  S=[1,10,100, 1000] 
  print("Test liste somme = 1111 -> 1 : "+ str(somme1(S))+ " 2 : "+ str(somme2(S))+ " 3 : "+ str(somme3(S))) 

#test_exercice1()

def moyenne(L:list):
    """Calcul moyenne"""
    moyenne = 0
    if len(L) > 0:
        moyenne = somme1(L) / len(L)
        
    return (moyenne)

# moyenne([1,2,3,4])
# moyenne([])

def test_moyenne():
    print("Test moyenne")
    #test liste vide
    print("Test liste vide -> 1 : "+ str(moyenne([])))
    
#test_moyenne()

def nb_sup(L:list, e:int):
    """Nombre supérieur

    Args:
        L (list): 
        e (int): 
    """
    i = 0
    liste = []
    for c in L:
        if c > e:
            i= i +1
            liste.append(c)

    return(liste)

def nb_sup2(L:list, e:int):
    """Valeur supérieures a un nombre donné

    Args:
        L (list): 
        e (int): 
    """
    i = 0
    for c in range(len(L)):
        if L[c] > e:
            i= i +1
    return("Il y a " + str(i) + " valeurs au dessus de " + str(e))

#nb_sup([1,2,3,4], 2)


def moy_sup(L:list, e:int):
    """[summary]

    Args:
        L (list): 
        e (int): 
    """
    L = nb_sup(L, e)
    moyenne(L)
    

#moy_sup([1,2,3,4], 2)

def val_max(L:list):
    """[summary]

    Args:
        L (list): 
    """
    resultat = L[0]
    for i in range(len(L) - 1):
        if L[i] < L[i + 1]:
            resultat = L[i+1]
    return(resultat)

print(val_max([1,2,3,100]))

def ind_max(L:list):

    """[summary]

    Args:
        L (list): [description]
    """

    i = 0
    while len(L) > i:
        i = i + 1

    return(i - 1)

#ind_max([1,2,3,4])

#---------------------------------------------------------------------------------------

def positionFor(L:list, e:int):
    """Recherche entier identique dans une liste

    Args:
        L (list): 
        e (int): 
    """

    message = 0
    for i in range(len(L)):
        if L[i] == e:
            message = -1
            return(message)
            
#positionFor([1,2,3,4], 5)

def positionWhile(L:list, e:int):
    """[summary]

    Args:
        L (list): 
        e (int): 
    """
    message = 0
    i = 0 
    while i < len(L):
        if L[i] == e:
            message = -1
            return(print(message))
        i = i + 1

#positionWhile([1,2,3,4], 5)

def nb_occurences(L:list,e:int):
    """Nombre d'occurence d'un nombre donné dans une liste

    Args:
        L (list):
        e (int): 
    """
    nbOccurence = 0
    for i in range(len(L)):
        if L[i] == e:
            nbOccurence = nbOccurence + 1
    return(nbOccurence)

#print(nb_occurences([1,2,3,3], 3))

def est_triee_for(L:list):
    for i in range(len(L) - 1):
        if L[i] < L[i + 1]:
            booleen = True
        else:
            booleen = False
    return(booleen)
            
    
#print(est_triee_for([1,2,3,4]))

def est_triee_while(L:list):
    i = 0
    while i < len(L) - 1 :
        if L[i] < L[i + 1]:
            booleen = True
            i = i + 1
        else: 
            booleen = False
            i = i + 1
            break


    return(booleen)

#print(est_triee_while([1,2,4,5]))

def position_tri(L, e):
    a = 0
    b = len(L) - 1

    if est_triee_for(L) ==  True:

        while a <= b:
            m = (a + b) // 2
            
            if L[m] == e:

                return True
            elif L[m] < e:
                a = m + 1
            else:
                b = m - 1
        return False

#print(position_tri([1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 9))

def a_repetition(L):
    i = 0
    o = 0
    L_t = []
    booleen = False
    

    while i < len(L) - 1 :


        if L[i+1] == L_t[0]:
            booleen = True
            return booleen
        else:        
            i = i + 1
            o = o + 1 
            if booleen == False:
                L_t.remove(0)
                L_t = L_t.append(L[0 + o])
        

#print(a_repetition([0,1,1,5]))

def separer(L):
    lst_sep = []

    for i in range(len(L)):
        o = i // 2
        if L[i] < 0:
            lst_sep.insert(0,L[i])
        if L[i] > 0:
            lst_sep.append(L[i])
        else:
            lst_sep.insert(o, L[i])        
    return(lst_sep)

#print(separer([-5, -6, -7, -8, 6, 7, 8, 9, -4, -1, 12, 13, 0, 0 , 0]))

def histo(lst_f: list) -> list:
    """
    Retourne L'histogramme de la liste en paramètre
    :param lst_f: list
    :return: list
    """
   
    MAXTAILLE =  val_max(lst_f) + 1
    lst_h = []
    for i in range(round(MAXTAILLE)):
        lst_h.append(nb_occurences(lst_f, i))
    return lst_h

#print(histo([6,8,3,2,1,5,9,5,3,1,8]))


def est_injective(lst_f):
    lst_f_histo = histo(lst_f)
    resultat = True
    i = 0
    while i < len(lst_f_histo):
        if lst_f_histo[i] > 1:
            resultat = False
        i = i + 1
    return resultat

# print(est_injective([6,8,3,2,1,5,9,5,3,1,8]))
# print(histo([6,8,3,2,1,5,9,5,3,1,8]))

def est_surjective(lst_f):
    lst_f_histo = histo(lst_f)
    resultat = True
    i = 0
    while i < len(lst_f_histo):
        if lst_f_histo[i] < 1:
            resultat = False
        i = i + 1
    return resultat
 
# print(est_surjective([6,8,3,2,1,5,9,5,3,1,8]))
# print(histo([6,8,3,2,1,5,9,5,3,1,8]))

def est_bijective(lst_f):
    resultat = False
    if est_surjective(lst_f) == True and est_injective(lst_f) == True:
        resultat = True
    return(resultat)

# print(est_bijective([0,1,2,3,4,5,6,7,8,9]))
# print(est_injective([0,1,2,3,4,5,6,7,8,9]))
# print(est_surjective([0,1,2,3,4,5,6,7,8,9]))

# print(histo([0,1,2,3,4,5,6,7,8,9]))

