import os.path

def find_word(file_name, string_to_search):
    found =0
    with open(file_name,'r') as file:   
        for line in file:
            line=line.strip()
            if line==string_to_search:
                found=1
                return (line)
        if found == 0 :
            return 0 
    f.close()

def dechiffrer_letter(letter, is_upper,decaler):
    if is_upper:
        l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    else:
        l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    decrypted_index = (l.index(letter)-(decaler))
    return l[decrypted_index]

def find_key (crypted,file_name):
    found = 0
    for key in range (26):
        maybe=list()
        for letter in crypted :
            if letter.isalpha() :
                up= letter.isupper()
                maybe.append(dechiffrer_letter(letter,up,key))
            else :
                maybe.append(letter)
        maybe=''.join(maybe)
        if find_word(file_name,maybe)!= 0 :
            result = [key,maybe]
            return (result)
            found = 1
    if found == 0 :
        return -1 

def header ():
    print('''
𝕒𝕥𝕥𝕒𝕔𝕜 𝕕𝕚𝕔𝕥𝕚𝕠𝕟𝕟𝕒𝕚𝕣𝕖
        .-.
      '(o.o)'
        |_|
''')

def main():
    header()
    msg = input("Mot à decrypter : ")
    while True :
        dic = input("Nom de votre dictionnaire : ")
        if not (os.path.isfile(dic)):
            print("fichier introuvable !!")
        else:
            break
    if find_key(msg,dic) == -1 :
        print("\naucune correspondance dans le dictionnaire ")
    else :
        print("\nla clé est : "+str(find_key(msg,dic)[0]))
        print("le message decryptee est : " +find_key(msg,dic)[1])

main()