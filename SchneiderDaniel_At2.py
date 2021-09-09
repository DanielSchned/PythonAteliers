#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Daniel
#
# Created:     07/09/2021
# Copyright:   (c) Daniel 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from math import *
import datetime

def main():
    pass

if __name__ == '__main__':
    main()

def exo1(imc:float):
    """Interprétation en fonction de l'IMC rentrée"""
    interpretation = ""

    if imc > 40:
        interpretation = "Obésité morbide"
    elif imc > 35:
        interpretation = "Obésité sévère"
    elif imc > 30:
        interpretation = "Obésité modérée"
    elif imc > 25:
        interpretation = "Surpoid"
    elif imc > 18.5:
        interpretation = "Corpulence normale"
    elif imc > 16.5:
        interpretation = "Maigreur"
    else:
        interpretation = "Dénutrition ou famine"

    #interpretation retourne une chaine de caractère
    return(interpretation)

a = exo1(34.4)
b = exo1(15)
c = exo1(46)

def test_exo1():
    print(a)
    print(b)
    print(c)

#test()
#--------------------------------------------------------------------------------------
def est_bissextile(annee:int):
    """Fonction pour savoir si une année est bissextile ou non"""

    return(annee%4==0 and annee%100!=0) or annee%400==0

def test_est_bissextile():
    print(est_bissextile(2020))
    print(est_bissextile(2022))
    print(est_bissextile(2015))
    print(est_bissextile(2024))

test_est_bissextile()
#-------------------------------------------------------------------------------
def discriminant (a:float,b:float,c:float):
    """calcul discriminant"""
    delta = b*b - 4*a*c
    return(delta)


def racine_unique(a:float,b:float):
    """calcul racien unique"""
    x = -b / (2 * a)
    return x

def racine_double(a:float,b:float,delta:float,num:int):
    """calcul racine double"""
    if num == 1:
        x1 = (-b + sqrt(delta)) / (2*a)
        message = x1
    if num == 2:
        x2 = (-b - sqrt(delta)) / (2*a)
        message = x2
    #retourne le resultat du calcul, en float
    return(message)

def str_equation(a:float,b:float,c:float):
    """affichage equation"""
    #retourne une chaine de caractère
    return(str(a) + "x² + " + str(b) + "x + " + str(c) + " = 0")


#str_equation(2,3,4)

def solution_equation(a:float,b:float,c:float):
    """Solution de l'équation"""
    if discriminant(a,b,c) < 0:
        message = "Solution de l'équation : "+str_equation(a,b,c)+ "\nPas de racine"
    elif discriminant(a,b,c) == 0:
        message = "Solution de l'équation : "+str_equation(a,b,c)+ "\nRacine unique : x= " + str(racine_unique(a,b))
    elif discriminant(a,b,c) > 0:
        delta = discriminant(a,b,c)

        message = "Solution de l'équation : "+ str_equation(a,b,c) + "\nRacine double : x1= " + str(racine_double(a,b,delta,1)) + "\nx2= "+ str(racine_double(a,b,delta,2))
    #retourne une chaine de caractère
    return(print(message))


#discriminant(1,2,5)
def test_equation():

    solution_equation(1,5,4)
    solution_equation(2,3,1)
    solution_equation(1,0,0)


test_equation()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def date_est_valide(jour:int,mois:int,annee:int):
    if est_bissextile(annee):
        booleen = True
    return (booleen)

def saisie_date_naissance():
    print("Veuillez saisir une année")
    anneeSaisie = int(input())

    print("Veuillez saisir un mois")
    moisSaisie = int(input())

    print("Veuillez saisir un jour")
    jourSaisie = int(input())

    date_naissance = datetime.date(anneeSaisie, moisSaisie, jourSaisie)

    return(date_naissance)


def age(date_naissance):

    today = datetime.datetime.now()


    calculAgeAnnee = int(today.year) - date_naissance.year
    calculAgeMois = int(today.month) - date_naissance.month
    calculAgeJour = int(today.day) - date_naissance.day

    age = calculAgeAnnee

    if calculAgeMois > 0:
        age = age - 1
    elif calculAgeJour > 0:
        age = age - 1


    return(age)


def est_majeur(date_naissance):

    if age(date_naissance) >= 18:
        booleen = True
    else:
        booleen = False

    return(booleen)

def test_acces():

    date_naissance = saisie_date_naissance()

    age(date_naissance)

    if est_majeur(date_naissance):
        message = "Bonjour, vous avez " + str(age(date_naissance)) + " ans, Accès autorisé "
    else:
        message = "Désolé, vous avez " + str(age(date_naissance)) + " ans, Accès interdit"

    return(print(message))


#test_acces()

