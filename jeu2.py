import random

# Fonction permettant de poser une question à l'utilisateur et de s'assurer qu'il choisit une option valide
def prendre_decision(question, options):
    """
    Pose une question à l'utilisateur et s'assure qu'il choisit une option valide.
    :param question: Question posée à l'utilisateur.
    :param options: Liste des réponses valides.
    :return: Réponse validée de l'utilisateur.
    """
    decision = input(question).lower()
    while decision not in options:
        print("Action non reconnue. Veuillez choisir parmi les options suivantes: ", ", ".join(options))
        decision = input(question).lower()
    return decision

# Fonction simulant un défi avec une probabilité de réussite donnée
def lancer_defi(proba_reussite, succes_msg, echec_msg):
    """
    Simule un défi basé sur un tirage aléatoire.
    :param proba_reussite: Probabilité de réussite sur une échelle de 1 à 10.
    :param succes_msg: Message affiché en cas de succès.
    :param echec_msg: Message affiché en cas d'échec.
    :return: True si le défi est réussi, False sinon.
    """
    if random.randint(1, 10) <= proba_reussite:  # Génère un nombre aléatoire entre 1 et 10
        print(succes_msg)  # Succès du défi
        return True
    else:
        print(echec_msg)  # Échec du défi
        return False

# Fonction principale gérant l'aventure textuelle
def aventure():
    """
    Gère le déroulement de l'aventure textuelle interactive.
    """
    print("========================================")
    print("Bienvenue dans cette aventure textuelle !")
    print("========================================\n")

    # Premier choix : sélection du chemin
    chemin = prendre_decision(
        "Vous arrivez à une bifurcation dans la forêt. Choisissez votre chemin ('gauche' ou 'droite'): ",
        ['gauche', 'droite']
    )

    # Déroulement selon le choix de l'utilisateur
    if chemin == "gauche":
        print("\nVous avez choisi le chemin de gauche, bordé par de vieux arbres majestueux.")

        # Choix de traverser ou non la rivière
        decision_riviere = prendre_decision(
            "Au détour du chemin, vous arrivez à une rivière scintillante. Voulez-vous 'traverser' en nageant ou 'suivre' la rive pour trouver un pont? ",
            ['traverser', 'suivre']
        )

        if decision_riviere == "traverser":
            lancer_defi(7, "Vous traversez la rivière avec succès malgré le courant.", 
                        "Le courant est trop fort ! Vous perdez un peu de temps à regagner la rive en titubant.")
        else:
            print("\nVous suivez prudemment la rive et découvrez un vieux pont en pierre qui vous permet de traverser en toute sécurité.")

    else:  # Si l'utilisateur a choisi le chemin de droite
        print("\nVous avez choisi le chemin de droite, dans l'ombre dense des arbres.")

        # Rencontre avec un animal sauvage
        decision_animal = prendre_decision(
            "Soudain, un grognement retentit et un animal sauvage apparaît. Voulez-vous vous 'cacher' derrière un buisson ou 'combattre' l'animal? ",
            ['cacher', 'combattre']
        )

        if decision_animal == "cacher":
            print("\nVous vous faufilez derrière un buisson. L'animal, intrigué, passe sans vous remarquer.")
        else:
            lancer_defi(6, "Votre habileté vous permet de vaincre l'animal, qui s'enfuit en grognant.", 
                        "L'animal se révèle plus redoutable que prévu. Vous subissez quelques blessures, mais parvenez à le repousser.")

    # Découverte de la grotte
    print("\nAprès plusieurs heures de marche, vous découvrez enfin une grotte énigmatique, cachée sous la liane d'un grand arbre.")

    # Choix d'entrer ou non dans la grotte
    decision_grotte = prendre_decision(
        "Voulez-vous 'entrer' dans la grotte ou 'contourner' l'endroit pour explorer les environs? ",
        ['entrer', 'contourner']
    )

    tresor = False  # Variable indiquant si l'utilisateur a trouvé un trésor

    if decision_grotte == "entrer":
        print("\nVous décidez d'entrer dans la grotte. L'air est frais et l'obscurité vous enveloppe.")

        # Choix du passage dans la grotte
        decision_in_grotte = prendre_decision(
            "À l'intérieur, vous trouvez deux passages: l'un mène vers une zone éclairée ('lumière'), l'autre plonge dans l'obscurité ('ombre'). Que choisissez-vous? ",
            ['lumière', 'ombre']
        )

        if decision_in_grotte == "lumière":
            print("\nVous suivez le passage illuminé et découvrez une salle secrète remplie de coffres et de bijoux scintillants.")
            tresor = True  # Trésor trouvé

        else:  # Rencontre avec un gardien
            gardien = prendre_decision(
                "Le gardien vous observe. Voulez-vous essayer de 'parler' pour négocier ou 'attaquer' pour forcer le passage? ",
                ['parler', 'attaquer']
            )

            if gardien == "parler":
                print("\nVotre sincérité et vos bonnes manières impressionnent le gardien.")
                if chemin in ["gauche", "droite"]:
                    print("Le gardien vous accorde l'accès au trésor en vous conseillant une relique ancestrale.")
                    tresor = True
                else:
                    print("Malheureusement, votre parcours hésitant ne convainc pas le gardien. Vous quittez la grotte bredouille.")

            else:  # Tentative d'affrontement du gardien avec l'utilisation de lancer_defi
                tresor = lancer_defi(4, "Après un combat acharné, vous triomphez du gardien et découvrez le trésor caché derrière lui.", 
                                     "Le gardien est trop puissant et vous blesse grièvement. Vous devez fuir la grotte, le trésor restant hors de portée.")

    else:  # Exploration des environs à la place de la grotte
        print("\nVous choisissez de contourner la grotte. En explorant les environs, vous trouvez un vieux parchemin attaché à une branche.")
        print("Le parchemin décrit l'emplacement d'un trésor, mais comporte une énigme à résoudre.")

        # Résolution de l'énigme
        enigme = prendre_decision(
            "Enigme : 'Je suis léger comme une plume, mais même le plus fort des hommes ne peut me tenir plus de 5 minutes. Qui suis-je?' Tapez votre réponse: ",
            ['la respiration', 'respiration']
        )

        if enigme in ["la respiration", "respiration"]:
            print("\nBravo ! Vous avez résolu l'énigme. Le parchemin révèle l'emplacement d'un petit coffre enterré sous un vieux chêne.")
            tresor = lancer_defi(6, "En creusant sous le chêne, vous découvrez un coffre rempli de pièces d'or et de bijoux rares!", 
                                 "Malheureusement, le coffre est vide. La légende du trésor reste un mystère pour vous.")
        else:
            print("\nVotre réponse n'est pas correcte. Le parchemin se déchire et le secret du trésor reste à jamais perdu.")

    # Conclusion de l'aventure
    print("\n========================================")
    if tresor:
        print("Félicitations ! Vous avez trouvé le trésor et terminé votre aventure avec succès.")
    else:
        print("Votre aventure s'achève sans trésor")
    print("========================================")
    print("Merci d'avoir joué à cette aventure.")

# Exécution du jeu si ce script est exécuté directement
if __name__ == "__main__":
    aventure()