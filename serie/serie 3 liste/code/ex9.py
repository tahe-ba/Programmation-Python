'''
program to find the list of words that are longer than n
from a givenlist of words.
'''
li = []
li = [item for item in input("Enter the words seperated by space: ").split()] 

print (li)
n=int(input("longueur de mot "))

lw = []
for i in range(len(li)):
    if len(li[i]) > n :
        lw.append(li[i])
print (lw)