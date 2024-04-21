chaine = input("Entrer une chaîne de caractères: ")
def trouver_le_plus_long_mot(chaine):
    chaine_plus_longue = chaine.split(" ")
    mot = ""
    for i in range(len(chaine_plus_longue)):
        if len(chaine_plus_longue[i]) > len(mot):
            mot = chaine_plus_longue[i]
    return mot
print(trouver_le_plus_long_mot(chaine))