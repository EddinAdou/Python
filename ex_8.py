liste1 = input("entrer les valeurs de la liste 1 : ")
liste2 = input("entrer les valeurs de la liste 2 : ")

def elements_communs(liste1, liste2):
    liste_commune = []
    for i in range(len(liste1)):
        if liste1[i] in liste2:
            liste_commune.append(liste1[i])
    return liste_commune
print(elements_communs(liste1, liste2))