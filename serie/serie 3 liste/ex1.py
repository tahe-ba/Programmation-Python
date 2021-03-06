#somme de liste
li=[10, 20, 30, 40]
#methode 0
s=0
l=[10, 20, 30, 40]
for l in l:
    s=s+l
print (s)
#methode 1
si=0
for i in range(len(li)):
    si=si+li[i]
print (si)

#methode 2 predefined methode to get sum of list of integers
print (sum(li))

# recursive sum of elements in list
def sumOfList(list, size):
   if (size == 0):
     return 0
   else:
     return li[size - 1] + sumOfList(li, size - 1)
  
print(sumOfList(li, len(li)))
