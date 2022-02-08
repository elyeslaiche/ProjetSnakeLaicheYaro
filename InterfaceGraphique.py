
from tkinter import ttk
from GameLogic import *

def init():

    fenetre = tk.Tk()
    fenetre.title("Snake")
    fenetre.geometry("700x700")
    fenetre.resizable(False, False)
    # Gets both half the screen width/height and window width/height
    positionRight = int(fenetre.winfo_screenwidth() / 2 - 350)
    positionDown = int(fenetre.winfo_screenheight() / 2 - 350)

    # Positions the window in the center of the page.
    fenetre.geometry("+{}+{}".format(positionRight, positionDown))
    Plateau = tk.Canvas(fenetre, width=700, height=650, bg="black")
    #side désigne l'endroit où débute le canvas
    Plateau.pack(side="bottom",fill=tk.NONE)
    
    button = Button(fenetre, text = 'Recommencer la partie ', command =restart_program,fg='black', bg='#ffffff', activebackground='red', padx=15)
    button.pack(side = BOTTOM) 

    # On crée un Canvas pour le score
    Barre = tk.Text(fenetre, width=500, height=50, bg="light blue")
    # On écrit le score initial dans la barre
    Barre.tag_configure("tag_name", justify='center')
    Barre.insert("1.0","score: 0\n")
    Barre.tag_add("tag_name", "1.0", "end")
    # On place la barre
    Barre.pack()
    Barre.config(state=tk.DISABLED)
    fenetre.bind("<Left>", left_key)
    fenetre.bind("<Right>", right_key)
    fenetre.bind("<Up>", up_key)
    fenetre.bind("<Down>", down_key)
    fenetre.after(0, lambda: tache(fenetre, Plateau, Barre))
    globals.initializeGlobalVar(Plateau)
    return fenetre

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def initConfigWindow():
    fenetreConfig = tk.Tk()
    fenetreConfig.geometry("500x500")
    fenetreConfig.config(bg='black')
    fenetreConfig.title("Snake config")
    fenetreConfig.resizable(False, False)
    # Gets both half the screen width/height and window width/height
    positionRight = int(fenetreConfig.winfo_screenwidth() / 2 - 250)
    positionDown = int(fenetreConfig.winfo_screenheight() / 2 - 250)

    # Positions the window in the center of the page.
    fenetreConfig.geometry("+{}+{}".format(positionRight, positionDown))
    name = tk.Label(fenetreConfig, text="Player name", fg='white', bg='black')
    nameEntered = tk.Text(fenetreConfig, height=1, width=25, bg='white')
    name.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    nameEntered.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    buttonStart = tk.Button(fenetreConfig, text='start', fg='green', bg='darkgrey', activebackground='green',
    activeforeground='white', command=lambda: startGame(fenetreConfig))
    buttonQuit = tk.Button(fenetreConfig, text='quit', fg='red', bg='darkgrey', activebackground='red',
    activeforeground='white', command=fenetreConfig.destroy)
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


def startGame(fenetre):
    fenetre.destroy()
    fenetreGame = init()
    fenetreGame.mainloop()




#S'inspirer de test.py pour faire le serpent, comment il se deplace, comment les fruits sont générés (Elyes)
#fenetre après defaite pour afficher le top 3 des meilleurs scores, et ton personal best (Elyes)
#modifier l'interface graphique(Pascal), faire des skins de serpent(Pascal), nom du joueur(Elyes), pouvoir enregistrer le score a la fin(Elyes), pouvoir enregistrer la partie en cours(Elyes), mode de difficulté avec la vitesse (Pascal),