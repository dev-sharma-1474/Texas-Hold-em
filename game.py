from user import User
from deck import Deck

card_values = {
    'Ace': 14,
    'King': 13,
    'Queen': 12,
    'Jack': 11,
    '10': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}
hand_ranking = [
    'High Card',
    'One Pair',
    'Two Pair',
    'Three of a Kind',
    'Straight',
    'Flush',
    'Full House',
    'Four of a Kind',
    'Straight Flush',
    'Royal Flush'
]


class Game:
    def __init__(self):
        self.users = []
        self.deck = Deck()
        self.community_cards = []
        self.game_over = False
        self.total_pool = 0

    def add_user(self, user):
        self.users.append(user)

    # Function to deal cards to the user
    def deal_cards(self):
        for user in self.users:
            cards = self.deck.deal()
            user.user_hand(cards)

    # Function for the community cards (5 cards in the middle)
    def deal_community_cards(self, num_of_cards):
        for i in range(num_of_cards):
            card = self.deck.deal()
            self.community_cards.append(card)

    def calc_hand_strength(self, hand):
        # Sort the hand by card value for easier calculations
        sorted_hand = sorted(hand, key=lambda card: card_values[card.card_val], reverse=True)

        if self.is_royal_flush(sorted_hand):
            return hand_ranking.index('Royal Flush') + 1
        elif self.is_straight_flush(sorted_hand):
            return hand_ranking.index('Straight Flush') + 1
        elif self.is_four_of_a_kind(sorted_hand):
            return hand_ranking.index('Four of a Kind') + 1
        elif self.is_full_house(sorted_hand):
            return hand_ranking.index('Full House') + 1
        elif self.is_flush(sorted_hand):
            return hand_ranking.index('Flush') + 1
        elif self.is_straight(sorted_hand):
            return hand_ranking.index('Straight') + 1
        elif self.is_three_of_a_kind(sorted_hand):
            return hand_ranking.index('Three of a Kind') + 1
        elif self.is_two_pair(sorted_hand):
            return hand_ranking.index('Two Pair') + 1
        elif self.is_one_pair(sorted_hand):
            return hand_ranking.index('One Pair') + 1
        else:
            return hand_ranking.index('High Card') + 1

    def is_royal_flush(self, hand):
        return self.is_straight_flush(hand) and hand[0].card_val == 'Ace'

    def is_straight_flush(self, hand):
        return self.is_straight(hand) and self.is_flush(hand)

    def is_four_of_a_kind(self, hand):
        return self.get_matching_rank_count(hand) == 4

    def is_full_house(self, hand):
        return self.get_matching_rank_count(hand) == 3 and len(set([card.card_val for card in hand])) == 2

    def is_flush(self, hand):
        return len(set([card.suit for card in hand])) == 1

    def is_straight(self, hand):
        return all(card_values[hand[i].card_val] - card_values[hand[i + 1].card_val] == 1 for i in range(len(hand) - 1))

    def is_three_of_a_kind(self, hand):
        return self.get_matching_rank_count(hand) == 3

    def is_two_pair(self, hand):
        return self.get_matching_rank_count(hand) == 2 and len(set([card.card_val for card in hand])) == 3

    def is_one_pair(self, hand):
        return self.get_matching_rank_count(hand) == 2

    def get_matching_rank_count(self, hand):
        card_vals = [card.card_val for card in hand]
        return max([card_vals.count(card_val) for card_val in set(card_vals)])

    def betting_round(self, user):
        if user == self.users[1]:  # The second user is the AI player
            # AI betting logic
            # For simplicity, let's make AI always bet 10
            user.place_bet(10)
            self.total_pool += 10
        else:
            # Human user betting
            while True:
                try:
                    action = input("Enter your action (bet/fold/check): ").lower()
                    if action == "bet":
                        bet_amount = int(input("Enter your bet amount: "))
                        user.place_bet(bet_amount)
                        self.total_pool += bet_amount
                        break
                    elif action == "fold":
                        user.fold()
                        break
                    elif action == "check":
                        break
                    else:
                        print("Invalid action. Try again.")
                except ValueError:
                    print("Invalid input. Try again.")

    def play_round(self, user):
        if not self.game_over:
            # Deal cards and show user's hand
            self.deal_cards()
            print(f"{user.name}'s hand:")
            user.show_user_hand()
            print()

            # Betting Round 1
            self.betting_round(user)

            # Deal first 3 community cards
            self.deal_community_cards(3)
            self.show_community_cards()

            # Betting Round 2
            self.betting_round(user)

            # Deal the 4th community card
            self.deal_community_cards(1)
            self.show_community_cards()

            self.betting_round(user)

            self.deal_community_cards(1)
            self.show_community_cards()

            self.betting_round(user)

            return self.find_winner()

    def show_community_cards(self):
        print("Community cards:")
        for card in self.community_cards:
            print(f"{card.card_val} of {card.suit}")
        print()

    def find_winner(self):

        hand_strengths = {}

        for user in self.users:
            user_hand = user.hand + self.community_cards
            hand_strength = self.calc_hand_strength(user_hand)
            hand_strengths[user] = hand_strength

        max_strength = max(hand_strengths.values())

        winners = [user for user, strength in hand_strengths.items() if strength == max_strength]

        if len(winners) == 1:
            return winners[0]
        else:
            return winners[0]

    def play_game(self):
        while not self.game_over:
            for user in self.users:
                if self.play_round(user):
                    self.game_over = True
                    break

        # Determine the winner and display the result
        winner = self.find_winner()
        if winner:
            print(f"{winner.name} wins!")
        else:
            print("It's a tie!")
