import random
from cards import Cards


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        card_vals = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        self.cards = [Cards(suit, card_val) for suit in suits for card_val in card_vals]
        random.shuffle(self.cards)

    def deal(self):
        print(self.cards.peek)
        return self.cards.pop()
