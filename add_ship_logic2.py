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
print "You have 5 ships at varying lengths."
print "They are:"

#List all the ships for the player
# player1.list_ship_name_and_sizes()
for key, value in player1.ships.all_ships_dictionary.items():
	print key.ship_name, "with a length of", value


#Print empty ships board
player1.print_my_ships_board()

#*****************************************
#HARDCODED CARRIER
#creating carriers info
# player1.ships.carrier.start_location = "B3"
# player1.ships.carrier.end_location = "B7"
# player1.ships.carrier.create_grid_start_loc(player1.my_ships_board)
# player1.ships.carrier.create_grid_end_loc(player1.my_ships_board)
# player1.ships.carrier.create_grid_loc_list()



# player1.ships.add_ship_loc_dict(player1.ships.carrier)
# player1.my_ships_board.update_grid_ship(player1.ships.carrier)

# #Print empty ships board
# player1.print_my_ships_board()

#*************************************
#CREATING ADDING POSITIVE LOGIC 

#Code to ask user to place their ships
utilities.request_placement_of_ship(player1.ships.carrier, player1.my_ships_board, player1.ships, player1)
utilities.request_placement_of_ship(player1.ships.battleship, player1.my_ships_board, player1.ships, player1)
utilities.request_placement_of_ship(player1.ships.cruiser, player1.my_ships_board, player1.ships, player1)
utilities.request_placement_of_ship(player1.ships.sub, player1.my_ships_board, player1.ships, player1)
utilities.request_placement_of_ship(player1.ships.destroyer, player1.my_ships_board, player1.ships, player1)









