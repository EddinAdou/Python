chaine = input("Entrer une chaine de caractères: ")
def remplacer_espace(chaine):
    chaine = chaine.replace(" ", "-")
    return chaine
print(remplacer_espace(chaine))