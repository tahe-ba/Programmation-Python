'''
program to print the numbers of a specified list
after removing evennumbers from it.
'''
li = [1,2,3,4,5,6,7,8,9]
i=0
m=len(li)
while i<m:
    if (li[i]%2) == 0 :
        li.pop(i)
        m=len(li)
    i+=1
print (li)
'''
li = [x for x in li if x%2!=0]
print (li)
'''
