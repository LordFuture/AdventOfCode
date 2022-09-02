#!/usr/bin/env python3
"""
Code used to solve Advent of Code 2015 Day 1 exercise 1
Advent of Code 2015, Day 01, Exercise 1
# https://adventofcode.com/2015
"""

import os

def character_position(file_name):
    """
    It reads the file line by line, and for each line it reads each character, and
    if it's an opening bracket it adds 1 to the floor number, and if it's a closing
    bracket it subtracts 1 from the floor number, and if the floor number is -1 it
    breaks out of the loop and returns the character position

    :param file_name: The name of the file to be read
    :return: The character position of the first character that causes Santa to
    enter the basement.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        floor_number = 0
        while True:
            line = file.readline()
            if not line:
                break
            character_pos = 1
            for char in line:
                if char == '(':
                    floor_number += 1
                else:
                    floor_number -= 1
                if floor_number == -1:
                    break
                character_pos += 1
    return character_pos


def main():
    """
    It takes a file name as an argument, opens the file, reads the file, and
    returns the position of the character in the file
    """
    os.system("cls || clear")

    file_name_test_file = "C:/source/repos/AdventOfCode/AOC_2015/Day_01/test_file.txt"
    file_name_puzzle_file = "C:/source/repos/AdventOfCode/AOC_2015/Day_01/puzzle_input_file.txt"
    test_file_answer = character_position(file_name_test_file)
    puzzle_file_answer = character_position(file_name_puzzle_file)
    print(f"test file: {test_file_answer}")
    print(f"puzzle file: {puzzle_file_answer}")


if __name__ == '__main__':
    main()
