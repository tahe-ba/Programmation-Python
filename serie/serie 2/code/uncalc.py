"""
1-addition
2-soustraction
3-quitter
"""

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
    print(x,"+",y,"=",x+y)
elif choice == 2:
    print(x,"-",y,"=",x-y)
elif choice == 3:
    pass
else:
    print("Mauvais choix")
    print("")
