#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
import filecmp

# TODO: Définissez vos fonction ici
def mes_fonctions(f1,f2):

    with open(f1, "r", encoding="utf-8") as f1, open(f2, "r", encoding="utf-8") as f2: # on ecrit comme sa pour comparer deux fichiers
        f1.readline(0)                                                                 # on prend le premier élément du fichier
        f2.readline(0)                                                                 # on prend premier élément du fichier
        if f1 != f2:                                                                    # si les deux fichiers spnt pas pareils
           print("C'est different:", f1.readline(), f2.readline())                      # montrer ce qui n'estpas

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    mes_fonctions("notes.txt","exemple.txt")
