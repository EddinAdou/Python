chaine = input("entrer un mot ")

def inverser_chaine(chaine):
    chaine_inverse = ""
    for i in range(len(chaine)):
        chaine_inverse += chaine[len(chaine) - 1 - i]
    return chaine_inverse

print(inverser_chaine(chaine))