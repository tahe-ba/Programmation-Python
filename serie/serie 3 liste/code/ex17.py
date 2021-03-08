#program to get the difference between the two lists

l1=[1,2,3]
l2=[1,2,3]
d=[]

for x in l1:
        for y in l2:
            if x != y:
                d.append(x)
print(d)