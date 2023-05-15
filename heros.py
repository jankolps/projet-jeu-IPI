import sys
import time

class heros:
    pass

# Fonction de création du héros
def createHeros(filename="heros.txt", direction="droite", couleur=10, position=[5,5]):
    myHeros = heros()

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
        for lettres in lignes :
            if lettres != " ":
                sys.stdout.write("\033[" + str(y) + ";" + str(x+v)+"H")
            v += 1
        y += 1
    return

# Procédure de déplacement du héros
def move(h):
    if h.direction == "gauche":
        h.position[0] -= 1
    elif h.direction == "droite":
        h.position[0] += 1
    elif h.direction == "haut":
        h.position[1] -= 1
    elif h.direction == "bas":
        h.position[1] += 1

# ===== Getters =====
def getDirection(h):
    return h.direction

def getVies(h):
    return h.vies

# ===== Setters =====
def setCorps(h, newcorps):
    h.corps = newcorps
    return

def setVies(h, newVies):
    h.vies = newVies
    return

if __name__ == "__main__":
    Unhero = createHeros()
    show(Unhero)
    """
    time.sleep(2)
    move(Unhero)
    show(Unhero)
    """