#Modifications pour version 2.0 du jeu
"""
1- importations et entrées :
module time pour temporisations dans le jeu.
prendre_decision + .strip() pour détruire les espaces inutiles.

2- système combat :
nouvelle fonction combat.
boucle while pour rounds & boucles for pour les attaques.
time.sleep ajoutées pour améliorer l'immersion et empêcher le spam de texte.

3- fonction aventure :
quand animal sauvage est rencontré et que utilisateur choisit "combattre" -> "combat" est en action à la place de l'ancien lancer_defi.
même chose pour le gardien de la grotte, mais avec un message modifié et accès au trésor.
pour énigme: 3 tentatives pour résoudre l'énigme, sinon message d'échec.
si la réponse est correcte lancer_defi sinon échec et fin de l'aventure.

4- possibilité de rejouer au jeu sans avoir à relancer le programme :
main encapsule aventure dans une boucle while pour permettre au joueur de rejouer.
après la fin de l'aventure, le joueur est invité à rejouer ou quitter.
"""
