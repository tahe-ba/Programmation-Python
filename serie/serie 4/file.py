#Ex1
#file : 'w' : write (écriture)
#       'a' : Append (Ajout)
F1=open('Mydoc1','w') #écrasement du file
F2=open('Mydoc2','a') #Ajouter des infos
# N°    Nom    Email
# 1     User1  User1@Email.com
# 2     User2  User2@Email.com
# 3     User3  User3@Email.com
#.
#.
#.
#10     User10  User10@Email.com
for index in range(1,12):
    data=''
    name='User'+str(index-1)
    Email='User'+str(index-1)+'@Email.com'
    if index==1:
        data='{0:3s}{1:10s}{2:15s}\n'.format('N°','Nom','Email')
    else:
        data = '{0:3s}{1:10s}{2:15s}\n'.format(str(index-1), name, Email)
    F1.write(data)
    F2.write(data)
F1.close()
F2.close()