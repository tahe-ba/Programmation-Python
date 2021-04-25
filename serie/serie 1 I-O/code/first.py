# Calcule PrixTTC 
# Accepting only valid input 
# Asking before quit
exit = 'F'
while exit != 'T' :
    while True :
        try :
            prix=float(input("prix HT="))
            break
        except ValueError:
            print("Wrong input")

    while True :
        try :
            option=int(input("if tva = 15% press 1 or press 2 if tva is 19% : "))
            if option==1 :
                tva=0.15
                break
            elif option == 2 :
                tva =0.19
                break
            else :
                print("only 1 or 2 are acceptable")
        except ValueError:
            print("Wrong input")
    prixttc=prix+(tva*prix)
    print("Le prix ttc de votre prix ht est : %.2f est %.2f"%(prix, prixttc))
    # print("Le prix ttc de votre prix ht est : {:.2f} est {:.2f}".format(prix, prixttc))

    exit=input("if you want tou quit type T: ")
