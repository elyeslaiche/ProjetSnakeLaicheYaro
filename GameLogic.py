import tkinter as tk
import globals
# pour l'aléatoire
from random import randint

global NombreDeCases
NombreDeCases = 75


# Fonction qui détermine la taille des cases du plateau et qui les colore en vert pour symboliser le serpent
def remplir_case(x, y, Plateau):
    # On défini les coordonnées (origine_caseX1; origine_caseY1) du point en haut à gauche de la case
    # et (origine_caseX2;origine_caseY2) du point en bas à droite de la case
    OrigineCaseX1 = x * globals.LargeurCase
    OrigineCaseY1 = y * globals.HauteurCase
    OrigineCaseX2 = OrigineCaseX1 + globals.LargeurCase
    OrigineCaseY2 = OrigineCaseY1 + globals.HauteurCase

    # remplissage du rectangle
    Plateau.create_rectangle(OrigineCaseX1, OrigineCaseY1, OrigineCaseX2, OrigineCaseY2, fill="white")

def case_aleatoire():
    AleatoireX = randint(0, NombreDeCases - 1)
    AleatoireY = randint(0, NombreDeCases - 1)

    return (AleatoireX, AleatoireY)


# affiche le serpent, l'argument étant la liste snake
def dessine_serpent(snake, Plateau):
    # tant qu'il y a des cases dans snake
    for case in snake:
        # on récupère les coordonées de la case
        x, y = case
        # on colorie la case
        remplir_case(x, y, Plateau)


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

    OrigineCaseX1 = x * globals.LargeurCase
    OrigineCaseY1 = y * globals.HauteurCase
    OrigineCaseX2 = OrigineCaseX1 + globals.LargeurCase
    OrigineCaseY2 = OrigineCaseY1 + globals.HauteurCase

    # On remplie l'ovale en rouge pour le fruit

    Plateau.create_oval(OrigineCaseX1, OrigineCaseY1, OrigineCaseX2, OrigineCaseY2, fill="red")


########################################################################################################################

# Ces quatres fonctions permettent le déplacement dans quatres directions du serpent
# elles mettent à jour les coordonées du mouvement
def left_key(event):
    global MOUVEMENT
    MOUVEMENT = (-1, 0)


def right_key(event):
    global MOUVEMENT
    MOUVEMENT = (1, 0)


def up_key(event):
    global MOUVEMENT
    MOUVEMENT = (0, -1)


def down_key(event):
    global MOUVEMENT
    MOUVEMENT = (0, 1)


########################################################################################################################


# met à jour la variable PERDU indiquant si on a perdu
def serpent_mort(NouvelleTete):
    global PERDU

    NouvelleTeteX, NouvelleTeteY = NouvelleTete

    # si le serpent se mange lui-même (sauf au démarrage, c'est-à-dire: sauf quand MOUVEMENT vaut (0, 0))
    # OU si on sort du canvas
    if (etre_dans_snake(NouvelleTete) and MOUVEMENT != (0,
                                                        0)) or NouvelleTeteX < 0 or NouvelleTeteY < 0 or NouvelleTeteX >= globals.NombreDeCases or NouvelleTeteY >= globals.NombreDeCases:
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
    # on vérifie si on a perdu
    serpent_mort(NouvelleTete)
    # on ajoute la nouvelle tête
    SNAKE.insert(0, NouvelleTete)

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

# met à jour le score
def mise_a_jour_score(Barre):
    global SCORE

    SCORE = SCORE + 1
    Barre.config(state=tk.NORMAL)
    Barre.delete(0.0, 3.0)
    Barre.insert('1.0', "score obtenu: " + str(SCORE) + "\n")
    Barre.tag_add("tag_name", "1.0", "end")
    Barre.config(state=tk.DISABLED)

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



def tache(fenetre, Plateau, Barre):
    # on met à jour l'affichage et les événements du clavier
    globals.initializeGlobalVar(fenetre)
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
        reinitialiser_jeu()
        # on rappelle la fonction principale
        fenetre.after(70, lambda: tache(fenetre, Plateau, Barre))
    # sinon
    else:
        # on rappelle la fonction principale
        fenetre.after(70, lambda: tache(fenetre, Plateau, Barre))

#######################################################################################################################################

# le snake initial: une liste avec une case aléatoire
SNAKE = [case_aleatoire()]
# le fruit initial
FRUIT = fruit_aleatoire()
# le mouvement initial, une paire d'entiers représentant les coordonées du déplacement, au départ on ne bouge pas
MOUVEMENT = (0, 0)
# le score initial
SCORE = 0
# la variable permettant de savoir si on a perdu, sera mise à 1 si on perd
PERDU = 0