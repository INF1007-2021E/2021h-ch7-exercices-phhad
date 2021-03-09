#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici


import math
# TODO: Définissez vos fonction ici
def ellipse(a,b,c,ri):
    volume_ell = math.pi()*a*b*c*(4/3)
    masse_ell = ri*volume_ell
    return volume_ell, masse_ell

def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    frequency = dict()
    for letter in sentence:
        frequency[letter] = sentence.count(letter)

    sorted_keys = sorted(frequency, key=frequency.__getitem__, reverse=True)
    for key in sorted_keys:
        if frequency[key] > 5:
            print(f"Le caractère {key} revient {frequency[key]} fois.")

    return frequency

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    mass_vol = ellipse()
    print(mass_vol)
    pass
