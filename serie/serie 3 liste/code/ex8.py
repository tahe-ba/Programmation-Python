#program that clone or copy a list
l = [3, 3, 2, 1, 5, 1, 4, 2, 3]

#list methode
l1 = list(l) 

#slicing methode
l2 = l[:] 

#extend methode
l3 = [] 
l3.extend(l) 

#copy methode
l4 = l.copy()

#list comprehension methode
l5 = [i for i in l] 

print (l)
print (l1)
print (l2)
print (l3)
print (l4)
print (l5)