from tkinter import *
import webbrowser
from Entities.Zimmer import Zimmer


class zimmer_GUI:
    def __init__(self, gui_master, gast, controller, reservierungen):
        self.__window = gui_master
        self.__gast = gast
        self.__controller = controller
        self.__reservierungen = reservierungen

        self.__nummer_txt = Entry(self.__window, width=10)
        self.__anzahl_txt = Entry(self.__window, width=10)
        self.__preis_txt = Entry(self.__window, width=10)
        self.__farbe_txt = Entry(self.__window, width=10)
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
        self.__window.title("Menu Zimmer")

        # UI
        intro = Label(self.__window, text='- MENU ZIMMER -', font='Arial 10')
        intro.grid(column=0, row=0)

        hihi = Label(self.__window, text='Made by the best FP team :)', font='Arial 8')
        hihi.place(relx=1.0, rely=1.0, anchor=SE)

        nummer = Label(self.__window, text='Nummer: ')
        nummer.grid(column=0, row=1)
        self.__nummer_txt.grid(column=1, row=1)

        anzahl = Label(self.__window, text='Anzahl der Gäste: ')
        anzahl.grid(column=0, row=2)
        self.__anzahl_txt.grid(column=1, row=2)

        preis = Label(self.__window, text='Preis: ')
        preis.grid(column=0, row=3)
        self.__preis_txt.grid(column=1, row=3)

        farbe = Label(self.__window, text='Farbe: ')
        farbe.grid(column=0, row=4)
        self.__farbe_txt.grid(column=1, row=4)

        mehrblick = Label(self.__window, text='Mehrblick: ')
        mehrblick.grid(column=0, row=5)

        i = StringVar()
        ja_rbtn = Radiobutton(self.__window, text='Ja', value=0, variable=i, command=self.setJa)
        nein_rbtn = Radiobutton(self.__window, text='Nein', value=1, variable=i, command=self.setNein)
        ja_rbtn.grid(column=1, row=5)
        nein_rbtn.grid(column=2, row=5)

        btn1 = Button(self.__window, text='Füge eine neue Zimmer', font='Arial 10', width=19, relief=GROOVE,  bg='gray', fg='white', command=self.__add_zimmer)
        btn1.grid(column=0, row=6)

        btn2 = Button(self.__window, text='Aktualisierung des Preises einer Zimmer', font='Arial 10', width=28, relief=GROOVE,  bg='gray', fg='white', command=self.__change_price)
        btn2.grid(column=1, row=6)

        btn3 = Button(self.__window, text='Lösche ein Zimmer', font='Arial 10', width=15, relief=GROOVE,  bg='gray', fg='white', command=self.__delete_name)
        btn3.grid(column=2, row=6)

        btn4 = Button(self.__window, text='Zeige alle Zimmern', font='Arial 10', width=19, relief=GROOVE,  bg='gray', fg='white', command=self.__print_list)
        btn4.grid(column=1, row=7)

        btn_return = Button(self.__window, text='<', font='Arial 10', width=2, relief=GROOVE, bg='gray', fg='white', command=self.__window.destroy)
        btn_return.place(relx=0.0, rely=0.0, anchor=NW)

        btn_help = Button(self.__window, text='?', font='Arial 10', width=2, relief=GROOVE, bg='light blue', command=lambda: webbrowser.open_new('https://support.google.com/?hl=en'))
        btn_help.place(relx=1.0, rely=0.1, anchor=NE)

        btn_exit = Button(self.__window, text='x', font='Arial 10', width=2, relief=GROOVE, bg='red', command=quit)
        btn_exit.place(relx=1.0, rely=0.0, anchor=NE)

    # Commands for buttons
    def __add_zimmer(self):
        zimmer = Zimmer(self.__nummer_txt.get(), self.__anzahl_txt.get(), self.__preis_txt.get(), self.__farbe_txt.get(), self.__mehrblick, 0)
        self.__controller.add(zimmer)

        # clear textboxes
        self.__nummer_txt.delete(0, 'end')
        self.__anzahl_txt.delete(0, 'end')
        self.__preis_txt.delete(0, 'end')
        self.__farbe_txt.delete(0, 'end')

    def setJa(self):
        self.__mehrblick = "Ja"  # sets Mehrblick to Ja

    def setNein(self):
        self.__mehrblick = "Nein"  # sets Mehrblick to Nein

    def __change_price(self):
        self.__controller.change(self.__nummer_txt.get(), self.__preis_txt.get())

        # clear textboxes
        self.__nummer_txt.delete(0, 'end')
        self.__preis_txt.delete(0, 'end')

    def __delete_name(self):
        self.__controller.delete(self.__nummer_txt.get())

        # clear textboxes
        self.__nummer_txt.delete(0, 'end')
        self.__preis_txt.delete(0, 'end')

    def __print_list(self):
        self.__controller.print()


# Print elements in new window
def print_liste(print_elements):
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
    print_window.title('Liste von Zimmern')

    # TextBox
    text = Text(print_window)
    text.insert(INSERT, print_elements)
    text.tag_add("here", "1.0", "end")
    text.tag_config('here', font='Courier 8')
    text.pack()


# Print elements from filter in new window
def print_liste_preis(print_elements):
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
    print_window.title('Filter nach Preis und Mehrblick')

    # TextBox
    text = Text(print_window)
    text.insert(INSERT, print_elements)
    text.tag_add("here", "1.0", "end")
    text.tag_config('here', font='Courier 8')
    text.pack()
