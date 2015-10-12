import board
import game_pieces

class Player(object):

	def __init__(self, name):

		self.name = name
		self.bombs_placed = []
		self.my_ships_board = board.Board()
		self.enemy_ships_board = board.Board()
		self.ships = game_pieces.Game_Pieces(self.name)