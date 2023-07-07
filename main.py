from game import Game
from user import User


human_user = User("You")
ai_user = User("Computer")

game = Game([human_user, ai_user])
game.play_game()