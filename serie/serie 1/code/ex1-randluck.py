#choose a number and see if it's picked between randomized numbers
import random
from datetime import date
d=date.today()
print(d.strftime("   %d, %B %Y"))
exit = 'F'
while exit != 'T' and exit != 't' :
    l = random.sample(range(1,20), 10)
    while True :
            try :
                x=int(input("I am lucky tozday ? :"))
                if x<20 and x>0 :
                    if (x in l): 
                        print ("\n==========> Lucky you <==========\n") 
                    else :
                        print ("\n-------§ Maybe next time §-------\n")
                    print("These are meant to be your wining numbers")
                    print (l)
                    break
                else :
                    print("Wrong input .. Please choose a number between 1 and 20")  
            except ValueError:
                print("Wrong input")
    exit=input("\nIf you want tou quit type T/t: ")
