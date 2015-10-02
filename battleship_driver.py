import board

player_shipgrid = board.Board()
player_bombgrid = board.Board()
print "Player Ships"
player_shipgrid.draw_board_loop(player_shipgrid.board)
print "Player Bomb Board"
player_bombgrid.draw_board_loop(player_bombgrid.board)
