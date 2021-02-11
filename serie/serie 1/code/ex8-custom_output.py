#Function that takes x and returns x+2 and x**3
def function(x):
    x=x+2
    return (x,x**3)

while True :
    try :
        n=float(input("Donner un nombre n: "))
        break
    except ValueError:
        print("Wrong input")

a,b=function(n)
print("n vaut : "+str(format(a, ".2f"))+" et n^3 vaut "+str(format(b, ".3f")))