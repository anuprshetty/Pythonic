import random

from move import Move


class Player:

    PLAYER_MARKER = "X"
    COMPUTER_MARKER = "O"

    _MOVES = [num for num in range(1, 10)]

    def __init__(self, name, is_human=True):
        self.name  = name
        self._is_human = is_human

        if self._is_human:
            self._marker = Player.PLAYER_MARKER
        else:
            self._marker = Player.COMPUTER_MARKER

    @property
    def is_human(self):
        return self._is_human

    @property
    def marker(self):
        return self._marker

    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()

    def get_human_move(self):
        while True:
            try:
                player_input = input("Please enter your move (1-9): ")
                player_move = int(player_input)
            except:
                print(f"Invalid move: {player_input}")
                continue
            move = Move(player_move)
            if move.is_valid():
                return move
            else:
                print(f"Invalid move: {player_move}")
                continue

    def get_computer_move(self):
        computer_move = random.choice(Player._MOVES)
        move = Move(computer_move)
        print(f"{self.name} move (1-9): {move.value}")
        return move
