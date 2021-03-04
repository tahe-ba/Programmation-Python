from random import randrange
from math import ceil

def color (n):
    if n%2 == 0 :
        couleur="noir"
    else :
        couleur="rouge"
    return couleur

def same_color(n,m):
    if (n%2==0 and m%2==0 ) or (n%2!=0 and m%2!=0 ):
        return True
    else :
        return False

i=1
wallet = 1000 
continuer_partie = True 

while continuer_partie :
    print("\n####round(",i,")####")
    i+=1
    print("vous avez "+str(wallet)+" dans vos poche")

    bet = -1
    while bet == -1: 
        try:  
            bet = int(input("\nChoisissez un nombre sur lequel vous voulez miser [0 .. 999] : "))
            if bet >= 0 and bet <= 999 :
                break
            else :
                print("Nombre incorrect") 
        except ValueError: 
            print("Aucun nombre saisie")
            bet=-1
            continue 
    #print (bet)

    mise = 0
    while mise <= 0 or mise > wallet: 
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
            mise=-1
            continue
    #print(mise)

    win = randrange(999)
    print("\nLa roulette tourne et le numero gagnant est", win,"de couleur",str(color(win)),"\n")

    if win == bet: 
        print("\nVous avez gagnez ", mise * 3)
        wallet += mise * 3
    elif same_color(win,bet):
        print("Vous avez misé sur la couleur",str(color(bet)),"vous obtenez ", mise * 0.5)
        wallet += mise * 0.5
        wallet=ceil(wallet)
    else: 
        print("vous perdez votre mise.")
        wallet -= mise
    #print(wallet)

    if wallet <= 0: 
        print("poche vide")
        continuer_partie = False
    else :
        quitter = input("il vous reste "+str(wallet)+"\n\nSi vous voulez quitter tapez o : ")
        if quitter == "o" or quitter == "O": 
                print("Vous quittez avec vos gains.",wallet)
                continuer_partie = False