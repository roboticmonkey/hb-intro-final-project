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
		self.sunk = False
		self.boat = [str(self.size) for x in range(size)]

	#checks to see if ship is sunk. Returns TRUE when sunk. 
	def is_sunk(self, boat):
		pass

	#checks if bomb hit ship. returns TRUE is hit, FALSE if missed.
	def is_hit(self, ship_location, bomb_location):
		pass

	#changes boat list to reflect where a bomb hit it. 
	def hit_ship(self, boat, bomb_location):
		pass






carrier = Ship(5, "Carrier")
print carrier
print carrier.sunk
print carrier.end_location
print type(carrier.size)
print carrier.boat
print type(carrier.boat[3])
print len(carrier.boat)
		