location = ["", "A", "B", 1, "", "", 2, "", ""]

def draw_board(moves):
	print " %s | %s | %s " % (moves[0], moves[1], moves[2])
	print "-----------"
	print " %s | %s | %s " % (moves[3], moves[4], moves[5])
	print "-----------"
	print " %s | %s | %s " % (moves[6], moves[7], moves[8])

draw_board(location)

# Creates a list containing 5 lists initialized to 0
matrix = [["X" for x in range(5)] for x in range(5)] 
print matrix

matrix2 = [[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], 
	["A", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
	["B", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
	["C", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
	["D", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
	["E", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
	["F", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
	["G", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
	["H", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
	["I", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
	["J", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "] ]

def draw_board2(moves):
	print " %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (moves[0][0], moves[0][1], moves[0][2], 
		moves[0][3], moves[0][4], moves[0][5], moves[0][6], moves[0][7], moves[0][8], moves[0][9], moves[0][10])
	print "---------------------------------------------"
	print " %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (moves[1][0], moves[1][1], moves[1][2], 
		moves[1][3], moves[1][4], moves[1][5], moves[1][6], moves[1][7], moves[1][8], moves[1][9], moves[1][10])
	print "---------------------------------------------"
	print " %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (moves[2][0], moves[2][1], moves[2][2], 
		moves[2][3], moves[2][4], moves[2][5], moves[2][6], moves[2][7], moves[2][8], moves[2][9], moves[2][10])
	print "---------------------------------------------"
	print " %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (moves[3][0], moves[3][1], moves[3][2], 
		moves[3][3], moves[3][4], moves[3][5], moves[3][6], moves[3][7], moves[3][8], moves[3][9], moves[3][10])
	print "---------------------------------------------"
	print " %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (moves[4][0], moves[4][1], moves[4][2], 
		moves[4][3], moves[4][4], moves[4][5], moves[4][6], moves[4][7], moves[4][8], moves[4][9], moves[4][10])
	print "---------------------------------------------"
	print " %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (moves[5][0], moves[5][1], moves[5][2], 
		moves[5][3], moves[5][4], moves[5][5], moves[5][6], moves[5][7], moves[5][8], moves[5][9], moves[5][10])
	print "---------------------------------------------"
	print " %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (moves[6][0], moves[6][1], moves[6][2], 
		moves[6][3], moves[6][4], moves[6][5], moves[6][6], moves[6][7], moves[6][8], moves[6][9], moves[6][10])
	print "---------------------------------------------"
	print " %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (moves[7][0], moves[7][1], moves[7][2], 
		moves[7][3], moves[7][4], moves[7][5], moves[7][6], moves[7][7], moves[7][8], moves[7][9], moves[7][10])
	print "---------------------------------------------"
	print " %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (moves[8][0], moves[8][1], moves[8][2], 
		moves[8][3], moves[8][4], moves[8][5], moves[8][6], moves[8][7], moves[8][8], moves[8][9], moves[8][10])
	print "---------------------------------------------"
	print " %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (moves[9][0], moves[9][1], moves[9][2], 
		moves[9][3], moves[9][4], moves[9][5], moves[9][6], moves[9][7], moves[9][8], moves[9][9], moves[9][10])
	print "---------------------------------------------"
	print " %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (moves[10][0], moves[10][1], moves[10][2], 
		moves[10][3], moves[10][4], moves[10][5], moves[10][6], moves[10][7], moves[10][8], moves[10][9], moves[10][10])
	print "---------------------------------------------"

#draw_board2(matrix)

draw_board2(matrix2)
print " "
matrix2[4][3] = "X"
draw_board2(matrix2)