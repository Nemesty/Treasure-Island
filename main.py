# Made by Nemesty
import os

game_banner = ''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''
dont_stop = True

while dont_stop:
    print(game_banner)
    print("L'Île Au Trésors !!")
    
    begin = input("Voulez-vous commencer l'aventure (o/n) ?: ").lower()
    match begin:
        case "o":
            os.system("clear")
            print("L'aventure peut commencer...\n")
            print("Vous vous trouver à un croissement.")
            road_direction = input("Où souhaitez vous vous rendre (gauche/droite) ?: ").lower()
            match road_direction:
                case "gauche":
                    print("Vous arrivez en face d'un lac")
                    get_through = input("Voulez-vous traverser le lac ou bien le contourner (traverser/contourner) ?: ").lower()
                    match get_through:
                        case "traverser":
                            print("Vous avez fait preuve de courage !")
                            print("La traverser se passe sans encombre.")
                            print("Vous venez de trouver le trésors !!\n")

                            print("Vous avez gagné !")
                            print("Fin du jeu")

                            try_again = input("Voulez-vous recommancer (o/n): ").lower()
                            if try_again == "o":
                                continue
                            else:
                                print("Au revoir !")
                                break
                        case "contourner":
                            print("Vous avez fait preuve de lacheter")
                            print("Vous vous faite ratraper par les démons qui vous poursuivais\n")
                            print("Vous être mort !")

                            try_again = input("Voulez-vous recommancer (o/n): ").lower()
                            if try_again == "o":
                                continue
                            else:
                                print("Au revoir !")
                                break
                case "droite":
                    print("BING ! Vous recevez un grand coup de marteau !")
                    print("Vous êtes mort...")
                    try_again = input("Voulez-vous recommancer (o/n): ").lower()
                    if try_again == "o":
                        continue
                    else:
                        print("Au revoir !")
                        break
        case "n":
            print("Au revoir !")
            break
        case _:
            print("Erreur : o ou n attendu")
