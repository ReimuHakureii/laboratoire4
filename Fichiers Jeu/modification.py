"""
1. Importations et gestion des entrées :
Ajout de l'importation du module `time` pour introduire des temporisations dans le déroulement du jeu.
Dans la fonction `prendre_decision`, ajout de la méthode `.strip()` sur la réponse utilisateur afin d’éliminer les espaces superflus.

2. Système de combat :
Introduction d'une nouvelle fonction `combat` qui simule un affrontement entre le joueur et un adversaire.
Le système de combat utilise une boucle `while` pour gérer les rounds, ainsi que des boucles `for` pour simuler les attaques du joueur (3 frappes par round) et de l'adversaire (2 attaques par round).
Des temporisations (`time.sleep`) ont été ajoutées pour rythmer l'action et améliorer l'immersion.

3. Modifications dans la fonction `aventure` :
Dans le chemin "droite", lorsqu’un animal sauvage est rencontré et que le joueur choisit de "combattre", le système de combat (`combat`) est utilisé à la place de l'ancienne utilisation de `lancer_defi`.
Dans l'exploration de la grotte :
Pour le choix d’entrer, si le joueur se retrouve face à un gardien et choisit d’"attaquer", le combat se déroule désormais via la fonction `combat` (avec des paramètres adaptés pour le gardien) au lieu d’un simple défi.
Le choix "parler" au gardien affiche un message modifié et permet l'accès au trésor.
Pour le choix de contourner la grotte, un mini-jeu d'énigme a été intégré :
L'utilisateur dispose de jusqu'à 3 tentatives pour résoudre l'énigme.
En cas de réponse correcte, un défi est lancé avec `lancer_defi`; sinon, un message d'échec est affiché.

4. Rejouabilité :
Ajout de la fonction `main` qui encapsule l'appel à `aventure` dans une boucle permettant de rejouer l'aventure autant de fois que souhaité.
Après chaque partie, le joueur est invité à décider s'il souhaite rejouer.
"""
