
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
    max_nb = ""
    max_nb = max(L)
    return(max_nb)

#val_max([1,2,3,4])

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

#nb_occurences([1,2,3,4], 3)

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
    while i < len(L):
        if L[i] < L[i + 1]:
            booleen = True
        else:
            booleen = False


    return(booleen)

#print(est_triee_while([1,2,4,4]))

def position_tri(L, e):
    a = 0
    b = len(L) - 1
    
    if est_triee_for(L) ==  True:

        while a <= b:
            m = (a + b) // 2
            if L[m] == e:
                # on a trouvé v
                return True
            elif L[m] < e:
                a = m + 1
            else:
                b = m - 1
        # on a a > b
        return False

position_tri([1,2,4,5], 3)