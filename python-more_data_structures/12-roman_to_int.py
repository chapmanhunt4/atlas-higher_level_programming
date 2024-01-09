#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0
    for i in range(len(roman_string)):
        current_symbol = roman_dict[roman_string[i]]
        if i == len(roman_string) - 1 or current_symbol >= roman_dict[roman_string[i + 1]]:
            result += current_symbol
        else:
            result -= current_symbol
    return result
