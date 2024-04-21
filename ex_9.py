
liste = input("Entrer une liste de nombres avec espaces : ").split()
nombre = input("Entrer le nombre à compter: ")

def compter_occurrences(liste, nombre):
    occurrences = 0
    for i in range(len(liste)):
        if liste[i] == nombre:
            occurrences += 1
    return occurrences

print(compter_occurrences(liste, nombre))