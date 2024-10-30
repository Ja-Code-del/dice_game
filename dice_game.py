import random


def lancer_des():
    return random.randint(1, 6), random.randint(1, 6)


def jeu():
    print("Bienvenue dans le jeu de lancer de dés !")
    print("Devine le total des deux dés (entre 2 et 12)")

    de1, de2 = lancer_des()
    total = de1 + de2

    try:
        devine = int(input("Entre ta prédiction : "))

        if devine == total:
            print("Bravo ! Tu as deviné juste.")
        else:
            print(f"Dommage ! Le total était {total}.")
    except ValueError:
        print("S'il te plaît, entre un nombre valide.")


jeu()
