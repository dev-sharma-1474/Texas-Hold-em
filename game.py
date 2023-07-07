from user import User
from deck import Deck

class Game:
    def __init__(self):
        self.users = []
        self.deck = Deck()
        self.community_cards = []

    def add_user(self, user):
        self.users.append(user)

    # Function to deal cards to the user
    def deal_cards(self):
        for _ in range(2):
            for user in self.users:
                cards = self.deck.deal()
                user.user_hand(cards)

    # Function for the community cards (5 cards in the middle)
    def deal_community_cards(self):
        for _ in range(5):
            card = self.deck.deal()
            self.community_cards.append(card)

    # Deals the cards and displays the game state
    def play_game(self, users):
        for user in users:
            print(f"{user.name}'s hand:")
            user.show_user_hand()
            print()

        print("Community cards:")
        for card in self.community_cards:
            print(f"{card.card_val} of {card.suit}")
