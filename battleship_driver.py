import board
import ship


player_shipgrid = board.Board()
player_bombgrid = board.Board()
print "Player Ships"
player_shipgrid.draw_board_loop(player_shipgrid.board)
print "Player Bomb Board"
player_bombgrid.draw_board_loop(player_bombgrid.board)

carrier = ship.Ship(5, "Carrier")
print carrier
print carrier.sunk
print carrier.end_location
print type(carrier.size)
print carrier.boat
print type(carrier.boat[3])
print len(carrier.boat)