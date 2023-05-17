#!/usr/bin/env python3
# -*- coding: utf-8  -*-
# -*-  collision.py  -*-
# -*-   J. Lepers    -*-
# -*-       IPI      -*-

# import de modules créés
import heros
import arene

# fonction de test de collision entre le joueur et l'arène, renvoi True si collision
def isCollision_joueur_arene(HitboxHeros, HitboxArene):
    for coordonneesHeros in HitboxHeros :
        for coordonneesArene in HitboxArene :
            if coordonneesArene == coordonneesHeros:
                isCollision = True
                break
            else:
                isCollision = False

    return isCollision

# Fonction pour savoir si une boule est sortie de la zone de jeu
def isInBox(b, Xmax, Ymax):
    if b.position[0] >= Xmax or b.position[0] <= 0:
        myIsInBox = False
    elif b.position[1] >= Ymax or b.position[1] <= 0:
        myIsInBox = False
    else:
        myIsInBox = True
    return myIsInBox