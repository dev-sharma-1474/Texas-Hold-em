from game import Game
from user import User

game = Game()

human_user = User("Player", 500)  # Start with $500
ai_user = User("Computer", 500)  # Start with $500

game.add_user(human_user)
game.add_user(ai_user)

game.play_game()

winner = game.find_winner()
if winner:
    print(f"{winner.name} wins!")
else:
    print("It's a tie!")