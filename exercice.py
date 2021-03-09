#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici


import math
import sys
sys.path(0, "/Documents/GitHub/2021h-ch-6-1-exercices-phhad")
from _exercice_version_prof import frequence
from turtle import *
# TODO: Définissez vos fonction ici

def ellipse(a,b,c,ri):
    volume_ell = math.pi()*a*b*c*(4/3)
    masse_ell = ri*volume_ell
    return volume_ell, masse_ell

def draw_branch(branch_len, pen_size, angle):
    if branch_len > 0 and pensize > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len -10 , pen_size - 1, angle - 5)
        left(angle * 2)
        draw_branch(branch_len -10 , pen_size - 1, angle - 5)
        right(angle)
        backward(branch_len)


def draw_tree():
    setheading(90)
    color('green')
    draw_branch(70,7,35)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    mass_vol = ellipse()
    print(mass_vol)
    print(lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("test test test test")
    pass
