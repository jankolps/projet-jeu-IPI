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
    Collisions = {"haut":False, "bas":False, "gauche":False, "droite":False}

    # On regarde si la bande horizontale gauche et l'arène ont une coordonnée en commun
    for coordonneesHeros in hitboxHorizGauche :
        for coordonneesArene in HitboxArene :
            if coordonneesArene == coordonneesHeros:
                Collisions["gauche"] = True
                break
            elif not Collisions["gauche"]:
                Collisions["gauche"] = False
    
    # On regarde si la bande horizontale droite et l'arène ont une coordonnée en commun
    for coordonneesHeros in hitboxHorizDroite :
        for coordonneesArene in HitboxArene :
            if coordonneesArene == coordonneesHeros:
                Collisions["droite"] = True
                break
            elif not Collisions["droite"]:
                Collisions["droite"] = False
    
    # On regarde si la bande verticale haute et l'arène ont une coordonnée en commun
    for coordonneesHeros in hitboxVerticHaut :
        for coordonneesArene in HitboxArene :
            if coordonneesArene == coordonneesHeros:
                Collisions["haut"] = True
                break
            elif not Collisions["haut"]:
                Collisions["haut"] = False
    
    # On regarde si la bande verticale basse et l'arène ont une coordonnée en commun
    for coordonneesHeros in hitboxVerticBas :
        for coordonneesArene in HitboxArene :
            if coordonneesArene == coordonneesHeros:
                Collisions["bas"] = True
                h.isJumping = False
                break
            elif not Collisions["bas"]:
                Collisions["bas"] = False

    return Collisions

# Fonction pour savoir si une boule est sortie de la zone de jeu
def isBouleInBox(b, Xmax, Ymax):
    if b.position[0] >= Xmax or b.position[0] <= 0:
        myIsInBox = False
    elif b.position[1] >= Ymax or b.position[1] <= 0:
        myIsInBox = False
    else:
        myIsInBox = True
    return myIsInBox

# Fonction pour savoir si le héros est sortie de la zone de jeu
def collision_Heros_Box(h, Xmax, Ymax):    
    hitboxHorizGauche, hitboxHorizDroite, hitboxVerticHaut, hitboxVerticBas = heros.getHitBox(h)
    # coordonnées de l'arène
    Collisions = {"haut":False, "bas":False, "gauche":False, "droite":False}

    # On regarde si la bande horizontale gauche et l'arène ont une coordonnée en commun
    for coordonneesHeros in hitboxHorizGauche :
        if coordonneesHeros[0] <= 0:
            Collisions["gauche"] = True
            break
        elif not Collisions["gauche"]:
            Collisions["gauche"] = False
        
    # On regarde si la bande horizontale droite et l'arène ont une coordonnée en commun
    for coordonneesHeros in hitboxHorizDroite :
        if coordonneesHeros[0] >= Xmax:
            Collisions["droite"] = True
            break
        elif not Collisions["droite"]:
            Collisions["droite"] = False
    
    # On regarde si la bande verticale haute et l'arène ont une coordonnée en commun
    for coordonneesHeros in hitboxVerticHaut :
        if coordonneesHeros[1] <= 0:
            Collisions["haut"] = True
            break
        elif not Collisions["haut"]:
            Collisions["haut"] = False
    
    # On regarde si la bande verticale basse et l'arène ont une coordonnée en commun
    for coordonneesHeros in hitboxVerticBas :
        if coordonneesHeros[1] >= Ymax:
            Collisions["bas"] = True
            break
        elif not Collisions["bas"]:
            Collisions["bas"] = False
    return Collisions

# Fonction pour savoir si un joueur est en collision avec l'autre
def collision_j1_j2(h_j1, h_j2):
    # Différentes bandes de hitbox du Héros (qui forme un carré sans coins de 1 autour du héros)
    hitboxHorizGauche_j1, hitboxHorizDroite_j1, hitboxVerticHaut_j1, hitboxVerticBas_j1 = heros.getHitBox(h_j1)
    # coordonnées de l'arène
    Hitbox_j2 = heros.getHitBoxChars(h_j2)
    Collisions = {"haut":False, "bas":False, "gauche":False, "droite":False}

    # On regarde si la bande horizontale gauche et l'arène ont une coordonnée en commun
    for coordonnees_j1 in hitboxHorizGauche_j1 :
        for coordonnees_j2 in Hitbox_j2 :
            if coordonnees_j2 == coordonnees_j1:
                Collisions["gauche"] = True
                break
            elif not Collisions["gauche"]:
                Collisions["gauche"] = False
    
    # On regarde si la bande horizontale droite et l'arène ont une coordonnée en commun
    for coordonnees_j1 in hitboxHorizDroite_j1 :
        for coordonnees_j2 in Hitbox_j2 :
            if coordonnees_j2 == coordonnees_j1:
                Collisions["droite"] = True
                break
            elif not Collisions["droite"]:
                Collisions["droite"] = False
    
    # On regarde si la bande verticale haute et l'arène ont une coordonnée en commun
    for coordonnees_j1 in hitboxVerticHaut_j1 :
        for coordonnees_j2 in Hitbox_j2 :
            if coordonnees_j2 == coordonnees_j1:
                Collisions["haut"] = True
                break
            elif not Collisions["haut"]:
                Collisions["haut"] = False
    
    # On regarde si la bande verticale basse et l'arène ont une coordonnée en commun
    for coordonnees_j1 in hitboxVerticBas_j1 :
        for coordonnees_j2 in Hitbox_j2 :
            if coordonnees_j2 == coordonnees_j1:
                Collisions["bas"] = True
                #h_j1.isJumping = False
                break
            elif not Collisions["bas"]:
                Collisions["bas"] = False

    return Collisions


# Fonction pour savoir si un joueur est en collision avec la boule de feu de l'autre
def collision_joueur_bouleChars(h, b):
    if (b.position[0] > h.position[0]) and (b.position[0] < h.position[0]+7) and (b.position[1] > h.position[1]) and (b.position[1] < h.position[1]+5):
        Collision = True
    else :
        Collision = False
    return Collision

# Fonction pour savoir si la hitbox d'un joueur est en collision avec la boule de feu de l'autre joueur
def collision_joueur_boule(h, b):
    # Différentes bandes de hitbox du Héros (qui forme un carré sans coins de 1 autour du héros)
    hitboxHorizGauche, hitboxHorizDroite, hitboxVerticHaut, hitboxVerticBas = heros.getHitBox(h)
    Collisions = {"haut":False, "bas":False, "gauche":False, "droite":False}

    # On regarde si la bande horizontale gauche et l'arène ont une coordonnée en commun
    for coordonnees in hitboxHorizGauche :
        if coordonnees == b.position:
            Collisions["gauche"] = True
            break
        elif not Collisions["gauche"]:
            Collisions["gauche"] = False
    
    # On regarde si la bande horizontale droite et l'arène ont une coordonnée en commun
    for coordonnees in hitboxHorizDroite :
        if coordonnees == b.position:
            Collisions["droite"] = True
            break
        elif not Collisions["droite"]:
            Collisions["droite"] = False
    
    # On regarde si la bande verticale haute et l'arène ont une coordonnée en commun
    for coordonnees in hitboxVerticHaut :
        if coordonnees == b.position:
            Collisions["haut"] = True
            break
        elif not Collisions["haut"]:
            Collisions["haut"] = False
    
    # On regarde si la bande verticale basse et l'arène ont une coordonnée en commun
    for coordonnees in hitboxVerticBas :
        if coordonnees == b.position:
            Collisions["bas"] = True
            break
        elif not Collisions["bas"]:
            Collisions["bas"] = False
    
    return Collisions