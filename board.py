class Board(object):
	"""Class creates 10x10 game grid with labels.

	"""

	def __init__(self):
		#list of capital letters
		self.capital_letters = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

		#start of board matrix
		self.grid = [[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]]

		#for loop to create rest of the board
		for i in range(1,len(self.capital_letters)):
			temp = [self.capital_letters[i]]
			temp.extend(10 * " ")
			self.grid.append(temp)

		
		
	#draws grid one row at a time.
	def draw_grid_loop(self,matrix_grid):
		for row in matrix_grid:
			#print row
			#print len(item)
			print " %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % tuple(row)
			print "---------------------------------------------"


	#edit one cell in grid
	def update_one_cell(self, location, bomb):
		self.grid[location[0]][location[1]] = bomb

	#edits grid with ship placement
	def update_grid_ship(self, ship):
		i = 0 
		for item in ship.grid_loc_list:
			self.grid[item[0]][item[1]] = ship.boat[i]
			i += 1

	#update grid with all ship changes
	def update_grid_game_pieces(self, game_pieces):
		self.update_grid_ship(game_pieces.carrier)
		self.update_grid_ship(game_pieces.battleship)
		self.update_grid_ship(game_pieces.sub)
		self.update_grid_ship(game_pieces.cruiser)
		self.update_grid_ship(game_pieces.destroyer)

	#converts first letter of location string to and index
	def convert_loc_letter_index(self, location_string):
		#finds index of a letter on grid 
		for index in range(len(self.capital_letters)):
			if (location_string[0] == self.capital_letters[index]):
				
				return index
	#convert string number to int
	def convert_loc_str_index(self,location_string):
		#print location_string
		index = int(location_string[1:])
		return index

	#updates grid with a miss
	def record_miss(self, bomb_location):
		self.grid[bomb_location[0]][bomb_location[1]] = "O"




# print "Player Ship Grid"
# player_ship_grid.draw_grid_loop(player_ship_grid.grid)



