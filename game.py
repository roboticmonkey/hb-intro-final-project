import board
import ship
import game_pieces
import utilities
import player


print "Welcome to Battleship!"

#Game set up. Get player 1 name and validate input
raw_data = raw_input("Player 1 please enter your name. ")
raw_data = utilities.quick_fix(raw_data)

#Validate name
while (not raw_data.isalpha()):
	raw_data = raw_input("Please enter a valid name. ")
	raw_data = utilities.quick_fix(raw_data)

#Create player1 object
player1 = player.Player(raw_data)
print "Hello,", player1.name
print "You have 5 ships at varying lengths. You may place your ships horizontally or vertically."
print "Your 5 ships are:"

#List all the ships for the player
player1.list_ship_name_and_sizes()

#Print empty ships board
player1.print_my_ships_board()

#FIRST TIME THROUGH

#Ask user for start coordinate
print "Use letters A-J and numbers 1-10 for coordinates in the format 'A1'. "
print "Let's place your", player1.ships.carrier.ship_name, "."
print "Remember, the ", player1.ships.carrier.ship_name, "is ", player1.ships.carrier.size, "cells long."
raw_data = raw_input("Please give the starting coordinates. Ex. 'A1'. ")
raw_data = utilities.quick_fix(raw_data)

#If not valid coordinate format, re-ask for input
while (not utilities.validate_user_input(raw_data, player1.my_ships_board)):
	raw_data = raw_input("Please re-enter coordinates in format 'A1'. ")
	raw_data = utilities.quick_fix(raw_data)


#Save start location string into ships start_location attribute
player1.ships.carrier.ship_location_start(raw_data)
# print player1.ships.carrier.start_location

#Convert start_location to a grid_location and save 
player1.ships.carrier.create_grid_start_loc(player1.my_ships_board)
# print player1.ships.carrier.grid_loc_start

#Check if all_ship dict is empty
#If all_ship dict is empty get end coordinates
if (player1.ships.all_ships == {}):
	#Ask for end location coordinates
	print player1.ships.carrier.start_location, "is your starting location. Ships may only be horizontal or vertical."
	raw_data2 = raw_input("Enter your ending coordinates. ")
	raw_data2 = utilities.quick_fix(raw_data2)

	#If not valid coordinate format, re-ask for input
	while (not utilities.validate_user_input(raw_data, player1.my_ships_board)):
		raw_data = raw_input("Please re-enter coordinates in format 'A1'. ")
		raw_data = utilities.quick_fix(raw_data)

	#Save end location string into ship end_location attribute
	player1.ships.carrier.ship_location_end(raw_data2)
	player1.ships.carrier.create_grid_end_loc(player1.my_ships_board)
	#print player1.ships.carrier.grid_loc_end
	
	#Create ship grid location list
	#If true, add ships grid_loc_list to game_pieces all_ships dict
	if (player1.ships.carrier.create_grid_loc_list(player1.my_ships_board) == True):
		
		#print "list made man"
		player1.ships.add_ship_loc_dict(player1.ships.carrier)

		#print player1.ships.all_ships
		
		#update players ship_board
		player1.my_ships_board.update_grid_ship(player1.ships.carrier)
		
		#Print updated players ship board
		player1.print_my_ships_board()

	else:
		#If create_grid_loc_list returns false ask user to re-enter coordinates
		print "whoops"

#Repeat for each ship
#SECOND TIME THROUGH

#Ask for user input start coordinates
print "Let's place your", player1.ships.battleship.ship_name, "."
print "Remember, the ", player1.ships.battleship.ship_name, "is ", player1.ships.battleship.size, "cells long."
raw_data = raw_input("Please give the starting coordinates. Ex. 'A1'. ")
raw_data = utilities.quick_fix(raw_data)

#If not valid coordinate format, re-ask for input
while (not utilities.validate_user_input(raw_data, player1.my_ships_board)):
	raw_data = raw_input("Please re-enter coordinates in format 'A1'. ")
	raw_data = utilities.quick_fix(raw_data)

#Is valid save locaction string
player1.ships.battleship.ship_location_start(raw_data)

#Convert location string to grid coordinates
player1.ships.battleship.create_grid_start_loc(player1.my_ships_board)

#Check if ship already at location
while (player1.ships.is_taken(player1.ships.battleship.grid_loc_start) == True):
	#If ship already there ask for new location
	#Erase start locations
	player1.ships.battleship.erase_start_locations()
	# print raw_data, "before new input"
	raw_data = raw_input("Two ships cannot occupy the same spot. Please choose a new spot. ") 
	# print raw_data, "after new input"
	raw_data = utilities.quick_fix(raw_data)

	#If not valid coordinate format, re-ask for input
	while (not utilities.validate_user_input(raw_data, player1.my_ships_board)):
		raw_data = raw_input("Please re-enter coordinates in format 'A1'. ")
		raw_data = utilities.quick_fix(raw_data)

	#Is valid save locaction string
	player1.ships.battleship.ship_location_start(raw_data)

	#Convert location string to grid coordinates
	player1.ships.battleship.create_grid_start_loc(player1.my_ships_board)


#If not ask for end location
print player1.ships.battleship.start_location, "is your starting location. Ships may only be horizontal or vertical."
raw_data2 = raw_input("Enter your ending coordinates. ")
raw_data2 = utilities.quick_fix(raw_data2)

#If not valid coordinate format, re-ask for input
while (not utilities.validate_user_input(raw_data, player1.my_ships_board)):
	raw_data = raw_input("Please re-enter coordinates in format 'A1'. ")
	raw_data = utilities.quick_fix(raw_data)

#If valid save end location string into ship end_location attribute
player1.ships.battleship.ship_location_end(raw_data2)
player1.ships.battleship.create_grid_end_loc(player1.my_ships_board)
# print player1.ships.battleship.grid_loc_start[0], ":location start"
# print player1.ships.battleship.create_grid_loc_list(player1.my_ships_board)
# print player1.ships.battleship.grid_loc_end[0], ":location end"
# print player1.ships.battleship.grid_loc_list, ":location list"

# Create grid location list
# print "starting the check of ship list.\n"
if (player1.ships.battleship.create_grid_loc_list(player1.my_ships_board) == True):
	
	#Check if grid location list matches any already placed ship
	if (player1.ships.is_overlap(player1.ships.battleship) == True):
		
		#If True, give error and ask for new start location
		#Set all location values to empty
		print "Ships cannot overlap. Re-enter ship location.\n"
		
		#Erase start locations
		player1.ships.battleship.erase_start_locations()
	
		#Erase end locations
		player1.ships.battleship.erase_end_locations()
				
		#Erase grid location list
		player1.ships.battleship.erase_grid_location_list()
		# print "all ship location variables should be empty"
		# print "start_location:", player1.ships.battleship.start_location
		# print "end location:", player1.ships.battleship.end_location
		# print "grid location start:", player1.ships.battleship.grid_loc_start
		# print "grid location end:", player1.ships.battleship.grid_loc_end
		# print "grid location list:", player1.ships.battleship.grid_loc_list
	
	#START OVER FOR INFORMATION

		print "Let's place your", player1.ships.battleship.ship_name, "."
		print "Remember, the ", player1.ships.battleship.ship_name, "is ", player1.ships.battleship.size, "cells long."
		raw_data = raw_input("Please give the starting coordinates. Ex. 'A1'. ")
		raw_data = utilities.quick_fix(raw_data)

		#If not valid coordinate format, re-ask for input
		while (not utilities.validate_user_input(raw_data, player1.my_ships_board)):
			raw_data = raw_input("Please re-enter coordinates in format 'A1'. ")
			raw_data = utilities.quick_fix(raw_data)

		#Is valid save locaction string
		player1.ships.battleship.ship_location_start(raw_data)

		#Convert location string to grid coordinates
		player1.ships.battleship.create_grid_start_loc(player1.my_ships_board)
		#Check if ship already at location
		while (player1.ships.is_taken(player1.ships.battleship.grid_loc_start) == True):
			
			#If ship already there ask for new location
			# print raw_data, "before new input"
			raw_data = raw_input("Two ships cannot occupy the same spot. Please choose a new spot. ") 
			# print raw_data, "after new input"
			raw_data = utilities.quick_fix(raw_data)

			#If not valid coordinate format, re-ask for input
			while (not utilities.validate_user_input(raw_data, player1.my_ships_board)):
				raw_data = raw_input("Please re-enter coordinates in format 'A1'. ")
				raw_data = utilities.quick_fix(raw_data)

			#Is valid save locaction string
			player1.ships.battleship.ship_location_start(raw_data)

			#Convert location string to grid coordinates
			player1.ships.battleship.create_grid_start_loc(player1.my_ships_board)


		#If not ask for end location
		print player1.ships.battleship.start_location, "is your starting location. Ships may only be horizontal or vertical."
		raw_data2 = raw_input("Enter your ending coordinates. ")
		raw_data2 = utilities.quick_fix(raw_data2)

		#If not valid coordinate format, re-ask for input
		while (not utilities.validate_user_input(raw_data, player1.my_ships_board)):
			raw_data = raw_input("Please re-enter coordinates in format 'A1'. ")
			raw_data = utilities.quick_fix(raw_data)

		#If valid save end location string into ship end_location attribute
		player1.ships.battleship.ship_location_end(raw_data2)
		player1.ships.battleship.create_grid_end_loc(player1.my_ships_board)

		# Create grid location list
		if (player1.ships.battleship.create_grid_loc_list(player1.my_ships_board) == True):

			#Check if grid location list matches any already placed ship
			if (player1.ships.is_overlap(player1.ships.battleship) == True):
				print "again?"
			else:
				#If no, update all ships dictionary
				player1.ships.add_ship_loc_dict(player1.ships.battleship)

				#print player1.ships.all_ships
				
				#Update players ship_board
				player1.my_ships_board.update_grid_ship(player1.ships.battleship)
				
				#Print players ship board
				player1.print_my_ships_board()



	else:
		#If no, update all ships dictionary
		player1.ships.add_ship_loc_dict(player1.ships.battleship)

		#print player1.ships.all_ships
		
		#Update players ship_board
		player1.my_ships_board.update_grid_ship(player1.ships.battleship)
		
		#Print players ship board
		player1.print_my_ships_board()

# print player1.ship_tuple
# print player1.ship_tuple[1]
# print player1.ship_tuple[1][0]
# START AGAIN WITH NEXT SHIP











	

