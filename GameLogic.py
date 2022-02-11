# Import des différents fichiers pour accès aux méthodes
import tkinter as tk

import CsvFunctions
# Initialisation des variables globales
# pour l'aléatoire
from random import randint


LASTMOVE = None

# Fonction qui détermine la taille des cases du plateau et qui les colore en vert pour symboliser le serpent
def CaseDraw(x, y, Canvas):
    # On défini les coordonnées (origine_caseX1; origine_caseY1) du point en haut à gauche de la case
    # et (origine_caseX2;origine_caseY2) du point en bas à droite de la case
    X1 = x * LargeurCase
    Y1 = y * HauteurCase
    X2 = X1 + LargeurCase
    Y2 = Y1 + HauteurCase

    # remplissage du rectangle
    Canvas.create_rectangle(X1, Y1, X2, Y2, fill="white")


def case_aleatoire():
    # on met à jour l'affichage et les événements du clavier
    AleatoireX = randint(1, int(CASENUMBER) - 2)
    AleatoireY = randint(1, int(CASENUMBER) - 2)

    return AleatoireX, AleatoireY


# affiche le serpent, l'argument étant la liste snake
def dessine_serpent(snake, Plateau):
    # tant qu'il y a des cases dans snake
    for case in snake:
        # on récupère les coordonées de la case
        x, y = case
        # on colorie la case
        CaseDraw(x, y, Plateau)


# On retourne le chiffre 1 si la case est dans le snake, 0 sinon
def etre_dans_snake(case):
    if case in SNAKE:
        EtreDedans = 1
    else:
        EtreDedans = 0

    return EtreDedans


# On renvoie un fruit aléatoire qui n'est pas dans le serpent
def fruit_aleatoire():
    # choix d'un fruit aléatoire
    FruitAleatoire = case_aleatoire()

    # tant que le fruit aléatoire est dans le serpent
    while (etre_dans_snake(FruitAleatoire)):
        # on prend un nouveau fruit aléatoire
        FruitAleatoire = case_aleatoire

    return FruitAleatoire


# On dessine le fruit, idem que pour colorier une case, mais on utilise create_oval à la place
def dessine_fruit(Plateau):
    global FRUIT
    x, y = FRUIT

    OrigineCaseX1 = x * LargeurCase
    OrigineCaseY1 = y * HauteurCase
    OrigineCaseX2 = OrigineCaseX1 + LargeurCase
    OrigineCaseY2 = OrigineCaseY1 + HauteurCase

    # On remplie l'ovale en rouge pour le fruit

    Plateau.create_oval(OrigineCaseX1, OrigineCaseY1, OrigineCaseX2, OrigineCaseY2, fill="red")


# met à jour la variable PERDU indiquant si on a perdu
def serpent_mort(NouvelleTete):
    global PERDU

    # si le serpent se mange lui-même (sauf au démarrage, c'est-à-dire: sauf quand MOUVEMENT vaut (0, 0))
    # OU si on sort du canvas
    if etre_dans_snake(NouvelleTete) and MOUVEMENT != (0, 0):
        # alors, on a perdu
        PERDU = 1


############################################################################################################################

def mise_a_jour_snake(Barre):
    global SNAKE, FRUIT

    # on récupère les coordonées de la tête actuelle
    (AncienneTeteX, AncienneTeteY) = SNAKE[0]
    # on récupère les valeurs du mouvement
    MouvementX, MouvementY = MOUVEMENT
    # on calcule les coordonées de la nouvelle tête
    NouvelleTete = (AncienneTeteX + MouvementX, AncienneTeteY + MouvementY)

    # si on mange un fruit

    if NouvelleTete == FRUIT:
        # on génère un nouveau fruit
        FRUIT = fruit_aleatoire()
        # on met à jour le score
        mise_a_jour_score(Barre)
    # sinon
    else:
        # on enlève le dernier élément du serpent (c'est-à-dire: on ne grandit pas)
        SNAKE.pop()
        if NouvelleTete[0] >= int(CASENUMBER)-1 and LASTMOVE == 'right_key':
            NouvelleTete = (1, NouvelleTete[1])
        elif NouvelleTete[0] <= 1 and LASTMOVE == 'left_key':
            NouvelleTete = (int(CASENUMBER)-1, NouvelleTete[1])

        if NouvelleTete[1] >= int(CASENUMBER)-1 and LASTMOVE == 'down_key':
            NouvelleTete = (NouvelleTete[0], 1)
        elif NouvelleTete[1] <= 1 and LASTMOVE == 'up_key':
            NouvelleTete = (NouvelleTete[0], int(CASENUMBER)-1)

    # on vérifie si on a perdu
    serpent_mort(NouvelleTete)
    # on ajoute la nouvelle tête
    SNAKE.insert(0, NouvelleTete)


# met à jour le score
def mise_a_jour_score(Barre):
    global SCORE
    print()
    SCORE = SCORE + 1
    Barre.config(state=tk.NORMAL)
    Barre.delete(0.0, 3.0)
    Barre.insert('1.0', "score obtenu: " + str(SCORE) + "\n")
    Barre.tag_add("tag_name", "1.0", "end")
    Barre.config(state=tk.DISABLED)

########################################################################################################################

# Ces quatres fonctions permettent le déplacement dans quatres directions du serpent
# elles mettent à jour les coordonées du mouvement
def left_key(event):
    global LASTMOVE
    global MOUVEMENT
    if LASTMOVE != 'right_key' or None:
        MOUVEMENT = (-1, 0)
        LASTMOVE = 'left_key'


def right_key(event):
    global LASTMOVE
    global MOUVEMENT
    if LASTMOVE != 'left_key' or None:
        MOUVEMENT = (1, 0)
        LASTMOVE = 'right_key'


def up_key(event):
    global LASTMOVE
    global MOUVEMENT
    if LASTMOVE != 'down_key' or None:
        MOUVEMENT = (0, -1)
        LASTMOVE = 'up_key'


def down_key(event):
    global LASTMOVE
    global MOUVEMENT
    if LASTMOVE != 'up_key' or None:
        MOUVEMENT = (0, 1)
        LASTMOVE = 'down_key'


########################################################################################################################
# réinitialise les variables pour une nouvelle partie
def reinitialiser_jeu():
    global SNAKE, FRUIT, MOUVEMENT, SCORE, PERDU

    # serpent initial
    SNAKE = [case_aleatoire()]
    # fruit initial
    FRUIT = fruit_aleatoire()
    # mouvement initial
    MOUVEMENT = (0, 0)
    # score initial
    SCORE = 0
    # variable perdu initiale (sera mise à 1 si le joueur perd)
    PERDU = 0


def tache(fenetre, Plateau, Barre, CASENUMBER, NAME):
    global NombreCase
    NombreCase = CASENUMBER
    NAME = str(NAME).rstrip('\n')
    fenetre.update
    fenetre.update_idletasks()
    # on met à jour le snake
    mise_a_jour_snake(Barre)
    # on supprime tous les éléments du plateau
    Plateau.delete("all")
    # on redessine le fruit
    dessine_fruit(Plateau)
    # on redessine le serpent
    dessine_serpent(SNAKE, Plateau)

    # si on a perdu
    if PERDU:
        # on efface la barre des scores
        Barre.config(state=tk.NORMAL)
        Barre.delete(0.0, 3.0)
        # on affiche perdu
        Barre.insert('1.0', "Vous avez perdu avec un score de " + str(SCORE))
        Barre.tag_add("tag_name", "1.0", "end")
        Barre.config(state=tk.DISABLED)
        # on prépare la nouvelle partie
        CsvFunctions.addRow('testCsv.csv', int(SCORE), str(NAME))
        reinitialiser_jeu()
        # on rappelle la fonction principale
        fenetre.after(70, lambda: tache(fenetre, Plateau, Barre, CASENUMBER, NAME))
    # sinon
    else:
        # on rappelle la fonction principale
        fenetre.after(70, lambda: tache(fenetre, Plateau, Barre, CASENUMBER, NAME))



#######################################################################################################################################
def InitGame(NombreCase):
    global CASENUMBER
    CASENUMBER = NombreCase
    if CASENUMBER.rstrip('\n') == "" or int(CASENUMBER.rstrip('\n')) < 10 or int(CASENUMBER.rstrip('\n'))>200:
        CASENUMBER = 50
    # le snake initial: une liste avec une case aléatoire
    global SNAKE
    SNAKE = [case_aleatoire()]
    # le fruit initial
    global FRUIT
    FRUIT = fruit_aleatoire()
    # le mouvement initial, une paire d'entiers représentant les coordonées du déplacement, au départ on ne bouge pas
    global MOUVEMENT
    MOUVEMENT = (0, 0)
    # le score initial
    global SCORE
    SCORE = 0
    # la variable permettant de savoir si on a perdu, sera mise à 1 si on perd
    global PERDU
    PERDU = 0
    global LargeurCase
    global HauteurCase
    # On définit la longueur et la largeur du plateau
    LargeurCase = (700 / int(CASENUMBER))
    HauteurCase = (650 / int(CASENUMBER))
