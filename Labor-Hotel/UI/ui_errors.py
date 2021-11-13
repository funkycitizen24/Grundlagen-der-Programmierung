from tkinter import messagebox


# Gast
def invalid_vornanme(vorname):
    messagebox.askretrycancel('Invalid name', 'Dein Vorname, %s, ist nicht korekt!' % vorname)


def invalid_nachnanme(nachname):
    messagebox.askretrycancel('Invalid name', 'Dein Nachname, %s, ist nicht korekt!' % nachname)


def gast_inlist(vorname, nachname):
    messagebox.askretrycancel('Achtung', '%s %s ist schon in unsere Liste' % (vorname, nachname))


def gast_notinlist(vorname, nachname):
    messagebox.askretrycancel('Achtung', '%s %s ist nicht in unsere Liste' % (vorname, nachname))


# Zimmer
def already_room(number):
    messagebox.askretrycancel('Achtung', 'Das Zimmer mit der Nummer: "%s" ist schon in der Liste.' % number)


def not_number(element):
    messagebox.askretrycancel('Achtung', 'Bitte ein ganzen Zahl schreiben. "%s" ist nicht eine ganze Zahl.' % element)


def invalid_color(color):
    messagebox.askretrycancel('Invalid color', 'Deine Farbe, %s, ist nicht korekt!' % color)


def invalid_mehrblick():
    messagebox.askretrycancel('Invalid choice', 'Deine Farbe, %s, ist nicht korekt!')


def room_not_found(number):
    messagebox.askretrycancel('Achtung', 'Das Zimmer mit der Nummer: "%s" ist nicht in der Liste.' % number)


def wrong_anzahl():
    messagebox.askretrycancel('Achtung', 'Es gibt keine Zimmer mit den eingegebenen Anzahl von Gästen.')


def preis_not_found():
    messagebox.askretrycancel('Achtung', 'Es gibt keine Zimmer mit den eingegebenen Eigenschaften.')
