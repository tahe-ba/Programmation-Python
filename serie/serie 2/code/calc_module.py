"""
1-addition
2-soustraction
3-quitter
"""

def main():
    menu()

def plus(a,b):
    print(a,"+",b,"=",a+b)

def moin(a,b):
    print(a,"-",b,"=",a-b)

def quit():
    pass
    # sys.exit

def menu():
    while True :
        try :
            x=int(input("Donner x: "))
            break
        except ValueError:
            print("Wrong input")
    while True :
        try :
            y=int(input("Donner y: "))
            break
        except ValueError:
            print("Wrong input")
    while True:
        try:
            choice = int(
                input(
                    """
                    1-addition
                    2-soustraction
                    3-quitter

                    Choix: """
                )
            )
            break
        except ValueError:
            print("Entrer invalide")
    if choice == 1:
        plus(x,y)
    elif choice == 2:
        moin(x,y)
    elif choice == 3:
        quit()
    else:
        print("Mauvais choix")
        print("")
        menu()
    
main()
