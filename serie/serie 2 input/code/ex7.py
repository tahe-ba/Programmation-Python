"""
1 :Nouvelle partie => On commence tte suite 
2 : Recharger la partie => la partie se recharge .....
3 : Quitter => quitte le programme avec "pass"
"""


def main():
    menu()


def menu():
    print("### MAIN MENU ###")
    while True:
        try:
            choice = int(
                input(
                    """
                      1:Nouvelle Partie
                      2:Recharger la partie
                      3:Quitter

                      Choix: """
                )
            )
            break
        except ValueError:
            print("no")
    if choice == 1:
        New()
    elif choice == 2:
        Reload()
    elif choice == 3:
        quit()
    else:
        print("Mauvais choix")
        print("")
        menu()


def New():
    print("On commence tte suite ")
    pass


def Reload():
    print("la partie se recharge")
    pass


def quit():
    pass
    # sys.exit


main()
