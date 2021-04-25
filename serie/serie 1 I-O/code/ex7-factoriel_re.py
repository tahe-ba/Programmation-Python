# Find factorial of a specified number 
# Method recursive
def factoriel(n):  
   if n == 1 or n == 0:  
       n=1
       return n
   else:  
       return n*factoriel(n-1)  
while True :
    try :
        x=int(input("x: "))
        if x >= 0 :
            print("le factoriel de",x,"est",factoriel(x))
            break
        else :
            print("Wrong input .. x < 0 ")  
    except ValueError:
        print("Wrong input")
