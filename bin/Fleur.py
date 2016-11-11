# -*- coding: utf-8 -*-

from bin.Fonctions import *


class Fleur:
    """
    Classe représentant la fleur, elle possède comme caractéristiques:
    - Croissance : int entre 0 et 1000
    - Hydratation : int entre 0 et 1000 ( peut depasser cette valeur )
    - Vitalité : int entre 0 et 1000
    - Resistances : dictionnaire :
        - Clé : string "NomResistance"
        - Valeur : int en %

    - Maladie : dictionnaire :
        -
        - pass

    Une hydratation trop ou pas assez elevée baisse la vitalité
    La resistance est la chance de ne pas subir l'influance d'un evenement
    Atteindre 1000 de croissance fait baisser la vitalité
    Quand sa vitalité atteint 0 elle meurt.
    """

    def __init__(self):

        self.croissance = 0
        self.hydratation = 1000
        self.vitalite = 1000
        self.resistances = dict()
        # self.maladies = dict()

    def eau(self, quantite):

        if self.hydratation + quantite <= 0:
            self.hydratation = 0
        else:
            self.hydratation += quantite

    def dvp(self, quantite):

        if quantite < 0:
            raise ValueError("La croissance ne peut être que positive")

        if self.croissance + quantite > 1000:
            self.croissance = 1000
        else:
            self.croissance += quantite

    def vie(self, quantite):

        if self.vitalite + quantite > 1000:
            self.vitalite = 1000
        elif self.vitalite + quantite < 0:
            self.vitalite = 0
        else:
            self.vitalite += quantite

    def tic(self):

        if self.vitalite > 0:

            # La plante se desseche
            self.eau(-2)

            # La plante regenere lentement
            self.vie(1)

            # La plante grandit
            self.dvp(1)

            # Une hydratation trop ou pas assez elevée baisse la vitalité
            if self.hydratation < 500 or self.hydratation > 1300:
                self.vie(-5)

            # Atteindre 1000 de croissance fait baisser la vitalité
            if self.croissance == 1000:
                self.vie(-2)

            # Arrosage aléatoire par la pluie
            if alea(0.1):
                self.eau(600)
