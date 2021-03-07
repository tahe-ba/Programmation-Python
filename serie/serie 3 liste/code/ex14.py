'''
program to generate and print a list 
of first and last 5 elements 
where the values are 
square of numbers between 1 and 30 (both included)
'''

l = []
for i in range(1,31):
    l.append(i**2)
l=l[:5]+l[25:]
print (l)
