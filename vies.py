#!/usr/bin/env python3
# -*- coding: utf-8  -*-
# -*-     vies.py    -*-
# -*-   J. Lepers    -*-
# -*-       IPI      -*-

# import de librairies python
import sys

class vies:
    pass

# Procédure de création d'une vie
def createVies(filename ="vies.txt", couleur = 5, nombre = 5, position = [2,28]):
    myVies = vies()
    with open(filename, "r") as file:
        myVies.corps = file.read()
    myVies.couleur = couleur
    myVies.nombre = nombre
    myVies.position = position
    return myVies

# Procédure d'affichage d'une vie
def show(v):
    # Definition de la position du hero
    x = v.position[0]
    y = v.position[1]

    # Couleur noire pour le fond
    sys.stdout.write("\033[40m")

    # Couleur du héros
    c = v.couleur
    couleurPolice="\033[3"+str(c%7+1)+"m"
    sys.stdout.write(couleurPolice)

    # Affichage du corps du héros caratère par caractère en négligeant les " "
    
    sys.stdout.write("\033[" + str(y) + ";" + str(x)+"H")
    sys.stdout.write(str("Vies : "+(v.corps+" ")*v.nombre))

    return

# ===== Setters =====
def setPosition(v, newPosition):
    v.position = newPosition
    return