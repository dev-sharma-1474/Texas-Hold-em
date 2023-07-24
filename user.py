from cards import Cards


class User:
    def __init__(self, name, money):
        self.name = name
        self.hand = []
        self.money = money
        self.current_bet = 0

    def user_hand(self, cards):
        self.hand.append(cards)

    def show_user_hand(self):
        for cards in self.hand:
            print(f"{cards.card_val} of {cards.suit}")

    def place_bet(self, amount):
        if amount <= self.money:
            self.money -= amount
            self.current_bet += amount
        else:
            print("You don't have enough money")

    def fold(self):
        print(f"{self.name} folds.")
        self.hand = []

    def collect_winnings(self, amount):
        self.money += amount
