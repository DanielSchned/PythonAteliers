from random import *
import random

def gen_list_random_list(int_binf = 0, int_bsup = 9):
    i = 0
    int_nbr = []
    if not int_binf and not int_bsup:
        while i <= 9:
            r = random.randrange(int_binf, int_bsup)
            int_nbr.append(r)
            i = i + 1

    else:
        while i <= int_bsup - 1 :
            r = random.randrange(int_binf, int_bsup)
            int_nbr.append(r)
            i = i + 1
    print(int_nbr)

#gen_list_random_list(8, 16)


def mix_list(list_to_mix):
    ma_liste = list_to_mix
    i = random.randint(0, len(ma_liste) - 1)

    nb_elem = len(list_to_mix)
    indices = []
    while nb_elem > 0:
        i = random.randint(0, len(ma_liste) -1)
        while i in indices: 
            i = random.randint(0, len(ma_liste) -1)
        indices.append(i)
        nb_elem = nb_elem - 1
    resultat = []
    for index in indices:
        resultat.append(ma_liste[index])
    print(resultat)
#mix_list(["a","b","c","d","e","f","g","h","i","j"])
# mix_list([1,2,3,4,5,6,7,8])

def choose_element_list(list_in_which_to_choose, int_nbr_of_element_to_extract):
    lst_rand = []
    i =0
    while i < int_nbr_of_element_to_extract:
        rand = random.randrange(0, len(list_in_which_to_choose))
        lst_rand.append(list_in_which_to_choose[rand])
        print(list_in_which_to_choose[rand])
        i = i + 1
    print(lst_rand)




#choose_element_list(["a","b","c","d","e","f","g","h","i","j"], 3)

