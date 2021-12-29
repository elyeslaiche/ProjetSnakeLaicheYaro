import tkinter as tk

def init():
    global fenetre
    global interface
    global compteur

    compteur = 0
    fenetre = tk.Tk()
    fenetre.title("Snake")
    # notre interface
    interface = tk.Canvas(fenetre, width=600, height=600, bg="white")
    interface.pack(padx=5, pady=5)
    return fenetre

#S'inspirer de test.py pour faire le serpent, comment il se deplace, comment les fruits sont générés (Elyes)
#fenetre après defaite pour afficher le top 3 des meilleurs scores, et ton personal best (Elyes)
#modifier l'interface graphique(Pascal), faire des skins de serpent(Pascal), nom du joueur(Elyes), pouvoir enregistrer le score a la fin(Elyes), pouvoir enregistrer la partie en cours(Elyes), mode de difficulté avec la vitesse (Pascal),