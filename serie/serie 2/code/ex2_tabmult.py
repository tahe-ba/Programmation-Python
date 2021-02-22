quitter='F'
while quitter!='T':
    while True :
        x=input("Introduisez un entier ")
        if x.isdigit() is True :
            print("La table de multiplication de ", x)
            for i in range(11):
                print(x, '*' , i, ' = ', int(x)*i )
            break
        else :
            print("erreur de saisie ")
    quitter=input("si vous voulez quitter tapez T ")
    