from game import Game
from user import User

# Create users
human_user = User("Player")
ai_user = User("Computer")

# Create game
game = Game()
game.add_user(human_user)
game.add_user(ai_user)

# Play the game
game.deal_cards()
game.deal_community_cards()
game.play_game([human_user, ai_user])
