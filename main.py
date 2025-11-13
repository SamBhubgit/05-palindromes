#### Fonction secondaire
"""
Ce programme vérifie si des chaines de caractères sont des palindromes
"""
def ispalindrome(p):
    """
    Cette fonction permet de vérifier si une chaine de caractères est un palindrome
    """
    accent=""
    for i in p:
        if i not in " ,-':?!":
            accent=accent+i

    accent=accent.lower()
    phrase=""
    for i in accent:
        if i in "éèëê":
            phrase=phrase+"e"

        elif i in "àâä":
            phrase=phrase+"a"

        elif i in "îïì":
            phrase=phrase+"i"

        elif i=="ç":
            phrase=phrase+"c"

        elif i in "ùûü":
            phrase=phrase+"u"

        elif i in "ôöò":
            phrase=phrase+"o"

        else:
            phrase=phrase+i

    milieu=int(len(phrase)/2)
    inc_fin=len(phrase)-1 #incrémenteur commençant à la fin
    for i in range(0,milieu):
        if phrase[i]!=phrase[inc_fin] :
            return False
        inc_fin=inc_fin-1
    return True

#### Fonction principale
def main():
    """
    Teste la fonction is_palindrome avec plusieurs exemples.
    """
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
