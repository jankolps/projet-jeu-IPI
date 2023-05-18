#!/usr/bin/env python3
# -*- coding: utf-8  -*-
# -*-  collision.py  -*-
# -*-   J. Lepers    -*-
# -*-       IPI      -*-

# import des modules créés
import heros
import arene

# fonction de test de collision entre le joueur et l'arène, renvoi True si collision
def Collision_joueur_arene(h, a):
    hitboxHorizGauche, hitboxHorizDroite, hitboxVerticHaut, hitboxVerticBas = heros.getHitBox(h)
    HitboxArene = arene.getHitBox(a)

    for coordonneesHeros in hitboxHorizGauche :
        for coordonneesArene in HitboxArene :
            if coordonneesArene == coordonneesHeros:
                Collision = "gauche"
                break
            else:
                Collision = "None"
    for coordonneesHeros in hitboxHorizDroite :
        for coordonneesArene in HitboxArene :
            if coordonneesArene == coordonneesHeros:
                Collision = "droite"
                break
            else:
                Collision = "None"
    for coordonneesHeros in hitboxVerticHaut :
        for coordonneesArene in HitboxArene :
            if coordonneesArene == coordonneesHeros:
                Collision = "haut"
                break
            else:
                Collision = "None"
    for coordonneesHeros in hitboxVerticBas :
        for coordonneesArene in HitboxArene :
            if coordonneesArene == coordonneesHeros:
                Collision = "bas"
                break
            else:
                Collision = "None"
    return Collision

# Fonction pour savoir si une boule est sortie de la zone de jeu
def isInBox(b, Xmax, Ymax):
    if b.position[0] >= Xmax or b.position[0] <= 0:
        myIsInBox = False
    elif b.position[1] >= Ymax or b.position[1] <= 0:
        myIsInBox = False
    else:
        myIsInBox = True
    return myIsInBox