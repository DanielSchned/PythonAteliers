def somme1(L:list):
    """Calcul de la somme des nombre d'une liste"""
    for i in range(len(L)):
        somme = L[i] + L[i + 1] + L[i + 2] + L[i + 3]
        return(print(somme))


somme1([1,2,3,4])

def somme2(L:list):
    while len(L) == len(L):
        L[i] = L[i] + L[i + 1]
        

