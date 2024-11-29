
#### Imports et définition des variables globales
import sys

sys.setrecursionlimit(2000)

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    resultat = []
    Cx = s[0]
    Ox = 1
    for k in range(1, len(s)) : 
        if s[k] == s[k-1] :
            Ox += 1
        else :
            resultat.append((Cx, Ox))
            Cx = s[k]
            Ox = 1

    resultat.append((Cx, Ox))
    return resultat


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    if(len(s) == 0) :
        return []
    Ox = 1
    while Ox < len(s) and s[Ox] == s[0] :
        Ox += 1
    return [(s[0], Ox)]+artcode_r(s[Ox:]) 
    

    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif
    

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
