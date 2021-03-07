#progrm that removes duplucates from a list
'''
Remove all items: clear()
Remove an item by index and get its value: pop()
Remove an item by value: remove()
Remove items by index or slice: del
Remove items that meet the condition: List comprehensions
'''
l = [3, 3, 2, 1, 5, 1, 4, 2, 3]

#sort and delete duplicates : set(l)
print(list(set(l)))

#delete duplicates and keep order
print(sorted(set(l), key=l.index))