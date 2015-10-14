import board
import ship
import game_pieces
import utilities
import player


print "Welcome to Battleship!"
#**************************
#GAME SETUP

#***************************
#Create player1 player_object
player1 = player.Player("aiden")

#Hardcode player1 ship locations
player1.ships.carrier.grid_loc_start = [3,4]
player1.ships.carrier.grid_loc_end = [3,8]
player1.ships.carrier.create_grid_loc_list()
player1.ships.add_ship_loc_dict(player1.ships.carrier)
player1.my_ships_board.update_grid_ship(player1.ships.carrier)

player1.ships.battleship.grid_loc_start = [6,3]
player1.ships.battleship.grid_loc_end = [9,3]
player1.ships.battleship.create_grid_loc_list()
player1.ships.add_ship_loc_dict(player1.ships.battleship)
player1.my_ships_board.update_grid_ship(player1.ships.battleship)

player1.ships.cruiser.grid_loc_start = [5,8]
player1.ships.cruiser.grid_loc_end = [5,10]
player1.ships.cruiser.create_grid_loc_list()
player1.ships.add_ship_loc_dict(player1.ships.cruiser)
player1.my_ships_board.update_grid_ship(player1.ships.cruiser)

player1.ships.sub.grid_loc_start = [8,7]
player1.ships.sub.grid_loc_end = [10,7]
player1.ships.sub.create_grid_loc_list()
player1.ships.add_ship_loc_dict(player1.ships.sub)
player1.my_ships_board.update_grid_ship(player1.ships.sub)

player1.ships.destroyer.grid_loc_start = [2,3]
player1.ships.destroyer.grid_loc_end = [2,4]
player1.ships.destroyer.create_grid_loc_list()
player1.ships.add_ship_loc_dict(player1.ships.destroyer)
player1.my_ships_board.update_grid_ship(player1.ships.destroyer)

#Print updated players ship board
print player1.name
player1.print_my_ships_board()

#Create computer player_object
computer = player.Player("computer")
#Hardcode computer ship locations
computer.ships.carrier.grid_loc_start = [1,3]
computer.ships.carrier.grid_loc_end = [5,3]
computer.ships.carrier.create_grid_loc_list()
computer.ships.add_ship_loc_dict(computer.ships.carrier)
computer.my_ships_board.update_grid_ship(computer.ships.carrier)

computer.ships.battleship.grid_loc_start = [3,5]
computer.ships.battleship.grid_loc_end = [3,8]
computer.ships.battleship.create_grid_loc_list()
computer.ships.add_ship_loc_dict(computer.ships.battleship)
computer.my_ships_board.update_grid_ship(computer.ships.battleship)

computer.ships.cruiser.grid_loc_start = [7,8]
computer.ships.cruiser.grid_loc_end = [9,8]
computer.ships.cruiser.create_grid_loc_list()
computer.ships.add_ship_loc_dict(computer.ships.cruiser)
computer.my_ships_board.update_grid_ship(computer.ships.cruiser)

computer.ships.sub.grid_loc_start = [8,2]
computer.ships.sub.grid_loc_end = [8,4]
computer.ships.sub.create_grid_loc_list()
computer.ships.add_ship_loc_dict(computer.ships.sub)
computer.my_ships_board.update_grid_ship(computer.ships.sub)

computer.ships.destroyer.grid_loc_start = [5,9]
computer.ships.destroyer.grid_loc_end = [5,10]
computer.ships.destroyer.create_grid_loc_list()
computer.ships.add_ship_loc_dict(computer.ships.destroyer)
computer.my_ships_board.update_grid_ship(computer.ships.destroyer)

#Print updated players ship board
print computer.name
computer.print_my_ships_board()


#***********************************

#START CODE

# Ask for string bomb location
print "Use letters A-J and numbers 1-10 for coordinates in the format 'A1'."
print "Place a bomb."
raw_data = raw_input("Enter coordinates for a bomb. ")
raw_data = utilities.quick_fix(raw_data)
# print raw_data

# Validate string bomb location
# If invalid ask for string bomb location again
raw_data = utilities.request_valid_location(raw_data, player1.my_ships_board)

# print raw_data

# If valid save string
player1.bomb_str = raw_data

# Convert string location to a grid location
player1.create_bomb_grid(player1.enemy_ships_board)

# print player1.bomb_grid

# Check if bomb location is in bomb_list
if(player1.in_bombs_placed()):
# 	If TRUE, 
	# Print ERROR MSG: already used pick new location
	print "Already bombed that spot."

	# CODE ASK FOR NEW LOCATION
	
	print "Pick a new location."


else:
	# If FALSE in bomb_list,
	# Check if opponents ship @ location
	# print computer.ships.check_for_hit(player1.bomb_grid)
	
	if(computer.ships.check_for_hit(player1.bomb_grid) == False):
	# If MISS
		#print "got false"
		
		# Save bomb location to bomb_list
		player1.add_bombs()
		# print player1.bombs_placed
		
		# Update player enemy ship board with MISS
		player1.enemy_ships_board.update_one_cell(player1.bomb_grid, player1.bomb[0])
		
		# Update opponents  my ship board with MISS
		computer.my_ships_board.update_one_cell(player1.bomb_grid, player1.bomb[0])
		
		# Print MSG bomb missed
		print player1.bomb_str, "bomb missed."

		#DELETE bomb variables
		player1.erase_bomb_locations()
		
		# print "varify that bomb locations are empty again"
		# print player1.bomb_str
		# print player1.bomb_grid

		# Print updated enemy ship board
		print player1.name
		player1.print_enemy_ships_board()
		
		#Print updated computers ship board
		print computer.name
		computer.print_my_ships_board()
		
		# NEXT PLAYERS TURN


	else:
	# If HIT
		# print computer.ships.check_for_hit(player1.bomb_grid).ship_name
		ship_hit = computer.ships.check_for_hit(player1.bomb_grid)
		
		# Save bomb location to bomb_list
		player1.add_bombs()
		
		# Update enemy hit ship with HIT at bomb location
		ship_hit.record_ship_hit(player1.bomb_grid, player1.bomb[1])
		
		# Print MSG that a ship was HIT
		print "You hit one of %s's ships." %(computer.name)
		
		# 	Update player enemy ship board with HIT
		player1.enemy_ships_board.update_one_cell(player1.bomb_grid, player1.bomb[1])
		
		# Update opponents  my ship board with HIT
		computer.my_ships_board.update_grid_game_pieces(computer.ships)
		
		#Print updated enemy ship board
		print player1.name
		player1.print_enemy_ships_board()
		
		#Print updated computers ship board
		print computer.name
		computer.print_my_ships_board()

		# Check if opponents ship sunk

		ship_hit.boat = ["X","X","X","X","X"]
		print ship_hit.boat
		if(not ship_hit.is_sunk()):
		# If FALSE

			# Print MSG no ship sunk
			print "No ship sunk."

			# 	NEXT PLAYERS TURN
		else:
		# If TRUE
			# Print MSG that opponents ship sunk, Give name of sunk ship
			print "%s's %s ship sunk." %(computer.name, ship_hit.ship_name)


			computer.ships.battleship.boat = ["X","X","X","X"] 
			computer.ships.cruiser.boat = ["X","X","X"]
			computer.ships.sub.boat = ["X","X","X"]
			computer.ships.destroyer.boat = ["X","X"]

			# print computer.ships.battleship.boat  
			# print computer.ships.cruiser.boat 
			# print computer.ships.sub.boat 
			# print computer.ships.destroyer.boat

			# Check if all of opponents ships sunk
			computer.ships.all_sunk()
			if (computer.ships.fleet_sunk):
			# If FALSE
				print "You have not sunk all of %s's ships, yet." %(computer.name)
				
				# 	NEXT PLAYERS TURN
			else:
			# If TRUE

				# Print MSG congrats MSG to winner
				print "Congratulations %s," %(player1.name)
				# Print MSG the all of opponents ships are sunk
				print "All of %s ships have been sunk!" %(computer.name)

				# Print MSG that game is over
				print "GAME OVER!"

				# GAME OVER 
















	

