#only negative numbers in list are ^2
exit = 'F'
while exit != 'T' and exit != 't' :
    liste1=[1,5,-3,8,9,3,-4,-2,7]
    liste2=liste1.copy()
    i=0
    for i in range(len(liste1)):
        if liste1[i]<0 :
            liste2[i]=liste1[i]*liste1[i]
        else :
            liste2[i]=liste1[i]
    print(liste1)
    print(liste2)
    exit=input("\nIf you want tou quit type T/t: ")
