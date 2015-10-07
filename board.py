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



# print "Player Ship Grid"
# player_ship_grid.draw_grid_loop(player_ship_grid.grid)



