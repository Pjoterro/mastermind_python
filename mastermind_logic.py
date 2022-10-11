import random

def generate_combination(length, variety, unique):
    colours = list(range(0, variety))
    combination = []
    for i in range(length):
        index = random.randint(0, len(colours)-1)
        combination.append(str(colours[index]))
        if (unique):
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
