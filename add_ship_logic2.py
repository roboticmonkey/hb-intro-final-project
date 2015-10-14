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

#*****************************************
#HARDCODED CARRIER
#creating carriers info
player1.ships.carrier.start_location = "B3"
player1.ships.carrier.end_location = "B7"
player1.ships.carrier.create_grid_start_loc(player1.my_ships_board)
player1.ships.carrier.create_grid_end_loc(player1.my_ships_board)
player1.ships.carrier.create_grid_loc_list(player1.my_ships_board)



player1.ships.add_ship_loc_dict(player1.ships.carrier)
player1.my_ships_board.update_grid_ship(player1.ships.carrier)

#Print empty ships board
player1.print_my_ships_board()

#*************************************
#CREATING ADDING POSITIVE LOGIC 

#Ask user for start coordinate
print "Use letters A-J and numbers 1-10 for coordinates in the format 'A1'. "
print "Let's place your", player1.ship_tuple[1][0], "."
print "Remember, the ", player1.ship_tuple[1][0], "is ", player1.ship_tuple[1][1], "cells long."

raw_data = raw_input("Please give the starting coordinates. Ex. 'A1'. ")
raw_data = utilities.quick_fix(raw_data)

#Validates string, asks for new one till it validates
temp_location_str = utilities.request_valid_location(raw_data, player1.my_ships_board)

	#Save start location string into ships start_location attribute
player1.ships.battleship.ship_location_start(temp_location_str)
	
print player1.ships.battleship.start_location

	#Convert start_location to a grid_location and save 
player1.ships.battleship.create_grid_start_loc(player1.my_ships_board)
print player1.ships.battleship.grid_loc_start
	
	#Check of location is taken
	#If all_ship dictionary is empty get end coordinates
if (player1.ships.all_ships == {}):
	#Ask for end location coordinates
	print player1.ships.battleship.start_location, "is your starting location. Ships may only be horizontal or vertical."
	raw_data = raw_input("Enter your ending coordinates. ")
	raw_data = utilities.quick_fix(raw_data)

	#Valitdate user input string asks for valid string till it gets one. 
	temp_location_str = utilities.request_valid_location(raw_data, player1.my_ships_board)

	#Saves the location string
	player1.ships.battleship.ship_location_end(temp_location_str)	

	#Save end location string into ship end_location attribute
	player1.ships.battleship.create_grid_end_loc(player1.my_ships_board)

	#Create ship grid location list
	#If true, add ships grid_loc_list to game_pieces all_ships dict
	if (player1.ships.battleship.create_grid_loc_list(player1.my_ships_board) == True):
		
		#print "list made man"
		player1.ships.add_ship_loc_dict(player1.ships.battleship)

		#print player1.ships.all_ships
		
		#Update players ship_board
		player1.my_ships_board.update_grid_ship(player1.ships.battleship)
		
		#Print updated players ship board
		player1.print_my_ships_board()
	#If grid locations list could not be made
	else:
		#Print Error msg.
		print "Ships may only be placed horizontally or vertically. Please re-enter your coordinates."
		#DELETE all location variables
		player1.ships.battleship.erase_start_locations()
		player1.ships.battleship.end_locations()

		#Go Back to getting Start Location coordinates

		#WRITE CODE TO GO BACK TO START
		
			
#If all_ship dictionary has something in it, check location against the dictionary
else:
	#Check if start grid location is taken
	#Check if ship already at location
	print "dictionary not empty"
	if (player1.ships.is_taken(player1.ships.battleship.grid_loc_start) == False):
		#Location not taken ask for end location

		#Ask for end location coordinates
		print player1.ships.battleship.start_location, "is your starting location. Ships may only be horizontal or vertical."
		raw_data = raw_input("Enter your ending coordinates. ")
		raw_data = utilities.quick_fix(raw_data)

		#Valitdate user input string asks for valid string till it gets one. 
		temp_location_str = utilities.request_valid_location(raw_data, player1.my_ships_board)

		#Saves the location string
		player1.ships.battleship.ship_location_end(temp_location_str)
		#Creates the grid location
		player1.ships.battleship.create_grid_end_loc(player1.my_ships_board)
				
		#Check if end location is already taken
		if (player1.ships.is_taken(player1.ships.battleship.create_grid_end_loc) == False):
			#If it is not taken
			#Create ship grid location list
			
			if (player1.ships.battleship.create_grid_loc_list(player1.my_ships_board) == True):
				#If true, add ships grid_loc_list to game_pieces all_ships dict
				# print "list made man"
				print player1.ships.battleship.grid_loc_list
						
				#Check if ship location list overlaps a previous ship
				if (player1.ships.is_overlap(player1.ships.battleship) == False):
					#Save location list to ship location dictionary
					player1.ships.add_ship_loc_dict(player1.ships.battleship)

					#print player1.ships.all_ships
		
					#Update players ship_board
					player1.my_ships_board.update_grid_ship(player1.ships.battleship)
		
					#Print updated players ship board
					player1.print_my_ships_board()

					#WRITE CODE TO START AGAIN WITH NEXT SHIP
				else:
					#If it overlaps print error msg. 
					print "Ships maynot overlap. Please re-enter your coordinates."
					#DELETE all location variables
					player1.ships.battleship.erase_start_locations()
					player1.ships.battleship.end_locations()
					player1.ships.battleship.erase_grid_location_list()
					
					#Go Back to getting Start Location coordinates

					#WRITE CODE TO GO BACK TO START
			
			#If grid locations list could not be made
			else:
				#Print Error msg.
				print "Ships may only be placed horizontally or vertically. Please re-enter your coordinates."
				#DELETE all location variables
				player1.ships.battleship.erase_start_locations()
				player1.ships.battleship.end_locations()

				#Go Back to getting Start Location coordinates

				#WRITE CODE TO GO BACK TO START
		#If location is already taken ask user to re-enter coordinates
		else:
			
			print "Ships maynot overlap. Please re-enter your coordinates."
			#DELETE start and end location variables
			player1.ships.battleship.erase_start_locations()
			player1.ships.battleship.end_locations()

			#Go Back to getting Start Location coordinates
			
			#WRITE CODE TO GO BACK TO START
	


	#If start location is already taken 
	else:
		#Give error msg.
		print "Ships maynot overlap. Please re-enter your coordinates."
		#DELETE start location variables
		player1.ships.battleship.erase_start_locations()

	#WRITE CODE TO GO BACK TO START
			

	
















