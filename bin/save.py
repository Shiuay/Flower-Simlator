
import os
import pickle
import tkinter.messagebox

from bin.fonctions import pause_resume, continuer_test
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

    def delete(alert):
        alert.destroy()
        pause_resume(0)

    pause_resume(0)

    def main():
        alert = Tk()
        alert.title("Sauvegarde")
        msg = Message(alert, width=400,
                      text="Choisisez le nom de votre sauvegarde :")
        msg.pack(side=TOP, padx=5, pady=5)
        texte = Entry(alert, width=40)
        texte.pack(side=TOP, padx=10, pady=5)
        button = Button(alert, width=7, text="Ok",
                        command=lambda: get(texte, alert))
        annuler = Button(alert, width=7, text="Annuler",
                         command=lambda: delete(alert))
        annuler.pack(side=RIGHT, padx=40, pady=10)
        button.pack(side=LEFT, padx=40, pady=10)

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

    def delete(alert):
        alert.destroy()
        pause_resume(0)

    args = setargs()

    if args != []:
        pause_resume(0)
        alerte = Tk()
        alerte.title("Charger")
        alerte.resizable(width=False, height=False)
        msg = Message(alerte, width=400)
        msg.pack(side=TOP, padx=5, pady=5)

        liste = Listbox(alerte, exportselection=0, width=40, selectmode='single')
        liste.pack(padx=5, pady=5)

        for i in args:
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
            liste.insert('end', i)

        button = Button(alerte, text="Ok", width=7,
                        command=lambda: get(alerte))
        annuler = Button(alerte, width=7, text="Annuler",
                         command=lambda: delete(alerte))
        annuler.pack(side=RIGHT, padx=35, pady=10)
        button.pack(side=LEFT, padx=35, pady=10)

    else:
        tkinter.messagebox.showerror(
            "Erreur !", "Désoler, il n'y a pas de sauvegarde valide dans votre fichier \"save\".")


def charger_save():
    global save_plantes
    if continuer_test(1) == True:
        pause_resume(1)
        return save_plantes[0]
