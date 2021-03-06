# creating an empty list 
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele) # adding the element 
print(lst) 

lst1=[]
lst1 = [int(item) for item in input("Enter the elements of list seperated by space: ").split()] 
print(lst1)

