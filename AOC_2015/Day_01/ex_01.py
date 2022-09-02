#!/usr/bin/env python3
"""
Code used to solve Advent of Code 2015 Day 1 exercise 1
Advent of Code 2015, Day 01, Exercise 1
# https://adventofcode.com/2015
"""

import os

def correct_floor(file_name):
    """
    It opens the file, reads it line by line, and for each line, it reads each
    character and adds or subtracts 1 from the floor number depending on whether
    the character is an opening or closing parenthesis

    :param file_name: the name of the file you want to read
    :return: The floor number
    """
    with open(file_name, "r", encoding="utf-8") as file:
        floor_number = 0
        while True:
            line = file.readline()
            if not line:
                break
            for char in line:
                if char == '(':
                    floor_number += 1
                else:
                    floor_number -= 1
    return floor_number


def main():
    """
    It opens the file, reads the file, and then counts the number of '(' and ')'
    characters in the file
    """
    os.system("cls || clear")

    file_name_test_file = "C:/source/repos/AdventOfCode/AOC_2015/Day_01/test_file.txt"
    file_name_puzzle_file = "C:/source/repos/AdventOfCode/AOC_2015/Day_01/puzzle_input_file.txt"
    test_file_answer = correct_floor(file_name_test_file)
    puzzle_file_answer = correct_floor(file_name_puzzle_file)
    print(f"test file: {test_file_answer}")
    print(f"puzzle file: {puzzle_file_answer}")


if __name__ == '__main__':
    main()
