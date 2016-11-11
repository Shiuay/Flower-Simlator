# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 20:01:52 2016

@author: Roméo
"""

from random import *


def test_degage(duree):
    tirage = random()

    if tirage < 0.1 * (1 + (1 / -duree)):
        return ["Nuageux3", 1]

    if tirage < 0.3 * (1 + (1 / -duree)):
        return ["Nuageux2", 1]

    if tirage < 1 * (1 + (1 / -duree)):
        return ["Nuageux1", 1]

    else:
        return ["Dégagé", duree + 1]


def test_nuageux1(duree):
    tirage = random()

    if tirage < 0.03 * (1 + (1 / -duree)):
        return ["Nuageux4", 1]

    if tirage < 0.1 * (1 + (1 / -duree)):
        return ["Nuageux3", 1]

    if tirage < 0.3 * (1 + (1 / -duree)):
        return ["Nuageux2", 1]

    if tirage < 1 * (1 + (1 / -duree)):
        return ["Dégagé", 1]

    else:
        return ["Nuageux1", duree + 1]


def test_nuageux2(duree):
    tirage = random()

    if tirage < 0.03 * (1 + (1 / -duree)):
        return ["Nuageux5", 1]

    if tirage < 0.1 * (1 + (1 / -duree)):
        return ["Nuageux4", 1]

    if tirage < 0.3 * (1 + (1 / -duree)):
        return ["Nuageux3", 1]

    if tirage < 0.53 * (1 + (1 / -duree)):
        return ["Dégagé", 1]

    if tirage < 1 * (1 + (1 / -duree)):
        return ["Nuageux1", 1]

    else:
        return ["Nuageux2", duree + 1]


def test_nuageux3(duree):
    tirage = random()

    if tirage < 0.1 * (1 + (1 / -duree)):
        return ["Nuageux5", 1]

    if tirage < 0.3 * (1 + (1 / -duree)):
        return ["Nuageux4", 1]

    if tirage < 0.37 * (1 + (1 / -duree)):
        return ["Dégagé", 1]

    if tirage < 0.53 * (1 + (1 / -duree)):
        return ["Nuageux1", 1]

    if tirage < 1 * (1 + (1 / -duree)):
        return ["Nuageux2", 1]

    else:
        return ["Nuageux3", duree + 1]


def test_nuageux4(duree):
    tirage = random()

    if tirage < 0.3 * (1 + (1 / -duree)):
        return ["Nuageux5", 1]

    if tirage < 0.32 * (1 + (1 / -duree)):
        return ["Nuageux1", 1]

    if tirage < 0.37 * (1 + (1 / -duree)):
        return ["Nuageux2", 1]

    if tirage < 0.53 * (1 + (1 / -duree)):
        return ["Nuageux3", 1]

    if tirage < 0.55 * (1 + (1 / -duree)):
        return ["Pluvieux2", 1]

    if tirage < 0.6 * (1 + (1 / -duree)):
        return ["Pluvieux3", 1]

    if tirage < 0.9 * (1 + (1 / -duree)):
        return ["Pluvieux4", 1]

    if tirage < 1 * (1 + (1 / -duree)):
        return ["Pluvieux5", 1]

    else:
        return ["Nuageux4", duree + 1]


def test_nuageux5(duree):
    tirage = random()

    if tirage < 0.02 * (1 + (1 / -duree)):
        return ["Nuageux2", 1]

    if tirage < 0.07 * (1 + (1 / -duree)):
        return ["Nuageux3", 1]

    if tirage < 0.23 * (1 + (1 / -duree)):
        return ["Nuageux4", 1]

    if tirage < 0.27 * (1 + (1 / -duree)):
        return ["Pluvieux3", 1]

    if tirage < 0.35 * (1 + (1 / -duree)):
        return ["Pluvieux4", 1]

    if tirage < 1 * (1 + (1 / -duree)):
        return ["Pluvieux5", 1]

    else:
        return ["Nuageux5", duree + 1]


def test_pluvieux1(duree):
    tirage = random()

    if tirage < 0.85 * (1 - (1 + (1 / -duree**1.5))):
        return ["Pluvieux2", duree + 1]

    if tirage < 1 * (1 - (1 + (1 / -duree**0.52))):
        return ["Pluvieux1", duree + 1]

    else:
        return ["Dégagé", 1]


def test_pluvieux2(duree):
    tirage = random()

    if tirage < 0.85 * (1 - (1 + (1 / -duree**1.5))):
        return ["Pluvieux3", duree + 1]

    if tirage < 1 * (1 - (1 + (1 / -duree**0.52))):
        return ["Pluvieux2", duree + 1]

    else:
        return ["Pluvieux1", duree + 1]


def test_pluvieux3(duree):
    tirage = random()

    if tirage < 0.85 * (1 - (1 + (1 / -duree**1.5))):
        return ["Pluvieux4", duree + 1]

    if tirage < 1 * (1 - (1 + (1 / -duree**0.52))):
        return ["Pluvieux3", duree + 1]

    else:
        return ["Pluvieux2", duree + 1]


def test_pluvieux4(duree):
    tirage = random()

    if tirage < 0.85 * (1 - (1 + (1 / -duree**1.5))):
        return ["Pluvieux5", duree + 1]

    if tirage < 1 * (1 - (1 + (1 / -duree**0.52))):
        return ["Pluvieux4", duree + 1]

    else:
        return ["Pluvieux3", duree + 1]


def test_pluvieux5(duree):
    tirage = random()

    if tirage < 1 * (1 - (1 + (1 / -duree**0.52))):
        return ["Pluvieux5", duree + 1]
    else:
        return ["Pluvieux4", duree + 1]


def degage(meteo):
    if meteo[0] == "Dégagé":
        return True
    else:
        return False


def nuageux1(meteo):
    if meteo[0] == 'Nuageux1':
        return True
    else:
        return False


def nuageux2(meteo):
    if meteo[0] == 'Nuageux2':
        return True
    else:
        return False


def nuageux3(meteo):
    if meteo[0] == 'Nuageux3':
        return True
    else:
        return False


def nuageux4(meteo):
    if meteo[0] == 'Nuageux4':
        return True
    else:
        return False


def nuageux5(meteo):
    if meteo[0] == 'Nuageux5':
        return True
    else:
        return False


def pluvieux(meteo):
    if meteo[0].startswith('Pluvieux'):
        return True
    else:
        return False


def test_temps(meteo):

    changement = True

    if meteo[0] == "Dégagé" and changement:
        meteo = test_degage(meteo[1] + 1)
        changement = False

    if meteo[0] == "Nuageux1" and changement:
        meteo = test_nuageux1(meteo[1] + 1)
        changement = False

    if meteo[0] == "Nuageux2" and changement:
        meteo = test_nuageux2(meteo[1] + 1)
        changement = False

    if meteo[0] == "Nuageux3" and changement:
        meteo = test_nuageux3(meteo[1] + 1)
        changement = False

    if meteo[0] == "Nuageux4" and changement:
        meteo = test_nuageux4(meteo[1] + 1)
        changement = False

    if meteo[0] == "Nuageux5" and changement:
        meteo = test_nuageux5(meteo[1] + 1)
        changement = False

    if meteo[0] == "Pluvieux1" and changement:
        meteo = test_pluvieux1(meteo[1] + 1)
        changement = False

    if meteo[0] == "Pluvieux2" and changement:
        meteo = test_pluvieux2(meteo[1] + 1)
        changement = False

    if meteo[0] == "Pluvieux3" and changement:
        meteo = test_pluvieux3(meteo[1] + 1)
        changement = False

    if meteo[0] == "Pluvieux4" and changement:
        meteo = test_pluvieux4(meteo[1] + 1)
        changement = False

    if meteo[0] == "Pluvieux5" and changement:
        meteo = test_pluvieux5(meteo[1] + 1)
        changement = False

    return meteo
