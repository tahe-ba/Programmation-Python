#program to get the difference between the two lists

l1=[1,2,3]
l2=[1,2,3]
d=[]

for x in l1:
        if x in l2:
            d.append(x)
print(d)