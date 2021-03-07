#program to generate and print a list 
# except for the first 5 elements,
# where the values are square of numbers between 1 and 20
l = []
for i in range(1,20):
    l.append(i**2)
l=l[5:]
print (l)