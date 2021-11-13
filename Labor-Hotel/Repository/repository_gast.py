
from UI.ui_gast import *
from UI.ui_errors import *
from UI.ui_confirmation import *
from Testing.testing import gast_name


class repository_gast:
    def __init__(self,  file='gaeste.txt'):
        self.__fName = file
        self.__liste = []
        self.__loadFromFile()

    # Load from File
    def __loadFromFile(self):
        f = open(self.__fName, 'r')
        for line in f:
            data = line.strip().split(' ')
            try:
                gast = Gast(data[1], data[4], int(data[8]))
                self.__liste.append(gast)
            except ValueError:
                print('Bitte den Datein korekt schreiben!')

    # Store to File
    def __storeToFile(self):
        f = open(self.__fName, 'w')
        for el in self.__liste:
            f.write(str(el) + '\n')
        f.close()

    # Check if a guest is already in list
    def check_name(self, gast):
        for el in range(len(self.__liste)):
            if gast.vorname == self.__liste[el].vorname and gast.nachname == self.__liste[el].nachname:
                return True
        return False

    # Add Guest
    def add_gast(self, gast):
        try:
            vorname = gast.vorname
            gast_name(vorname)
            assert gast_name(vorname) is True
        except AssertionError:
            return invalid_vornanme(vorname)

        try:
            nachname = gast.nachname
            gast_name(nachname)
            assert gast_name(nachname) is True
        except AssertionError:
            return invalid_nachnanme(nachname)

        else:
            gast = Gast(vorname, nachname, 0)
            if self.check_name(gast) is True:
                gast_inlist(vorname, nachname)
            else:
                self.__liste.append(gast), self.__storeToFile(), new_gast_welcome(vorname, nachname)

    # Change Guest last name
    def change_name(self, gast):
        ok = 0
        for el in range(len(self.__liste)):
            if gast.vorname == self.__liste[el].vorname:
                ok = ok + 1
                self.__liste.pop(el)
                self.__liste.insert(el, gast)
                self.__storeToFile()
                change_name_confirmation(gast.vorname, gast.nachname)
        if ok == 0:
            gast_notinlist(gast.vorname, gast.nachname)

    # Delete Guest
    def delete_gast(self, gast):
        el = 0
        ok = 0
        while el < len(self.__liste):
            if gast.vorname == self.__liste[el].vorname and gast.nachname == self.__liste[el].nachname:
                self.__liste.pop(el)
                ok = ok + 1
                self.__storeToFile()
                delete_name_confirmation(gast.vorname, gast.nachname)
            else:
                el = el + 1
        if ok == 0:
            gast_notinlist(gast.vorname, gast.nachname)

    # Show all Guests
    def print_gast(self):
        print_elements = ('\n'.join(map(str, self.__liste)))
        print_liste(print_elements)

    # Shows that a guest has a room (Reservierungen)
    def add_reserv(self, vorname, nachname, nummer):
        for el in range(len(self.__liste)):
            if vorname == self.__liste[el].vorname and nachname == self.__liste[el].nachname:
                self.__liste[el].reservierungen = nummer
                self.__storeToFile()

# For timer (Threads)
                # seconds = (zeitrraum - datetime.now()) * 86400
                # seconds = 30
                # while seconds > 0:
                #     seconds = seconds - 1
                #     time.sleep(1)
                # self.__liste[el].reservierungen = 0
