#!/usr/bin/env python3
# -*- coding: utf-8  -*-
# -*-    heros.py    -*-
# -*-   J. Lepers    -*-
# -*-       IPI      -*-

# import de librairies python
import sys
import time

class heros:
    pass

# Fonction de création du héros
def createHeros(filename="heros.txt", direction="droite", couleur=10, position=[5,5]):
    myHeros = heros()

    # Ouverture du fichier texte contenant l'ASCII art du héros et mise dans une liste de lignes
    with open(filename, "r") as file:
        corpsEntier = file.read()
    corpsLignes = corpsEntier.split("\n")
    myHeros.corps = corpsLignes

    myHeros.direction = direction
    myHeros.couleur = couleur
    myHeros.position = position
    return myHeros

# Procédure d'affichage du héros
def show(h):
    # Definition de la position du hero
    x = h.position[0]
    y = h.position[1]

    # Couleur noire pour le fond
    sys.stdout.write("\033[40m")

    # Couleur du héros
    c = h.couleur
    couleurPolice="\033[3"+str(c%7+1)+"m"
    sys.stdout.write(couleurPolice)

    for lignes in h.corps :
        v = 0
        for lettre in lignes :
            if lettre != " ":
                sys.stdout.write("\033[" + str(y) + ";" + str(x+v)+"H")
                sys.stdout.write(lettre)
            v += 1
        y += 1
    return

# Procédure de déplacement du héros
def move(h, Xmax = 80, Ymax = 24):
    if h.direction == "gauche":
        h.position = [(h.position[0]-1)%Xmax, h.position[1]]
    elif h.direction == "droite":
        h.position = [(h.position[0]+1)%Xmax, h.position[1]]
    elif h.direction == "haut":
        h.position = [h.position[0], (h.position[1]-1)%Ymax]
    elif h.direction == "bas":
        h.position = [h.position[0], (h.position[1]+1)%Ymax]

# ===== Getters =====
def getDirection(h):
    return h.direction

def getVies(h):
    return h.vies

def getPosition(h):
    return h.position

# ===== Setters =====
def setCorps(h, newCorps):
    h.corps = newCorps
    return

def setVies(h, newVies):
    h.vies = newVies
    return

def setDirection(h, newDirection):
    h.direction = newDirection
    return

if __name__ == "__main__":
    Unhero = createHeros()
    show(Unhero)