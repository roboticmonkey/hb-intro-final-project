import board
import game_pieces

class Player(object):

	def __init__(self, name):
		
		self.name = name
		
		self.my_ships_board = board.Board()
		self.enemy_ships_board = board.Board()
		self.ships = game_pieces.Game_Pieces(self.name)

		self.ships.add_ships_dictionary()

		self.bombs_placed = []
		self.bomb_str = " "
		self.bomb_grid = []
		self.bomb = ["O", "X"]


	# Prints my_ships_board
	def print_my_ships_board(self):
		print "My Ships"
		self.my_ships_board.draw_grid_loop(self.my_ships_board.grid)

	# Prints enemy ships board
	def print_enemy_ships_board(self):
		print "Enemy Ships"
		self.enemy_ships_board.draw_grid_loop(self.enemy_ships_board.grid)

	#Creates bomb grid location
	def create_bomb_grid(self, board_object):
		self.bomb_grid = [
			board_object.convert_loc_letter_index(self.bomb_str),
			board_object.convert_loc_str_index(self.bomb_str)]

	#Check if bomb_grid is in bombs_placed Returns True or False
	def in_bombs_placed(self):
		#If bombs_placed is empty
		if(self.bombs_placed == []):
			return False
		#If not empty
		else:
			#look for bomb in list
			for each_bomb in self.bombs_placed:
				if (each_bomb == self.bomb_grid):
					#if found 
					return True
			#if not found
			return False
	#Add bombs to bombs_places list
	def add_bombs(self):
		self.bombs_placed.append(self.bomb_grid)

	#Erases bomb location variables
	def erase_bomb_locations(self):
		self.bomb_str = " "
		self.bomb_grid = []

