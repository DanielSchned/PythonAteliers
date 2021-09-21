from random import *
import random
import time
import matplotlib.pyplot as plt 

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
    return(int_nbr)

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


    return(resultat)
#mix_list(["a","b","c","d","e","f","g","h","i","j"])
mix_list([1,2,3,4,5,6,7,8])

def choose_element_list(list_in_which_to_choose, int_nbr_of_element_to_extract):
    lst_rand = []
    i =0
    while i < int_nbr_of_element_to_extract:
        rand = random.randrange(0, len(list_in_which_to_choose))
        lst_rand.append(list_in_which_to_choose[rand])
        print(list_in_which_to_choose[rand])
        i = i + 1
    return(print(lst_rand))




# choose_element_list(["a","b","c","d","e","f","g","h","i","j"], 3)

#----------------------------------------------------------------------------------------------------------------------------------

# #Pour mesurer le temps d'exécution nous avons à notre disposition  
# #la fonction perf_counter() 
# n = 10000000 
# #Récupération du temps système et démarrage du chronomètre 
# start_pc = time.perf_counter() 
# for i in range(n): 
#     #on ne fait rien... 
#     None 
# end_pc = time.perf_counter() 
 
# elapsed_time_pc = end_pc-start_pc 
 
# print("Temps écoulé entre les deux mesures : ",elapsed_time_pc) 
# print("Temps estimé pour une instruction",elapsed_time_pc/n) 
# # Exécutez ce code et vérifiez par vous-même la variabilité des mesures.

def mix_list_shuffle(list_to_mix):
    random.shuffle(list_to_mix)
    return(list_to_mix)



def perf_mix(mix_list:callable, mix_list_shuffle:callable, lst_it = [10, 500, 5000, 50000, 100000], it = 10):
    start_pc1 = time.perf_counter() 
    j = 0
    
    for i in range(len(lst_it)):
        lst_test = mix_list(gen_list_random_list(0, lst_it[i]))
    print(lst_test)
    end_pc1 = time.perf_counter() 
    start_pc2 = time.perf_counter()
    j = 0 
    for i in range(len(lst_it)):
        while j != lst_it[i]:
            mix_list_shuffle
            j = j+1
    end_pc2 = time.perf_counter() 
    elapsed_time_pc1 = end_pc1-start_pc1
    elapsed_time_pc2 = end_pc2-start_pc2
    lst_comp = [elapsed_time_pc1, elapsed_time_pc2]
    return(print(lst_comp))


#perf_mix(mix_list, mix_list_shuffle) 