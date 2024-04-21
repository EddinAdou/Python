chaine = input("Entrer une chaine de caractères: ")
def detecter_dates(chaine):
    dates = []
    for i in range(len(chaine)):
        if chaine[i].isdigit() and chaine[i+1].isdigit() and chaine[i+2].isdigit() and chaine[i+3].isdigit():
            dates.append(chaine[i:i+4])
    return dates
print(detecter_dates(chaine))