import board
import game_pieces

class Player(object):

	def __init__(self, name):
		self.ship_tuple = (["Carrier",5],["Battleship",4],["Cruiser",3],["Submarine",3],["Destroyer",2])
		self.name = name
		self.bombs_placed = []
		self.my_ships_board = board.Board()
		self.enemy_ships_board = board.Board()
		self.ships = game_pieces.Game_Pieces(self.name, self.ship_tuple)
		


	# Prints my_ships_board
	def print_my_ships_board(self):
		print "My Ships"
		self.my_ships_board.draw_grid_loop(self.my_ships_board.grid)

	# Prints all the ships and their sizes
	def list_ship_name_and_sizes(self):
		for each_ship in self.ship_tuple:
			print each_ship[0], "which has a length of", each_ship[1], "cells."