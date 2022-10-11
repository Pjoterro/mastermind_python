def print_welcome(length, max_number, is_unique):
	print('Welcome to Mastermind game!')
	print('Your task is to guess the code created by the computer.')
	print('The code will be between ' + str(length) + ' digits long.')
	print('The code may contain numbers from 0 to ' + str(max_number) + '.')
	if(is_unique):
		print('Duplicates are not allowed.')
	else:
		print('Duplicates are allowed.')

def print_instruction():
	print('Your task is to guess the combination created by computer.')
	print('After you each try computer will give you back a result.')
	print('You will be informed if you guessed the correct number on the correct place, \nif the number occurs on different place or if the number does not occur at all.')
	print('You win if you manage to guess the combination within the move limit.')

def print_mechanic():
	print('When providing your solution please use either dashes (-), spaces ( ) or nothing between digits.')
	print('For example a valid input for four digits long solution is: \"1234\", \"1-2-3-4\", \"1 2 3 4\".')
	print('After providing your guess, program will return a combination of letters \"C\", \"I\" and \"M\".')
	print('\"C\" - correct number in correct place')
	print('\"I\" - incorrect number (is not present in combination)')
	print('\"M\" - missplaced letter (correct letter in incorrect place)')
	print('For combination \"4-8-2-6\", a guess \"4-5-3-8\" will result in \"C-I-I-M\."')
	print('4 - is (C)orrect')
	print('5 - is (I)ncorrect')
	print('3 - is (I)ncorrect')
	print('8 - is (M)issplaced')

def print_example():
	print('TODO: mastermind_menu.py::print_example()')

def print_credits():
	print('Game created by Piotr Twardowski.')
	print('My GitHub: Pjoterro')