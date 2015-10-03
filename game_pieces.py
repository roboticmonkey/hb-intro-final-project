import ship


class Game_Pieces(ship.Ship):
	"""docstring for Game_Pieces"""
	
	def __init__(self, size, ship_name, player_name):
		super(Game_Pieces, self).__init__()
		self.player_name = player_name
		self.carrier = ship.Ship(5, "Carrier")
		self.battleship = ship.Ship(4, "Battleship")
		self.cruiser = ship.Ship(3, "Cruiser")
		self.sub = ship.Ship(3, "Submarine")
		self.destroyer = ship.Ship(3, "Destroyer")

computer = Game_Pieces("Computer")
print computer.sub

