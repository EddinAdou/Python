chaine = input("entrer un mot ")
def is_palindrome(chaine):
    chaine_inverse = ""
    for i in range(len(chaine)):
        chaine_inverse += chaine[len(chaine) - 1 - i]
    if chaine == chaine_inverse:
        return True
    else:
        return False
print(is_palindrome(chaine))