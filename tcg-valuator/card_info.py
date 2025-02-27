from color_enum import Color_Enum

class Prices:
    def __init__(self):
        self.usd = ""
        self.usd_foil = None
        self.usd_etched = None
        self.eur = ""
        self.eur_foil = None
        self.tix = None

class Purchase_Uris:
    def __init__(self):
        self.tcgplayer = ""
        self.cardmarket = ""
        self.cardhoarder = ""

    def get_tcgplayer(self):
        return self.tcgplayer

    def set_tcgplayer(self, tcgplayer):
        self.tcgplayer = tcgplayer

    def get_cardmarket(self):
        return self.cardmarket

    def set_cardmarket(self, cardmarket):
        self.cardmarket = cardmarket

    def get_cardhoarder(self):
        return self.cardhoarder

    def set_cardhoarder(self, cardhoarder):
        self.cardhoarder = cardhoarder

class Card:
    def __init__(self):
        # The following variables are in order according to JSON returned by Scryfall (however, not all variables in the JSON output are used)
        self.cardmarket_id = 0
        self.name = ""
        self.uri = ""
        self.image_uri = "" #for now, use 'normal' image as default - we can decide later to flesh this out to have an image_uri object like the JSON structure
        self.mana_cost = ""
        self.colors = []
        self.foil = False
        self.nonfoil = True
        self.promo = False
        self.variation = False
        self.illustration_id = ""
        self.prices = Prices()
        self.purchase_uris = Purchase_Uris()

    def get_card_name(self):
        return self.name

    def set_card_name(self, name):
        self.name = name