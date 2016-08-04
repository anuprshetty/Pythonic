class WarCardGame:

    _PLAYER = 0
    _COMPUTER = 1
    _TIE = 2

    def __init__(self, player, computer, deck):
        self._player = player
        self._computer = computer
        self._deck = deck

        self.make_initial_decks()

    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._computer)

    def make_deck(self, character):
        for i in range(26):
            character.add_card(self._deck.draw())

    def start_battle(self, cards_from_previous_war=list()):

        print("\n== Let's Start the Battle ==\n")

        player_card = self._player.draw_card()
        computer_card = self._computer.draw_card()

        print("Your Card:")
        player_card.show()
        print("\nComputer Card:")
        computer_card.show()

        winner = self.get_round_winner(player_card, computer_card)
        cards_from_battle = self.get_cards_from_battle(player_card, computer_card, cards_from_previous_war)

        if winner == WarCardGame._PLAYER:
            print("\nYou won this round!")
            self.add_cards_to_character(self._player, cards_from_battle)
        elif winner == WarCardGame._COMPUTER:
            print("\nComputer won this round!")
            self.add_cards_to_character(self._computer, cards_from_battle)
        else:
            print("\nIt's a tie. This is war!")
            self.start_war(cards_from_battle)

    def get_round_winner(self, player_card, computer_card):
        if player_card.value > computer_card.value:
            return WarCardGame._PLAYER
        elif computer_card.value > player_card.value:
            return WarCardGame._COMPUTER
        else:
            return WarCardGame._TIE
    
    def get_cards_from_battle(self, player_card, computer_card, cards_from_previous_war):
        return [player_card, computer_card] + cards_from_previous_war

    def add_cards_to_character(self, character, cards_from_battle):
        for card in cards_from_battle:
            character.add_card(card)

    def start_war(self, cards_from_battle):
        if self._player.deck.size == 0 or self._computer.deck.size == 0:
            print("\nNO hidden cards\n")
            return

        player_cards = []
        computer_cards = []

        if self._player.deck.size >= 4 and self._computer.deck.size >= 4:
            for _ in range(3):
                player_cards.append(self._player.draw_card())
                computer_cards.append(self._computer.draw_card())

            print("\nSIX hidden cards: XXX XXX\n")
        else:
            print("\nNO hidden cards\n")
        self.start_battle(player_cards + computer_cards + cards_from_battle)

    def check_game_over(self):
        if not self._player.has_empty_deck() and not self._computer.has_empty_deck():
            return False

        print("\n================================\n")
        print("|           GAME OVER           |")
        print("\n================================\n")

        if self._player.has_empty_deck() and self._computer.has_empty_deck():
            print("It's a draw game! Try again.")
        elif self._player.has_empty_deck():
            print("Computer won! Better luck next time.")
        else:
            print(f"Excellent. You won, {self._player.name}! Congratulations")

        return True

    def print_stats(self):
        print("\n-------------------------------------")
        print(f"You have {self._player.deck.size} cards on your deck.")
        print(f"Computer has {self._computer.deck.size} cards on it's deck.")
        print("-------------------------------------\n")

    def print_welcome_message(self):
        print("\n================================\n")
        print("|         WAR CARD GAME        |")
        print("\n================================\n")