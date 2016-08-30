class Move:

    # | 1 | 2 | 3 |
    # | 4 | 5 | 6 |
    # | 7 | 8 | 9 |

    _row_count = 3
    _col_count = 3

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def is_valid(self):
        return isinstance(self._value, int) and 1 <= self._value <= 9

    def get_row(self):
        return (self._value -1) // Move._row_count # returns row no --> (0, 1, 2)

    def get_col(self):
        return (self._value -1) % Move._col_count # returns col no --> (0, 1, 2)
