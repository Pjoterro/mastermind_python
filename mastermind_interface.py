4-9 znakow
 |===========================|
 |    M.A.S.T.E.R.M.I.N.D    |
 |===========================|
 |        COMBINATION:       |
 |    X-X-X-X-X-X-X-X-X-X    |
 |===========================|
 |1:  1 2 3 4 5 6 7 8 9 0    |
 |R:  C M I C M I C M I C    |
 |===========================|


def format_combination(input):
	result = ''
	for i in range(len(input)):
		result += input[i]
		if (i != len(input) - 1):
			result += '-'
	return result

def print_header():
	print(' |===========================|')
	print(' |    M.A.S.T.E.R.M.I.N.D    |')

def print_difficulty():
	#TODO


def print_combination(length):
	print(' |===========================|')
	print(' |        COMBINATION:       |')
	line = ' |' + (13-length)*' ' + format_combination('X'*length) + (13-length)*' ' + '|'
	print(line)

def print_try(number, guess, result):
	print(' |===========================|')
	line1 = ' |' + str(number) + ':' + (13-len(str(number))-len(guess))*' ' + format_combination(guess) + (13-len(guess))*' ' + '|'
	print(line1)
	line2 = ' |R:' + (12-len(guess))*' ' + format_combination(result) + (13-len(guess))*' ' + '|'
	print(line2)

def print_win():
	print(' |===========================|')
	print(' |      Congratulations,     |')
	print(' |   you guessed correctly!  |')
	print(' |===========================|')

def print_loose(combination):
	print(' |===========================|')
	print(' |          You lost,        |')
	print(' |   better luck next time.  |')
	print(' |                           |')
	print(' | PS: The combinationw was: |')
	line = ' |' + (13-len(combination))*' ' + format_combination(combination) + (13-len(combination)*' ' + '|'
	print(' |===========================|')
