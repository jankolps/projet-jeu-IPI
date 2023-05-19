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
    # Différentes bandes de hitbox du Héros (qui forme un carré sans coins de 1 autour du héros)
    hitboxHorizGauche, hitboxHorizDroite, hitboxVerticHaut, hitboxVerticBas = heros.getHitBox(h)
    # coordonnées de l'arène
    HitboxArene = arene.getHitBox(a)

    # On regarde si la bande horizontale gauche et l'arène ont une coordonnée en commun
    for coordonneesHeros in hitboxHorizGauche :
        for coordonneesArene in HitboxArene :
            if coordonneesArene == coordonneesHeros:
                Collision = "gauche"
                break
            else:
                Collision = "None"
    
    # On regarde si la bande horizontale droite et l'arène ont une coordonnée en commun
    for coordonneesHeros in hitboxHorizDroite :
        for coordonneesArene in HitboxArene :
            if coordonneesArene == coordonneesHeros:
                Collision = "droite"
                break
            else:
                Collision = "None"
    
    # On regarde si la bande verticale haute et l'arène ont une coordonnée en commun
    for coordonneesHeros in hitboxVerticHaut :
        for coordonneesArene in HitboxArene :
            if coordonneesArene == coordonneesHeros:
                Collision = "haut"
                break
            else:
                Collision = "None"
    
    # On regarde si la bande verticale basse et l'arène ont une coordonnée en commun
    for coordonneesHeros in hitboxVerticBas :
        for coordonneesArene in HitboxArene :
            if coordonneesArene == coordonneesHeros:
                Collision = "bas"
                h.isJumping = False
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