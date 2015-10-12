import board
import ship
import game_pieces
import utilities
import player


print "Welcome to Battleship!"

#game set up. Get player 1 name and validate input
raw_data = raw_input("Player 1 please enter your name. ")
raw_data = utilities.quick_fix(raw_data)

#validate name
while (not raw_data.isalpha()):
	raw_data = raw_input("Please enter a valid name. ")
	raw_data = utilities.quick_fix(raw_data)

#create player1 object
player1 = player.Player(raw_data)
print "Hello,", player1.name
print "You have 5 ships at varying lengths. You may place your ships horizontally or vertically."
print "Your 5 ships are:"
print player1.ships.carrier.ship_name, "which has a length of", player1.ships.carrier.size
print player1.ships.battleship.ship_name, "which has a length of", player1.ships.battleship.size
print player1.ships.cruiser.ship_name, "which has a length of", player1.ships.cruiser.size
print player1.ships.sub.ship_name, "which has a length of", player1.ships.sub.size
print player1.ships.destroyer.ship_name, "which has a length of", player1.ships.destroyer.size

#print empty ships board
print "My Ships"
player1.my_ships_board.draw_grid_loop(player1.my_ships_board.grid)

#ask user for start coordinate
print "Use letters A-J and numbers 1-10 for coordinates in the format 'A1'. "
print "Let's place your", player1.ships.carrier.ship_name, "first."
print "Remember, the ", player1.ships.carrier.ship_name, "is ", player1.ships.carrier.size, "cells long."
raw_data = raw_input("Please give the starting coordinates. Ex. 'A1'. ")
raw_data = utilities.quick_fix(raw_data)

#validating coordinate format
while (not utilities.valid_letter(raw_data, player1.my_ships_board) or not utilities.valid_number(raw_data)):
	raw_data = raw_input("Please re-enter coordinates in format 'A1'. ")
	raw_data = utilities.quick_fix(raw_data)


#save start location string into ships start_location attribute

#convert start_location to a grid_location and save 

#ask for end location coordinates

#check if grid location is already filled

#if not empty ask user new input

#if empty, ask for end location coordinates

#valid user input for end location

#save end location string into ship end_location attribute

#create ship grid location list

#if create_grid_loc_list returns false ask user to re-enter coordinates

#if true, add ships grid_loc_list to game_pieces all_ships dict

#update players ship_board

#print new players ship board

#repeat for each ship



#creating computer coordinates for ship
start_coord = [player1.my_ships_board.convert_loc_letter_index(raw_data), 
	player1.my_ships_board.convert_loc_str_index(raw_data)]




#check if there is already a ship there
if (player1.ships.all_ships == {}):
	#save string location into start_location
	player1.ships.carrier.ship_location_start(raw_data)
	print player1.ships.carrier.start_location, "is your starting location. Ships may only be horizontal or vertical."
	raw_data2 = raw_input("Enter your ending coordinates. ")
	raw_data2 = utilities.quick_fix(raw_data2)

	#validating valid coordinate format
	while (not utilities.valid_letter(raw_data2, player1.my_ships_board) or not utilities.valid_number(raw_data)):
		raw_data2 = raw_input("Please re-enter coordinates in format 'A1'. ")
		raw_data2 = utilities.quick_fix(raw_data2)

#save string location into end_location
	player1.ships.carrier.ship_location_end(raw_data2)

	print player1.ships.carrier.end_location






	

