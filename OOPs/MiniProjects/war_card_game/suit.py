class Suit:
    
    SUIT_MAPPING = {
        "diamonds": ["♦", "red"],
        "hearts": ["♥", "red"],
        "clubs": ["♠", "black"],
        "spades": ["♣", "black"]
    }

    def __init__(self, description):
        if description.lower() in Suit.SUIT_MAPPING:
            self._description = description
        else:
            raise Exception("Invalid description")

    @property
    def description(self):
        return self._description