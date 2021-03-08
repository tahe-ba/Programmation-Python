'''
Write a Python program to get a list, 
sorted in increasing order by the last element ineach tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

l=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def dernier(n): 
    return n[-1]
#print(dernier(l[0]))
#print(dernier(l))
print (l)
ls=sorted(l, key = dernier)
print (ls)

