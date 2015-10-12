import board


test_grid = board.Board()


#different error checking things. not sure how to organize yet.

# remove extra spaces
# raw_data = raw_input("Give a coordinate.")
# raw_data = raw_data.upper()
# if (len(raw_data) != 2):
# 	raw_data = raw_data.strip(" ")

# if (len(raw_data) != 2):
# 	print "Please enter coordinates in format 'A1'."
# 	raw_data = raw_input("Give a coordinate. ")

# if (not raw_data[0] in test_grid.capital_letters):
# 	print raw_data, "is in wrong format"

#check for valid number range. returns True of False
def valid_number(user_input):

	if (len(user_input) == 2):
		
		if (user_input[1] == "0"):
			return False
		else:
			return True

	if (len(user_input) !=2):
		if (len(user_input) == 3):
			number = user_input[1]+user_input[2]

			if (number == "10"):
				return True
			else:
				return False

#remove extra spaces and capitalizes letters returns fixed input
def quick_fix(user_input):
	#remove extra spaces
	user_input = user_input.strip(" ")

	#makes lowercase letters capital
	user_input = user_input.upper()

	return user_input

#check for valid letter range return True or False
def valid_letter(user_input, board):
	if (not user_input[0] in board.capital_letters):
		return False
	else:
		return True

name ="  fred  "
name2 = "fart knuckles"
name3 = "jim"
name4 = "djskah748"

name = quick_fix(name)
print name, "is all alpha:", name.isalpha()

name2 = quick_fix(name2)
print name2, "is all alpha:", name2.isalpha()

name3 = quick_fix(name3)
print name3, "is all alpha:", name3.isalpha()

name4 = quick_fix(name4)
print name4, "is all alpha:", name4.isalpha()

test_value = "   f10   "
test_value2 = "r6" 
test_value3 = "  d14"
test_value4 = "   H0"

print "test value 1"
print test_value
test_value = quick_fix(test_value)
print test_value
print "letter in range:", valid_letter(test_value, test_grid)
print "number in range:", valid_number(test_value)

print "test test_value2"
print test_value2
test_value2 = quick_fix(test_value2)
print test_value2
print "letter in range:", valid_letter(test_value2, test_grid)
print "number in range:", valid_number(test_value2)

print "test_value3"
print test_value3
test_value3 = quick_fix(test_value3)
print test_value3
print "letter in range:", valid_letter(test_value3, test_grid)
print "number in range." ,valid_number(test_value3)

print "test_value4"
print test_value4
test_value4 = quick_fix(test_value4)
print test_value4
print "letter in range:", valid_letter(test_value4, test_grid)
print "number in range:", valid_number(test_value4)

		# def check_valid_end_location(self, end_location):
		# if (self.start_location[0] == end_location[0]):
		# 	if (self.start_location[1] - end_location[1] == self.size):
		# 		return True 
		# 	else:
		# 		return False 
		# elif (self.start_location[1] == end_location[1]):
		# 	if ()