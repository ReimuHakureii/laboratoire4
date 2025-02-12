import random

# Fonction permettant de poser une question à l'utilisateur et de s'assurer qu'il choisit une option valide
def prendre_decision(question, options):
    """
    Pose une question à l'utilisateur et s'assure qu'il choisit une option valide.
    :param question: Question posée à l'utilisateur.
    :param options: Liste des réponses valides.
    :return: Réponse validée de l'utilisateur.
    """
    decision = input(question).lower().strip()
    while decision not in options:
        print("Action non reconnue. Veuillez choisir parmi les options suivantes: ", ", ".join(options))
        decision = input(question).lower().strip()
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

# Nouveau système de combat utilisant une boucle while (pour les rounds) et deux boucles for (pour simuler les attaques)
def combat(nom_adversaire, points_vie_adversaire, points_vie_joueur):
    print(f"\n*** Le combat contre {nom_adversaire} commence ! ***")
    round_number = 1
    # Boucle while principale du combat
    while points_vie_adversaire > 0 and points_vie_joueur > 0:
        print(f"\n--- Round {round_number} ---")
        
        # Attaque du joueur : il dispose de 3 frappes par round
        total_degats = 0
        for frappe in range(3):
            degats = random.randint(1, 3)
            total_degats += degats
            print(f"Votre frappe {frappe + 1} inflige {degats} points de dégâts.")
        points_vie_adversaire -= total_degats
        if points_vie_adversaire <= 0:
            print(f"\nVous avez vaincu {nom_adversaire} !")
            break
        else:
            print(f"{nom_adversaire} a encore {points_vie_adversaire} points de vie.")

        # Attaque de l'adversaire : il attaque 2 fois par round
        total_degats_adversaire = 0
        for attaque in range(2):
            degats = random.randint(1, 4)
            total_degats_adversaire += degats
            print(f"{nom_adversaire} attaque {attaque + 1} et vous inflige {degats} points de dégâts.")
        points_vie_joueur -= total_degats_adversaire
        if points_vie_joueur <= 0:
            print("\nVous avez été vaincu par votre adversaire...")
            break
        else:
            print(f"Il vous reste {points_vie_joueur} points de vie.")
        round_number += 1
    return points_vie_joueur > 0

# Fonction principale gérant l'aventure textuelle
def aventure():
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

    else:  # Chemin droit
        print("\nVous avez choisi le chemin de droite, dans l'ombre dense des arbres.")

        # Rencontre avec un animal sauvage
        decision_animal = prendre_decision(
            "Soudain, un grognement retentit et un animal sauvage apparaît. Voulez-vous vous 'cacher' derrière un buisson ou 'combattre' l'animal? ",
            ['cacher', 'combattre']
        )

        if decision_animal == "cacher":
            print("\nVous vous faufilez derrière un buisson. L'animal, intrigué, passe sans vous remarquer.")
        else:
            print("\nVous décidez d'affronter l'animal sauvage !")
            # Utilisation du système de combat
            if not combat("Animal Sauvage", points_vie_adversaire=10, points_vie_joueur=15):
                print("Trop blessé pour continuer votre aventure...")
                return  # Fin de l'aventure si le joueur est vaincu

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
                print("Il vous confie l'accès au trésor en vous recommandant une relique ancestrale.")
                tresor = True
            else:
                print("\nVous engagez un combat contre le gardien !")
                # Combat contre le gardien via notre système de combat
                tresor = combat("Gardien de la Grotte", points_vie_adversaire=12, points_vie_joueur=15)
                if not tresor:
                    print("Le gardien est trop puissant et vous blesse grièvement. Le trésor reste hors de portée.")

    else:  # Exploration des environs
        print("\nVous choisissez de contourner la grotte. En explorant les environs, vous trouvez un vieux parchemin attaché à une branche.")
        print("Le parchemin décrit l'emplacement d'un trésor, mais comporte une énigme à résoudre.")

        # Mini-jeu d'énigme avec plusieurs tentatives
        attempts = 0
        solved = False
        # Boucle while pour permettre jusqu'à 3 tentatives
        while attempts < 3 and not solved:
            reponse = input("Enigme : 'Je suis léger comme une plume, mais même le plus fort des hommes ne peut me tenir plus de 5 minutes. Qui suis-je?' Tapez votre réponse: ").lower().strip()
            # Si aucune réponse n'est donnée, on recommence l'itération
            if not reponse:
                print("Vous n'avez rien saisi. Veuillez entrer une réponse.")
                continue  # Passe directement à l'itération suivante
            if reponse in ["la respiration", "respiration"]:
                solved = True
                break
            else:
                attempts += 1
                print("Réponse incorrecte. Essayez encore.")
        if solved:
            print("\nBravo ! Vous avez résolu l'énigme. Le parchemin révèle l'emplacement d'un coffre.")
            tresor = lancer_defi(6, "En creusant sous le vieux chêne, vous découvrez un coffre rempli de pièces d'or et de bijoux rares !", 
                                 "Malheureusement, en creusant, vous ne trouvez rien d'intéressant.")
        else:
            print("\nVous n'avez pas réussi à résoudre l'énigme. Le secret du trésor reste à jamais perdu.")

    # Conclusion de l'aventure
    print("\n========================================")
    if tresor:
        print("Félicitations ! Vous avez trouvé le trésor et terminé votre aventure avec succès.")
    else:
        print("Votre aventure s'achève sans trésor.")
    print("========================================")
    print("Merci d'avoir joué à cette aventure.")

# Capacité à rejouer l'aventure
def main():
    play_again = True
    while play_again:
        aventure()
        rejouer = input("Voulez-vous rejouer l'aventure ? (oui/non) : ").lower().strip()
        if rejouer not in ["oui", "o"]:
            play_again = False
            print("Au revoir!")
# Exécution du jeu si ce script est exécuté directement
if __name__ == "__main__":
    main()