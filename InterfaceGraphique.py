# Interface graphique
from tkinter import ttk
# Import pour utilisation des méthodes de Gamelogic.py
from GameLogic import *

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
    Canvas.pack(side="bottom", fill=tk.NONE)
    Bar.pack()
    button.pack()

    # Affecter les events aux fleches directionnelles
    fenetre.bind("<Left>", left_key)
    fenetre.bind("<Right>", right_key)
    fenetre.bind("<Up>", up_key)
    fenetre.bind("<Down>", down_key)

    # affecter une tache a effectuer sur la fenetre tout le temps
    fenetre.after(0, lambda: tache(fenetre, Canvas, Bar))

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
    name = tk.Label(fenetreConfig, text="Player name", fg='Black', bg='grey')
    nameEntered = tk.Text(fenetreConfig, height=1, width=25, bg='white')

    # Affichage du champ texte centré horizontalement
    name.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    nameEntered.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    # Déclaration des boutons pour commencer le jeu et quitter le jeu
    buttonStart = tk.Button(fenetreConfig, text='start', fg='green', bg='darkgrey', activebackground='green',
                            activeforeground='white', command=lambda: startGame(fenetreConfig, nameEntered))
    buttonQuit = tk.Button(fenetreConfig, text='quit', fg='red', bg='darkgrey', activebackground='red',
                           activeforeground='white', command=fenetreConfig.destroy)

    #Affichage des boutons sur la fenetre
    buttonStart.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
    buttonQuit.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

    style = ttk.Style(fenetreConfig)
    # set ttk theme to "clam" which support the fieldbackground option
    style.theme_use("clam")
    style.configure("Treeview", background="black",
                    fieldbackground="black", foreground="white")

    game_frame = tk.Frame(fenetreConfig)
    my_game = ttk.Treeview(game_frame)

    my_game['columns'] = ('player_name', 'player_Rank', 'player_states')

    my_game.column("#0", width=0, stretch=tk.NO)
    my_game.column("player_name", anchor=tk.CENTER, width=100)
    my_game.column("player_Rank", anchor=tk.CENTER, width=100)
    my_game.column("player_states", anchor=tk.CENTER, width=100)

    my_game.heading("#0", text="", anchor=tk.CENTER)
    my_game.heading("player_name", text="Name", anchor=tk.CENTER)
    my_game.heading("player_Rank", text="Rank", anchor=tk.CENTER)
    my_game.heading("player_states", text="States", anchor=tk.CENTER)

    my_game.insert(parent='', index='end', iid=0, text='',
                   values=('1', 'Ninja', '101', 'Oklahoma', 'Moore'))
    my_game.insert(parent='', index='end', iid=1, text='',
                   values=('2', 'Ranger', '102'))
    my_game.insert(parent='', index='end', iid=2, text='',
                   values=('3', 'Deamon', '103'))
    my_game.insert(parent='', index='end', iid=3, text='',
                   values=('4', 'Dragon', '104'))
    my_game.insert(parent='', index='end', iid=4, text='',
                   values=('5', 'CrissCross'))
    my_game.insert(parent='', index='end', iid=5, text='',
                   values=('6', 'ZaqueriBlack', '106'))
    game_frame.pack()
    my_game.pack()

    return fenetreConfig


def LastWindow():
    return 0


def startGame(fenetre, Textbox):
    global NAME
    NAME = Textbox.get("1.0", tk.END)
    fenetre.destroy()
    fenetreGame = init()
    fenetreGame.mainloop()

# S'inspirer de test.py pour faire le serpent, comment il se deplace, comment les fruits sont générés (Elyes)
# fenetre après defaite pour afficher le top 3 des meilleurs scores, et ton personal best (Elyes)
# modifier l'interface graphique(Pascal), faire des skins de serpent(Pascal), nom du joueur(Elyes), pouvoir enregistrer le score a la fin(Elyes), pouvoir enregistrer la partie en cours(Elyes), mode de difficulté avec la vitesse (Pascal),
