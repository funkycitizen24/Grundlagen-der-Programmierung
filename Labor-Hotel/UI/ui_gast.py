from tkinter import *
import webbrowser
from Entities.Gast import Gast


class gast_GUI:
    def __init__(self, gui_master, controller, zimmer, reservierungen):
        self.__window = gui_master
        self.__controller = controller
        self.__zimmer = zimmer
        self.__reservierungen = reservierungen

        self.__vorname_txt = Entry(self.__window, width=25)
        self.__nachname_txt = Entry(self.__window, width=25)

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
        self.__window.title("Menu Gast")

        # UI
        intro = Label(self.__window, text='- MENU GAST -', font='Arial 10')
        intro.grid(column=0, row=0)

        hihi = Label(self.__window, text='Made by the best FP team :)', font='Arial 8')
        hihi.place(relx=1.0, rely=1.0, anchor=SE)

        vorname = Label(self.__window, text='Vorname: ')
        vorname.grid(column=0, row=1)
        self.__vorname_txt.grid(column=1, row=1)

        nachname = Label(self.__window, text='Nachname: ')
        nachname.grid(column=0, row=2)
        self.__nachname_txt.grid(column=1, row=2)

        btn1 = Button(self.__window, text='Füge ein neuen Gast', font='Arial 10', width=19, relief=GROOVE,  activebackground='gray', activeforeground='white', command=self.__add_gast)
        btn1.grid(column=0, row=3)

        btn2 = Button(self.__window, text='Aktualisierung der Name', font='Arial 10', width=19, relief=GROOVE,  activebackground='gray', activeforeground='white', command=self.__change_name)
        btn2.grid(column=1, row=3)

        btn3 = Button(self.__window, text='Lösche ein Gast', font='Arial 10', width=19, relief=GROOVE,  activebackground='gray', activeforeground='white', command=self.__delete_name)
        btn3.grid(column=2, row=3)

        btn4 = Button(self.__window, text='Zeige alle Gäste', font='Arial 10', width=19, relief=GROOVE,  activebackground='gray', activeforeground='white', command=self.__print_list)
        btn4.grid(column=1, row=4)

        btn_return = Button(self.__window, text='<', font='Arial 10', width=2, relief=GROOVE, activebackground='gray', activeforeground='white', command=self.__window.destroy)
        btn_return.place(relx=0.0, rely=0.0, anchor=NW)

        btn_help = Button(self.__window, text='?', font='Arial 10', width=2, relief=GROOVE, activebackground='light blue', command=lambda: webbrowser.open_new('https://support.google.com/?hl=en'))
        btn_help.place(relx=1.0, rely=0.1, anchor=NE)

        btn_exit = Button(self.__window, text='x', font='Arial 10', width=2, relief=GROOVE, activebackground='red', activeforeground='white', command=self.__window.destroy)
        btn_exit.place(relx=1.0, rely=0.0, anchor=NE)

    # Commands for buttons

    def __add_gast(self):
        gast = Gast(self.__vorname_txt.get(), self.__nachname_txt.get(), 0)
        self.__controller.add(gast)

        # clear textboxes
        self.__vorname_txt.delete(0, 'end')
        self.__nachname_txt.delete(0, 'end')

    def __change_name(self):
        gast = Gast(self.__vorname_txt.get(), self.__nachname_txt.get(), 0)
        self.__controller.change_name(gast)

        # clear textboxes
        self.__vorname_txt.delete(0, 'end')
        self.__nachname_txt.delete(0, 'end')

    def __delete_name(self):
        gast = Gast(self.__vorname_txt.get(), self.__nachname_txt.get(), 0)
        self.__controller.delete(gast)

        # clear textboxes
        self.__vorname_txt.delete(0, 'end')
        self.__nachname_txt.delete(0, 'end')

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
    print_window.title('Liste von Gäste')

    # TextBox
    text = Text(print_window)
    text.insert(INSERT, print_elements)
    text.tag_add("here", "1.0", "end")
    text.tag_config('here', font='Courier 8')
    text.pack()
