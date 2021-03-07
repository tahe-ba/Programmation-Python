#program to generate all permutations of a list
#Sample List : [1,2,3]
# Expected Output : [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

from itertools import permutations

li=[1,2,3]
lp=list(permutations(li))
#print(type(lp))
print (lp)