#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici


import math
import sys
sys.path(0, "/Documents/GitHub/2021h-ch-6-1-exercices-phhad")
from _exercice_version_prof import frequence
# TODO: Définissez vos fonction ici
def ellipse(a,b,c,ri):
    volume_ell = math.pi()*a*b*c*(4/3)
    masse_ell = ri*volume_ell
    return volume_ell, masse_ell

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    mass_vol = ellipse()
    print(mass_vol)
    print(lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("test test test test")
    pass
