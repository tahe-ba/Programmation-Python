# Find how many times a numbber is devided by 2
while True :
    try :
        x=int(input("Donner un nombre: "))
        break
    except ValueError:
        print("Wrong input")
i=0
while x%2==0 :
    x/=2
    i =i+1
print ("Le nombre"+str(x) +"se divise "+str(i)+" fois par 2")