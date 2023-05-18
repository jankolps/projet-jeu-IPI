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
def createHeros(filename="heros.txt", direction=None, couleur=10, position=[50,5], vitesse=[0,0], acceleration = [40, -20]):
    myHeros = heros()

    # Ouverture du fichier texte contenant l'ASCII art du héros et mise dans une liste de lignes
    with open(filename, "r") as file:
        corpsEntier = file.read()
    corpsLignes = corpsEntier.split("\n")
    myHeros.corps = corpsLignes

    myHeros.direction = direction
    myHeros.couleur = couleur
    myHeros.position = position
    myHeros.vitesse = vitesse
    myHeros.acceleration = acceleration
    return myHeros

# Procédure d'affichage du héros
def show(h):
    # Definition de la position du hero
    x = int(h.position[0])
    y = int(h.position[1])

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

# Procédure de réglace de la vitesse du héros
def setVelocity(h, collision):
    if h.direction == None:
        h.vitesse[0] = 0
    elif h.direction == "haut" and collision != "haut":
        h.vitesse[1] = 5
    elif h.direction == "gauche" and collision != "gauche":
        h.vitesse[0] = -30
    elif h.direction == "droite" and collision != "droite":
        h.vitesse[0] = 30
    elif h.direction == "bas" and collision != "bas":
        h.vitesse[1] = -5
    return

# Fonction décélération
def move(h, dt, collision):
    # déplacement gauche
    if h.direction == "gauche" and collision != "gauche":
        h.vitesse[0] += dt*(h.acceleration[0])
        if h.vitesse[0] < 0:
            h.position[0] = int(h.position[0]+dt*(h.vitesse[0]))
        else:
            h.vitesse[0] = 0
    
    # déplacement droite
    elif h.direction == "droite" and collision != "droite":
        h.vitesse[0] -= dt*(h.acceleration[0])
        if h.vitesse[0] > 0:
            h.position[0] = int(h.position[0]+dt*(h.vitesse[0]))
        else:
            h.vitesse[0] = 0
    # saut
    if h.direction == "haut" and collision != "haut":
        h.vitesse[1] += dt*(h.acceleration[1])
        h.position[1] = int(h.position[1]-dt*(h.vitesse[1]))
    
    # "accroupis"
    if h.direction == "bas" and collision != "bas":
        h.vitesse[1] += dt*(h.acceleration[1])
        h.position[1] = int(h.position[1]-dt*(h.vitesse[1]))
    
    # gravité
    if collision != "bas":
        h.vitesse[1] += dt*(h.acceleration[1])
        h.position[1] = int(h.position[1]-dt*(h.vitesse[1]))
    return


# ===== Getters =====
def getHitBox(h):
    x = int(h.position[0])
    y = int(h.position[1])
    hitbox = []
    coordonneesMin = [x, y]
    coordonneesMax = [x, y]
    
    for lignes in h.corps :
        v = 0
        for lettre in lignes :
            if lettre != " ":
                hitbox.append([x+v, y])
                if coordonneesMax[0] < x+v:
                    coordonneesMax[0] = x+v
                
                if coordonneesMax[1] < y:
                    coordonneesMax[1] = y
            v += 1
        y += 1
    
    hitboxHorizGauche = []
    hitboxHorizDroite = []
    for y in range(coordonneesMin[1], coordonneesMax[1]+1):
        hitboxHorizGauche.append([coordonneesMin[0]-1, y])
        hitboxHorizDroite.append([coordonneesMax[0]+1, y])
    
    hitboxVerticHaut = []
    hitboxVerticBas = []
    for x in range(coordonneesMin[0], coordonneesMax[0]+1):
        hitboxVerticHaut.append([x, coordonneesMin[1]-1])
        hitboxVerticBas.append([x, coordonneesMax[1]+1])
    
    return hitboxHorizGauche, hitboxHorizDroite, hitboxVerticHaut, hitboxVerticBas


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