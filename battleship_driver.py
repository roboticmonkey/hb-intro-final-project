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
#testing horizontal placement
computer.sub.start_location = "A1"
computer.sub.end_location = "A3"
print computer.sub.start_location
print computer.sub.size

computer.sub.grid_loc_start = [
			computer.convert_loc_letter_index(player_ship_grid, computer.sub.start_location),
			computer.convert_loc_str_index(computer.sub.start_location)]
print computer.sub.grid_loc_start

computer.sub.grid_loc_end = [
			computer.convert_loc_letter_index(player_ship_grid, computer.sub.end_location),
			computer.convert_loc_str_index(computer.sub.end_location)]
print computer.sub.grid_loc_end

if (computer.sub.grid_loc_start[0] == computer.sub.grid_loc_end[0]):
	print "Horizontal"
else: 
	print "verticle"

player_ship_grid.update_grid_ship_hor(player_ship_grid.grid, computer.sub)
print "Player Ship Grid"
player_ship_grid.draw_grid_loop(player_ship_grid.grid)

#testing vertical placement
computer.cruiser.start_location = "H1"
computer.cruiser.end_location = "J1"
print computer.cruiser.start_location
print computer.cruiser.size

computer.cruiser.grid_loc_start = [
			computer.convert_loc_letter_index(player_ship_grid, computer.cruiser.start_location),
			computer.convert_loc_str_index(computer.cruiser.start_location)]
print computer.cruiser.grid_loc_start

computer.cruiser.grid_loc_end = [
			computer.convert_loc_letter_index(player_ship_grid, computer.cruiser.end_location),
			computer.convert_loc_str_index(computer.cruiser.end_location)]
print computer.cruiser.grid_loc_end

player_ship_grid.update_grid_ship_vert(player_ship_grid.grid, computer.cruiser)
print "Player Ship Grid"
player_ship_grid.draw_grid_loop(player_ship_grid.grid)

print computer.sub.boat
computer.sub.boat[0]= "X" 
player_ship_grid.grid[1][1] = "X"
print computer.sub.boat

print "Player Ship Grid"
player_ship_grid.draw_grid_loop(player_ship_grid.grid)


