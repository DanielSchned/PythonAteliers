#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Daniel
#
# Created:     06/09/2021
# Copyright:   (c) Daniel 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


def exo1(Travail, Horaire):
    """ Calcule horaire """
    Pourcentage1 = 1.25
    Pourcentage2 = 1.50

    if Travail > 160 :

        if Travail < 200:
            surplusTravail = Travail - 160
            horaireMajore = surplusTravail * Pourcentage1
            Horaire = Horaire + horaireMajore


    if Travail > 200:

        surplusTravail = Travail - 200
        horaireMajore = surplusTravail * Pourcentage2
        Horaire = Horaire + horaireMajore



    print(Horaire)


exo1(210, 1200)

def exo2(caractere):

    chaine = caractere

    if type(caractere) == int:
        chaine = str(caractere)
    chaine = ord(chaine)

    if chaine > 122:
        print("C'est un caractère spécial")
    elif chaine > 96:
        print("C'est une lettre minuscule")
    elif chaine > 90:
        print("C'est bun caractère spécial")
    elif chaine > 64:
        print("C'est une lettre majuscule")
    elif chaine > 57:
        print("C'est un caractère spécial")
    elif chaine > 47:
        print("C'est un chiffre")
    else:
        print("C'est un caractère spécial")



#exo2(3)


def exo3(age, genre):

    if genre == "homme":
        if age > 20:
            print("Il paie les impôts")
        else:
            print("Il ne paie pas d'impôts")

    if genre == "femme":
        if age >= 18 & age <= 35:
            print("Elle paie les impôts")
        else:
            print("Elle ne paie pas d'impôts")



#exo3(21, "homme")

def exo4():
    """Calcul du prix en fonction du nombre de photocopies"""
    print("Nombre de photocopies à effectuer")
    photocopies = int(input())
    prix1 = 0
    prix2 = 0
    prix3 = 0
    prix4 = 0
    prix5 = 0
    prix6 = 0
    prix = 0


    dizaine = 0
    vingtaine = 0
    trentaine = 0


    if photocopies < 10:
        prix1 = 0.10 * photocopies


    if photocopies >= 10:
        prix2 = 0.10 * 10
        if photocopies < 20:
            vingtaine = photocopies - 10
            prix3 = 0.09 * vingtaine

    if photocopies >= 20:
        prix4 = 0.09 * 10
        if photocopies < 30:
            trentaine = photocopies - 20
            prix5 = 0.08 * trentaine

    if photocopies >= 30:
        trentaine = photocopies - 20
        prix6 = 0.08 * trentaine


    prix = prix1 + prix2 + prix3 + prix4 + prix5 + prix6

    print("-------------RESTES :")
    print(dizaine)
    print(vingtaine)
    print(trentaine)
    print("-------------PRIX :")

    print(prix1)
    print(prix2)
    print(prix3)
    print(prix4)
    print(prix5)
    print(prix6)
    print(prix)


#exo4()

def exo5():
    """ Calcul du cout annuel d'une place de port pour un voilier """
    coutMensuel = 0
    coutAnnuel = 0
    taxeSpeciale = 0

    print("Nom du voilier")
    nomVoilier = str(input())


    print("Longueur du voilier")
    longueurVoilier = int(input())


    print("Catégorie du voilier")
    categorieVoilier = int(input())

    if longueurVoilier < 5:
        coutMensuel = coutMensuel + 100


    if longueurVoilier >= 5:
        if longueurVoilier <= 10:
            coutMensuel = coutMensuel + 200


    if longueurVoilier > 10:
        if longueurVoilier <= 12:
            coutMensuel = coutMensuel + 400


    if longueurVoilier > 12:
        coutMensuel = coutMensuel + 600


    if categorieVoilier == 1:
        taxeSpeciale = 100
    elif categorieVoilier == 2:
        taxeSpeciale = 150
    elif categorieVoilier == 3:
        taxeSpeciale = 200

    print(taxeSpeciale)

    coutAnnuel = taxeSpeciale + (coutMensuel * 12)
    print("le coût annuel d’une place au port pour le voilier " + nomVoilier + " est de " + str(coutAnnuel) + " euros")


def exo6(type, cm3, prixCarburant, nbKm):
    """ Calcul des frais mensuels des véhicules """
    consommation = 0
    fraisMensuels = 0
    prixBrut = 0
    nbKmMensuel = nbKm/12

    if cm3 < 2000:
        consommation = 8 * (nbKmMensuel/100)
        if type == "D":
            frais = 1.70

        elif type == "E":
            frais = 1.50


    if cm3 >= 2000:
        consommation = 10 * (nbKmMensuel/100)

        if type == "E":
            frais = 1.50

    if type == "D":
            frais = 1.70

    prixBrut = consommation * prixCarburant
    fraisMensuels = prixBrut * frais

    #retourne un float
    return(print(round(fraisMensuels, 2)))

exo6("D", 2600, 1.40, 10000)

def exo7():
    """ Resultat des élections législatives """
    k = 0
    g = 0
    messageFavorable = ""

    resultatCandidat1 = int(input())
    resultatCandidat2 = int(input())
    resultatCandidat3 = int(input())
    resultatCandidat4 = int(input())

    totalVotes = resultatCandidat1 + resultatCandidat2 + resultatCandidat3 + resultatCandidat4

    pourcentageVotes1 = (resultatCandidat1 / totalVotes) * 100
    pourcentageVotes2 = (resultatCandidat2 / totalVotes) * 100
    pourcentageVotes3 = (resultatCandidat3 / totalVotes) * 100
    pourcentageVotes4 = (resultatCandidat4 / totalVotes) * 100

    listeCandidats = [pourcentageVotes1, pourcentageVotes2, pourcentageVotes3, pourcentageVotes4]

    for i in range(len(listeCandidats)):

        if listeCandidats[i] >= 50:
            g = g + 1
            print("Le candidat numéro " + str(i + 1) + " est gagnant dès le premier tour.")

    if g == 0:

        for l in range(len(listeCandidats)):
            if listeCandidats[l] >= 12.5:
                k = k + 1
                for c in range(len(listeCandidats)):
                    if listeCandidats[c] > listeCandidats [c - 1]:
                        messageFavorable = "Le candidat "+ str(c + 1) +" est favorable, les autres candidats sont défavorables."

        print("Il y a "+ str(k) + " candidats qui passe/passent au deuxième tour")
    #affichage des gagnants du premier tour
    print(messageFavorable)

    #retourne 4 float, limités a 2 chiffres après a virgule
    print(round(pourcentageVotes1, 2), round(pourcentageVotes2, 2), round(pourcentageVotes3, 2), round(pourcentageVotes4, 2))



#exo7()

def exo8():
    print("Votre age")
    ageConducteur = int(input())

    print("Depusi combien de temps avez vous votre permis")
    agePermis = int(input())

    print("Combien d'accidents avez vous eu ?")
    accident = int(input())

    print("Etes vous depuis plus d'un an dans notre compagnie ? (Oui/Non)")

    #compagnieAssurance = str(input())

    choix = ""
    superieur = False
    tarif = ["refus", "rouge", "orange", "vert", "bleu"]


    if ageConducteur <= 25:
        if agePermis < 2:
            if accident == 0:
                choix = tarif[1]
            else :
                choix = tarif[0]
        else:
            if accident == 0:
                choix = tarif[2]
            if accident == 1:
                choix = tarif[1]
            else:
                choix = tarif[0]
    else:
        if agePermis < 2:
            if accident == 0:
                choix = tarif[2]

            if accident == 1:
                choix = tarif[1]

            else:
                choix = tarif[0]

        if agePermis > 2:


            if accident == 0:
                choix = tarif[3]
            if accident == 1:
                choix = tarif[2]
            if accident == 2:
                choix = tarif[1]
            else:
                choix = tarif[0]

    """if compagnieAssurance == "Oui":
                superieur = True

    if superieur == True:
        for i in range(len(tarif)):
            choix = tarif[i]"""

    print(choix)

#exo8()