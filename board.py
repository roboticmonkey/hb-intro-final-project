class Board(object):
	"""Class creates a 10x10 game board with labels.

	"""

	def __init__(self):
		#list of capital letters
		self.capital_letters = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

		#start of board matrix
		self.board = [[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]]

		#for loop to create rest of the board
		for i in range(1,len(self.capital_letters)):
			temp = [self.capital_letters[i]]
			temp.extend(10 * " ")
			self.board.append(temp)

		
		
	#draws board one row at a time
	def draw_board_loop(self,matrix_board):
		for row in matrix_board:
			#print row
			#print len(item)
			print " %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % tuple(row)
			print "---------------------------------------------"

#player_board = Board()

#player_board.draw_board_loop(player_board.board)
