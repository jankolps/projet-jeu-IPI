import sys

class heros:
    pass

# Fonction de création du héros
def createHeros(filename="herosDroite.txt", direction="droite", couleur=10, position=[5,5]):
    myHeros = heros()

    CorpsHeros = []
    with open(filename, "r") as file:
        corpsEntier = file.read()
    corpsLignes = corpsEntier.split("\n")
    for lignes in corpsLignes:
        for lettres in lignes:
            
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

    # Defintion du sens du héros
    if h.direction == "droite":
        filename = "herosDroite.txt"
        with open(filename, "r") as file:
            h.corps = file.read()
    elif h.direction == "gauche":
        filename = "herosDroite.txt"
        with open(filename, "r") as file:
            h.corps = file.read()
    else:
        pass

    #sys.stdout.write("\033["+str(y)+";"+str(x)+"H")
    #sys.stdout.write(h.corps)
    print(h.corps[0])
    return


# Procédure de déplacement du héros
def move(h, dt):
    if h.direction == "gauche":

        pass
        # Aller a gauche
    elif h.direction == "droite":
        pass
        # Aller a droite
    elif h.direction == "haut":
        pass
        # Faire un saut


# Procédure


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
    print(Unhero.corps[0])
    #show(Unhero)