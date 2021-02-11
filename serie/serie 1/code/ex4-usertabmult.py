#Tab mult of specefic number from input
exit = 'F'
while exit != 'T' and exit != 't' :
    while True :
        try :
            x=int(input("Donner un nombre: "))
            break
        except ValueError:
            print("Wrong input")
    for i in range (11) :
        print(str(x)+" * "+str(i)+" = "+str(i*x))
    exit=input("\nIf you want tou quit type T/t: ")

