from tkinter import *
from tkinter import ttk
from valuator_collection import Valuator_Collection

class Valuator_Menu:
    def __new__(cls, root):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Valuator_Menu, cls).__new__(cls)
        return cls.instance


    def __init__(self, root):
        root.title("TCG Valuator")

        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        # Area to display card art
        display_area = Frame(self.mainframe, bg='red', width=350, height=500)
        display_area.grid(row=1, column=0, sticky=(W, S))
       
        # Frame that contains buttons that will be to the side of the card art area
        self.button_frame = ttk.Frame(self.mainframe)
        self.button_frame.grid(column=1, row=1, sticky=(N, W, E, S))

        # Text entry to enter card name
        self.card_name = StringVar()
        self.card_entry = ttk.Entry(self.button_frame, width = 50, textvariable=self.card_name)
        self.card_entry.grid(column=1, row=0, sticky=(N, W, E))

        # Calculate and display card value for entered card name
        ttk.Button(self.button_frame, text='Calculate', command=self.calculate).grid(column=2, row=0, sticky=(N, W))
        self.card_value = StringVar()
        ttk.Label(self.button_frame, textvariable=self.card_value).grid(column=2, row=1, sticky=(N, W, E))

        # Display confirmation that card was added to collection
        self.display_message = StringVar()
        self.collection_message = StringVar()
        ttk.Button(self.button_frame, text='Add to Collection', command=self.add_to_collection).grid(column=2, row = 2, sticky=W)
        ttk.Label(self.button_frame, textvariable=self.display_message).grid(column=1, row=2, sticky=(W))
        
        # Display current collection list
        ttk.Label(self.button_frame, textvariable=self.collection_message).grid(column=1, row=4, sticky=(W))

    def calculate(self, *args):
        try:
            value = self.card_name.get()
            self.card_value.set(value + " is big monies")
        except ValueError:
            pass

    def add_to_collection(self):
        try:
            test_str = self.card_name.get()
            Valuator_Collection.add_to_collection(Valuator_Collection(), test_str)
            self.display_message.set("Card added!")
            self.collection_message.set("collection here: " + "".join(Valuator_Collection().get_collection()))
        except ValueError:
            pass