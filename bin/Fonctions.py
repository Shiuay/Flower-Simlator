# -*- coding: utf-8 -*-

from random import *
from math import *

continuer = [True, False]


def inclinaison_soleil(latitude, jour):

    declinaison = 23.45 * sin(((2 * pi) / 365) * (jour + 284))
    hauteur = latitude - declinaison
    exposition = cos(radians(hauteur)) * 100
    return exposition


def alea(x):
    """Renvoie True avec une probabilité de x%"""
    if random() * 100 < x:
        return True
    else:
        return False


def pause_resume(x):
    global continuer
    if continuer[x] == True:
        continuer[x] = False
    else:
        continuer[x] = True


def continuer_test(x):
    global continuer
    return continuer[x]


def charger_parametres():
    """Extrait les paramètres d'un fichier texte dedié"""
    with open('parametres.txt', 'r') as fichier:
        contenu = fichier.read()
        lignes = contenu.split()
        parametres = dict()
        for ligne in lignes:
            parametre = ligne.split("=")
            parametres[parametre[0]] = parametre[1]
        return parametres
