def initializeGlobalVar(Plateau):
    # On défini le nombre de cases du plateau
    global NombreDeCases
    # On défini les dimenssions d'une case
    global LargeurCase
    global HauteurCase
    NombreDeCases = 75
    # On défini le nombre de cases du plateau
    LargeurCase = (Plateau.winfo_width() / NombreDeCases)
    HauteurCase = (Plateau.winfo_height() / NombreDeCases)