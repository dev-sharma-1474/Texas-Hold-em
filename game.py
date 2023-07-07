from user import User
from deck import Deck


class Game:
    def __init__(self, users):
        self.users = users
        self.deck = Deck()

    def deal_cards(self):
        for user in self.users:
            cards = self.deck.deal()
            user.user_hand(cards)

    def play_game(self):
        self.deal_cards()
        for user in self.users:
            print(user.show_user_hand())


