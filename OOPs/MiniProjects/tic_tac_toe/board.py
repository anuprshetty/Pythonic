class Board:

    _EMPTY_CELL = 0

    def __init__(self):
        self.game_board = [
            [Board._EMPTY_CELL, Board._EMPTY_CELL, Board._EMPTY_CELL],
            [Board._EMPTY_CELL, Board._EMPTY_CELL, Board._EMPTY_CELL],
            [Board._EMPTY_CELL, Board._EMPTY_CELL, Board._EMPTY_CELL]
        ]

    def print_board(self):
        print("\nPositions:")
        self.print_board_with_positions()

        print("\nBoard:")
        self.print_board_with_moves()

    def print_board_with_positions(self):
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")

    def print_board_with_moves(self):
        for row in self.game_board:
            print("| ", end="")
            for cell in row:
                if cell == Board._EMPTY_CELL:
                    empty_cell = " "
                    print(f"{empty_cell} | ", end="")
                else:
                    print(f"{cell} | ", end="")
            print()
        print()

    def submit_move(self, player, move):
        row = move.get_row()
        col = move.get_col()
        cell = self.game_board[row][col]
        if cell == Board._EMPTY_CELL:
            self.game_board[row][col] = player.marker
            return True
        else:
            print(f"The position {move.value} is already taken. Please choose another position.")
            return False

    def is_game_over(self, player, last_move):
        return self.is_game_won(player, last_move) or self.is_game_tie()

    def is_game_won(self, player, last_move):
        is_player_won = (
            (self.check_row(player, last_move))
            or (self.check_column(player, last_move))
            or (self.check_diagonal(player))
            or (self.check_antidiagonal(player))
        )

        if is_player_won:
            if player.is_human:
                print(f"Awesome {player.name}! you won the game. Congrats!")
            else:
                print(f"Oops... {player.name} won the game! Try again.")

        return is_player_won

    def is_game_tie(self):
        for row in self.game_board:
            if row.count(self._EMPTY_CELL) > 0:
                return False
        print("It's a tie! Try again.")
        return True

    def check_row(self, player, last_move):
        row_index = last_move.get_row()
        board_row = self.game_board[row_index]
        board_row_len = len(board_row)

        return board_row.count(player.marker) == board_row_len

    def check_column(self, player, last_move):
        col_index = last_move.get_col()
        board_col = []
        for row in self.game_board:
            board_col.append(row[col_index])
        board_col_len = len(board_col)

        return board_col.count(player.marker) == board_col_len

    def check_diagonal(self, player):
        board_row_len = len(self.game_board)
        board_diagonal = [self.game_board[index][index] for index in range(0, board_row_len)]
        board_diagonal_len = len(board_diagonal)

        return board_diagonal.count(player.marker) == board_diagonal_len

    def check_antidiagonal(self, player):
        board_row_len = len(self.game_board)
        board_antidiagonal = []
        for row_index in range(0, board_row_len):
            col_index = board_row_len - row_index - 1
            board_antidiagonal.append(self.game_board[row_index][col_index])
        board_antidiagonal_len = len(board_antidiagonal)

        return board_antidiagonal.count(player.marker) == board_antidiagonal_len
