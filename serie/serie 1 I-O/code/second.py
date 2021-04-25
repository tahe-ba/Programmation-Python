# Find how many numbers are even and how many are odd in a sequenece of inputs without arrays
while True :
        try :
            n=int(input("combien d'entier vous aller entrer: "))
            break
        except ValueError:
            print("Wrong input")
j=z=0
for i in range(n):
    while True :
        try :
            x=int(input("saisir le "+str(i+1)+"° nombre: "))
            if (x%2==0) :
                j=j+1
            else :
                z=z+1
            break
        except ValueError:
            print("Wrong input")
print("Il y a "+str(j)+" nombre pair")
print("Il y a "+str(z)+" nombre impair")
