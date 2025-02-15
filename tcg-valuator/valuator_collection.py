class Valuator_Collection:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Valuator_Collection, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if not hasattr(self, 'collection'):
            self.collection = []

    def add_to_collection(self, card):
        try:
            self.collection.append(card)
        except ValueError:
            pass

    def get_collection(self):
        return self.collection