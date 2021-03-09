from os import system, name
import sys
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
    print("")
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
    print("")
    codage()

def codage():
    while True:
        print(''' 
 \t+-+-+-+-+-+-+
 \t|c|o|d|a|g|e|
 \t+-+-+-+-+-+-+''')
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
    crypted_index = (l.index(letter)+(decaler%26))%26
    return l[crypted_index]   
  
def dechiffrer_letter(letter, is_upper,decaler):
    if is_upper:
        l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    else:
        l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    decrypted_index = (l.index(letter)-(decaler%26))%26
    return l[decrypted_index]

def chiffrer():
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
    chiffrement()

def dechiffrer():
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
    chiffrement()

def chiffrement():
    while True:
        print('''
 \t+-+-+-+-+-+-+-+-+-+-+-+
 \t|C|H|I|F|F|R|E|M|E|N|T|
 \t+-+-+-+-+-+-+-+-+-+-+-+''')
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
        chiffrer()
    elif choice == 2:
        dechiffrer()
    elif choice == 3:
        menu()
    else:
        print("Mauvais choix")
        chiffrement()

def quit():
    sure=input("\n\t Si vous voulez quitter tapez 'o' : ")
    if sure == 'o' or sure == 'O' :
        sys.exit
    else :
        menu()

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
            menu()
    if choice == 1:
        codage()
    elif choice == 2:
        chiffrement()
    elif choice == 3:
        quit()
    else:
        menu()
    
main()