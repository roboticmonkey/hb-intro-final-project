class Ship(object):
	"""Base Class for ships. Takes size of ship in INT and the ship_name of ship in STRING.
	Holds attributes start_location and end_location which are two character STRINGS.
	And sunk which is a Boolean. Attribute boat holds a LIST of STRING characters of size,
	lenght of boat LIST is equal to size. 
	"""

	def __init__(self, size, ship_name):
		super(Ship, self).__init__()
		self.size = size
		self.ship_name = ship_name
		self.start_location = ""
		self.end_location = ""
		self.grid_loc_start = []
		self.grid_loc_end = []
		self.sunk = False
		self.boat = [str(self.size) for x in range(size)]
		self.grid_loc_list = []

	#checks to see if ship is sunk. Returns TRUE when sunk. 
	def is_sunk(self):
		winning_lists = [["X","X","X","X","X"], ["X","X","X","X"], ["X","X","X"], ["X","X"]]
		for i in range(len(winning_lists)):
			if (self.boat == winning_lists[i]):
				return True
							
		return False

	

	#checks if bomb hit ship. returns TRUE is hit, FALSE if missed.
	def is_hit(self, bomb_location):
		# for i in range(len(self.grid_loc_list)):
		# 	if (bomb_location == self.grid_loc_list[i]):
		if (bomb_location in self.grid_loc_list):
			return True
		else:
			return False
		

	#changes boat list to reflect where a bomb hit it. 
	def record_ship_hit(self, bomb_location):
		for i in range(len(self.grid_loc_list)):
			if (bomb_location == self.grid_loc_list[i]):
				self.boat[i] = "X"
				print self.ship_name


	#adds ship start location
	def ship_location_start(self, start_location):
		self.start_location = start_location

	#adds ship end location
	def ship_location_end(self, end_location):
		self.end_location = end_location


	def create_grid_start_loc(self, board_object):
		self.grid_loc_start = [
			board_object.convert_loc_letter_index(self.start_location),
			board_object.convert_loc_str_index(self.start_location)]
	
	#create grid end location
	def create_grid_end_loc(self, board_object):
		self.grid_loc_end = [
			board_object.convert_loc_letter_index(self.end_location),
			board_object.convert_loc_str_index(self.end_location)]

	#check if horizontal after grid_loc_start and grid_loc_end defined
	def is_horizontal(self):
		if (self.grid_loc_start[0] == self.grid_loc_end[0]):
			return True
		else:
			return False

	#check if vertical
	def is_vertical(self):
		if (self.grid_loc_start[1] == self.grid_loc_end[1]):
			return True
		else:
			return False 

	#creates list for grid placement
	def create_grid_loc_list(self, grid):
		# print self.ship_name
		# print "in ship method to create list of lists"
		self.create_grid_start_loc(grid)
		# print "grid loc start:", self.grid_loc_start
		self.create_grid_end_loc(grid)
		# print "grid loc end:", self.grid_loc_end

	 	if (self.is_horizontal()):
	 		i = 0
	 		while i < self.size:
				temp = [self.grid_loc_start[0], self.grid_loc_start[1]+i]
				self.grid_loc_list.append(temp)
				i += 1
			return True
		elif (self.is_vertical()):
			i = 0
			while i < self.size:
				temp = [self.grid_loc_start[0] +i,self.grid_loc_start[1]]
				self.grid_loc_list.append(temp)
				i += 1
			return True
		else:
			return False


			
			








# sub = Ship(3, "Submarine")
# sub.ship_location_start("D1")
# sub.ship_location_end("F1")
# print sub.start_location, sub.end_location
# sub.grid_loc_start = [4,1]
# print sub.grid_loc_start
# sub.grid_loc_end = [6,1]
# print sub.grid_loc_end
# sub.create_grid_loc_list()
# print sub.grid_loc_list

# class Game_Pieces(Ship):

# 	def __init__(self, player_name):
# 		#super(Game_Pieces, self).__init__(size, ship_name)
# 		self.player_name = player_name
# 		self.carrier = Ship(5, "Carrier")
		


# carrier = Ship(5, "Carrier")
# print carrier
# print carrier.sunk
# print carrier.end_location
# print type(carrier.size)
# print carrier.boat
# print type(carrier.boat[3])
# print len(carrier.boat)


# print "game pieces"
# computer = Game_Pieces("computer")
# print computer.carrier.ship_name

# 		