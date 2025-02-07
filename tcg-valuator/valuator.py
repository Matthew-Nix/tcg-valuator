from tkinter import *
from tkinter import ttk

class Valuator:
    def __init__(self, root):

        root.title("TCG Valuator")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
       
        self.card_name = StringVar()
        card_entry = ttk.Entry(mainframe, width = 20, textvariable=self.card_name)
        card_entry.grid(column=2, row=1, sticky=(W, E))
        self.card_value = StringVar()

        ttk.Label(mainframe, textvariable=self.card_value).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text='Calculate', command=self.calculate).grid(column=3, row=3, sticky=W)


    def calculate(self, *args):
        try:
            value = self.card_name.get()
            self.card_value.set(value + " is big monies")
        except ValueError:
            pass