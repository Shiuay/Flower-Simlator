# -*- coding: utf-8 -*-

import os, pickle, tkinter.messagebox

from random  import *
from math    import *
from tkinter import *

continuer    = [True, False]
save_plantes = []

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

def pause_resume():
    global continuer
    if continuer[0] == True:
        continuer[0] = False
    else:
        continuer[0] = True

def continuer_test():
    global continuer
    return continuer[0]

def sauvegarder_partie(**args):

    global continuer

    def save(alert, name):
        global continuer
        alert.destroy()
        with open("save/" + name + ".plantes", "wb") as save:
            mon_pickler = pickle.Pickler(save)
            mon_pickler.dump(args)
        tkinter.messagebox.showinfo('Completed !', 'Partie sauvegarder avec succes !')
        continuer[0] = True

    def get(texte, alert):
        name = texte.get()
        if name != "":
            if os.path.exists('save\\' + name + '.plantes'):
                if tkinter.messagebox.askyesno("Confirmer l'enregisterment", "Ce fichier existe déja. voulez vous le remplacer ?"):
                    save(alert, name)
            else:
                save(alert, name)

    continuer[0] = False

    def main():
        alert = Tk()
        alert.title("Sauvegarde")
        msg = Message(alert, width=400, text="Choisisez le nom de votre sauvegarde :")
        msg.pack(side=TOP, padx=5, pady=5)
        texte = Entry(alert, width=40)
        texte.pack(side=TOP, padx=20, pady=5)
        button = Button(alert, width=7, text="Ok", command=lambda:get(texte, alert))
        button.pack(side=TOP, padx=5, pady=10)

    main()

def charger_save():
    global save_plantes, continuer
    if continuer[1] == True:
        continuer[1] = False
        return save_plantes[0]

def charger_partie():

    global continuer

    def charger(name):
        global save_plantes, continuer
        with open("save/" + name + ".plantes", "rb") as save:
            pickler = pickle.Unpickler(save)
            save_plantes.append(pickler.load())
            continuer[1] = True

    def split_plante(fichier):
        for i in range(len(fichier)):
            fichier[i] = fichier[i][:-8]
        return fichier

    def setargs():
        nom = os.listdir('Save')
        nom = [nb for nb in nom if nb.endswith(".plantes")]
        return split_plante(nom)

    def get(alerte):
        args = setargs()
        name = liste.curselection()
        name = args[name[0]]
        alerte.destroy()
        charger(name)

    continuer[0] = False
    args = setargs()

    if args != []:
        alerte = Tk()
        alerte.resizable(width=False, height=False)
        msg = Message(alerte, width=400)
        msg.pack(side=TOP, padx=5, pady=5)

        liste = Listbox(alerte, exportselection=0, selectmode='single')
        liste.pack(padx=5, pady=5)

        for i in args:
            liste.insert('end', i)

        button = Button(alerte, text="Ok", width=7, command=lambda:get(alerte))
        button.pack(side=TOP, padx=5, pady=10)

    else:
        tkinter.messagebox.showerror("Erreur !", "Désoler, il n'y a pas de sauvegarde valide dans votre fichier \"save\".")

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
        