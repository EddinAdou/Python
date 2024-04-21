chaine = input("entrer un mot ")
def compter_lettres(chaine):
    for i in range(len(chaine)):
        print(chaine[i], chaine.count(chaine[i]))
compter_lettres(chaine)