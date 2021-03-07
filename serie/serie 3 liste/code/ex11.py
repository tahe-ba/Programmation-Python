'''
program to print a specified list after removing 
the 0th, 4th and 5th lements
'''
def del_i(li):
    n=0
    while True :
        x=int(input("indice a supprimer "))
        li.pop(x-n)
        n+=1
        cc=(input("press 0 to stop "))
        if cc == '0' :
            break

l=[1,2,3,4,5,6,8]
#  0,1,2,3,4,5,6

# li.pop(0)
# li.pop(4-1)
# li.pop(5-2)

del_i(l)
print (l)