# creating an empty list 
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
for i in range(n): 
    ele = int(input("element n° "+str(i+1)+": ")) 
    lst.append(ele)

print (lst)
