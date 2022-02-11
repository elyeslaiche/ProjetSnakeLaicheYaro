# Interface graphique
import os
import sys
import tkinter as tk
from tkinter import ttk
import GameLogic
from CsvFunctions import readScore
from GameLogic import reinitialiser_jeu, tache, left_key, right_key, up_key, down_key, case_aleatoire, fruit_aleatoire


def init():
    # declaration de la fenetre du jeu
    fenetre = tk.Tk()
    fenetre.title("Snake")
    fenetre.geometry("700x700")
    fenetre.resizable(False, False)
    # Pour obtenir les positions centrales de l'ecran
    positionRight = int(fenetre.winfo_screenwidth() / 2 - 400)
    positionDown = int(fenetre.winfo_screenheight() / 2 - 400)

    # Centre la fenetre
    fenetre.geometry("+{}+{}".format(positionRight, positionDown))

    # déclaration du plateau de jeu
    Canvas = tk.Canvas(fenetre, width=700, height=650, bg="black")
    Canvas.pack(side="bottom", fill=tk.NONE)

    # Déclaration du bouton recommencer la partie
    button = tk.Button(fenetre, text='Recommencer la partie ', command=reinitialiser_jeu, fg='black',
                       bg='#ffffff', activebackground='red', padx=15)

    # On crée un Canvas pour le score
    Bar = tk.Text(fenetre, width=500, height=50, bg="light blue")

    # On écrit le score initial dans la barre
    Bar.tag_configure("tag_name", justify='center')
    Bar.insert("1.0", "score: 0\n")  # Centrer le texte horizontalement
    Bar.tag_add("tag_name", "1.0", "end")

    # Configurer le score comme read-Only
    Bar.config(state=tk.DISABLED)

    # Affichage des elements declarés sur la fenetre*
    button.pack()
    Bar.pack()

    # Affecter les events aux fleches directionnelles
    fenetre.bind("<Left>", left_key)
    fenetre.bind("<Right>", right_key)
    fenetre.bind("<Up>", up_key)
    fenetre.bind("<Down>", down_key)

    # affecter une tache a effectuer sur la fenetre tout le temps
    fenetre.after(0, lambda: tache(fenetre, Canvas, Bar, CASENUMBER=CASENUMBER, NAME=NAME))

    return fenetre


def initConfigWindow():

    # declaration de la fenetre de configuration du jeu
    fenetreConfig = tk.Tk()
    fenetreConfig.geometry("500x500")
    fenetreConfig.config(bg='grey')
    fenetreConfig.title("Snake config")
    fenetreConfig.resizable(False, False)

    # Pour obtenir les positions centrales de l'ecran
    positionRight = int(fenetreConfig.winfo_screenwidth() / 2 - 250)
    positionDown = int(fenetreConfig.winfo_screenheight() / 2 - 250)

    # Centre la fenetre
    fenetreConfig.geometry("+{}+{}".format(positionRight, positionDown))

    # Déclaration du champ texte pour pouvoir entrer le nom du joueur
    name = tk.Label(fenetreConfig, text="Nom du joueur", fg='Black', bg='grey')
    nameEntered = tk.Text(fenetreConfig, height=1, width=25, bg='white')

    # Déclaration du champ texte pour pouvoir entrer le nom du joueur
    caseNumber = tk.Label(fenetreConfig, text="Nombre de case", fg='Black', bg='grey')
    caseNumberEntered = tk.Text(fenetreConfig, height=1, width=25, bg='white')

    # Affichage du champ texte centré horizontalement
    name.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    nameEntered.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

    # Affichage du champ texte centré horizontalement
    caseNumber.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    caseNumberEntered.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

    # Déclaration des boutons pour commencer le jeu et quitter le jeu
    buttonStart = tk.Button(fenetreConfig, text='start', fg='green', bg='darkgrey', activebackground='green',
                            activeforeground='white',
                            command=lambda: startGame(fenetreConfig, nameEntered, caseNumberEntered))
    buttonQuit = tk.Button(fenetreConfig, text='quit', fg='red', bg='darkgrey', activebackground='red',
                           activeforeground='white', command=fenetreConfig.destroy)

    # Affichage des boutons sur la fenetre
    buttonStart.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
    buttonQuit.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

    return fenetreConfig

def LastWindow(fenetre):
    fenetre.destroy()
    fenetreLast = tk.Tk()
    fenetreLast.geometry("500x500")
    fenetreLast.config(bg='grey')
    fenetreLast.title("Snake End")
    fenetreLast.resizable(False, False)

    buttonStart = tk.Button(fenetreLast, text='Restart', fg='green', bg='darkgrey', activebackground='green',
                            activeforeground='white',
                            command=reInitPrgm)
    buttonQuit = tk.Button(fenetreLast, text='quit', fg='red', bg='darkgrey', activebackground='red',
                           activeforeground='white', command=fenetreLast.destroy)

    # Affichage des boutons sur la fenetre


    # On crée un Canvas pour le score
    Bar = tk.Label(fenetreLast, text="\nvous avez perdu avec un score de: " + str(GameLogic.SCORE), fg='Black', bg='grey')

    # Utilisation de ttk pour pouvoir insérer le tableau des scores dans la fenetre
    style = ttk.Style(fenetreLast)
    style.theme_use("clam")
    style.configure("Treeview", background="grey",
                    fieldbackground="grey", foreground="grey")

    configFrame = tk.Frame(fenetreLast)
    Table = ttk.Treeview(configFrame)

    # Attribution des colonnes
    Table['columns'] = ('Name', 'Score')
    Table['show'] = 'headings'
    Table.column("Name", anchor=tk.CENTER, width=100)
    Table.column("Score", anchor=tk.CENTER, width=100)

    # Configuration des nom de colonnes
    Table.heading("Name", text="Name", anchor=tk.CENTER)
    Table.heading("Score", text="Score", anchor=tk.CENTER)
    readScore('testCsv.csv', Table)
    # Affichage du tableau et du Frame qui contient le tableau

    buttonQuit.pack(side=tk.BOTTOM)
    buttonStart.pack(side=tk.BOTTOM)
    configFrame.pack()
    Table.pack()
    Bar.pack()




def startGame(fenetre, TextboxName, TextboxCase):
    # Définition d'une variable globale qui contiendra le nom du joueur
    global NAME
    # Récupération du nom
    NAME = TextboxName.get("1.0", tk.END)
    global CASENUMBER
    CASENUMBER = TextboxCase.get("1.0", tk.END)
    # On ferme la fenêtre de configuration
    fenetre.destroy()

    # On affiche la fenetre du jeu grace à la fonction init() déclarée plus haut
    GameLogic.InitGame(CASENUMBER)
    fenetreGame = init()

    fenetreGame.mainloop()

def reInitPrgm():
    python = sys.executable
    os.execl(python, python, * sys.argv)