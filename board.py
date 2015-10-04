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
	def update_one_cell(self, grid, location, bomb):
		self.grid[location[0]][location[1]] = bomb

	#edit grid with ships horizontal
	def update_grid_ship_hor(self, grid, ship):
		i = 0
		while i < ship.size:
			grid[ship.grid_loc_start[0]][ship.grid_loc_start[1] +i] = ship.boat[i]
			i += 1

	#edit grid with ships vertical
	def update_grid_ship_vert(self, grid, ship):
		i = 0
		while i < ship.size:
			grid[ship.grid_loc_start[0] +i ][ship.grid_loc_start[1]] = ship.boat[i]
			i += 1

# print "Player Ship Grid"
# player_ship_grid.draw_grid_loop(player_ship_grid.grid)



