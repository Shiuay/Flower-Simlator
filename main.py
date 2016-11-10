# -*- coding: utf-8 -*-

# Import ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from bin.calendrier import *
from bin.fonctions import *
from bin.Fleur import *
from bin.Meteo import *
from threading import *
from tkinter import *
from math import *

import tkinter.messagebox
import time

parametres = charger_parametres()

stop = [True, False]
continuer = continuer_test()
argent = 5
# [Jour, Mois, Années, Jour, rectangle afficheur calendrier, ticks, jour]
date = [30, 8, 2016, "Mardi", 81, 0, 1]
Meteo = ["Dégagé", 1]

fleurs = list()
for i in range(12):
    fleurs.append(None)


def save():
    global date, Meteo, argent, fleur
    sauvegarder_partie(date=date, meteo=Meteo, fric=argent, fleur=fleurs)


def load():
    global date, Meteo, argent, fleurs
    save = charger_save()
    if save is None:
        pass
    else:
        date = save["date"]
        Meteo = save["meteo"]
        argent = save["fric"]
        fleurs = save["fleur"]

        b = 0
        for i in fleurs:
            if i is not None:
                boutons_fleur[b].config(image=photo_fleur)
            b += 1
        del b

        label_gold.config(text="${}".format(argent))
        tkinter.messagebox.showinfo(
            'Charger !', 'Votre partie a été bien charger !')
        pause_resume()


def arroser_fleur():

    try:
        fleur = fleurs[int(choix_fleur.get())]
    except ValueError:
        return None

    if fleur is not(None):
        fleur.eau(100)


def acheter_fleur():

    global argent

    try:
        fleur = fleurs[int(choix_fleur.get())]
    except ValueError:
        return None

    if fleur is None and argent >= 5:
        for i in range(len(boutons_fleur)):
            if choix_fleur.get() == str(i):
                boutons_fleur[i].config(image=photo_fleur)
                fleurs[i] = Fleur()
                argent -= 5
                label_gold.config(text="${}".format(argent))


def jeter_fleur():
    for i in range(len(boutons_fleur)):
        if choix_fleur.get() == str(i):
            boutons_fleur[i].config(image=photo_pot)
            fleurs[i] = None


def vendre_fleur():

    global argent

    try:
        fleur = fleurs[int(choix_fleur.get())]
    except ValueError:
        return None

    if fleur is not(None):
        if fleur.croissance == 1000:
            argent += round(fleur.vitalite, -2) / 100
            jeter_fleur()
            label_gold.config(text="${}".format(argent))


def quit():
    global stop
    stop[0] = False
    time.sleep(1)
    fenetre.quit()


def main():

    global date, LMois, Meteo, continuer, stop

    while stop[0]:

        continuer = continuer_test()
        load()
        if continuer == True:
            aff(date, LMois, Calendrier)

        while continuer:

            continuer = continuer_test()

            for fleur in fleurs:
                if fleur is not(None):
                    fleur.tic()

            date[5] += 1
            if date[5] == int(parametres["VitesseJour"]):
                date = jour(date, LMois, LJours, Calendrier)
                Meteo = test_temps(Meteo)

                if degage(Meteo):
                    label_meteo.config(image=photo_soleil)
                elif nuageux1(Meteo):
                    label_meteo.config(image=photo_nuage1)
                elif nuageux2(Meteo):
                    label_meteo.config(image=photo_nuage2)
                elif nuageux3(Meteo):
                    label_meteo.config(image=photo_nuage3)
                elif nuageux4(Meteo):
                    label_meteo.config(image=photo_nuage4)
                elif nuageux5(Meteo):
                    label_meteo.config(image=photo_nuage5)
                elif pluvieux(Meteo):
                    label_meteo.config(image=photo_pluie)

                if date[0] == 1:
                    aff(date, LMois, Calendrier)
                date[5] = 0

            if choix_fleur.get() == "":
                label_stats.configure(
                    label_stats, text="\nCroissance : {}\n\nHydratation : {}\n\nVitalité : {}".format(0, 0, 0))

            elif fleurs[int(choix_fleur.get())] is None:
                label_stats.configure(
                    label_stats, text="\nCroissance : {}\n\nHydratation : {}\n\nVitalité : {}".format(0, 0, 0))

            else:
                choix = int(choix_fleur.get())
                label_stats.configure(label_stats, text="\nCroissance : {}\n\nHydratation : {}\n\nVitalité : {}".format(
                    fleurs[choix].croissance, fleurs[choix].hydratation, fleurs[choix].vitalite))
            time.sleep(eval(parametres["VitesseTic"]))

programme = Thread(target=main)

# Fenêtre ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fenetre = Tk()

fenetre.title("Enculer Grosméo")

fenetre.resizable(width=False, height=False)

# Alerte temporaire ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def alert():
    tkinter.messagebox.showinfo("CE BOUTON NE MARCHE PAS ENCORE !",
                                "Vous venez de cliquer sur un bouton qui n'a pas encore été assigné.")

    # Menubar ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier", menu=menu1)
menu1.add_command(label="Charger", command=charger_partie)
menu1.add_command(label="Sauvegarder", command=save)
menu1.add_separator()
menu1.add_command(label="Quitter", command=quit)

menu2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Shop", menu=menu2)
menu2.add_command(label="Eau", command=alert)
menu2.add_command(label="Engrais", command=alert)
menu2.add_command(label="Plantes", command=alert)
menu2.add_command(label="Radio", command=alert)

menu3 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Aide", menu=menu3)
menu3.add_command(label="Accès fichier Python", command=alert)
menu3.add_command(label="A propos", command=alert)

fenetre.config(menu=menubar)

# Canvas & Image ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

canvas = Canvas(fenetre, width=700, height=500, bg='#F0F0F0')
canvas.pack(side=LEFT, anchor=SW, padx=5, pady=5)

photo_fleur = PhotoImage(file="image\\fleur.png")
photo_pot = PhotoImage(file="image\\fleur_pot.png")
photo_soleil = PhotoImage(file="image\\soleil.png")
photo_nuage1 = PhotoImage(file="image\\nuage 1.png")
photo_nuage2 = PhotoImage(file="image\\nuage 2.png")
photo_nuage3 = PhotoImage(file="image\\nuage 3.png")
photo_nuage4 = PhotoImage(file="image\\nuage 4.png")
photo_nuage5 = PhotoImage(file="image\\nuage 5.png")
photo_pluie = PhotoImage(file="image\\pluie.png")

choix_fleur = StringVar()
# Création des boutons des fleurs

boutons_fleur = list()
for i in range(12):
    boutons_fleur.append(Radiobutton(
        canvas, image=photo_pot, bg='#F0F0F0', variable=choix_fleur, value=i))

# Placement des boutons des fleurs
y = 10
b = 0
for t in range(4):
    x = 20
    for i in range(3):
        canvas.create_window(y, x, anchor=NW, window=boutons_fleur[b])
        b += 1
        x += 165
    if y == 10:
        y += 165
    elif y == 175:
        y += 175
    else:
        y += 170

canvas.pack(side=LEFT, anchor=SW, padx=5, pady=5)

# Labels ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

label_gold = Label(fenetre, anchor=NW, width=40, height=5, text="${}".format(
    argent), relief=FLAT, fg='black', command=None, font=("Helvetica", 16))
label_gold.place(x=10, y=10)

label_meteo = Label(fenetre, bg='#F0F0F0', image=photo_soleil)
label_meteo.place(x=0, y=40)

label_stats = Label(fenetre, width=20, height=5, text="\nCroissance : {}\n\nHydratation : {}\n\nVitalité : {}".format(
    0, 1000, 1000), relief=FLAT, fg='black', command=None)
label_stats.pack(side=TOP, padx=5, pady=5)
label_stats.config(fg='Black', bd=12)

bouton_arroser = Button(fenetre, width=25, height=5,
                        text="Arroser la fleur", command=arroser_fleur)
bouton_acheter = Button(fenetre, width=25, height=5,
                        text="Acheter une fleur", command=acheter_fleur)
bouton_vendre = Button(fenetre, width=25, height=5,
                       text="Vendre la fleur", command=vendre_fleur)
bouton_jeter = Button(fenetre, width=25, height=5,
                      text="Jeter la fleur", command=jeter_fleur)

bouton_jeter.pack(side=BOTTOM, padx=5, pady=5)
bouton_vendre.pack(side=BOTTOM, padx=5, pady=5)
bouton_acheter.pack(side=BOTTOM, padx=5, pady=5)
bouton_arroser.pack(side=BOTTOM, padx=5, pady=5)

# Calendrier ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LJours = ("Lundi", "Mardi", "Mercredi", "Jeudi",
          "Vendredi", "Samedi", "Dimanche")
LMois = (("Janvier", 31), ("Février", 28), ("Mars", 31), ("Avril", 30), ("Mai", 31), ("Juin", 30),
         ("Juillet", 31), ("Août", 31), ("Septembre", 30), ("Octobre", 31), ("Novembre", 30), ("Décembre", 31))

Calendrier = Canvas(fenetre, width=244, height=284, bg='#F0F0F0')
Calendrier.pack(side=BOTTOM, padx=5, pady=5)

Calendrier.create_text(122, 20, tags="année")
Calendrier.create_text(122, 50, tags="mois")

# Affichage des jours (lundi mardi mercredi...) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

a = 0
x = 20
for i in range(7):
    Calendrier.create_text(x, 80, text=LJours[a][0])
    a += 1
    x += 35

# Affichage du numero du jour (le trois octobre: le 3.) ~~~~~~~~~~~~~~~~~~

a = 1
x = 20
y = 110
for i in range(6):
    for u in range(7):
        # premier tag a partir de 10. me demande pas. python powa
        Calendrier.create_text(x, y, tags=a)
        a += 1
        x += 35
    y += 30
    x = 20

x0 = 10
x1 = 30
y0 = 100
y1 = 120
for i in range(6):
    for u in range(7):
        Calendrier.create_rectangle(
            x0, y0, x1, y1, tags=a, fill='', outline='red', width=0)
        x0 += 35
        x1 += 35
        a += 1
    y0 += 30
    y1 += 30
    x0 = 10
    x1 = 30

Calendrier.itemconfig(date[4], width=2)

aff(date, LMois, Calendrier)

# Calendrier.itemconfig("10", text="42", fill='black') # pour les texte. tags : [10, 51]
# Calendrier.itemconfig("52", width=1) # pour les cadres. tags : [52, 93]

# Mainloop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

programme.start()
fenetre.mainloop()
