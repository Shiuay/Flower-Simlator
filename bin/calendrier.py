# -*- coding: utf-8 -*-

# Calendrier.itemconfig("10", text="42", fill='black') # pour les texte. tags : [10, 51]
# Calendrier.itemconfig("52", width=1) # pour les cadres. tags : [52, 93]


def aff(date, c):

    mois = (("Janvier", 31), ("Février", 28), ("Mars", 31), ("Avril", 30), ("Mai", 31), ("Juin", 30),
            ("Juillet", 31), ("Août", 31), ("Septembre", 30), ("Octobre", 31), ("Novembre", 30), ("Décembre", 31))

    # [Jour, Mois, Années, Jour, rectangle afficheur calendrier, ticks, jour]

    t = 10

    # remise a zero du carré rouge de selection de date

    for i in range(52, 93):
        c.itemconfig(i, width=0)

    for i in range(42):
        c.itemconfig(t, text="", fill='black')
        t += 1

    c.itemconfig(date[4], width=2)

    # Affichage du mois et de l'année

    c.itemconfig("année", text=date[2])
    c.itemconfig("mois", text=mois[date[1] - 1][0])

    # Création du calendrier

    t = date[6] + 10
    for i in range(mois[date[1] - 1][1]):
        r = i + 1
        c.itemconfig(t, text=r, fill='black')
        t += 1

    r = 1
    while 52 != t:
        c.itemconfig(t, text=r, fill='gray')
        r += 1
        t += 1

    t = date[6] + 9

    try:
        tgris = mois[date[1] - 2][1]
    except:
        tgris = mois[11][1]

    while 11 != tgris and t != 9:
        c.itemconfig(t, text=tgris, fill='gray')
        t -= 1
        tgris -= 1


def jour(date, c):

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
    date[0] += 1
    date[6] += 1
    if date[6] == 7:
        date[6] = 0

    date[3] = jour[date[6]]

    # check si le mois est terminer

    if date[1] == 1 or \
            date[1] == 3  or \
            date[1] == 5  or \
            date[1] == 7  or \
            date[1] == 8  or \
            date[1] == 10 or \
            date[1] == 12:

        if date[0] == 32:
            date = adv(date)

    elif date[1] == 4 or \
            date[1] == 6 or \
            date[1] == 9 or \
            date[1] == 11:

        if date[0] == 31:
            date = adv(date)

    elif date[1] == 2:

        if date[0] == 29:
            date = adv(date)

        # check si année fini

    if date[1] == 13:
        date[1] = 1
        date[2] += 1

    c.itemconfig(date[4], width=0)
    date[4] += 1
    if date[0] == 1:
        date[4] = date[6] + 52
    c.itemconfig(date[4], width=2)

    return date
