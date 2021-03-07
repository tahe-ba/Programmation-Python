'''
program to print the numbers of a specified list
after removing evennumbers from it.
'''
li = [1,3,6,8,10,12]
'''n=0
i=0
m=len(li)
while i<m:
    if (li[i]%2) == 0 :
        li.pop(i-n)
        n+=1
    m=len(li)
    i+=1
print (li)
'''
li = [x for x in li if x%2!=0]
print (li)
