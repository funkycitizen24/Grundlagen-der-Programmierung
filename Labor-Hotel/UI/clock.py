import tkinter as tk
import time

class Clock(tk.Label):
    #diese Klasse zeigt und aktualisiert den aktuellen Zeitraum
    def __init__(self, parent=None, seconds=True, colon=False):
        #clock widget
        tk.Label.__init__(self, parent)
        self.display_seconds = seconds

        if self.display_seconds:
            self.time = time.strftime('%I:%M:%S %p')
        else:
            self.time = time.strftime('%I:%M:%S %p').lstrip('0')
        self.display_time = self.time
        self.configure(text=self.display_time, bg='#ffffe6')

        if colon:
            self.blink_colon()

        self.after(200, self.tick)


    def tick(self):
        #die Zeit jeden 200 Milisekunden aktualisiert
        if self.display_seconds:
            new_time = time.strftime('%I:%M:%S %p')
        else:
            new_time = time.strftime('%I:%M:%S %p').lstrip('0')
        if new_time != self.time:
            self.time = new_time
            self.display_time = self.time
            self.config(text=self.display_time)
        self.after(200, self.tick)

