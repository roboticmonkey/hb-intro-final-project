import board
import game_pieces
import utilities


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
		print "\n   ",
		print  "%s's Ships\n" %(self.name)
		self.my_ships_board.draw_grid_loop(self.my_ships_board.grid)

	# Prints enemy ships board
	def print_enemy_ships_board(self):
		# print "Enemy Ships"
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

	# Save computer generated bomb location to bomb_grid and bomb_str
	def save_comp_bomb_location(self):
		self.bomb_grid = utilities.generates_grid_location()
		# print players[1].bomb_grid,
		self.bomb_str = self.my_ships_board.convert_grid_location_str(self.bomb_grid)
		# print players[1].bomb_str

	#Handles bombs that miss
	def handle_bomb_miss(self, enemy_player_object):
		# Save bomb location to bomb_list
		self.add_bombs()
		# print self.bombs_placed
		
		# Update player enemy ship board with MISS
		self.enemy_ships_board.update_one_cell(self.bomb_grid, self.bomb[0])
		
		# Update opponents  my ship board with MISS
		enemy_player_object.my_ships_board.update_one_cell(self.bomb_grid, self.bomb[0])
		
		# Print MSG bomb missed
		print self.bomb_str, "bomb missed."

		

	#Handles bombs that hit
	def handle_bomb_hit(self, enemy_player_object):
		ship_hit = enemy_player_object.ships.check_for_hit(self.bomb_grid)
		
		# Save bomb location to bomb_list
		self.add_bombs()
		
		# Update enemy hit ship with HIT at bomb location
		ship_hit.record_ship_hit(self.bomb_grid, self.bomb[1])
		
		
		
		# 	Update player enemy ship board with HIT
		self.enemy_ships_board.update_one_cell(self.bomb_grid, self.bomb[1])
		
		# Update opponents  my ship board with HIT
		enemy_player_object.my_ships_board.update_grid_game_pieces(enemy_player_object.ships)
		# Print MSG that a ship was HIT
		print "\nOne of %s's ships was hit at location %s." %(enemy_player_object.name, self.bomb_str)

	#Prints out MSG when game ends
	def game_over_msg(self, enemy_player_object):
		# Print MSG congrats MSG to winner
		print "Congratulations %s," %(self.name)
		# Print MSG the all of opponents ships are sunk
		print "All of %s's ships have been sunk!" %(enemy_player_object.name)

		# Print MSG that game is over
		print "GAME OVER!"

	#Prints out MSG when a players ship has sunk. Self is the owner of the sunken ship
	def msg_ship_sunk(self, hit_ship_object ):
		# Print MSG that opponents ship sunk, Give name of sunk ship
		print "%s's %s ship sunk." %(self.name, hit_ship_object.ship_name)

	# Print Player boards, my_ship_board and enemy_board
	def print_player_boards(self):
		#Print my ship board
		print  "%s's My Ships\n" %(self.name)
		self.print_my_ships_board()
		#Print updated enemy ship board
		print  "%s's Enemy Ships\n" %(self.name)
		# print self.name, ""
		self.print_enemy_ships_board()

	#draws 2 grids one row at a time.
	def print_both_boards(self):
		

		print "\n   ",
		print  "%s's Ships" %(self.name),
		print "                                             ",
		print  "Enemy's Ships\n"
		for i in range(len(self.my_ships_board.grid)):
			
			print "     %-2s | %-2s | %-2s | %-2s | %-2s | %-2s | %-2s | %-2s | %-2s | %-2s | %-2s |" % tuple(self.my_ships_board.grid[i]),
			
			print "     %-2s | %-2s | %-2s | %-2s | %-2s | %-2s | %-2s | %-2s | %-2s | %-2s | %-2s |" % tuple(self.enemy_ships_board.grid[i])
			print "    -------------------------------------------------------",
			
			print "    -------------------------------------------------------"
		print " "



		
		

