from deck import Deck
from player import Player
from war_card_game import WarCardGame


player = Player("Anup", Deck(is_deck_to_be_empty=True))
computer = Player("Computer", Deck(is_deck_to_be_empty=True), is_computer=True)

deck = Deck()

game = WarCardGame(player, computer, deck)
game.print_welcome_message()
while not game.check_game_over():
    game.start_battle()
    game.print_stats()

    answer = input("\nAre you ready for the next round?\nPress ENTER to continue.\nEnter X to stop.\n")

    if answer.lower() == "x":
        break
    