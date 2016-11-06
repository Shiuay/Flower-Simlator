# -*- coding: utf-8 -*-

import os, pickle
from random  import *
from math    import *
from tkinter import *

continuer = True

def inclinaison_soleil(latitude, jour):

    declinaison = 23.45 * sin(((2*pi)/365) * (jour + 284))
    hauteur = latitude - declinaison
    exposition = cos(radians(hauteur)) * 100
    return exposition

def alea(x):

    """Renvoie True avec une probabilité de x%"""
    if random() * 100 < x:
        return True
    else:
        return False

def continuer_test():
    global continuer
    return continuer

def sauvegarder_partie(*args):

    global continuer

    def save():
        global alert, msg, name, continuer
        path = "Save/" + name + ".plantes"
        with open(path, "wb") as Save:
            mon_pickler = pickle.Pickler(Save)
            for i in args:
                mon_pickler.dump(i)
        alert.title("Completed")
        msg.config(text="Partie sauvegarder !")
        button = Button(alert, width=7, text="Ok", command=delete)
        button.pack(side=TOP, padx=5, pady=5)
        continuer = True

    def set():
        global alert, msg
        alert = Tk()
        alert.resizable(width=False, height=False)
        msg = Message(alert, width=400)
        msg.pack(side=TOP, padx=5, pady=5)

    def delete():
        global alert
        alert.destroy()

    def reset():
        delete()
        set()

    def get():
        global alert, texte, name
        def testo():
            reset()
            save()

        def testn():
            reset()
            main()

        name = texte.get()
        if os.path.exists('Save\\' + name + '.plantes'):
            reset()
            alert.title("Confirmer l'enregistrement")
            msg.config(text="Cette sauvegarde existe déja.\nVoulez vous le remplacer ?")
            button1 = Button(alert, width=7, text="Oui", command=testo)
            button2 = Button(alert, width=7, text="Non", command=testn)
            button1.pack(side=LEFT, padx=5, pady=5)
            button2.pack(side=RIGHT, padx=5, pady=5)
        else:
            if name != "":
                reset()
                save()

    def main():
        global alert, button, msg, texte
        alert.title("Sauvegarde")
        msg.config(text="Choisisez le nom de votre sauvegarde :")
        texte = Entry(alert, width=40)
        button = Button(alert, width=7, text="Ok", command=get)
        texte.pack(side=TOP, padx=20, pady=5)
        button.pack(side=TOP, padx=5, pady=10)

    continuer = False
    name = "Sauvegarde"
    set()
    main()

def charger_partie():
    """"""
    pass


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
        