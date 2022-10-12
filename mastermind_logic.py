import random
import re

def generate_combination(combination_length, digits_variety, difficulty):
    colours = list(range(0, digits_variety))
    combination = []
    for i in range(combination_length):
        index = random.randint(0, len(colours)-1)
        combination.append(str(colours[index]))
        if (difficulty == 0):
            del colours[index]
    return combination

# TODO: redo when implementing difficulty
def compare_combinations(combination, guess, difficulty):
    result = ''

#     for i in range(len(guess)):
#         if (guess[i] == combination[i]):
#             result += 'C'
#             if (difficulty != 2):
#                 combination[i] = ' ' # wstawia pusty znak
#         else:
#             if (guess[i] in combination & guess[i] != combination[i]):


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

def input_regex_comparing(combination, regex):
    pattern = re.compile(regex)
    match = re.match(pattern, combination)
    if match:
        return True
    else:
        return False

def regex_creator(combination_length, digits_variety):
    return '[0-' + str(digits_variety - 1) + ']{' + str(combination_length) + '}'