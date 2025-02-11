from tkinter import *
from tkinter import ttk
from turtle import bgcolor

class Valuator:
    def __init__(self, root):

        root.title("TCG Valuator")

        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
       
        # Text entry to enter card name
        self.card_name = StringVar()
        self.card_entry = ttk.Entry(self.mainframe, width = 50, textvariable=self.card_name)
        self.card_entry.grid(column=1, row=0, sticky=(N, W, E))

        # Calculate and display card value for entered card name
        ttk.Button(self.mainframe, text='Calculate', command=self.calculate).grid(column=2, row=0, sticky=(N, W))
        self.card_value = StringVar()
        ttk.Label(self.mainframe, textvariable=self.card_value).grid(column=2, row=1, sticky=(N, W, E))

        # Display confirmation that card was added to collection
        self.display_message = StringVar()
        ttk.Button(self.mainframe, text='Add to Collection', command=self.add_to_collection).grid(column=3, row = 2, sticky=W)
        ttk.Label(self.mainframe, textvariable=self.display_message).grid(column=2, row=2, sticky=(E))

        # Area to display card art
        display_area = Frame(self.mainframe, bg='red', width=350, height=500)
        display_area.grid(row=0, column=0, sticky=(W, S))

        # To-do: create separate Frame to hold buttons so that they line up better

        



    def calculate(self, *args):
        try:
            value = self.card_name.get()
            self.card_value.set(value + " is big monies")
        except ValueError:
            pass

    def add_to_collection(self, *args):
        try:
            self.display_message.set("Card added!")
        except ValueError:
            pass