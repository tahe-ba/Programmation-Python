from random import randrange
from math import ceil
from os import system, name

def clear(): 
    #windows
    if name == 'nt': 
        _ = system('cls') 
    #mac linux posix
    else: 
        _ = system('clear') 

def color(n):
    if n % 2 == 0:
        couleur = "noir"
    else:
        couleur = "rouge"
    return couleur

chances = 1000  # le domaine du randrange
i = 1  # combien de tour
wallet = 1000  # argent du depart
continuer_partie = True  # pourquoi continuer a jouer

while continuer_partie:
    clear()
    print("\n\tTour(", i, ")", "\t\t" + str(wallet) + "$")
    i += 1

    #input bet
    bet = -1
    while bet < 0 or bet > chances:tround
        try:
            bet = int(
                input(
                    "\nChoisissez un nombre sur lequel vous voulez miser [0 .. "
                    + str(chances)
                    + "] : "
                )
            )
            if bet >= 0 and bet <= chances:
                break
            else:
                print("Nombre incorrect")
        except ValueError:
            print("Aucun nombre saisie")
            bet = -1
            continue
    # print (bet)

    #input mise
    mise = 0
    while mise <= 0 or mise > wallet:
        try:
            mise = int(input("Tapez le montant de votre mise : "))
            if mise > wallet:
                print("Mise impossible vous n'avez que ", wallet)
                continue
            if mise > 0 and mise <= wallet:
                break
            else:
                print("mise impossible")
        except ValueError:
            print("Aucun nombre saisie")
            mise = -1
            continue
    # print(mise)

    #roulette pick number
    win = randrange(chances + 1)
    print(
        "\nLa roulette tourne et le numero gagnant est",
        win,
        "de couleur",
        str(color(win)),
        "\n",
    )

    #cases win and loose
    if win == bet:
        print("\nVous avez gagnez ", mise * 3)
        wallet += mise * 3
    elif win % 2 == bet % 2:
        print(
            "Vous avez misé sur la couleur",
            str(color(bet)),
            "vous obtenez ",
            mise * 0.5,
        )
        wallet += mise * 0.5
        wallet = ceil(wallet)
    else:
        print("vous perdez votre mise.")
        wallet -= mise
    # print(wallet)

    #when to quit
    if wallet <= 0:
        print("poche vide")
        continuer_partie = False
    else:
        quitter = input(
            "vous avez "
            + str(wallet)
            + " dans vos poche\n\nSi vous voulez quitter tapez o : "
        )
        if quitter == "o" or quitter == "O":
            print("Vous quittez avec vos gains.", wallet)
            continuer_partie = False
