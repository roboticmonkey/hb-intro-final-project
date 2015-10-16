import board
import ship
import game_pieces
import utilities
import player


print "\n\nWelcome to Battleship!\n"
#**************************
#GAME SETUP

#***************************
#Create human player_object
human = player.Player("Aiden")
#Create computer player_object
computer = player.Player("Computer")

players = [human, computer]
turns_taken = 2
# turns_taken = 1

#Hardcode human ship locations
human.ships.carrier.grid_loc_start = [3,4]
human.ships.carrier.grid_loc_end = [3,8]
human.ships.carrier.create_grid_loc_list()
human.ships.add_ship_loc_dict(human.ships.carrier)
human.my_ships_board.update_grid_ship(human.ships.carrier)

human.ships.battleship.grid_loc_start = [6,3]
human.ships.battleship.grid_loc_end = [9,3]
human.ships.battleship.create_grid_loc_list()
human.ships.add_ship_loc_dict(human.ships.battleship)
human.my_ships_board.update_grid_ship(human.ships.battleship)

human.ships.cruiser.grid_loc_start = [5,8]
human.ships.cruiser.grid_loc_end = [5,10]
human.ships.cruiser.create_grid_loc_list()
human.ships.add_ship_loc_dict(human.ships.cruiser)
human.my_ships_board.update_grid_ship(human.ships.cruiser)

human.ships.sub.grid_loc_start = [8,7]
human.ships.sub.grid_loc_end = [10,7]
human.ships.sub.create_grid_loc_list()
human.ships.add_ship_loc_dict(human.ships.sub)
human.my_ships_board.update_grid_ship(human.ships.sub)

human.ships.destroyer.grid_loc_start = [2,3]
human.ships.destroyer.grid_loc_end = [2,4]
human.ships.destroyer.create_grid_loc_list()
human.ships.add_ship_loc_dict(human.ships.destroyer)
human.my_ships_board.update_grid_ship(human.ships.destroyer)

# #Print updated players ship board
# print player1.name
# player1.print_my_ships_board()

#Create computer player_object
# players[(turns_taken%2)-1] = player.Player("computer")
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

# #Print updated players ship board
# print computer.name
# computer.print_my_ships_board()

# Print Human player boards
players[0].print_both_boards()

# Prints alternating boards human then computer
# players[turns_taken%2].print_player_boards()

# Print computer boards
# players[1].print_player_boards()


# human    player_object players[turns_taken%2]
# computer player_object players[(turns_taken%2)-1]


#***********************************


# while (utilities.no_winner(players[(turns_taken%2)-1])):
while (utilities.no_winner(players[(turns_taken%2)])):
	# turns_taken += 1
	# print turns_taken, "turns_taken"
	# First time player picks each turn
	# Ask for string bomb location
	print "%s's turn to place a bomb. " %(players[turns_taken%2].name)
	
	
	#computer getting a bomb location
	if (players[turns_taken%2] == players[1]):
		# print "computers special place. :) "
		# players[1].bomb_grid = utilities.generates_grid_location()
		# print players[1].bomb_grid,
		# players[1].bomb_str = players[1].my_ships_board.convert_grid_location_str(players[1].bomb_grid)
		# print players[1].bomb_str
		raw_input("Hit 'ENTER' for the Computer to take it's turn. ")

		players[1].save_comp_bomb_location()
		# print players[1].bomb_grid, players[1].bomb_str

		while(players[1].in_bombs_placed()):
			players[1].erase_bomb_locations()
			players[1].save_comp_bomb_location()

		print "\n%s placed a bomb at location %s." %(players[1].name, players[1].bomb_str)


	#human getting a bomb location
	if (players[turns_taken%2] == players[0]):
		print "Use letters A-J and numbers 1-10 for coordinates in the format 'A1'."
		#save valid bomb location str
		players[0].bomb_str = utilities.get_bomb_str(players[0].my_ships_board)
		# print players[turns_taken%2].bomb_str
		# Convert string location to a grid location
		players[0].create_bomb_grid(players[0].enemy_ships_board)

		# While bomb location is in bomb_list
		while (players[0].in_bombs_placed()):
		# 	While TRUE, 
			# Print ERROR MSG: already used pick new location
			print "Already bombed that spot."
			print "Pick a new location."
			
			# Get new bomb location
			# Save valid bomb location str
			players[0].bomb_str = utilities.get_bomb_str(players[0].my_ships_board)

			# Convert string location to a grid location
			players[0].create_bomb_grid(players[0].enemy_ships_board)
	
	# print players[(turns_taken%2)-1].name, "bomb at:", players[(turns_taken%2)-1].bomb_str
	
	# NOT in bomb_list,
	# Check if opponents ship @ location

	if(players[(turns_taken%2)-1].ships.check_for_hit(players[turns_taken%2].bomb_grid) == False):
	# If MISS

		# Handles all steps for when bomb misses ships
		players[turns_taken%2].handle_bomb_miss(players[(turns_taken%2)-1])
		# # Print Human player boards
		players[0].print_both_boards()
		
		# Print computer boards
		#players[1].print_player_boards()
		
		# NEXT PLAYERS TURN
		turns_taken += 1
		# print turns_taken, "turns_taken after the miss"
	else:
	# If HIT
		# Save ship object that was hit
		ship_hit = players[(turns_taken%2)-1].ships.check_for_hit(players[turns_taken%2].bomb_grid)
		
		# Handles all steps for when bomb hits a ship
		players[turns_taken%2].handle_bomb_hit(players[(turns_taken%2)-1])

		# # Print Human player boards
		# players[0].print_both_boards()
		# Print MSG that a ship was HIT
		
		# print players[(turns_taken%2)-1].name, "bomb at:", players[(turns_taken%2)-1].bomb_str
		# print "One of %s's ships was hit at location %s." %(players[(turns_taken%2)-1].name, players[(turns_taken%2)-1].bomb_str)
		
		

		# Print computers boards
		# players[1].print_player_boards()
		 #TEST code for ship being sunk
		# ship_hit.boat = ["X","X","X","X","X"]	
		# # TEST code for testing all ships sunk
		# players[0].ships.battleship.boat = ["X","X","X","X"] 
		# players[0].ships.cruiser.boat = ["X","X","X"]
		# players[0].ships.sub.boat = ["X","X","X"]
		# players[0].ships.destroyer.boat = ["X","X"]
		
		
		# print "before running is_sunk()"

		# print "carrier is sunk:", players[1].ships.carrier.sunk
		# print "battleship is sunk:", players[1].ships.battleship.sunk
		# print "cruiser is sunk:", players[1].ships.cruiser.sunk
		# print "sub is sunk:", players[1].ships.sub.sunk
		# print "destroyer is sunk:", players[1].ships.destroyer.sunk

		ship_hit.is_sunk()
		#TEST CODE
		# players[0].ships.battleship.is_sunk()
		# players[0].ships.cruiser.is_sunk()
		# players[0].ships.sub.is_sunk()
		# players[0].ships.destroyer.is_sunk()
		# print "after running is_sunk()"

		# print ship_hit.ship_name, "is sunk:",  ship_hit.sunk
		# print "battleship is sunk:", players[0].ships.battleship.sunk
		# print "cruiser is sunk:", players[0].ships.cruiser.sunk
		# print "sub is sunk:", players[0].ships.sub.sunk
		# print "destroyer is sunk:", players[0].ships.destroyer.sunk

		# Check if opponents ship sunk
		if(ship_hit.sunk):
			# Ship sunk
			# Print MSG that opponents ship sunk, Give name of sunk ship
			players[(turns_taken%2)-1].msg_ship_sunk(ship_hit)
			# print "before all ships set to sunk"
			# print players[1].ships.fleet_sunk, "computers fleet sunk"

			

			# print players[1].ships.battleship.boat  
			# print players[1].ships.cruiser.boat 
			# print players[1].ships.sub.boat 
			# print players[1].ships.destroyer.boat

			# print "after all ships set to sunk"

			# print "carrier is sunk:", players[1].ships.carrier.is_sunk()
			# print "battleship is sunk:", players[1].ships.battleship.is_sunk()
			# print "cruiser is sunk:", players[1].ships.cruiser.is_sunk()
			# print "sub is sunk:", players[1].ships.sub.is_sunk()
			# print "destroyer is sunk:", players[1].ships.destroyer.is_sunk()
			# print players[1].ships.fleet_sunk, "computers fleet sunk"

			# Check if all of opponents ships sunk
			players[(turns_taken%2)-1].ships.all_sunk()
			# players[1].ships.all_sunk()
			# print players[0].ships.fleet_sunk, players[0].name
			# print players[(turns_taken%2)-1].ships.fleet_sunk, players[(turns_taken%2)-1].name
			# if (players[(turns_taken%2)-1].ships.fleet_sunk == True):
			# # If FALSE
			# 	# print "Not all of %s's ships have been sunk." %(players[(turns_taken%2)-1].name)
			# 	print "All of %s's ships have been sunk." %(players[(turns_taken%2)-1].name)
			
			# 	NEXT PLAYERS TURN
				# turns_taken += 1
				# print turns_taken, "turns_taken after ship sunk but not fleet"
			# else:
			# NEXT PLAYERS TURN
				# print players[1].ships.fleet_sunk, "computers fleet sunk"
		
		#DELETE bomb variables
		players[(turns_taken%2)-1].erase_bomb_locations()
		# Print Human player boards
		players[0].print_both_boards()
		turns_taken += 1
		# print turns_taken, "turns_taken after check ship sunk"
			

if(not utilities.no_winner(players[(turns_taken%2)])):
	players[(turns_taken%2)-1].game_over_msg(players[(turns_taken%2)])
# if(not utilities.no_winner(players[(turns_taken%2-1)])):
# 	players[(turns_taken%2)].game_over_msg(players[(turns_taken%2-1)])

