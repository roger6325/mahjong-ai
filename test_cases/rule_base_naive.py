import Game
import Player
import Move_generator

def test():

	player_names = [("Amy", Move_generator.Human), ("Billy", Move_generator.RuleBasedAINaive), ("Clark", Move_generator.Human), ("Doe", Move_generator.RuleBasedAINaive)]

	players = []
	game = None
	for player_name, move_generator_class in player_names:
		players.append(Player.Player(move_generator_class, player_name))

	game = Game.Game(players)
	winner, losers, penalty = game.start_game()

	if winner is None:
		print("No one wins.")
	else:
		print("Winner: %s"%winner.name)
		print("Loser(s): %s"%(', '.join([player.name for player in losers])))
		print("Penalty: %d"%penalty)