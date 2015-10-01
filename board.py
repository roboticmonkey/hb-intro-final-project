class Board(object):
	"""Class creates a 10x10 game board with labels.

	"""
	
	def __init__(self):
		#list of capital letters
		capital_letters = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

		#start of board matrix
		board = [[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]]

		#for loop to create rest of the board
		for i in range(1,len(capital_letters)):
			temp = [capital_letters[i]]
			temp.extend(10 * " ")
			board.append(temp)

		
		
		