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

# Validate string bomb location

# If invalid ask for string bomb location again

# If valid save string

# Convert string location to a grid location

# Check if bomb location is in bomb_list

# 	If TRUE, 
# 		Print ERROR MSG: already used pick new location

# 		CODE ASK FOR NEW LOCATION

# 	If FALSE in bomb_list, 

# 		Check if opponents ship @ location

# 			If FALSE

# 				Save bomb location to bomb_list

# 				Update player enemy ship board with MISS

# 				Update opponents  my ship board with MISS

# 				Print MSG bomb missed

# 				Print updated enemy ship board

# 				NEXT PLAYERS TURN

# 			If TRUE

# 				Save bomb location to bomb_list

# 				Update enemy hit ship with HIT at bomb location

# 				Print MSG that a ship was HIT

# 				Update player enemy ship board with HIT

# 				Update opponents  my ship board with HIT

# 				Print updated enemy ship board

# 				Check if opponents ship sunk

# 				If FALSE

# 					Print MSG no ship sunk

# 					NEXT PLAYERS TURN

# 				If TRUE

# 					Print MSG that opponents ship sunk, Give name of sunk ship

# 					Check if all of opponents ships sunk

# 						If FALSE

# 							NEXT PLAYERS TURN

# 						If TRUE

# 							Print MSG the all of opponents ships are sunk

# 							Print MSG congrats MSG to winner

# 							Print MSG that game is over

# 							GAME OVER 
















	

