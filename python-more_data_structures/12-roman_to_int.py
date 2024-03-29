#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0
    for i in range(len(roman_string)):
        cur_symbol = r_dict[roman_string[i]]
        if i == len(roman_string) - 1:
            result += cur_symbol
        elif cur_symbol >= r_dict[roman_string[i + 1]]:
            result += cur_symbol
        else:
            result -= cur_symbol
    return result
