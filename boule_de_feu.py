#!/usr/bin/env python3
# -*-  coding: utf-8  -*-
# -*- boule_de_feu.py -*-
# -*-    J. Lepers    -*-
# -*-       IPI       -*-

# import de librairies python
import sys

class boule_de_feu :
    pass

# procédure de création d'une boule de feu
def createBoule_de_feu(corps = "@",position = [5,5], direction="droite", couleur=10):
    MyBoule_de_feu = boule_de_feu()
    MyBoule_de_feu.corps = corps
    MyBoule_de_feu.position = position
    MyBoule_de_feu.direction = direction
    MyBoule_de_feu.couleur = couleur

    return MyBoule_de_feu

# Procédure d'affichage de la boule de feu
def show(b):
    # Definition de la position de la boule de feu
    x = b.position[0]
    y = b.position[1]

    # Couleur noire pour le fond
    sys.stdout.write("\033[40m")

    # Couleur de la boule de feu
    c = b.couleur
    couleurPolice="\033[3"+str(c%7+1)+"m"
    sys.stdout.write(couleurPolice)

    sys.stdout.write("\033[" + str(y) + ";" + str(x)+"H")
    sys.stdout.write(b.corps)
    return

# Procédure de déplacement de la boule de feu
def move(b):
    if b.direction == "gauche":
        b.position[0] -= 1
    elif b.direction == "droite":
        b.position[0] += 1
    elif b.direction == "haut":
        b.position[1] -= 1
    elif b.direction == "bas":
        b.position[1] += 1
    return