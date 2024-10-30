import random
import os


def lancer_des():
    return random.randint(1, 6), random.randint(1, 6)


def calculer_points(devine, total):
    difference = abs(devine - total)
    if difference == 0:
        return 10
    elif difference <= 2:
        return 5
    elif difference <= 4:
        return 2
    return 0


def sauvegarder_meilleur_score(score_total):
    fichier_score = "meilleur_score.txt"

    # Lire le meilleur score actuel
    meilleur_score = 0
    if os.path.exists(fichier_score):
        with open(fichier_score, "r") as file:
            meilleur_score = int(file.read().strip())

    # Vérifier si le score actuel est supérieur au meilleur score
    if score_total > meilleur_score:
        with open(fichier_score, "w") as file:
            file.write(str(score_total))
        print(f"Nouveau record ! Meilleur score sauvegardé : {score_total} points 🎉")
    else:
        print(f"Meilleur score actuel : {meilleur_score} points")


def jeu():
    print("Bienvenue dans le jeu de lancer de dés !")
    print("Devine le total des deux dés (entre 2 et 12)")
    print("Plus tu es proche, plus tu gagnes de points !")
    print("- Résultat exact : 10 points")
    print("- Différence de 1 ou 2 : 5 points")
    print("- Différence de 3 ou 4 : 2 points")
    print("- Différence de 5 ou plus : 0 point\n")

    score_total = 0
    partie = 1
    historique = []  # Historique des parties

    while True:
        print(f"\n--- Partie {partie} ---")
        de1, de2 = lancer_des()
        total = de1 + de2

        try:
            devine = int(input("Entre ta prédiction (ou 0 pour quitter) : "))

            if devine == 0:
                break

            if devine < 2 or devine > 12:
                print("Ta prédiction doit être entre 2 et 12 !")
                continue

            points = calculer_points(devine, total)
            score_total += points

            # Stocker les détails de la partie dans l'historique
            historique.append({
                "partie": partie,
                "predicted": devine,
                "total_des": total,
                "points": points
            })

            print(f"\nDé 1 : {de1}")
            print(f"Dé 2 : {de2}")
            print(f"Total : {total}")

            if points == 10:
                print("🎉 BRAVO ! Prédiction parfaite ! +10 points")
            else:
                print(f"Tu gagnes {points} points !")

            print(f"Score total : {score_total}")
            partie += 1

        except ValueError:
            print("S'il te plaît, entre un nombre valide.")

    # Afficher le récapitulatif des parties
    print("\n--- Résumé des parties ---")
    for entry in historique:
        print(
            f"Partie {entry['partie']} : Prédiction = {entry['predicted']}, Total des dés = {entry['total_des']}, Points gagnés = {entry['points']}")

    print(f"\nPartie terminée ! Score final : {score_total} points en {partie - 1} parties.")
    if partie > 1:
        print(f"Moyenne de points par partie : {score_total / (partie - 1):.1f}")

    # Sauvegarder le meilleur score
    sauvegarder_meilleur_score(score_total)


if __name__ == "__main__":
    jeu()
