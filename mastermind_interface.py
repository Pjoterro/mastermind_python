# | <--  27 characters    --> |
# | <--  betweeen pipes   --> |

def format_combination(input):
	result = ''
	for i in range(len(input)):
		result += input[i]
		if (i != len(input) - 1):
			result += '-'
	return result

def print_header(version):
	print('\n |###########################|')
	print(' |     MASTERMIND v' + version + '     |')

def print_difficulty(combination_length, digits_variety, is_unique):
	print(' |===========================|')
	print(' | Digits Variety: 0 - ' + str(digits_variety-1) + '     |')
	if (is_unique):
		is_unique_symbol = 'Yes'
	else:
		is_unique_symbol = 'No '
	print(' | Is Unique: ' + is_unique_symbol + '            |')
	print(' |        COMBINATION:       |')
	line = ' |' + (14-combination_length)*' ' + format_combination('X'*combination_length) + (14-combination_length)*' ' + '|'
	print(line)
	print(' |===========================|')

def print_input():
	print(' |Your guess:', end = ' ')

def print_try(guess_number, guess, result):
	print(' |---                     ---|')
	line1 = ' |T' + str(guess_number) + ':' + (12-len(str(guess_number))-len(guess))*' ' + format_combination(guess) + (14-len(guess))*' ' + '|'
	print(line1)
	line2 = ' |R:' + (12-len(guess))*' ' + format_combination(result) + (14-len(guess))*' ' + '|'
	print(line2)
	print(' |=======             =======|')

def print_win():
	print(' |      Congratulations,     |')
	print(' |   you guessed correctly!  |')
	print(' |###########################|\n')

def print_loose(combination):
	print(' |          You lost,        |')
	print(' |   better luck next time.  |')
	print(' | PS: The combinationw was: |')
	line = ' |' + (14-len(combination))*' ' + format_combination(combination) + (14-len(combination))*' ' + '|'
	print(line)
	print(' |###########################|\n')

def print_wrong_input():
	print(' |  WRONG INPUT, TRY AGAIN!  |')
	print(' |---                     ---|')