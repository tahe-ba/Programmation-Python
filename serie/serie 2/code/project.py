from random import randrange
from math import ceil

i=1
wallet = 1000 
continuer_partie = True 

while continuer_partie :
    print("\n####round(",i,")####")
    i+=1
    print("vous avez "+str(wallet)+" dans vos poche")
    while True: 
        try:  
            bet = int(input("\nChoisissez un nombre sur lequel vous voulez miser [0 .. 999] : "))
            if bet >= 0 and bet <= 999 :
                break
            else :
                print("Nombre incorrect") 
        except ValueError: 
            print("Aucun nombre saisie")   
            continue 
    #print (bet)

    while True: 
        try: 
            mise = int(input("Tapez le montant de votre mise : "))
            if mise > wallet: 
                print("Mise impossible vous n'avez que ", wallet)
                continue
            if mise > 0 and mise <= wallet :
                break
            else:
                print("mise impossible")
        except ValueError: 
            print("Aucun nombre saisie")
            continue
    #print(mise)

    win = randrange(999)
    print("\nLa roulette tourne et le numero gagnant est ", win,"\n")

    if win%2 == 0 :
        win_c="noir"
    else :
        win_c="rouge"

    if win == bet: 
        print("\nVous avez gagnez ", mise * 3)
        wallet += mise * 3
    elif win % 2 == bet % 2:
        print("Vous avez misé sur la couleur "+ win_c +" vous obtenez ", mise * 0.5)
        wallet += mise * 0.5
        wallet=ceil(wallet)
    else: 
        print("vous perdez votre mise.")
        wallet -= mise
    #print(wallet)

    if wallet <= 0: 
        print("poche vide vous avez perdu")
        continuer_partie = False
    else :
        quitter = input("il vous reste "+str(wallet)+"\n\nSi vous voulez quitter tapez o : ")
        if quitter == "o" or quitter == "O": 
                print("Vous quittez avec vos gains.",wallet)
                continuer_partie = False