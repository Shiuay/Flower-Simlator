# -*- coding: utf-8 -*-

from tkinter import *
from bin.fonctions import *
from bin.Fleur import *
from bin.save import *


class Interface():

    def __init__(self, **args):

        # Les variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.fenetre = Tk()
        self.argent = 5
        self.date = [30, 8, 2016, "Mardi", 81, 0, 1]

        # Parametre de la fenetre ~~~~~~~~~~~~~~~~~~~

        self.fenetre.title("Enculer Gromeo")
        self.fenetre.resizable(width=False, height=False)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


class Main_Fenetre():

    def __init__(self, interface, Meteo):

        self.fleurs = list()
        for i in range(12):
            self.fleurs.append(None)

        # Menu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        interface.menubar = Menu(interface.fenetre)

        # Cascade 1

        interface.menu1 = Menu(interface.menubar, tearoff=0)
        interface.menubar.add_cascade(label="Fichier", menu=interface.menu1)
        interface.menu1.add_command(label="Charger", command=charger_partie)
        interface.menu1.add_command(label="Sauvegarder", command=lambda: sauvegarder_partie(
            date=interface.date, meteo=Meteo, fric=interface.argent, fleur=self.fleurs))
        interface.menu1.add_separator()
        interface.menu1.add_command(
            label="Quitter", command=interface.fenetre.quit)

        # Cascade 2

        interface.menu2 = Menu(interface.menubar, tearoff=0)
        interface.menubar.add_cascade(label="Shop", menu=interface.menu2)
        interface.menu2.add_command(label="Eau", command=alert)
        interface.menu2.add_command(label="Engrais", command=alert)
        interface.menu2.add_command(label="Plantes", command=alert)
        interface.menu2.add_command(label="Radio", command=alert)

        # Cascade 3

        interface.menu3 = Menu(interface.menubar, tearoff=0)
        interface.menubar.add_cascade(label="Aide", menu=interface.menu3)
        interface.menu3.add_command(
            label="Accès fichier Python", command=alert)
        interface.menu3.add_command(label="A propos", command=alert)

        interface.fenetre.config(menu=interface.menubar)

        # Photo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        self.photo = dict()

        self.photo["fleur"] = PhotoImage(file="image\\fleur.png")
        self.photo["pot"] = PhotoImage(file="image\\fleur_pot.png")
        self.photo["soleil"] = PhotoImage(file="image\\soleil.png")
        self.photo["nuage_1"] = PhotoImage(file="image\\nuage 1.png")
        self.photo["nuage_2"] = PhotoImage(file="image\\nuage 2.png")
        self.photo["nuage_3"] = PhotoImage(file="image\\nuage 3.png")
        self.photo["nuage_4"] = PhotoImage(file="image\\nuage 4.png")
        self.photo["nuage_5"] = PhotoImage(file="image\\nuage 5.png")
        self.photo["pluie"] = PhotoImage(file="image\\pluie.png")

        # Création selection fleurs ~~~~~~~~~~~~~~~~~

        self.selection_fleurs = Canvas(
            interface.fenetre, width=700, height=500, bg='#F0F0F0')
        self.selection_fleurs.pack(side=LEFT, anchor=SW, padx=5, pady=5)

        self.choix_fleur = StringVar()

        # Création des boutons des fleurs

        self.boutons_fleur = list()
        for i in range(12):
            self.boutons_fleur.append(Radiobutton(
                self.selection_fleurs, image=self.photo["pot"], bg='#F0F0F0', variable=self.choix_fleur, value=i))

        # Placement des boutons des fleurs

        y = 10
        b = 0
        for t in range(4):
            x = 20
            for i in range(3):
                self.selection_fleurs.create_window(
                    y, x, anchor=NW, window=self.boutons_fleur[b])
                b += 1
                x += 165
            if y == 10:
                y += 165
            elif y == 175:
                y += 175
            else:
                y += 170

        del y, x, b

        self.selection_fleurs.pack(side=LEFT, anchor=SW, padx=5, pady=5)

        # Labels ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        self.label_gold = Label(interface.fenetre, anchor=NW, width=40, height=5, text="${}".format(
            interface.argent), relief=FLAT, fg='black', command=None, font=("Helvetica", 16))
        self.label_gold.place(x=10, y=10)

        self.label_meteo = Label(
            interface.fenetre, bg='#F0F0F0', image=self.photo["soleil"])
        self.label_meteo.place(x=0, y=40)

        self.label_stats = Label(interface.fenetre, width=20, height=5, text="\nCroissance : {}\n\nHydratation : {}\n\nVitalité : {}".format(
            0, 1000, 1000), relief=FLAT, fg='black', bd=12, command=None)
        self.label_stats.pack(side=TOP, padx=5, pady=5)

        self.bouton_arroser = Button(interface.fenetre, width=25, height=5,
                                     text="Arroser la fleur", command=self.arroser_fleur)
        self.bouton_acheter = Button(interface.fenetre, width=25, height=5,
                                     text="Acheter une fleur", command=lambda: self.acheter_fleur(interface))
        self.bouton_vendre = Button(interface.fenetre, width=25, height=5,
                                    text="Vendre la fleur", command=lambda: self.vendre_fleur(interface))
        self.bouton_jeter = Button(interface.fenetre, width=25, height=5,
                                   text="Jeter la fleur", command=self.jeter_fleur)

        self.bouton_jeter.pack(side=BOTTOM, padx=5, pady=5)
        self.bouton_vendre.pack(side=BOTTOM, padx=5, pady=5)
        self.bouton_acheter.pack(side=BOTTOM, padx=5, pady=5)
        self.bouton_arroser.pack(side=BOTTOM, padx=5, pady=5)

        # Création calendrier ~~~~~~~~~~~~~~~~~~~~~~~

        self.calendrier = Canvas(
            interface.fenetre, width=244, height=284, bg='#F0F0F0')
        self.calendrier.pack(side=BOTTOM, padx=5, pady=5)

        self.calendrier.create_text(122, 20, tags="année")
        self.calendrier.create_text(122, 50, tags="mois")

        # affichage des premierre lettre des jours

        self.calendrier.create_text(20, 80, text="L")
        self.calendrier.create_text(55, 80, text="M")
        self.calendrier.create_text(90, 80, text="M")
        self.calendrier.create_text(125, 80, text="J")
        self.calendrier.create_text(160, 80, text="V")
        self.calendrier.create_text(195, 80, text="S")
        self.calendrier.create_text(230, 80, text="D")

        # création des emplacement pour les numeros des jour

        tag = 1
        x = 20
        y = 110
        for i in range(6):
            for u in range(7):
                self.calendrier.create_text(x, y, tags=tag)
                tag += 1
                x += 35
            y += 30
            x = 20
        del x, y

        # Création des emplacement pour les cadres de selection du jour

        tag = 1
        x0 = 10
        x1 = 30
        y0 = 100
        y1 = 120
        for i in range(6):
            for u in range(7):
                self.calendrier.create_rectangle(
                    x0, y0, x1, y1, tags=tag, fill='', outline='red', width=0)
                x0 += 35
                x1 += 35
                tag += 1
            y0 += 30
            y1 += 30
            x0 = 10
            x1 = 30

        del x0, y0, x1, y1, tag

        self.afficheur_calendrier(interface)

    def afficheur_calendrier(self, interface):

        mois = (("Janvier", 31), ("Février", 28), ("Mars", 31), ("Avril", 30), ("Mai", 31), ("Juin", 30),
                ("Juillet", 31), ("Août", 31), ("Septembre", 30), ("Octobre", 31), ("Novembre", 30), ("Décembre", 31))

        # [Jour, Mois, Années, Jour, rectangle afficheur calendrier, ticks, jour]

        tag = 10

        # remise a zero du carré rouge de selection de date

        for i in range(52, 93):
            self.calendrier.itemconfig(i, width=0)

        for i in range(42):
            self.calendrier.itemconfig(tag, text="", fill='black')
            tag += 1

        self.calendrier.itemconfig(interface.date[4], width=2)

        # Affichage du mois et de l'année

        self.calendrier.itemconfig("année", text=interface.date[2])
        self.calendrier.itemconfig("mois", text=mois[interface.date[1] - 1][0])

        # Création du calendrier

        tag = interface.date[6] + 10
        for i in range(mois[interface.date[1] - 1][1]):
            r = i + 1
            self.calendrier.itemconfig(tag, text=r, fill='black')
            tag += 1

        r = 1
        while 52 != tag:
            self.calendrier.itemconfig(tag, text=r, fill='gray')
            r += 1
            tag += 1

        tag = interface.date[6] + 9

        try:
            tgris = mois[interface.date[1] - 2][1]
        except:
            tgris = mois[11][1]

        while 11 != tgris and tag != 9:
            self.calendrier.itemconfig(tag, text=tgris, fill='gray')
            tag -= 1
            tgris -= 1

    def jour(self, interface):

        def adv(date):
            date[0] = 1
            date[1] += 1
            return date

        jour = ("Lundi", "Mardi", "Mercredi", "Jeudi",
                "Vendredi", "Samedi", "Dimanche")

        mois = (("Janvier", 31), ("Février", 28), ("Mars", 31), ("Avril", 30), ("Mai", 31), ("Juin", 30),
                ("Juillet", 31), ("Août", 31), ("Septembre", 30), ("Octobre", 31), ("Novembre", 30), ("Décembre", 31))

        # affichage des jour

        ad = 0
        interface.date[0] += 1
        interface.date[6] += 1
        if interface.date[6] == 7:
            interface.date[6] = 0

        interface.date[3] = jour[interface.date[6]]

        # check si le mois est terminer

        if interface.date[1] == 1 or \
                interface.date[1] == 3  or \
                interface.date[1] == 5  or \
                interface.date[1] == 7  or \
                interface.date[1] == 8  or \
                interface.date[1] == 10 or \
                interface.date[1] == 12:

            if interface.date[0] == 32:
                interface.date = adv(interface.date)

        elif interface.date[1] == 4 or \
                interface.date[1] == 6 or \
                interface.date[1] == 9 or \
                interface.date[1] == 11:

            if interface.date[0] == 31:
                interface.date = adv(interface.date)

        elif interface.date[1] == 2:

            if interface.date[0] == 29:
                interface.date = adv(interface.date)

            # check si année fini

        if interface.date[1] == 13:
            interface.date[1] = 1
            interface.date[2] += 1

        self.calendrier.itemconfig(interface.date[4], width=0)
        interface.date[4] += 1
        if interface.date[0] == 1:
            interface.date[4] = interface.date[6] + 52
        self.calendrier.itemconfig(interface.date[4], width=2)

        return interface.date

    def arroser_fleur(self):

        try:
            fleur = self.fleurs[int(self.choix_fleur.get())]
        except ValueError:
            return None

        if fleur is not(None):
            fleur.eau(100)

    def acheter_fleur(self, interface):

        try:
            fleur = self.fleurs[int(self.choix_fleur.get())]
        except ValueError:
            return None

        if fleur is None and interface.argent >= 5:
            for i in range(len(self.boutons_fleur)):
                if self.choix_fleur.get() == str(i):
                    self.boutons_fleur[i].config(image=self.photo["fleur"])
                    self.fleurs[i] = Fleur()
                    interface.argent -= 5
                    self.label_gold.config(text="${}".format(interface.argent))

    def jeter_fleur(self):
        for i in range(len(self.boutons_fleur)):
            if self.choix_fleur.get() == str(i):
                self.boutons_fleur[i].config(image=self.photo["pot"])
                self.fleurs[i] = None

    def vendre_fleur(self, interface):

        try:
            fleur = self.fleurs[int(self.choix_fleur.get())]
        except ValueError:
            return None

        if fleur is not(None):
            if fleur.croissance == 1000:
                interface.argent += round(fleur.vitalite, -2) / 100
                self.jeter_fleur()
                self.label_gold.config(text="${}".format(interface.argent))
