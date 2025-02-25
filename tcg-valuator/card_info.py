from color_enum import Color_Enum

class Card_Info:
    def __init__(self):
        self.card_name = ""
        self.card_value = 0.0
        self.card_image_url = "DEFAULT"
        self.card_color = Color_Enum.NOT_SET
        self.card_color_2 = Color_Enum.NOT_SET

    def get_card_name(self):
        return self.card_name

    def set_card_name(self, name):
        self.card_name = name

    def get_card_value(self):
        return self.card_value

    def set_card_value(self, value):
        self.card_value = value

    def get_card_image_url(self):
        return self.card_image_url

    def set_card_image_url(self, url):
        self.card_image_url = url

    def get_card_color(self):
        return self.card_color

    def set_card_color(self, color):
        if not isinstance(color, Color_Enum):
            raise TypeError("set_card_color() requires a valid Color_Enum color value")
        else:
            self.card_color = color

    def get_card_color_2(self):
        return self.card_color_2

    def set_card_color_2(self, color):
        if not isinstance(color, Color_Enum):
            raise TypeError("set_card_color_2() requires a valid Color_Enum color value")
        else:
            self.card_color_2 = color