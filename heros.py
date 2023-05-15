import sys

class heros:
    pass

# Fonction de création du héros
def createHeros(filename="heros.txt", direction="gauche", couleur=5):
    myHeros = heros()
    with open(filename, "r") as file:
        myHeros.corps = file.read()
    myHeros.direction = direction
    myHeros.couleur = couleur
    return myHeros

# Procédure d'affichage du héros
def show(h) :
    """
    On positionne le "curseur" à la position "zéro" en haut à gauche de la fenêtre
    Remarque la position "zéro" vaut 1, 1
    """
    sys.stdout.write("\033[1;1H")

    """
    Initialisation des couleurs du terminal
    Polices en blanc : code 37
    """
    sys.stdout.write("\033[37m")

    """
    background en noir : code 40
    """
    sys.stdout.write("\033[40m")
    
    """
    Affichage du héro
    """
    sys.stdout.write(str(h.corps))
    
    """
    background en cyan (bleu clair) : code 46
    """
    sys.stdout.write("\033[46m")

    return


# Procédure de déplacement du héros

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
    show(Unhero)