import random
from suit import Suit
from card import Card

    
class Deck:

    def __init__(self, is_deck_to_be_empty=False):
        self._cards = []
        if not is_deck_to_be_empty:
            self.build()

    @property
    def size(self):
        return len(self._cards)

    def build(self):
        for suit_description in Suit.SUIT_MAPPING.keys():
            for value in range(2, 15):
                self._cards.append(Card(Suit(suit_description), value))

    def show(self):
        for card in self._cards:
            card.show()

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if self._cards: # if self._cards IS NOT empty
            return self._cards.pop() # Top Card
        else: # if self._cards IS empty
            return None

    def add(self, card):
        self._cards.insert(0, card)