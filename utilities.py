import board


test_grid = board.Board()

#check for valid number range. returns True of False
def valid_number(user_input):

	if (len(user_input) == 2):
		
		if (user_input[1] == "0"):
			return False
		else:
			return True

	if (len(user_input) !=2):
		if (len(user_input) == 3):
			number = user_input[1]+user_input[2]

			if (number == "10"):
				return True
			else:
				return False

#remove extra spaces and capitalizes letters returns fixed input
def quick_fix(user_input):
	#remove extra spaces
	user_input = user_input.strip(" ")

	#makes lowercase letters capital
	user_input = user_input.upper()

	return user_input

#check for valid letter range return True or False
def valid_letter(user_input, board):
	if (not user_input[0] in board.capital_letters):
		return False
	else:
		return True

#Validating coordinate format
def validate_user_input(user_input, board):
	if (valid_letter(user_input, board) and valid_number(user_input)):
		return True
	else:
		return False

#Ask for and return valid location string
def request_valid_location(raw_data, board):
	
	while(not validate_user_input(raw_data, board)):
		raw_data = raw_input("Please give coordinates in format 'A1'. ")
		raw_data = quick_fix(raw_data)
	
	return raw_data

def request_placement_of_ship(ship_object, board_object, game_pieces_object, player_object):
	while (ship_object.location_list_full() == False):
		#Grid location list is empty. 
		
		print "Ships may only be placed horizontally or vertically."

		#Ask user for start coordinate
		print "Use letters A-J and numbers 1-10 for coordinates in the format 'A1'. "
		print "Let's place your", ship_object.ship_name, "."
		print ship_object.ship_name, "is ", ship_object.size, "cells long."

		raw_data = raw_input("Please give the starting coordinates. Ex. 'A1'. ")
		raw_data = quick_fix(raw_data)
		# print raw_data

		#Validates string, asks for new one till it validates
		temp_location_str = request_valid_location(raw_data, board_object)

			#Save start location string into ships start_location attribute
		ship_object.ship_location_start(temp_location_str)
			
		# print ship_object.start_location

			#Convert start_location to a grid_location and save 
		ship_object.create_grid_start_loc(board_object)
		# print ship_object.grid_loc_start

		#Check of location is taken
		#If all_ship dictionary is empty get end coordinates
		if (game_pieces_object.all_ship_locations == {}):
		#Ask for end location coordinates
			print ship_object.start_location, "is your starting location. Ships may only be horizontal or vertical."
			raw_data = raw_input("Enter your ending coordinates. ")
			raw_data = quick_fix(raw_data)

			#Valitdate user input string asks for valid string till it gets one. 
			temp_location_str = request_valid_location(raw_data, board_object)

			#Saves the location string
			ship_object.ship_location_end(temp_location_str)	

			#Save end location string into ship end_location attribute
			ship_object.create_grid_end_loc(board_object)

			#Create ship grid location list
			#If true, add ships grid_loc_list to game_pieces all_ships dict
			ship_object.create_grid_loc_list()
		else:
		#Check if start grid location is taken
		#Check if ship already at location
			# print "dictionary not empty"

			if (game_pieces_object.is_taken(ship_object.grid_loc_start) == False):
			#Location not taken ask for end location

			#Ask for end location coordinates
				print ship_object.start_location, "is your starting location. Ships may only be horizontal or vertical."
				raw_data = raw_input("Enter your ending coordinates. ")
				raw_data = quick_fix(raw_data)

				#Valitdate user input string asks for valid string till it gets one. 
				temp_location_str = request_valid_location(raw_data, board_object)

				#Saves the location string
				ship_object.ship_location_end(temp_location_str)
				#Creates the grid location
				ship_object.create_grid_end_loc(board_object)
						
				#Check if end location is already taken
				if (game_pieces_object.is_taken(ship_object.create_grid_end_loc) == True):
					#If it is not taken
					#Create ship grid location list
					#DELETE all location variables
					ship_object.erase_start_locations()
					ship_object.erase_end_locations()
					print "Ships maynot overlap. Please re-enter your coordinates."
				else:
					#Create ship grid location list
					#If true, add ships grid_loc_list to game_pieces all_ships dict
					ship_object.create_grid_loc_list()
				#Check if ship location list overlaps a previous ship
				if (game_pieces_object.is_overlap(ship_object) == True):
					
					#If it overlaps print error msg. 
					print "Ships maynot overlap. Please re-enter your coordinates."
					#DELETE all location variables
					ship_object.erase_start_locations()
					ship_object.erase_end_locations()
					ship_object.erase_grid_location_list()
					
					#Go Back to getting Start Location coordinates

	# print ship_object.grid_loc_list

	# Save location list to ship location dictionary
	game_pieces_object.add_ship_loc_dict(ship_object)


	#Update players ship_board
	board_object.update_grid_ship(ship_object)

	#Print updated players ship board
	player_object.print_my_ships_board()

#Asks for and returns a valid str bomb location
def get_bomb_str(player_board_object):
	raw_data = raw_input("Enter coordinates for a bomb. ")
	raw_data = quick_fix(raw_data)
	# print raw_data

	# Validate string bomb location
	# If invalid ask for string bomb location again
	raw_data = request_valid_location(raw_data, player_board_object)
	# print raw_data 
	return raw_data



