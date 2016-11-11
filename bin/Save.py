
import os
import pickle
import tkinter.messagebox

from bin.Fonctions import pause_resume, continuer_test
from tkinter import *

save_plantes = []


def sauvegarder_partie(**args):

    def save(alert, name):
        alert.destroy()
        with open("save/" + name + ".plantes", "wb") as save:
            mon_pickler = pickle.Pickler(save)
            mon_pickler.dump(args)
        tkinter.messagebox.showinfo(
            'Completed !', 'Partie sauvegarder avec succes !')
        pause_resume(0)

    def get(texte, alert):
        name = texte.get()
        if name != "":
            if os.path.exists('save\\' + name + '.plantes'):
                if tkinter.messagebox.askyesno("Confirmer l'enregisterment", "Ce fichier existe déja. voulez vous le remplacer ?"):
                    save(alert, name)
            else:
                save(alert, name)

    pause_resume(0)

    def main():
        alert = Tk()
        alert.title("Sauvegarde")
        msg = Message(alert, width=400,
                      text="Choisisez le nom de votre sauvegarde :")
        msg.pack(side=TOP, padx=5, pady=5)
        texte = Entry(alert, width=40)
        texte.pack(side=TOP, padx=20, pady=5)
        button = Button(alert, width=7, text="Ok",
                        command=lambda: get(texte, alert))
        button.pack(side=TOP, padx=5, pady=10)

    main()


def charger_partie():

    def charger(name):
        global save_plantes
        with open("save/" + name + ".plantes", "rb") as save:
            pickler = pickle.Unpickler(save)
            save_plantes.append(pickler.load())
            pause_resume(1)

    def setargs():
        nom = os.listdir('Save')
        nom = [nb for nb in nom if nb.endswith(".plantes")]
        for i in range(len(nom)):
            nom[i] = nom[i][:-8]
        return nom

    def get(alerte):
        args = setargs()
        name = liste.curselection()
        name = args[name[0]]
        alerte.destroy()
        charger(name)

    pause_resume(0)
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

        button = Button(alerte, text="Ok", width=7,
                        command=lambda: get(alerte))
        button.pack(side=TOP, padx=5, pady=10)

    else:
        tkinter.messagebox.showerror(
            "Erreur !", "Désoler, il n'y a pas de sauvegarde valide dans votre fichier \"save\".")


def charger_save():
    global save_plantes
    if continuer_test(1) == True:
        pause_resume(1)
        return save_plantes[0]