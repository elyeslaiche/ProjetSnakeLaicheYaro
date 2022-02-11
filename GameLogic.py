# Import des différents fichiers pour accès aux méthodes
import collections
import tkinter as tk
import InterfaceGraphique
import CsvFunctions

# pour l'aleatoire
from random import randint

LASTMOVE = None


# Methode pour obtenir une case aleatoire utilise pour dessiner un fruit
def randomTuple():
    # on met à jour l'affichage et les événements du clavier
    X = randint(0, int(BOXCOUNT) - 1)
    Y = randint(0, int(BOXCOUNT) - 1)

    return X, Y


# Fonction qui détermine la taille des cases du plateau et qui les colore en blanc pour symboliser le serpent
def CaseDraw(x, y, Canvas):
    # On défini les coordonnées (X1, Y1) du point en haut à gauche de la case
    # et (X2, Y2) du point en bas à droite de la case
    X1 = x * boxWidth
    Y1 = y * boxHeight
    X2 = X1 + boxWidth
    Y2 = Y1 + boxHeight

    # remplissage du rectangle
    Canvas.create_rectangle(X1, Y1, X2, Y2, fill="white")


# affiche le serpent, l'argument étant la liste snake et la plateau de jeu
def drawSnake(snake, canvas):
    # tant qu'il y a des cases dans snake
    for case in snake:
        # on récupère les coordonées de la case
        x, y = case
        # on colorie la case
        CaseDraw(x, y, canvas)


# On dessine le fruit, idem que pour colorier une case, mais on utilise create_oval à la place
def drawFruit(Canvas):
    global FRUIT
    if not isinstance(FRUIT, collections.abc.Sequence):
        FRUIT = randomTuple()
    x, y = FRUIT

    X1 = x * boxWidth
    Y1 = y * boxHeight
    X2 = X1 + boxWidth
    Y2 = Y1 + boxHeight

    # On rempli la figure en rouge pour le fruit
    Canvas.create_oval(X1, Y1, X2, Y2, fill="red")


# On retourne le true si la case est dans le snake, 0 sinon
def IsInSnake(case):
    if case in SNAKE:
        return True
    else:
        return False


# On renvoie un fruit aléatoire qui n'est pas dans le serpent
def randomFruitPos():
    # choix d'un fruit aléatoire
    randFruit = randomTuple()

    # tant que le fruit aléatoire est dans le serpent
    while (IsInSnake(randFruit)):
        # on prend un nouveau fruit aléatoire
        randFruit = randomTuple

    return randFruit


# met à jour la variable DEFEAT indiquant si on a perdu
def deadSnake(Head):
    global DEFEAT

    # si le serpent se mange lui-même (sauf au démarrage, c'est-à-dire: sauf quand MOUVEMENT vaut (0, 0))
    if IsInSnake(Head) and MOVE != (0, 0):
        # alors, on a perdu
        DEFEAT = 1


# ----------------------------------------------------------------------------------------------------------------

def updateSnake(Bar):
    global SNAKE, FRUIT

    # on récupère les coordonées de la tête actuelle
    (lastHeadX, lastHeadY) = SNAKE[0]
    # on récupère les valeurs du mouvement
    moveX, moveY = MOVE
    # on calcule les coordonées de la nouvelle tête
    newHead = (lastHeadX + moveX, lastHeadY + moveY)

    # si on mange un fruit

    if newHead == FRUIT:
        # on génère un nouveau fruit
        FRUIT = randomFruitPos()
        # on met à jour le score
        updateScore(Bar)
    # sinon
    else:
        # on enlève le dernier élément du serpent (c'est-à-dire: on ne grandit pas)
        SNAKE.pop()
        if newHead[0] >= int(BOXCOUNT) and LASTMOVE == 'right_key':
            newHead = (0, newHead[1])
        elif newHead[0] < 0 and LASTMOVE == 'left_key':
            newHead = (int(BOXCOUNT), newHead[1])

        if newHead[1] >= int(BOXCOUNT) and LASTMOVE == 'down_key':
            newHead = (newHead[0], 0)
        elif newHead[1] < 0 and LASTMOVE == 'up_key':
            newHead = (newHead[0], int(BOXCOUNT))

    # on vérifie si on a perdu
    deadSnake(newHead)
    # on ajoute la nouvelle tête
    SNAKE.insert(0, newHead)


# met à jour le score
def updateScore(Barre):
    global SCORE
    SCORE += 1
    Barre.config(state=tk.NORMAL)
    Barre.delete(0.0, 3.0)
    Barre.insert('1.0', "score obtenu: " + str(SCORE) + "\n")
    Barre.tag_add("tag_name", "1.0", "end")
    Barre.config(state=tk.DISABLED)


# ----------------------------------------------------------------------------------------------------------------

# Ces quatres fonctions permettent le déplacement dans quatres directions du serpent
# elles mettent à jour les coordonées du mouvement
def left_key(event):
    global LASTMOVE
    global MOVE
    if LASTMOVE != 'right_key' or None:
        MOVE = (-1, 0)
        LASTMOVE = 'left_key'


def right_key(event):
    global LASTMOVE
    global MOVE
    if LASTMOVE != 'left_key' or None:
        MOVE = (1, 0)
        LASTMOVE = 'right_key'


def up_key(event):
    global LASTMOVE
    global MOVE
    if LASTMOVE != 'down_key' or None:
        MOVE = (0, -1)
        LASTMOVE = 'up_key'


def down_key(event):
    global LASTMOVE
    global MOVE
    if LASTMOVE != 'up_key' or None:
        MOVE = (0, 1)
        LASTMOVE = 'down_key'


# ----------------------------------------------------------------------------------------------------------------
# réinitialise les variables pour une nouvelle partie
def reinitialiser_jeu():
    global SNAKE, FRUIT, MOVE, SCORE, DEFEAT

    # serpent initial
    SNAKE = [randomTuple()]
    # fruit initial
    FRUIT = randomFruitPos()
    # mouvement initial
    MOVE = (0, 0)
    # score initial
    SCORE = 0
    # variable perdu initiale (sera mise à 1 si le joueur perd)
    DEFEAT = 0


def tache(fenetre, Plateau, Barre, CASENUMBER, NAME):
    global NombreCase
    NombreCase = CASENUMBER
    NAME = str(NAME).rstrip('\n').rstrip('\t')
    fenetre.update
    fenetre.update_idletasks()
    # on met à jour le snake
    updateSnake(Barre)
    # on supprime tous les éléments du plateau
    Plateau.delete("all")
    # on redessine le fruit
    drawFruit(Plateau)
    # on redessine le serpent
    drawSnake(SNAKE, Plateau)

    # si on a perdu
    if DEFEAT:
        CsvFunctions.addRow(int(SCORE), str(NAME))
        InterfaceGraphique.LastWindow(fenetre)
    # sinon
    else:
        # on rappelle la fonction principale
        fenetre.after(70, lambda: tache(fenetre, Plateau, Barre, CASENUMBER, NAME))


# ----------------------------------------------------------------------------------------------------------------
def InitGame(boxCount):
    global BOXCOUNT
    BOXCOUNT = boxCount
    if not BOXCOUNT.rstrip('\n').isdigit() or (
            BOXCOUNT.rstrip('\n') == "" or int(BOXCOUNT.rstrip('\n')) < 25 or int(BOXCOUNT.rstrip('\n')) > 200):
        BOXCOUNT = 50
    # le snake initial: une liste avec une case aléatoire
    global SNAKE
    SNAKE = [randomTuple()]
    # le fruit initial
    global FRUIT
    FRUIT = randomFruitPos()
    # le mouvement initial, une paire d'entiers représentant les coordonées du déplacement, au départ on ne bouge pas
    global MOVE
    MOVE = (0, 0)
    # le score initial
    global SCORE
    SCORE = 0
    # la variable permettant de savoir si on a perdu, sera mise à 1 si on perd
    global DEFEAT
    DEFEAT = 0
    global boxWidth
    global boxHeight
    # On définit la longueur et la largeur du plateau
    boxWidth = (700 / int(BOXCOUNT))
    boxHeight = (650 / int(BOXCOUNT))
