import random
import re

def generate_combination(combination_length, digits_variety, is_unique):
    colours = list(range(0, digits_variety))
    combination = []
    for i in range(combination_length):
        index = random.randint(0, len(colours)-1)
        combination.append(str(colours[index]))
        if (is_unique):
            del colours[index]
    return combination

# TODO: redo when implementing difficulty
def compare_combinations(combination, guess, difficulty):
    if (difficulty == 0 or difficulty == 2):
        return compare_easy_or_hard(combination, guess)
    else:
        return compare_medium(combination, guess)

def compare_easy_or_hard(combination, guess):
    result = ''
    for i in range(len(guess)):
        if (guess[i] in combination):
            if (guess[i] == combination[i]):
                result += 'C'
            else:
                result += 'M'
        else:
            result += 'I'
    return result

def compare_medium(combination, guess):
    combination_temp = combination
    result = [None] * len(combination_temp)
    for i in range(len(result)):
        if (guess[i] == combination_temp[i]):
            result[i] = 'C'
            guess[i] = ' '
            combination_temp[i] = ' '
    for j in range(len(result)):
        if(guess[j] != ' '):
            if (guess[j] in combination_temp):
                result[j] = 'M'
            else:
                result[j] = 'I'
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