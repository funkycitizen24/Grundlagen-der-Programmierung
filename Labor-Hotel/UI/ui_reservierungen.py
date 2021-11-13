from tkinter import *
import webbrowser
from datetime import datetime


class reservierungen_GUI:
    def __init__(self, gui_master, gast, controller_zimmer, controller_reservierungen):
        self.__window = gui_master
        self.__gast = gast
        self.__controller_zimmer = controller_zimmer
        self.__controller_reservierungen = controller_reservierungen

        self.__vorname_txt = Entry(self.__window, width=10)
        self.__nachname_txt = Entry(self.__window, width=10)
        self.__anzahl_gaste_txt = Entry(self.__window, width=10)
        self.__wahl_txt = Entry(self.__window, width=10)
        self.__anzahl_nacht_txt = Entry(self.__window, width=10)
        self.__preis_txt = Entry(self.__window, width=10)
        self.__mehrblick = "NA"

    def draw_window(self):
        w = 525  # width for the window
        h = 300  # height for the window
        # get screen width and height
        ws = self.__window.winfo_screenwidth()  # width of the screen
        hs = self.__window.winfo_screenheight()  # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.__window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.__window.title("Menu Reservierungen")

        # UI
        intro = Label(self.__window, text='- MENU RESERVIERUNGEN -', font='Arial 10')
        intro.grid(column=0, row=0)

        hihi = Label(self.__window, text='Made by the best FP team :)', font='Arial 8')
        hihi.place(relx=1.0, rely=1.0, anchor=SE)

        anzahl = Label(self.__window, text='Anzahl der Gäste: ')
        anzahl.grid(column=0, row=1)
        self.__anzahl_gaste_txt.grid(column=1, row=1)

        btn1 = Button(self.__window, text='Suche Zimmer', font='Arial 10', width=12, relief=GROOVE,  bg='gray', fg='white', command=self.__anzahl_gaste)
        btn1.grid(column=1, row=2)

        vorname = Label(self.__window, text='Vorname: ')
        vorname.grid(column=0, row=3)
        self.__vorname_txt.grid(column=1, row=3)

        nachname = Label(self.__window, text='Nachname: ')
        nachname.grid(column=0, row=4)
        self.__nachname_txt.grid(column=1, row=4)

        wahl = Label(self.__window, text='Nummer der gewählte Zimmer: ')
        wahl.grid(column=0, row=5)
        self.__wahl_txt.grid(column=1, row=5)

        nacht = Label(self.__window, text='Anazhl der Nächte: ')
        nacht.grid(column=0, row=6)
        self.__anzahl_nacht_txt.grid(column=1, row=6)

        btn2 = Button(self.__window, text='Mach den Reservierung', font='Arial 10', width=17, relief=GROOVE,  bg='gray', fg='white', command=self.__make_a_reservation)
        btn2.grid(column=1, row=7)

        btn3 = Button(self.__window, text='Zimmer die ' + datetime.today().strftime('%d %B %Y') + ' frei sind', font='Arial 10', width=30, relief=GROOVE,  bg='gray', fg='white', command=self.__free_rooms_today)
        btn3.grid(column=0, row=8)

        btn4 = Button(self.__window, text='Zeige die Liste von Reservierungen', font='Arial 10', width=25, relief=GROOVE,  bg='gray', fg='white', command=self.__print_list)
        btn4.grid(column=1, row=8)

        preis = Label(self.__window, text='Preis: ')
        preis.grid(column=0, row=9)
        self.__preis_txt.grid(column=1, row=9)

        mehrblick = Label(self.__window, text='Mehrblick: ')
        mehrblick.grid(column=0, row=10)

        i = StringVar()
        ja_rbtn = Radiobutton(self.__window, text='Ja', value=0, variable=i, command=self.setJa)
        nein_rbtn = Radiobutton(self.__window, text='Nein', value=1, variable=i, command=self.setNein)
        ja_rbtn.grid(column=1, row=10)
        nein_rbtn.grid(column=2, row=10)

        btn5 = Button(self.__window, text='Filtern nach Preis und Mehrblick', font='Arial 10', width=23, relief=GROOVE,  bg='gray', fg='white', command=self.__filter)
        btn5.grid(column=0, row=11)

        btn_return = Button(self.__window, text='<', font='Arial 10', width=2, relief=GROOVE, bg='gray', fg='white', command=self.__window.destroy)
        btn_return.place(relx=0.0, rely=0.0, anchor=NW)

        btn_help = Button(self.__window, text='?', font='Arial 10', width=2, relief=GROOVE, bg='light blue', command=lambda: webbrowser.open_new('https://support.google.com/?hl=en'))
        btn_help.place(relx=1.0, rely=0.1, anchor=NE)

        btn_exit = Button(self.__window, text='x', font='Arial 10', width=2, relief=GROOVE, bg='red', fg='white', command=quit)
        btn_exit.place(relx=1.0, rely=0.0, anchor=NE)

    # Commands for buttons
    def __anzahl_gaste(self):
        self.__controller_zimmer.anzahl(self.__anzahl_gaste_txt.get())

    def __make_a_reservation(self):
        self.__controller_reservierungen.add(self.__vorname_txt.get(), self.__nachname_txt.get(), self.__wahl_txt.get(), self.__anzahl_nacht_txt.get(), self.__anzahl_gaste_txt.get())

        # clear textboxes
        self.__vorname_txt.delete(0, 'end')
        self.__nachname_txt.delete(0, 'end')
        self.__anzahl_gaste_txt.delete(0, 'end')
        self.__wahl_txt.delete(0, 'end')
        self.__anzahl_nacht_txt.delete(0, 'end')

    def __free_rooms_today(self):
        self.__controller_zimmer.frei()

    def __filter(self):
        self.__controller_zimmer.filter(self.__preis_txt.get(), self.__mehrblick)

        # clear textboxes
        self.__preis_txt.delete(0, 'end')

    def setJa(self):
        self.__mehrblick = "Ja"  # sets Mehrblick to Ja

    def setNein(self):
        self.__mehrblick = "Nein"  # sets Mehrblick to Nein

    def __print_list(self):
        self.__controller_reservierungen.print()


# Print elements in new window
def print_liste_anzahl(print_elements):
    print_window = Tk()
    w = 525  # width for the window
    h = 300  # height for the window

    # get screen width and height
    ws = print_window.winfo_screenwidth()  # width of the screen
    hs = print_window.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    print_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    print_window.title('Liste von Reservierungen')

    # TextBox
    text = Text(print_window)
    text.insert(INSERT, print_elements)
    text.tag_add("here", "1.0", "end")
    text.tag_config('here', font='Courier 8')
    text.pack()
