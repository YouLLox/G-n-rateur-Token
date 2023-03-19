#########################################################
##                                                     ##         
## Projet : Générateur de Token                        ##
## Programme de génération de token                    ##
## Auteurs : YouLLox                                   ##
## Spécialité NSI, classe de 1ère                      ##
## Version : V1.0 du 19/03/2023                        ##
##                                                     ##  
#########################################################


import random
from simple_chalk import *


def token():

    while True:
        generation = int(input("Combien de token souhaitez vous générer ? "))
        intervales = int(input("Combien d'intervale doit contenir le token ?"))
        caracteres = int(input("Combien de caractères doit contenir une seule intervale ?"))

        number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        lettre = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                  "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        lettre_m = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        symbole = ["&", "#", "@", "ç", "]", "+", "$", "*", "%", "/", "!"]

        for a in range(generation):
            base = ""
            for i in range(intervales):
                compteur = 0
                for t in range(caracteres):
                    gen = random.randint(1, 4)
                    if gen == 1:
                        result = number
                    elif gen == 2:
                        result = lettre
                    elif gen == 3:
                        result = lettre_m
                    elif gen == 4:
                        result = symbole
                    else:
                        print(chalk.red("Erreur: Une erreur est survenue !"))
                    caractere = random.randint(0, (len(result) - 1))
                    base += result[caractere]
                if len(base) < ((intervales*caracteres + intervales) - 1):
                    base += "-"
            print(base)
        print("Génération Terminée !")
token()
