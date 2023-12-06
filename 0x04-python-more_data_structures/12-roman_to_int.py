#!/usr/bin/python3

def roman_to_int(roman_string):
    romans = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'DM': 900,
        'M': 1000,
    }
    num = 0

    if roman_string is None or not isinstance(roman_string, str):
        return 0

    for figure in sorted(romans.keys(), key=len, reverse=True):
        while figure in roman_string:
            roman_string = roman_string.replace(figure, '', 1)
            num += romans[figure]
    return num
