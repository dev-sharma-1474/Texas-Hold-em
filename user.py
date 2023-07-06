from cards import Cards


class User:
    def __init__(self):
        self.hand = []

    def user_hand(self, cards):
        self.hand.append(cards)

    def show_user_hand(self):
        for cards in self.hand:
            print({cards.card_val} + " of " + {cards.suit})




