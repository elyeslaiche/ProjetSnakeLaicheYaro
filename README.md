Sommaire
---------------------------------------------------------------------------

1°)Le projet : Snake
2°)Description du jeu
3°)Fonctionnement du jeu
4°)Exécution du code  
5°) Aide 
6°) Structure du projet Snake
7°) Auteurs
8°) Documentation pour le projet

1°)Le projet : Snake
---------------------------------------------------------------------------
Nous avons eu à effectuer un projet en python qui consiste à créer un jeu Snake.

2°)Description du jeu 
----------------------------------------------------------------------------

Le jeu Snake est un jeu dans lequel nous avons un joueur qui controle une ligne semblable à un serpent. Ainsi le serpent doit slalomer entre les bords de l'écran . Pour pouvoir gagner le maximum de points , le joueur doit faire manger à son serpent un certain nombre de fruits présents de facon aléatoire au niveau de l'écran. Ce qui permet d'allonger à chaque fois la taille du serpent. Aussi le joueur ne peut que lui indiquer une direction à suivre qui peut etre : en haut, en bas, à gauche, à droite et il faut  éviter que la tête du serpent touche son propre corps, sinon il risque de mourir.


3°)Fonctionnement du jeu 
----------------------------------------------------------------------------
Avant le lancement de la partie, il faut ajouter son nom.
On peut aussi ajouter le nombre de cases que l'on veut pour la taille de l'interface. Le nombre de cases minimum qu'on peut choisir est de 25.
Après cela appuyer sur le bouton start pour lancer la partie et commencer à jouer. 
Le score est affiché en haut au niveau l'interface de jeu et il s'incrémente de 1 à chaque fois que le serpent mange un fruit.
Possibilité de redémarrer le jeu.
Si on perd et que la partie se termine le score est stocké dans un fichier csv et un résultat est affiché sous forme d'une liste avec les meilleurs scores obtenus.


4°)Exécution du code
----------------------------------------------------------------------------
Exécution du code via le fichier principal main.py
commande :
$ python3 main.py

5°) Aide
----------------------------------------------------------------------------

Problème possible qu'on peut rencontrer :
-- message d'erreur : No module named Pandas
s'assurer d'avoir la version de python3 et bien installer pandas
voir le fichier requirements.txt pour plus d'informations.


6°) Structure du projet Snake
---------------------------------------------------------------------------
----CsvFunctions.py 
Importation de pandas qui est une bibliothèque utilisée en python pour manipuler et analyser les données.
Dans ce fichier on retrouve une fonction qui va lire les scores, une fonction qui va ajouter des colonnes pour le score et le nom d'un nouveau partcipant, et une autre fonction pour sauvegarder le meilleur score d'un joueur.

-----GameLogic.py
On retrouve dans ce fichier des fonctions pour :
Dessiner les fruits de manière aléatoire
Dessiner le serpent et le mettre à jour(faire en sorte qu'il grandisse)
Mettre à jour le score 
Définir les directions du serpents et les touches à utiliser
Réinitialiser les variables en cas de nouvelle partie 

----globals.py
Ce fichier contient une fonction qui permet de définir le nombre de cases de l'interface et les dimensions de chaque case.

---------InterfaceGraphique.py
Ce fichier contient un ensemble de fonctions qui nous permettent :
d'avoir une page d'accueil ou le joueur va rentrer son nom et pouvoir commencer sa partie ou la quitter.
d'avoir l'interface de jeu centrée pour jouer et une partie pour voir son score et pour redémarrer une partie.
Afficher les évènements aux flèches directionnelles.
Avoir une fenetre de fin avec l'affichage d'un tableau avec le score du joueur et sa position sur le classement des meilleurs scores.

Github_push.py
Ce fichier contient des fonctions qui vont nous permettre de sauvegarder les scores des différents joueurs et de pouvoir faire directement un push vers notre répertoire github.

-----main.py
C'est le fichier principal à exécuter pour tester le jeu.

-----requirements.txt 
Contient toutes les librairies et modules à installer pour faire marcher le code.

7°) Auteurs
----------------------------------------------------------------------------
Elyes Laiche ---- DE2
Eugène Pascal Yaro ------DE2

8°) Documentation pour le projet
---------------------------------------------------------------------------

https://openclassrooms.com/forum/sujet/projet-snake-avec-python3
https://codes-sources.commentcamarche.net/source/51022-jeu-du-serpent-snake
http://tableauxmaths.fr/spip/spip.php?article191
https://github.com/MelissaDaCosta/Snake-en-Python/blob/master/Projet%20ISN/Snake.py
http://silanus.fr/nsi/premiere/snake/snake.html
https://docs.python.org/3/library/index.html

