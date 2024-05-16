#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num_list = []
    for letter in roman_string:
        if (letter in roman):
            num_list.append(roman[letter])
        else:
            return None
    for i in range(len(num_list) - 1):
        if num_list[i] < num_list[i + 1]:
            num_list[i] = -num_list[i]
    return sum(num_list)
        