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
    data["Boules_de_feu"]["Boules_de_feu_j1"] = {}
    data["Boules_de_feu"]["Boules_de_feu_j2"]= {}
    data["Numeros_Boules_de_feu"]["NumeroBouleDeFeu_j1"] = 0
    data["Numeros_Boules_de_feu"]["NumeroBouleDeFeu_j2"] = 0
    data["Heros"]["Heros_j1"] = heros.createHeros("herosDroite.txt", None, 3, data["Spawn1"].copy(), [0,0], [1,-40], False, "droite", data["Spawn1"].copy())
    data["Heros"]["Heros_j2"] = heros.createHeros("herosGauche.txt", None, 0, data["Spawn2"].copy(), [0,0], [1,-40], False, "gauche", data["Spawn2"].copy())
    vies.setPosition(data["Heros"]["Heros_j1"].vies, [37,28])
    vies.setPosition(data["Heros"]["Heros_j2"].vies, [96, 28])
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
    Nettoyage complet de l'écran (console) et repositionnement du curseur en 1, 1
    """
    sys.stdout.write("\033[2J")

    #On affiche les différents elements du jeu
    for myHeros in data["Heros"].values():
        if myHeros.directionAttaque == "gauche":
            heros.setCorps(myHeros, "herosGauche.txt")
        elif myHeros.directionAttaque == "droite":
            heros.setCorps(myHeros, "herosDroite.txt")
        heros.show(myHeros)
    arene.show(data["Arene"])
    vies.show(data["Heros"]["Heros_j1"].vies)
    vies.show(data["Heros"]["Heros_j2"].vies)

    if data["Boules_de_feu"]["Boules_de_feu_j1"] != {}:
        for My_boule_de_feu in data["Boules_de_feu"]["Boules_de_feu_j1"]:
            boule_de_feu.show(data["Boules_de_feu"]["Boules_de_feu_j1"][My_boule_de_feu])
    
    if data["Boules_de_feu"]["Boules_de_feu_j2"] != {}:
        for My_boule_de_feu in data["Boules_de_feu"]["Boules_de_feu_j2"]:
            boule_de_feu.show(data["Boules_de_feu"]["Boules_de_feu_j2"][My_boule_de_feu])
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
    for joueur_boules in data["Boules_de_feu"].values():
        if joueur_boules != {}:
            for My_boule_de_feu in joueur_boules:
                boule_de_feu.move(joueur_boules[My_boule_de_feu])

    # faire bouger le heros
    heros.move(data["Heros"]["Heros_j1"], data["myTimeStep"], collision.Collision_joueur_arene(data["Heros"]["Heros_j1"], data["Arene"]), collision.collision_Heros_Box(data["Heros"]["Heros_j1"], data["Xmax"], data["Ymax"]), collision.collision_j1_j2(data["Heros"]["Heros_j1"], data["Heros"]["Heros_j2"]))
    heros.move(data["Heros"]["Heros_j2"], data["myTimeStep"], collision.Collision_joueur_arene(data["Heros"]["Heros_j2"], data["Arene"]), collision.collision_Heros_Box(data["Heros"]["Heros_j2"], data["Xmax"], data["Ymax"]), collision.collision_j1_j2(data["Heros"]["Heros_j2"], data["Heros"]["Heros_j1"]))
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
    for joueur_boules in data["Boules_de_feu"].values() :
        for MyBouleDeFeu in (joueur_boules).copy() :
            if not collision.isBouleInBox(joueur_boules[MyBouleDeFeu], data['Xmax'], data['Ymax']):
                del joueur_boules[MyBouleDeFeu]
    
    for myHeros in data["Heros"].values():
        for myCollision in collision.collision_Heros_Box(myHeros, data["Xmax"], data["Ymax"]).values():
            if myCollision != False:
                myHeros.vies.nombre -= 1
                myHeros.vitesse = [0,0]
                myHeros.position = myHeros.spawn.copy()
    
    
    for boule in data["Boules_de_feu"]["Boules_de_feu_j2"].copy():
        if collision.collision_joueur_bouleChars(data["Heros"]["Heros_j1"], data["Boules_de_feu"]["Boules_de_feu_j2"][boule]):
            if data["Boules_de_feu"]["Boules_de_feu_j2"][boule].direction == "haut":
                data["Heros"]["Heros_j1"].position[1] += 1
            elif data["Boules_de_feu"]["Boules_de_feu_j2"][boule].direction == "bas":
                data["Heros"]["Heros_j1"].position[1] -= 1
            elif data["Boules_de_feu"]["Boules_de_feu_j2"][boule].direction == "gauche":
                data["Heros"]["Heros_j1"].position[0] -= 4
            elif data["Boules_de_feu"]["Boules_de_feu_j2"][boule].direction == "droite":
                data["Heros"]["Heros_j1"].position[0] += 4
            data["Heros"]["Heros_j1"].vies.nombre -= 1
            del data["Boules_de_feu"]["Boules_de_feu_j2"][boule]
    
    for boule in data["Boules_de_feu"]["Boules_de_feu_j1"].copy():
        if collision.collision_joueur_bouleChars(data["Heros"]["Heros_j2"], data["Boules_de_feu"]["Boules_de_feu_j1"][boule]):
            if data["Boules_de_feu"]["Boules_de_feu_j1"][boule].direction == "haut":
                data["Heros"]["Heros_j2"].position[1] += 1
            elif data["Boules_de_feu"]["Boules_de_feu_j1"][boule].direction == "bas":
                data["Heros"]["Heros_j2"].position[1] -= 1
            elif data["Boules_de_feu"]["Boules_de_feu_j1"][boule].direction == "gauche":
                data["Heros"]["Heros_j2"].position[0] -= 4
            elif data["Boules_de_feu"]["Boules_de_feu_j1"][boule].direction == "droite":
                data["Heros"]["Heros_j2"].position[0] += 4
            data["Heros"]["Heros_j2"].vies.nombre -= 1
            del data["Boules_de_feu"]["Boules_de_feu_j1"][boule]
    
    return


# Procédure pour quitter de jeu
def quitGame(data, joueur):
    i=0
    if joueur == "Heros_j1":
        while i<3:
            sys.stdout.write("\033[2J")
            sys.stdout.write("\033[40m")
            couleurPolice="\033[3"+str((data["Heros"]["Heros_j2"].couleur)%7+1)+"m"
            sys.stdout.write(couleurPolice)
            sys.stdout.write("\033[15;60H")
            sys.stdout.write("Bravo joueur 2 ! Tu as gagné !")
            
            sys.stdout.write("\033[37m")
            sys.stdout.write("\033[40m")
            sys.stdout.write("\033[0;0H\n")
            
            i += data["myTimeStep"]
            time.sleep(data["myTimeStep"])

    else:
        while i<3:
            sys.stdout.write("\033[2J")
            sys.stdout.write("\033[40m")
            couleurPolice = str("\033[3"+str((data["Heros"]["Heros_j1"].couleur)%7+1)+"m")
            sys.stdout.write(couleurPolice)
            sys.stdout.write("\033[15;60H")
            sys.stdout.write("Bravo joueur 1 ! Tu as gagné !")
            
            sys.stdout.write("\033[37m")
            sys.stdout.write("\033[40m")
            sys.stdout.write("\033[0;0H\n")

            i += data["myTimeStep"]
            time.sleep(data["myTimeStep"])
    i=0
    while i<3:
        sys.stdout.write("\033[2J")
        sys.stdout.write("\033[40m")
        couleurPolice = str("\033[37m")
        sys.stdout.write(couleurPolice)
        sys.stdout.write("\033[" + str(15) + ";" + str(65)+"H")
        sys.stdout.write("Merci d'avoir joué.")
        
        sys.stdout.write("\033[37m")
        sys.stdout.write("\033[40m")
        sys.stdout.write("\033[0;0H\n")

        i += data["myTimeStep"]
        time.sleep(data["myTimeStep"])
    
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
    for joueur in data["Heros"].keys():
        if data["Heros"][joueur].vies.nombre <= 0:
            quitGame(data, joueur)
    return

def interact(data):
    """
    Si une touche est appuyée (si un caractère est récupéré dans le fichier de l'entrée standard)
    """
    #on vérifie si une touche est pressée
    ready, _, _ = select.select([sys.stdin], [], [], 0)

    j1_interact = False
    j2_interact = False

    if ready:
        while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            key = sys.stdin.read(1)

            # contrôles du joueur 1
            if key == 'z' and data["Heros"]["Heros_j1"].isJumping == False:
                j1_interact = True
                heros.setDirection(data["Heros"]["Heros_j1"], "haut")
                data["Heros"]["Heros_j1"].directionAttaque = "haut"
            elif key == 's':
                j1_interact = True
                heros.setDirection(data["Heros"]["Heros_j1"], "bas")
                data["Heros"]["Heros_j1"].directionAttaque = "bas"
            elif key == 'q':
                j1_interact = True
                heros.setDirection(data["Heros"]["Heros_j1"], "gauche")
                data["Heros"]["Heros_j1"].directionAttaque = "gauche"
            elif key == 'd':
                j1_interact = True
                heros.setDirection(data["Heros"]["Heros_j1"], "droite")
                data["Heros"]["Heros_j1"].directionAttaque = "droite"
            elif key== 'a':
                j1_interact = True
                data["Numeros_Boules_de_feu"]["NumeroBouleDeFeu_j1"] += 1
                myBoulePosition = (heros.getPosition(data["Heros"]["Heros_j1"])).copy()
                # centrage au milieu du héros
                myBoulePosition[0] = int(myBoulePosition[0])+4
                myBoulePosition[1] = int(myBoulePosition[1])+2
                data["Boules_de_feu"]["Boules_de_feu_j1"]["Boule_de_feu_"+str(data["Numeros_Boules_de_feu"]["NumeroBouleDeFeu_j1"])] = boule_de_feu.createBoule_de_feu("@",myBoulePosition, data["Heros"]["Heros_j1"].directionAttaque,data["Heros"]["Heros_j1"].couleur)
            
            # contrôles du joueur 2
            if key == '8' and data["Heros"]["Heros_j2"].isJumping == False:
                j2_interact = True
                heros.setDirection(data["Heros"]["Heros_j2"], "haut")
                data["Heros"]["Heros_j2"].directionAttaque = "haut"
            elif key == '5':
                j2_interact = True
                heros.setDirection(data["Heros"]["Heros_j2"], "bas")
                data["Heros"]["Heros_j2"].directionAttaque = "bas"
            elif key == '4':
                j2_interact = True
                heros.setDirection(data["Heros"]["Heros_j2"], "gauche")
                data["Heros"]["Heros_j2"].directionAttaque = "gauche"
            elif key == '6':
                j2_interact = True
                heros.setDirection(data["Heros"]["Heros_j2"], "droite")
                data["Heros"]["Heros_j2"].directionAttaque = "droite"
            elif key== '7':
                j2_interact = True
                data["Numeros_Boules_de_feu"]["NumeroBouleDeFeu_j2"] += 1
                myBoulePosition = (heros.getPosition(data["Heros"]["Heros_j2"])).copy()
                # centrage au milieu du héros
                myBoulePosition[0] = int(myBoulePosition[0])+4
                myBoulePosition[1] = int(myBoulePosition[1])+2
                data["Boules_de_feu"]["Boules_de_feu_j2"]["Boule_de_feu_"+str(data["Numeros_Boules_de_feu"]["NumeroBouleDeFeu_j2"])] = boule_de_feu.createBoule_de_feu("@",myBoulePosition, data["Heros"]["Heros_j2"].directionAttaque, data["Heros"]["Heros_j2"].couleur)
    
    else:
        if not j2_interact:
            # si aucune touche n'est pressée
            heros.setDirection(data["Heros"]["Heros_j2"], "None")

        if not j1_interact:
            # si aucune touche n'est pressée
            heros.setDirection(data["Heros"]["Heros_j1"], "None")
    
    heros.setVelocity(data["Heros"]["Heros_j1"], collision.Collision_joueur_arene(data["Heros"]["Heros_j1"], data["Arene"]), collision.collision_Heros_Box(data["Heros"]["Heros_j1"], data["Xmax"], data["Ymax"]), collision.collision_j1_j2(data["Heros"]["Heros_j1"], data["Heros"]["Heros_j2"]))
    heros.setVelocity(data["Heros"]["Heros_j2"], collision.Collision_joueur_arene(data["Heros"]["Heros_j2"], data["Arene"]), collision.collision_Heros_Box(data["Heros"]["Heros_j2"], data["Xmax"], data["Ymax"]), collision.collision_j1_j2(data["Heros"]["Heros_j2"], data["Heros"]["Heros_j1"]))

    return

# Procédure de lancement du jeu
def run(data):
    #Boucle de simulation
    while True :
        interact(data)
        move(data)
        isCollision(data)
        isInLife(data)
        show(data)
        time.sleep(data["myTimeStep"])

# jeu de tests
if __name__ == "__main__":
    data = {"Heros":{}, "Boules_de_feu":{}, "Numeros_Boules_de_feu":{},"Spawn1": [41,15], "Spawn2":[101,15],"Arene":None, "Xmax":None, "Ymax":None, "old_settings":None, "Winner":None}
    init(data)
    run(data)