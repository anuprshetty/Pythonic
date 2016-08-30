from player import Player
from board import Board


class TicTacToe:

    def start(self):

        self.print_welcome_message()

        player_name = input("What's your name? ")

        while True:

            play_first = input(f"Hey, {player_name}! Would you like to play first? Enter (y/n): ").lower()
            if play_first == "y":
                player1 = Player(player_name)
                player2 = Player("Computer", is_human=False)
            elif play_first == "n":
                player1 = Player("Computer", is_human=False)
                player2 = Player(player_name)
            else:
                print("Sorry! Your input is not valid. But I will assume that you want to play first.")
                player1 = Player(player_name)
                player2 = Player("Computer", is_human=False)

            board = Board()
            board.print_board()

            while True:
                
                while True:
                    player1_move = player1.get_move()
                    if board.submit_move(player1, player1_move):
                        break
                board.print_board()
                if board.is_game_over(player1, player1_move):
                    break

                while True:
                    player2_move = player2.get_move()
                    if board.submit_move(player2, player2_move):
                        break
                board.print_board()
                if board.is_game_over(player2, player2_move):
                    break

            play_again = input("Would you like to play again? Enter (y/n): ").lower()
            if play_again == "n":
                print("Bye! Come back soon.")
                break
            elif play_again == "y":
                pass
            else:
                print("Sorry! Your input is not valid. But I will assume that you want to play again.")
            self.start_new_round()
    
    def print_welcome_message(self):
        print("\n==========================================\n")
        print("|      Welcome to Tic-Tac-Toe Game       |")
        print("\n==========================================\n")

    def start_new_round(self):
        print("\n========================\n")
        print("|       New Round       |")
        print("\n========================\n")


tic_tac_toe = TicTacToe()
tic_tac_toe.start()
