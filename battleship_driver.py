import board
import ship
import game_pieces


player_ship_grid = board.Board()
player_bomb_grid = board.Board()
print "Player Ship Grid"
player_ship_grid.draw_grid_loop(player_ship_grid.grid)
print "Player Bomb Grid"
player_bomb_grid.draw_grid_loop(player_bomb_grid.grid)

computer = game_pieces.Game_Pieces("Computer")

#testing how to place ships and keep track of location

print "testing ship placement"
#hardcoding ship locations
computer.carrier.start_location ="D8"
computer.carrier.end_location = "H8"

computer.battleship.start_location = "I3"
computer.battleship.end_location ="I6"

computer.cruiser.start_location = "A7"
computer.cruiser.end_location = "A9"

computer.sub.start_location = "B1"
computer.sub.end_location = "B3"

computer.destroyer.start_location ="E4"
computer.destroyer.end_location = "F4"
#creating the gird locations
computer.create_ship_grid_locations(player_ship_grid)

#updateing the ship board
player_ship_grid.update_grid_ship(computer.carrier)
player_ship_grid.update_grid_ship(computer.destroyer)
player_ship_grid.update_grid_ship(computer.battleship)
player_ship_grid.update_grid_ship(computer.sub)
player_ship_grid.update_grid_ship(computer.cruiser)

#printing an updated board
print "Player Ship Grid"
player_ship_grid.draw_grid_loop(player_ship_grid.grid)

#working out finding bombs in ships
bomb = [6,8]
print "bomb:", bomb

# def test_funct (bomb, game_pieces):
# 	for key, value in game_pieces.all_ships.items():
# 		#print key, value
# 		for i in range(len(value)):
# 			if (bomb == value[i]):
# 				print "ship hit:", key
# 				print "bomb found index: ", i
# 				print key.ship_name
# 				return key, i
			
# test_var = test_funct(bomb, computer)

# print test_var
# print test_var[0].boat
# print test_var[0].boat[test_var[1]]
# test_var[0].boat[test_var[1]] = "X"
# print test_var[0].boat[test_var[1]]
# print test_var[0].boat

# print computer.carrier.boat

# player_ship_grid.update_grid_ship(computer.carrier)

# print "Player Ship Grid"
# player_ship_grid.draw_grid_loop(player_ship_grid.grid)

bomb2 = [5,4]
print "bomb2:", bomb2
bomb3 = [1,4]
print "bomb3:", bomb3

 
# checking bomb for hit and update
if (computer.check_for_hit(bomb) != False):
	computer.check_for_hit(bomb).record_ship_hit(bomb)
else:
	player_ship_grid.grid[bomb[0]][bomb[1]] = "O"
	print "miss"

if (computer.check_for_hit(bomb2) != False):
	computer.check_for_hit(bomb2).record_ship_hit(bomb2)
else:
	player_ship_grid.grid[bomb2[0]][bomb2[1]] = "O"
	print "miss"

if (computer.check_for_hit(bomb3) != False):
	computer.check_for_hit(bomb3).record_ship_hit(bomb3)
else:
	player_ship_grid.record_miss(bomb3)
	print "miss"



player_ship_grid.update_grid_game_pieces(computer)

print "Player Ship Grid"
player_ship_grid.draw_grid_loop(player_ship_grid.grid)

computer.destroyer.boat = ["X", "X"]
print computer.destroyer.boat
print computer.destroyer.is_sunk()
print "sub sunk:", computer.sub.is_sunk()








# print computer.sub.boat
# computer.sub.boat[0]= "X" 
# player_ship_grid.grid[1][1] = "X"
# print computer.sub.boat

# print "Player Ship Grid"
# player_ship_grid.draw_grid_loop(player_ship_grid.grid)




