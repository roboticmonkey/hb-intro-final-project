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











# print computer.sub.boat
# computer.sub.boat[0]= "X" 
# player_ship_grid.grid[1][1] = "X"
# print computer.sub.boat

# print "Player Ship Grid"
# player_ship_grid.draw_grid_loop(player_ship_grid.grid)




