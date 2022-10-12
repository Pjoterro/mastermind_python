# This is my take on mastermind game. It is not perfect but it is mine
#	- Pjoter 06.10.2022
VERSION = '3.1.1'

from mastermind_interface import *
from mastermind_menu import *
from mastermind_logic import *

# Length of the combination can be between 4 and 10
COMBINATION_LENGTH = 4

# Numbers of colours between 6 and 10
DIGITS_VARIETY = 6

# Max number of guesses bewteen 4 and 99
MAX_GUESSES = 10

# Combination can be unique (without duplicated digits) or not unique
#TODO: change this to difficulty level
IS_UNIQUE = True

# 0 - easy - no duplicates
# 1 - medium - with duplicates but result count number of occurence
# 2 - hard - with duplicates and result does not show number of occurance
DIFFICULTY = 0

combination = generate_combination(COMBINATION_LENGTH, DIGITS_VARIETY, IS_UNIQUE)

print_header(VERSION)
print_difficulty(COMBINATION_LENGTH, DIGITS_VARIETY, IS_UNIQUE)
guess_taken = 0
while guess_taken < MAX_GUESSES:
	print_input()
	guess = list(input())

	# TODO: make it work with regex
	# if (input_regex_comparing(combination_to_string(guess), regex_creator(COMBINATION_LENGTH, DIGITS_VARIETY))):
	# 	print_wrong_input()

	if (len(guess) != len(combination)):
		print_wrong_input()
	else:
		guess_taken += 1
		print_try(guess_taken, guess, compare_combinations(combination, guess))
		if (guess == combination):
			break

if (guess == combination):
	print_win()
else:
	print_loose(combination)
