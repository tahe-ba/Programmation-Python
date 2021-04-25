#Ex2 :
#Lecture d'un fichier
F1=open('Mydoc1','r')
F2=open('Mydoc2','r')
import sys
def Reading_File(F):
    while True :
        data=F.readline()
        if data == '' or data ==None:
            break
        sys.stdout.write(data)

print("Le contenu du fichier Mydoc1 : ")
Reading_File(F1)
print("Le contenu du fichier Mydoc2 : ")
Reading_File(F2)