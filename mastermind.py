# This is my take on mastermind game. It is not perfect but it is mine
#	- Pjoter 06.10.2022
VERSION = '3.0.0'

from mastermind_interface import *
from mastermind_menu import *
from mastermind_logic import *

#Length of the combination can be between 4 and 10
LENGTH_OF_COMBINATION = 5

#Numbers of colours between 6 and 10
NUMBER_OF_COLOURS = 7

#Max number of guesses bewteen 4 and 99
MAX_NUMBER_OF_GUESSES = 6

#Combination can be unique (without duplicated digits) or not unique
#TODO: change this to difficulty level
UNIQUE_COMBINATION = True

# 0 - easy - no duplicates
# 1 - medium - with duplicates but result count number of occurence
# 2 - hard - with duplicates and result does not show number of occurance
DIFFICULTY = 0

print('____ MASTERMIND GAME ' + VERSION + ' ____\n')
print_welcome(LENGTH_OF_COMBINATION, NUMBER_OF_COLOURS, UNIQUE_COMBINATION)
print_instruction()
print_mechanic()
combination = generate_combination(LENGTH_OF_COMBINATION, NUMBER_OF_COLOURS, UNIQUE_COMBINATION)
print('--- The setup is done, try to guess the combination! ---\n')

print_header()
print_combination(LENGTH_OF_COMBINATION)
for guess_taken in range(0, MAX_NUMBER_OF_GUESSES):
	print_input()
	guess = list(input())
	print_try(guess_taken, guess, compare_combinations(combination, guess))
	if (guess == combination):
		break

if (guess == combination):
	print_win()
else:
	print_loose(combination)
