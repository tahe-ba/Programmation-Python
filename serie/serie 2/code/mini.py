from random import randrange
i=1
wallet = 1000 
continuer_partie = True 

print("Vous commencez avec ", wallet)

while continuer_partie: 
    i+=1
    bet = -1
    while bet < 0 or bet > 999: 
        try: 
            bet = int(input("\nChoisissez un nombre sur lequel vous voulez miser (entre 0 et 999) : "))
        except ValueError: 
            print("Aucun nombre saisie")
            bet = -1
            continue
        if bet < 0: 
            print("Ce nombre est négatif")
        if bet > 999: 
            print("Ce nombre est supérieur à 999")

    mise = 0
    while mise <= 0 or mise > wallet: 
        try: 
            mise = int(input("Tapez le montant de votre mise : "))
        except ValueError: 
            print("Vous n'avez pas saisi de nombre")
            mise = -1
            continue
        if mise <= 0: 
            print("La mise saisie est négative ou nulle.")
        if mise > wallet: 
            print("Vous ne pouvez miser autant, vous n'avez que ", wallet)
    
    win = randrange(999)
    print("\n La roulette tourne le numero gagnant est ", win,"\n")
    if win == bet: 
        print("Félicitations vous avez gagnez ", mise * 3)
        wallet += mise * 3
    elif win % 2 == bet % 2:
        mise +=mise * 0.5
        print("Vous avez misé sur la bonne couleur. Vous obtenez ", mise)
        wallet += mise
    else: 
        print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
        wallet -= mise

    if wallet <= 0: 
        print("Vous êtes ruiné ! C'est la fin de la partie.")
        continuer_partie = False
    else: 
        print("\nVous avez à présent ", wallet)

        quitter = input("Si vous voulez quitter tapez o : ")
        if quitter == "o" or quitter == "O": 
                print("Vous quittez le casino avec vos gains.",wallet)
                continuer_partie = False
        else :
            print("\n#### round ",i," ####")
