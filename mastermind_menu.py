def print_instruction():
        print('Welcome to Mastermind game!')
        print('You will be playing against computer. Try to gues the combination in ' + str(MAX_NUMBER_OF_GUESSES) +' tries')
        print('Computer will create combination of length ' + str(LENGTH_OF_COMBINATION) +  ' from ' + str(NUMBER_OF_COLOURS) + ' diffe>
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
