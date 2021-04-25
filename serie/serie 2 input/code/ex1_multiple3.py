# Find how many times a numbber is devided by 2
import random
from datetime import date
d=date.today()
print(20*"\t",d.strftime("%d, %B %Y"))
while True :
    try :
        x=int(input("Donner un nombre: "))
        break
    except ValueError:
        print("Wrong input")

if x%2==0 :
    print("Ce nombre est pair")
elif x%3==0 :
    print("Ce nombre est impair, mais est multiple de 3")
else :
    print("Ce nombre n’est ni pair ni multiple de 3")