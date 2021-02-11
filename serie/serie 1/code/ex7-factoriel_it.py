# Find factorial of a specified number 
# Method iterative
while True :
    try :
        x=int(input("x: "))
        if x >= 0 :
            n=1
            for i in range(1,x+1):
                n=n*i
            print("le factoriel de",x,"est",n)
            break
        else :
            print("Wrong input .. x < 0 ")  
    except ValueError:
        print("Wrong input")

#print("Le factoriel de "+str(x)+" est "+str(n))