'''
program to count the number of strings where
Sample List : [’abc’, ’xyz’, ’aba’, ’1221’]
list item >=2 and first letter = last letter
Expected Result : 2
'''

li=["abc", "xyz", "aba", "1221"]
o=0
for i in range(len(li)):
    a=list(li[i])
    if len(li[i]) >= 2 and a[0] == a[len(a)-1]: 
        o=o+1
print (o)