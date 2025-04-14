from card_info import Card

class Valuator_Collection:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Valuator_Collection, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if not hasattr(self, 'collection'):
            self.collection = []
        self.index = 0


    def add_to_collection(self, card):
        try:
            self.collection.append(card)
        except ValueError:
            pass

    def get_collection(self):
        return self.collection

    def get_card(self, card_index):
        """
        get_card 
        Return card from collection based on the passed index.
        This method is primarily used internally to process the next
        card in the collection.

        :card_index: Index within collection 
        """
        if card_index < 0 or card_index >= len(self.collection):
            return -1
        else 
            self.index = card_index
            return self.collection[self.index]
