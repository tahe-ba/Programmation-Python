#Asked to run this function
#accept many arguments in function 
#return their sum
#nbre inside the function behaves as a tuple
def function(*nbre):
    resu=0
    for x in nbre:
        resu += x
    print(resu)
function(1,2,3) 