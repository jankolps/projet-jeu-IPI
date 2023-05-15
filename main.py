#!/usr/bin/env python3
# -*- coding: utf-8  -*-
# -*-     main.py    -*-
# -*-   J. Lepers    -*-
# -*-       IPI      -*-

# import des librairies python
import sys
import time
import termios
import tty
import select

# import des modules créés
import heros
import arene
import vies
import collision

# Procédure d'initalisation du jeu
def init():
    # Définition de la fenêtre de jeu
    data["Xmax"] = 80
    data["Ymax"] = 24
    sys.stdout.write("\x1b[8;{hauteur};{largeur}t".format(hauteur=data["Ymax"], largeur=data["Xmax"]))

    # creation des éléments du jeu
    data["myTimeStep"]=0.2
    data["Vies"] = vies.createVies()
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

# Procédure de déplacement
def move(data):
    heros.move(data["Heros"], data["Xmax"], data["Ymax"])
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
    
    #On affiche les différents elements

    vies.show(data['Vies'], data['Xmax'])
    arene.show(data["Arene"])
    heros.show(data["Heros"])
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

# Fonction permettant de tester si un caractère (touche clavier) est disponible
def isDataReady():
    """
    On teste si un caractère est immédiatement disponible au clavier (non bloquant)
    """
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def interact(data):
    """
    Si une touche est appuyée (si un caractère est récupéré dans le fichier de l'entrée standard)
    """
    if isDataReady():
        # On lit ce caractère
        c = sys.stdin.read(1)
        # On test et compare ce caractère
        if c=='z':
            heros.setDirection(data["Heros"], "haut")
        elif c=='s':
            heros.setDirection(data["Heros"], "bas")
        elif c=='q':
            heros.setDirection(data["Heros"], "gauche")
        elif c=='d':
            heros.setDirection(data["Heros"], "droite")
    return

# Procédure de gestion des collisions
def isCollision(data):
    if collision.isCollision_joueur_arene(data["Heros"], data["Arene"]):
        # Ici il faut gérer la collision entre le joueur et l'arène
        pass

    if not collision.isInBox(data['Heros'], data['Xmax'], data['Ymax']):
        # Gérer si le joueur sort de la zone de jeu
        pass
    return

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

# Procédure de lancement du jeu
def run(data):
    #Boucle de simulation
    while True :
        #Faire la boucle de simu
        """
        interact(data)
        move(data)
        show(data)
        isCollision(data)
        isInLife(data)
        time.sleep(data['myTimeStep'])
        """

# jeu de tests
if __name__ == "__main__":
    data = {"Heros":None, "Arene":None, "Xmax":None, "Ymax":None,"Vies":None, "old_settings":None}