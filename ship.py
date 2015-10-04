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

	#checks to see if ship is sunk. Returns TRUE when sunk. 
	def is_sunk(self, boat):
		pass

	#checks if bomb hit ship. returns TRUE is hit, FALSE if missed.
	def is_hit(self, ship_location, bomb_location):
		pass

	#changes boat list to reflect where a bomb hit it. 
	def record_ship_hit(self, boat, bomb_location):
		pass

	#adds ship start location
	def ship_location_start(self, start_location):
		self.start_location = start_location

	#adds ship end location
	def ship_location_end(self, end_location):
		self.end_location = end_location

	#converts the computer index for human letter coordinates
	def convert_loc_letter_index(self, board_object, location_string):
		#finds index of a letter on grid 
		for index in range(len(board_object.capital_letters)):
			if (location_string[0] == board_object.capital_letters[index]):
				#print "letter is at index:", index
				return index
	#convert string number to int
	def convert_loc_str_index(self,location_string):
		#print location_string
		index = int(location_string[1])
		return index

	





# sub = Ship(3, "Submarine")
# sub.ship_location_start("D2")
# sub.ship_location_end("D5")
# print sub.start_location, sub.end_location

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