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
computer.carrier.create_grid_start_loc(player_ship_grid)
computer.carrier.create_grid_end_loc(player_ship_grid)

computer.battleship.start_location = "I3"
computer.battleship.end_location ="I6"
computer.battleship.create_grid_start_loc(player_ship_grid)
computer.battleship.create_grid_end_loc(player_ship_grid)


computer.cruiser.start_location = "A7"
computer.cruiser.end_location = "A9"
computer.cruiser.create_grid_start_loc(player_ship_grid)
computer.cruiser.create_grid_end_loc(player_ship_grid)

computer.sub.start_location = "B1"
computer.sub.end_location = "B3"
computer.sub.create_grid_start_loc(player_ship_grid)
computer.sub.create_grid_end_loc(player_ship_grid)

computer.destroyer.start_location ="H4"
computer.destroyer.end_location = "I4"
computer.destroyer.create_grid_start_loc(player_ship_grid)
computer.destroyer.create_grid_end_loc(player_ship_grid)
#creating the grid locations



if (computer.carrier.create_grid_loc_list(player_ship_grid) == True):
	# print "list made man"
	computer.add_ship_loc_dict(computer.carrier)
	# print computer.all_ships
else:
	print "whoops"


computer.battleship.create_grid_loc_list(player_ship_grid)
computer.add_ship_loc_dict(computer.battleship)
computer.cruiser.create_grid_loc_list(player_ship_grid)
computer.add_ship_loc_dict(computer.cruiser)
computer.sub.create_grid_loc_list(player_ship_grid)

print computer.sub.ship_name, "found overlap:", computer.is_overlap(computer.sub)

computer.add_ship_loc_dict(computer.sub)
computer.destroyer.create_grid_loc_list(player_ship_grid)

# for key, value in computer.all_ships.items():
# 	# print key, value
# 	for i in range(len(value)):
# 		for n in range(len(computer.destroyer.grid_loc_list)):
# 			print "n:", n, "i:", i
# 			print "destroyer:",computer.destroyer.grid_loc_list[n], key, value[i]
# 			if (computer.destroyer.grid_loc_list[n] == value[i]):
# 				print "destroyer:", computer.destroyer.grid_loc_list[n]
# 				print "matches:", key.ship_name, value[i], "at index:", i

print computer.destroyer.ship_name, "found overlap:", computer.is_overlap(computer.destroyer)

computer.add_ship_loc_dict(computer.destroyer)
# print computer.all_ships




#updateing the ship board
player_ship_grid.update_grid_ship(computer.carrier)
player_ship_grid.update_grid_ship(computer.battleship)
player_ship_grid.update_grid_ship(computer.cruiser)
player_ship_grid.update_grid_ship(computer.sub)
player_ship_grid.update_grid_ship(computer.destroyer)

# #printing an updated board
print "Player Ship Grid"
player_ship_grid.draw_grid_loop(player_ship_grid.grid)

# #working out finding bombs in ships
# bomb = [6,8]
# print "bomb:", bomb

# # def test_funct (bomb, game_pieces):
# # 	for key, value in game_pieces.all_ships.items():
# # 		#print key, value
# # 		for i in range(len(value)):
# # 			if (bomb == value[i]):
# # 				print "ship hit:", key
# # 				print "bomb found index: ", i
# # 				print key.ship_name
# # 				return key, i
			
# # test_var = test_funct(bomb, computer)

# # print test_var
# # print test_var[0].boat
# # print test_var[0].boat[test_var[1]]
# # test_var[0].boat[test_var[1]] = "X"
# # print test_var[0].boat[test_var[1]]
# # print test_var[0].boat

# # print computer.carrier.boat

# # player_ship_grid.update_grid_ship(computer.carrier)

# # print "Player Ship Grid"
# # player_ship_grid.draw_grid_loop(player_ship_grid.grid)

# bomb2 = [5,4]
# print "bomb2:", bomb2
# bomb3 = [1,4]
# print "bomb3:", bomb3

 
# # checking bomb for hit and update
# if (computer.check_for_hit(bomb) != False):
# 	computer.check_for_hit(bomb).record_ship_hit(bomb)
# else:
# 	player_ship_grid.grid[bomb[0]][bomb[1]] = "O"
# 	print "miss"

# if (computer.check_for_hit(bomb2) != False):
# 	computer.check_for_hit(bomb2).record_ship_hit(bomb2)
# else:
# 	player_ship_grid.grid[bomb2[0]][bomb2[1]] = "O"
# 	print "miss"

# if (computer.check_for_hit(bomb3) != False):
# 	computer.check_for_hit(bomb3).record_ship_hit(bomb3)
# else:
# 	player_ship_grid.record_miss(bomb3)
# 	print "miss"



# player_ship_grid.update_grid_game_pieces(computer)

# print "Player Ship Grid"
# player_ship_grid.draw_grid_loop(player_ship_grid.grid)

# computer.destroyer.boat = ["X", "X"]
# print computer.destroyer.boat
# print computer.destroyer.is_sunk()
# print "sub sunk:", computer.sub.is_sunk()








# print computer.sub.boat
# computer.sub.boat[0]= "X" 
# player_ship_grid.grid[1][1] = "X"
# print computer.sub.boat

# print "Player Ship Grid"
# player_ship_grid.draw_grid_loop(player_ship_grid.grid)




