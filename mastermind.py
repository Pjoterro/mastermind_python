# This is my take on mastermind game. It is not perfect but it is mine
#	- Pjoter 06.10.2022
VERSION = '2.0'

import random

#rules:
LENGTH_OF_COMBINATION = 6
NUMBER_OF_COLOURS = 9
MAX_NUMBER_OF_GUESSES = 8
UNIQUE_COMBINATION = True

def generate_combination():
	colours = list(range(1, NUMBER_OF_COLOURS + 1))
	combination = []
	for i in range(LENGTH_OF_COMBINATION):
		index = random.randint(0, len(colours)-1)
		combination.append(str(colours[index]))
		if (UNIQUE_COMBINATION):
			del colours[index]
	return combination

def compare_combinations(combination, guess):
	result = ''
	for i in range(len(guess)):
		if (guess[i] in combination):
			if (guess[i] == combination [i]):
				result += 'C'
			else:
				result += 'M'
		else:
			result += 'I'
	return result

def combination_to_string(combination):
	string = ''
	for i in range(len(combination)):
		string += str(combination[i])
	return string

def print_instruction():
	print('Welcome to Mastermind game!')
	print('You will be playing against computer. Try to gues the combination in ' + str(MAX_NUMBER_OF_GUESSES) +' tries')
	print('Computer will create combination of length ' + str(LENGTH_OF_COMBINATION) +  ' from ' + str(NUMBER_OF_COLOURS) + ' different colours (without blank spaces).')
	if(UNIQUE_COMBINATION):
		print('Duplicates are not allowed')
	else:
		print('Duplicates are allowed')
	print('When guessing combination write your guess and confirm using \"ENTER\" key')
	print('For example for unique combination of 4 using 6 colours - 4261')
	print('Program will print out combination of letters \"C\", \"I\" and \"M\"')
	print('\"C\" - correct number in correct place')
	print('\"I\" - incorrect number (is not present in combination)')
	print('\"M\" - missplaced letter (correct letter in incorrect place)')
	print('\n--- WARNING! ---\nGuess 4556 for combination 4567 will result in CCMM. The algorith does not check number of occurance\n')

print('____ MASTERMIND GAME ' + VERSION + ' ____\n')
print_instruction()
combination = generate_combination()

print('--- The setup is done, try to guess the combination! ---\n')
for guess_taken in range(0, MAX_NUMBER_OF_GUESSES):
	print('guess no. ' + str(guess_taken + 1) + ':\t', end='')
	guess = list(input())
	if (guess != combination):
		print('result: \t' + compare_combinations(combination, guess) + '\n')
	else:
		break

if (guess == combination):
	print('Congartulation! The combination was ' + combination_to_string(combination) + ' and you got it right')
else:
	print('Better luck next time.\nPS: the combination was ' + combination_to_string(combination))
