#!/usr/bin/env python3
# -*- coding: utf-8  -*-
# -*-  dev_tools.py  -*-
# -*-   J. Lepers    -*-
# -*-       IPI      -*-

# Petit programme pour afficher des données du jeu et débuggerSS

# import de module python
import sys

def showVariable(Name, Variable):
    x = 100
    y = 0

    # Couleur noire pour le fond
    sys.stdout.write("\033[40m")

    # Couleur de l'affichage
    c = 5
    couleurPolice="\033[3"+str(c%7+1)+"m"
    sys.stdout.write(couleurPolice)

    sys.stdout.write("\033[" + str(y) + ";" + str(x)+"H")
    sys.stdout.write(str(Name+" : "+Variable)) 
    return