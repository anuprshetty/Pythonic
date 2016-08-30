from suit import Suit


class Card:

    _SPECIAL_CARDS = {
        11: "Jack",
        12: "Queen",
        13: "King",
        14: "Ace"
    }

    def __init__(self, suit, value):
        self._suit = suit
        
        if 2 <= value <= 14:
            self._value = value
        else:
            print("Invalid card value")

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    def is_special(self):
        return self._value > 10

    def show(self):
        if self.is_special():
            card_description = Card._SPECIAL_CARDS[self._value]
        else:
            card_description = self._value

        suit_description = self._suit.description
        suit_symbol = Suit.SUIT_MAPPING[suit_description][0]
        suit_color = Suit.SUIT_MAPPING[suit_description][1]
        suit_description = suit_description.capitalize()

        print(f"{card_description} of {suit_description} ({suit_symbol} {suit_color})")