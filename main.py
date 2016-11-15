# -*- coding: utf-8 -*-

# Import ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from bin.fonctions import *
from bin.Interface import *
from bin.Fleur import *
from bin.Meteo import *
from bin.save import *

from threading import *
from tkinter import *
from math import *

import tkinter.messagebox
import time

parametres = charger_parametres()

stop = True
continuer = continuer_test(0)
# [Jour, Mois, Années, Jour, rectangle afficheur calendrier, ticks, jour]


def load():
    global interface, main_fenetre
    save = charger_save()
    if save is None:
        pass
    else:
        interface.date = save["date"]
        interface.argent = save["fric"]
        main_fenetre.fleurs = save["fleur"]
        main_fenetre.Meteo = save["meteo"]

        b = 0
        for i in main_fenetre.fleurs:
            if i is not None:
                main_fenetre.boutons_fleur[b].config(
                    image=main_fenetre.photo["fleur"])
            b += 1
        del b

        main_fenetre.label_gold.config(text="${}".format(interface.argent))
        tkinter.messagebox.showinfo(
            'Charger !', 'Votre partie a été bien charger !')
        pause_resume(0)


def main():

    global interface, continuer, stop

    while stop:

        continuer = continuer_test(0)
        load()
        if continuer:
            main_fenetre.afficheur_calendrier(interface)

        while continuer:

            continuer = continuer_test(0)

            for fleur in main_fenetre.fleurs:
                if fleur is not(None):
                    fleur.tic()

            interface.date[5] += 1
            if interface.date[5] == int(parametres["VitesseJour"]):
                interface.date = main_fenetre.jour(interface)
                main_fenetre.Meteo = test_temps(main_fenetre.Meteo)

                if degage(main_fenetre.Meteo):
                    main_fenetre.label_meteo.config(
                        image=main_fenetre.photo["soleil"])
                elif nuageux1(main_fenetre.Meteo):
                    main_fenetre.label_meteo.config(
                        image=main_fenetre.photo["nuage_1"])
                elif nuageux2(main_fenetre.Meteo):
                    main_fenetre.label_meteo.config(
                        image=main_fenetre.photo["nuage_2"])
                elif nuageux3(main_fenetre.Meteo):
                    main_fenetre.label_meteo.config(
                        image=main_fenetre.photo["nuage_3"])
                elif nuageux4(main_fenetre.Meteo):
                    main_fenetre.label_meteo.config(
                        image=main_fenetre.photo["nuage_4"])
                elif nuageux5(main_fenetre.Meteo):
                    main_fenetre.label_meteo.config(
                        image=main_fenetre.photo["nuage_5"])
                elif pluvieux(main_fenetre.Meteo):
                    main_fenetre.label_meteo.config(
                        image=main_fenetre.photo["pluie"])

                if interface.date[0] == 1:
                    main_fenetre.afficheur_calendrier(interface)
                interface.date[5] = 0

            if main_fenetre.choix_fleur.get() == "":
                main_fenetre.label_stats.configure(
                    main_fenetre.label_stats, text="\nCroissance : {}\n\nHydratation : {}\n\nVitalité : {}".format(0, 0, 0))

            elif main_fenetre.fleurs[int(main_fenetre.choix_fleur.get())] is None:
                main_fenetre.label_stats.configure(
                    main_fenetre.label_stats, text="\nCroissance : {}\n\nHydratation : {}\n\nVitalité : {}".format(0, 0, 0))

            else:
                choix = int(main_fenetre.choix_fleur.get())
                main_fenetre.label_stats.configure(main_fenetre.label_stats, text="\nCroissance : {}\n\nHydratation : {}\n\nVitalité : {}".format(
                    main_fenetre.fleurs[choix].croissance, main_fenetre.fleurs[choix].hydratation, main_fenetre.fleurs[choix].vitalite))
            time.sleep(eval(parametres["VitesseTic"]))

programme = Thread(target=main)

# Fenêtre ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

interface = Interface()

main_fenetre = Main_Fenetre(interface)

# Mainloop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

programme.start()
interface.fenetre.mainloop()
interface.fenetre.destroy()
