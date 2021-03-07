#program that check if there is at least one common element in two lists
def commun(l1, l2):
    result = False
    for x in l1:
        for y in l2:
            if x == y:
                return True
li=[1,2,3,4]
lo=[5,6,7]

if commun(li,lo) :
    print("same element exists in both lists")
else :
    print("no common elements in the lists")