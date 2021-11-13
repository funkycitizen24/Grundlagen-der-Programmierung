from tkinter import *
import webbrowser
from UI.ui_gast import gast_GUI
from UI.ui_zimmer import zimmer_GUI
from UI.ui_reservierungen import reservierungen_GUI
# import pygame
# pygame.mixer.init()
# pygame.init()

class menu_GUI:
    # clock = pygame.time.Clock() #ora actuala pe fereastra

    def __init__(self, gui_master, controller_gast, controller_zimmer, controller_reservierungen):
        self.__window = gui_master
        self.__controller_gast = controller_gast
        self.__controller_zimmer = controller_zimmer
        self.__controller_reservierungen = controller_reservierungen

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
        self.__window.title("Hotel")

        # UI
        intro = Label(self.__window, text='Herzliche Willkommen bei unserer Hotel!', font='Arial 12', bg='light blue')
        intro.place(relx=0.5, rely=0.1, anchor=CENTER)

        hihi = Label(self.__window, text='Made by the best FP team :)', font='Arial 8')
        hihi.place(relx=1.0, rely=1.0, anchor=SE)

        btn_gast = Button(self.__window, text='Gäste', font='Arial 10', width=12, relief=GROOVE,  bg='gray', fg='white', command=self.__menu_gast)
        btn_gast.place(relx=0.5, rely=0.2, anchor=CENTER)

        btn_zimmer = Button(self.__window, text='Zimmern', font='Arial 10', width=12, relief=GROOVE, bg='gray', fg='white', command=self.__menu_zimmer)
        btn_zimmer.place(relx=0.5, rely=0.3, anchor=CENTER)

        btn_reservierung = Button(self.__window, text='Reservierungen', font='Arial 10',   width=12, relief=GROOVE, bg='gray', fg='white', command=self.__menu_reservierungen)
        btn_reservierung.place(relx=0.5, rely=0.4, anchor=CENTER)

        btn_help = Button(self.__window, text='?', font='Arial 10', width=2, relief=GROOVE, bg='light blue', command=lambda: webbrowser.open_new('https://support.google.com/?hl=en'))
        btn_help.place(relx=1.0, rely=0.1, anchor=NE)

        btn_exit = Button(self.__window, text='x', font='Arial 10', width=2, relief=GROOVE, bg='brown', fg='white', command=quit)
        btn_exit.place(relx=1.0, rely=0.0, anchor=NE)


    # Commands for buttons
    def __menu_gast(self):
        self.__window = Tk()
        self.app = gast_GUI(self.__window, self.__controller_gast, self.__controller_zimmer, self.__controller_reservierungen)
        self.app.draw_window()
        self.__window.mainloop()


    def __menu_zimmer(self):
        self.__window = Tk()
        self.app = zimmer_GUI(self.__window, self.__controller_gast, self.__controller_zimmer, self.__controller_reservierungen)
        self.app.draw_window()
        self.__window.mainloop()

    def __menu_reservierungen(self):
        self.__window = Tk()
        self.app = reservierungen_GUI(self.__window, self.__controller_gast, self.__controller_zimmer, self.__controller_reservierungen)
        self.app.draw_window()
        self.__window.mainloop()
