#!/usr/bin/env python3
# -*- coding: utf-8  -*-
# -*-    arene.py    -*-
# -*-   J. Lepers    -*-
# -*-       IPI      -*-

# import de librairies python
import sys


class arene:
    pass

# Fonction de creation de l'arène
def createArene(filename = "arene.txt", position = [50, 24], couleur = 5):
    myArene = arene()

    # Ouverture du fichier texte contenant l'ASCII art de l'arène et mise dans une liste de lignes
    with open(filename, "r") as file:
        corpsEntier = file.read()
    corpsLignes = corpsEntier.split("\n")
    myArene.corps = corpsLignes

    myArene.position = position
    myArene.couleur = couleur
    return myArene

# Fonction d'affichage de l'arene
def show(a):
    # Definition de la position de l'arene
    x = a.position[0]
    y = a.position[1]

    # Couleur noire pour le fond
    sys.stdout.write("\033[40m")

    # Couleur de l'arene
    c = a.couleur
    couleurPolice="\033[3"+str(c%7+1)+"m"
    sys.stdout.write(couleurPolice)

    hitbox = []

    for lignes in a.corps :
        v = 0
        for lettre in lignes :
            if lettre != " ":
                sys.stdout.write("\033[" + str(y) + ";" + str(x+v)+"H")
                hitbox.append([y, x+v])
                sys.stdout.write(lettre)
            v += 1
        y += 1
    return hitbox

# jeu de tests
if __name__ == "__main__":
    UneArene = createArene()
    show(UneArene)
