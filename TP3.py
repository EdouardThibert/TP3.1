"""
Édouard Thibert
TP3
Faire un combat de monstre
"""
import random
import time
point_de_vie = 20
force_ennemi = random.randint(1, 5)

play_game = True
while play_game:
    print("Vous tombez face a face avec un ennemi de niveau", force_ennemi,)
    choix_premiere_porte = int(input("Que voulez vous faire\n"
                                     "1 - L'attaquer\n"
                                     "2 - Le contourner et aller ouvrir une porte\n"
                                     "3 - Afficher les règles du jeu\n"
                                     "4 - Quitter la partie\n"))
    if choix_premiere_porte == 1:
        attaque = random.randint(1, 6)
        if attaque <= 4:
            print("Vous avez roulé", attaque, "et vous vous êtes fait battre,")
            point_de_vie = point_de_vie - 4
            print("Vous avez Maintenant", point_de_vie, "point de vie\n")
            time.sleep(1)
        if attaque >= 5:
            print("Vous avez roulé", attaque, "et vous avez battu l'ennemi")
            point_de_vie = point_de_vie + 4
            print("Vous avez Maintenant", point_de_vie,  "point de vie\n")
            time.sleep(1)