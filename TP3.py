"""
Édouard Thibert
TP3
Faire un combat de monstre
"""
import random
import time
point_de_vie = 20
victoire = 0
defaites = 0
numero_adversaire = 0
numero_combat = 0
force_ennemi = random.randint(1, 5)

play_game = True
while play_game:
    print("Vous tombez face a face avec un ennemi")
    choix_porte = int(input("Que voulez vous faire\n"
                                     "1 - L'attaquer\n"
                                     "2 - Le contourner et aller ouvrir une porte\n"
                                     "3 - Afficher les règles du jeu\n"
                                     "4 - Quitter la partie\n"))
    if choix_porte == 1: #attaquer le monstre
        numero_adversaire = numero_adversaire + 1;
        print("Ennemi: #", numero_adversaire, )
        print("Force de l'ennemi:", force_ennemi, )
        print("Niveau de vie de l'usager:", point_de_vie, )
        print("Combat #", numero_combat, ":", victoire, "victoires vs", defaites,"défaites")
        attaque = random.randint(1, 6)
        if attaque <= 4: #defaite
            print("Vous vous êtes fait battre,")
            point_de_vie = point_de_vie - 4
            defaites = defaites + 1
            print("Vous avez maintenant", point_de_vie, "point de vie\n")
            time.sleep(2)
        if attaque >= 5: #victoire
            print("Vous avez battu l'ennemi")
            point_de_vie = point_de_vie + 4;
            victoire = victoire + 1;
            print("Vous avez Maintenant", point_de_vie,  "point de vie")
            print("Vous avez maintenant", victoire, "victoire\n")
            time.sleep(2)
    if choix_porte == 2: #prendre la fuite
        print("Vous partez, mais vous avez perdu 1 point de vie et vous avez maintenant", point_de_vie,"points de vie")
        point_de_vie = point_de_vie - 1
    if choix_porte == 3:
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.\n"
              "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n"
              "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.\n"
              "Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
              "La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
              "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie\n")
        time.sleep(2)
    if choix_porte == 4: #quitter le jeu
        print("Merci et au revoir...")
        play_game = False
