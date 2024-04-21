liste = input("entrer une liste de nombre :")
def inverser_liste(liste):
    liste_inverse = []
    for i in range(len(liste)):
        liste_inverse.append(liste[len(liste) - 1 - i])
    return liste_inverse
print(inverser_liste(liste))