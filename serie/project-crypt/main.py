'''
1-codage
    coder en base 64
    decoder en base64
    retour au menu principal
      principe
        Take the ASCII value of each character in the string
        Calculate the 8-bit binary equivalent of the ASCII values
        Convert the 8-bit chunks into chunks of 6 bits by simply re-grouping the digits
        Convert the 6-bit binary groups to their respective decimal values.
        Using a base64 encoding table, assign the respective base64 character for each decimal value.
2-chiffrement
    chiffrer par un decalage dun clef
    dechiffrement par un decalage dun clef
    retour au menu principal
      principe
        take a string 
        each letter will be replaced with the n_th letter after it exemple a -> d , aaa -> ddd for n=3 
        all characters other than letters are kept the same
3-quitter
'''
from os import system, name
import base64
    
def clear():
    #windows
    if name == 'nt': 
        _ = system('cls') 
    #mac linux posix
    else: 
        _ = system('clear')    

def main():
    menu()

def code64():
    print('''
 +-+-+-+-+-+-+ +-+-+
 |c|o|d|a|g|e| |6|4|
 +-+-+-+-+-+-+ +-+-+
 ''')
    msg = input("Message à encoder: ")
    msg_bytes = msg.encode('ascii')
    base64_bytes = base64.b64encode(msg_bytes)
    coded = base64_bytes.decode('ascii')
    print("\nMessage codé:",coded)

    codage()

def decode64():
    print('''
 +-+-+-+-+-+-+-+-+ +-+-+
 |d|e|c|o|d|a|g|e| |6|4|
 +-+-+-+-+-+-+-+-+ +-+-+
 ''')
    msg = input("Message à decoder: ")
    base64_bytes = msg.encode('ascii')
    msg_bytes = base64.b64decode(base64_bytes)
    decoded = msg_bytes.decode('ascii')
    print("\nMessage décodé:",decoded)
    codage()

def codage():
    print(''' \t+-+-+-+-+-+-+
 \t|c|o|d|a|g|e|
 \t+-+-+-+-+-+-+''')
    while True:
        try:
            choice = int(
                input(
                    """
    1-Codage en base 64
    2-Decodage en base 64
    3-Retour au menu principal

  Choix: """
                )
            )
            break
        except ValueError:
            print("Entrer invalide")
    if choice == 1:
        code64()
    elif choice == 2:
        decode64()
    elif choice == 3:
        menu()
    else:
        print("Mauvais choix")
        print("")
        codage()

def clef() :
    while True :
        try :
            x=int(input("Donner la clef entre 30 et 1000: "))
            if x>=30 and x<=1000:
                break
            else :
                print("Clef non valide")
        except ValueError:
            print("Wrong input")
    return (x)

def chiffrer_letter(letter, is_upper,decaler):
    if is_upper:
        l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    else:
        l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return l[l.index(letter)+(decaler%26)]

    
def dechiffrer_letter(letter, is_upper,decaler):
    if is_upper:
        l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    else:
        l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return l[l.index(letter)-(decaler%26)]

def chiffrement():
    print('''
 +-+-+-+-+-+-+-+-+
 |c|h|i|f|f|r|e|r|
 +-+-+-+-+-+-+-+-+
 ''')
    c=clef()
    msg=input("Message à chiffrer: ")
    crypted=list()
    for letter in msg :
        if letter.isalpha() :
            up= letter.isupper()
            crypted_letter=chiffrer_letter(letter,up,c)
            crypted.append(crypted_letter)
        else :
            crypted.append(letter)
    crypted=''.join(crypted)
    print ("\nMessage chiffré:",crypted)
    chiffrer()

def dechiffrement():
    print('''
 +-+-+-+-+-+-+-+-+-+-+
 |d|e|c|h|i|f|f|r|e|r|
 +-+-+-+-+-+-+-+-+-+-+
 ''')
    c=clef()
    msg=input("Message à dechiffrer: ")
    decrypted=list()
    for letter in msg :
        if letter.isalpha() :
            up= letter.isupper()
            decrypted_letter=dechiffrer_letter(letter,up,c)
            decrypted.append(decrypted_letter)
        else :
            decrypted.append(letter)
    decrypted=''.join(decrypted)
    print ("\nMessage déchiffré:",decrypted)
    chiffrer()

def chiffrer():
    print('''
 \t+-+-+-+-+-+-+-+-+-+-+-+
 \t|C|H|I|F|F|R|E|M|E|N|T|
 \t+-+-+-+-+-+-+-+-+-+-+-+''')
    while True:
        try:
            choice = int(
                input(
                    """
   1-Chiffrer un message par une clef
   2-Dechiffrer un message par une clef
   3-Retour au menu principal

 Choix: """
                )
            )
            break
        except ValueError:
            print("Entrer invalide")
    if choice == 1:
        chiffrement()
    elif choice == 2:
        dechiffrement()
    elif choice == 3:
        menu()
    else:
        print("Mauvais choix")
        print("")
        codage()

def quit():
    sure=input("\n\t Si vous voulez quitter tapez 'o' : ")
    if sure == 'o' or sure == 'O' :
        pass
    else :
        menu()
    # sys.exit

def menu():
    clear()
    print ("""  +-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+-+
  |O|u|t|i|l| |d|e| |c|o|d|a|g|e| |e|t| |c|h|i|f|f|r|e|m|e|n|t|
  +-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+-+""")
    while True:
        try:
            choice = int(
                input(
                    """
                        1-Codage
                        2-Chiffrement
                        3-Quitter

                        Choix: """
                )
            )
            break
        except ValueError:
            print("Entrer invalide")
    if choice == 1:
        codage()
    elif choice == 2:
        chiffrer()
    elif choice == 3:
        quit()
    else:
        print("Mauvais choix")
        print("")
        menu()
    
main()