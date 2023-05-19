#!/usr/bin/env python3
# -*- coding: utf-8  -*-
# -*-     main.py    -*-
# -*-   J. Lepers    -*-
# -*-       IPI      -*-

# import des librairies python
import sys
import os
import time
import termios
import tty
import select

# import des modules créés
import heros
import arene
import vies
import collision
import boule_de_feu
import dev_tools

# Procédure d'initalisation du jeu
def init(data):
    # Définition de la fenêtre de jeu
    data["Xmax"] = 150
    data["Ymax"] = 30
    sys.stdout.write("\x1b[8;{hauteur};{largeur}t".format(hauteur=data["Ymax"], largeur=data["Xmax"]))

    # creation des éléments du jeu
    data["myTimeStep"]=0.1
    data["Boules_de_feu"]={}
    data["NumeroBouleDeFeu"] = 0
    data["Heros"] = heros.createHeros()
    data["Arene"] = arene.createArene()

    # Récupération du numéro du descripteur de fichier de l'entrée standard (ici zéro) / (0 = entrée standard, 1 = sortie standard, 2 = erreur standard)
    # Pour plus d'infos, lire : https://fr.wikipedia.org/wiki/Descripteur_de_fichier
    fd = sys.stdin.fileno()

    """
    Sauvegarde la configuration actuelle (les attributs) du flux STDIN du terminal
    de manière à pouvoir restaurer la configuration du terminal à la fin
    """
    data['old_settings'] = termios.tcgetattr(fd)

    """
    Modification du mode du descripteur de fichier (récupération des entrées clavier)
    Il existe 2 modes :
        setcbreak() qui récupère toutes les entrées claviers dont les entrées du type CTRL + Z
        setraw() qui récupère les entrées claviers moins certaines options (ex. ne prend pas en compte les CTRL +)
    """
    tty.setcbreak(fd)
    return

# Procédure d'affichage
def show(data):
    """
    rafraichissement de l'affichage
    
    On positionne le "curseur" à la position "zéro" en haut à gauche de la fenêtre
    Remarque la position "zéro" vaut 1, 1
    sys.stdout.write("\033[1;1H")
    ou
    Nettoyage complet de l'écran (console) et repositionnement du curseur en 1, 1
    """
    sys.stdout.write("\033[2J")
    
    # == Affichage de données pour le dev ===

    #sys.stdout.write(str(data))
    dev_tools.showVariable("Collision", str(collision.Collision_joueur_arene(data["Heros"], data["Arene"])))
    #dev_tools.showVariable("Hitbox Arene : ", str(arene.getHitBox(data["Arene"])))
    #hitboxHorizGauche, hitboxHorizDroite, hitboxVerticHaut, hitboxVerticBas = heros.getHitBox(data["Heros"])
    #dev_tools.showVariable("Hitbox Heros : ", str(hitboxVerticBas))

    #On affiche les différents elements du jeu

    heros.show(data["Heros"])
    arene.show(data["Arene"])

    if data["Boules_de_feu"] != {}:
        for My_boule_de_feu in data["Boules_de_feu"]:
            boule_de_feu.show(data["Boules_de_feu"][My_boule_de_feu])
    """
    Restauration des couleurs du terminal
    Polices en blanc : code 37
    """
    sys.stdout.write("\033[37m")
    """
    background en noir : code 40
    """
    sys.stdout.write("\033[40m")

    """
    deplacement curseur
    """
    sys.stdout.write("\033[0;0H\n")
    return

# Procédure de déplacement
def move(data):
    # faire bouger les boules de feu
    if data["Boules_de_feu"] != {}:
        for My_boule_de_feu in data["Boules_de_feu"]:
            boule_de_feu.move(data["Boules_de_feu"][My_boule_de_feu])
    
    # faire bouger le heros
    heros.move(data["Heros"], data["myTimeStep"], collision.Collision_joueur_arene(data["Heros"], data["Arene"]))
    return

# Fonction permettant de tester si un caractère (touche clavier) est disponible
def isDataReady():
    """
    On teste si un caractère est immédiatement disponible au clavier (non bloquant)
    """
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


# Procédure de gestion des collisions
def isCollision(data):
    # Si la boule de feu sort de la zone de jeu, on supprime la boule de feu
    for MyBouleDeFeu in (data["Boules_de_feu"]).copy() :
        if not collision.isInBox(data['Boules_de_feu'][MyBouleDeFeu], data['Xmax'], data['Ymax']):
            del data["Boules_de_feu"][MyBouleDeFeu]
    return

'''
# Procédure pour quitter de jeu
def quitGame(data):
    """
    Restauration des couleurs du terminal
    Polices en blanc : code 37
    """
    sys.stdout.write("\033[37m")

    """
    background en noir : code 40
    """
    sys.stdout.write("\033[40m")
    
    """
    rafraichissement de l'affichage
    """
    sys.stdout.write("\033[2J")

    """
    Restauration du flux STDIN comme il était au début (on l'a sauvegardé au préalable)
    """
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, data['old_settings'])
    sys.exit()
    return

# Procédure de gestion des vies
def isInLife(data):
    if vies.getNbrVies(data["Vies"]) == 0:
        # Ici on doit faire perdre / gagner un joueur
        pass
    return
'''
def interact(data):
    """
    Si une touche est appuyée (si un caractère est récupéré dans le fichier de l'entrée standard)
    """
    #on vérifie si une touche est pressée
    ready, _, _ = select.select([sys.stdin], [], [], 0)

    if ready:
        while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            key = sys.stdin.read(1)
            if key == 'z' and data["Heros"].isJumping == False:
                heros.setDirection(data["Heros"], "haut")
                data["DirectionAttaques"] = "haut"
            elif key == 's':
                heros.setDirection(data["Heros"], "bas")
                data["DirectionAttaques"] = "bas"
            elif key == 'q':
                heros.setDirection(data["Heros"], "gauche")
                data["DirectionAttaques"] = "gauche"
            elif key == 'd':
                heros.setDirection(data["Heros"], "droite")
                data["DirectionAttaques"] = "droite"
            elif key== 'a':
                data["NumeroBouleDeFeu"] += 1
                myBoulePosition = (heros.getPosition(data["Heros"])).copy()
                # centrage au milieu du héros
                myBoulePosition[0] = int(myBoulePosition[0])+4
                myBoulePosition[1] = int(myBoulePosition[1])+2
                data["Boules_de_feu"]["Boule_de_feu_"+str(data["NumeroBouleDeFeu"])] = boule_de_feu.createBoule_de_feu("@",myBoulePosition, data["DirectionAttaques"],10)
    else:
        # si aucune touche n'est pressée
        heros.setDirection(data["Heros"], "None")
    heros.setVelocity(data["Heros"], collision.Collision_joueur_arene(data["Heros"], data["Arene"]))
# Procédure de lancement du jeu
def run(data):
    #Boucle de simulation
    while True :
        interact(data)
        move(data)
        isCollision(data)
        show(data)
        time.sleep(data["myTimeStep"])

# jeu de tests
if __name__ == "__main__":
    data = {"Heros":None, "Arene":None, "Xmax":None, "Ymax":None,"Vies":None, "old_settings":None, "DirectionAttaques":None}
    init(data)
    run(data)