#program that finds the min and max value in list 
li=[-5,6,1,2,8,0,99]
max=li[0]
min=li[0]
for i in range(1,len(li)):
    if li[i] > max:
        max = li[i]
    if li[i] < min :
        min = li[i]
print(min,max)