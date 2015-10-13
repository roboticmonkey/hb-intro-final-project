import ship


class Game_Pieces(ship.Ship):
	"""Creates a group of ship for game play. 
	Keeps track of all the players ships. 
	Methond all_sunk checks to see if all ships have been sunk.
	 """
	
	def __init__(self, player_name, ship_tuple):
		#super(Game_Pieces, self).__init__()
		self.player_name = player_name
		self.carrier = ship.Ship(ship_tuple[0][0], ship_tuple[0][1])
		self.battleship = ship.Ship(ship_tuple[1][0],ship_tuple[1][1])
		self.cruiser = ship.Ship(ship_tuple[2][0], ship_tuple[2][1])
		self.sub = ship.Ship(ship_tuple[3][0],ship_tuple[3][1])
		self.destroyer = ship.Ship(ship_tuple[4][0],ship_tuple[4][1])
		
		# self.carrier = ship.Ship("Carrier", 5)
		# self.battleship = ship.Ship("Battleship",4)
		# self.cruiser = ship.Ship("Cruiser", 3)
		# self.sub = ship.Ship("Submarine",3)
		# self.destroyer = ship.Ship("Destroyer",2)
		self.fleet_sunk = False
		self.all_ships = {}

	#changes Game_Pieces attribute fleet_sunk to True
	def all_sunk(self):
		if (self.carrier.sunk == True and (self.battleship.sunk == True and
			 (self.cruiser.sunk == True and (self.sub.sunk == True and 
			 	self.destroyer.sunk == True)))):
			self.fleet_sunk = True
		

	#create grid location for all pieces
	def add_ship_loc_dict(self, ship):
		#carrier
		self.all_ships[ship] = ship.grid_loc_list
		

		# #battleship
		# self.battleship.create_grid_start_loc(grid)
		# self.battleship.create_grid_end_loc(grid)
		# self.battleship.create_grid_loc_list()
		# self.all_ships[self.battleship.ship_name] = self.battleship.grid_loc_list

		# #cruiser
		# self.cruiser.create_grid_start_loc(grid)
		# self.cruiser.create_grid_end_loc(grid)
		# self.cruiser.create_grid_loc_list()
		# self.all_ships[self.cruiser.ship_name] = self.cruiser.grid_loc_list

		# #submarine
		# self.sub.create_grid_start_loc(grid)
		# self.sub.create_grid_end_loc(grid)
		# self.sub.create_grid_loc_list()
		# self.all_ships[self.sub.ship_name] = self.sub.grid_loc_list

		# #destroyer
		# self.destroyer.create_grid_start_loc(grid)
		# self.destroyer.create_grid_end_loc(grid)
		# self.destroyer.create_grid_loc_list()
		# self.all_ships[self.destroyer.ship_name] = self.destroyer.grid_loc_list

	#checks all ships for hit
	def check_for_hit(self, bomb_location):
		if self.carrier.is_hit(bomb_location):
			return self.carrier
		elif self.battleship.is_hit(bomb_location):
			return self.battleship
		elif self.cruiser.is_hit(bomb_location):
			return self.cruiser
		elif self.sub.is_hit(bomb_location):
			return self.sub
		elif self.destroyer.is_hit(bomb_location):
			return self.destroyer
		else:
			return False

	#check to see if new ship has same location as already placed ships
	def is_overlap(self, ship):
		print "got into is_overlap method"
		for key, value in self.all_ships.items():
			print key.ship_name, value
			for i in range(len(value)):
				print "i:", i
				print ship.ship_name, ship.grid_loc_list
				for n in range(len(ship.grid_loc_list)):
					print "n:", n, "i:", i
					print ship.ship_name, ship.grid_loc_list[n], key.ship_name, value[i]
					if (ship.grid_loc_list[n] == value[i]):
						print ship.ship_name, ship.grid_loc_list[n]
						print "matches:", key.ship_name, value[i], "at index:", i
						return True
					
		return False

	#check if ship already at location
	def is_taken(self, ship_location):
		for key, value in self.all_ships.items():
			# print key, value, ship_location
			for i in range(len(value)):
				if (value[i] == ship_location):
					return True
		return False

		













# computer = Game_Pieces("Computer")
# print computer.sub.ship_name
# print computer.sub.size
# print computer.sub.boat
# print computer.sub.sunk

# print computer.destroyer.ship_name
# print computer.carrier.ship_name
# print computer.cruiser.ship_name
# print computer.battleship.ship_name


# print "fleet sunk: ", computer.fleet_sunk

# computer.carrier.sunk = True
# print "sunk carrier", computer.carrier.sunk
# computer.all_sunk()
# print "fleet sunk: ", computer.fleet_sunk

# computer.battleship.sunk = True
# print "sunk battleship", computer.battleship.sunk 
# computer.all_sunk()
# print "fleet sunk: ",computer.fleet_sunk

# computer.sub.sunk = True
# print "sunk sub", computer.sub.sunk
# computer.all_sunk()
# print "fleet sunk: ",computer.fleet_sunk

# computer.cruiser.sunk = True
# print "sunk cruiser", computer.cruiser.sunk
# computer.all_sunk()
# print "fleet sunk: ",computer.fleet_sunk

# computer.destroyer.sunk = True
# print "sunk destroyer", computer.destroyer.sunk
# computer.all_sunk()
# print "fleet sunk: ",computer.fleet_sunk

