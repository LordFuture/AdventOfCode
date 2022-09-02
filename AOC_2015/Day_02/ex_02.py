#!/usr/bin/env python3
"""
Code used to solve Advent of Code 2015 Day 2 exercise 1
Advent of Code 2015, Day 02, Exercise 1
# https://adventofcode.com/2015
"""

import os


def length_of_ribbon_in_feet(length, width, height):
    """
    It takes the length, width, and height of a present, sorts the dimensions, and
    then returns the length of the ribbon needed to wrap the present plus the
    length of the bow needed to tie it
    
    :param length: the length of the present
    :param width: the width of the ribbon
    :param height: the height of the box
    :return: The length of the ribbon in feet.
    """
    sorted_dimensions = [length, width, height]
    sorted_dimensions.sort()
    length_of_ribbon = (2 * sorted_dimensions[0]) + (2 * sorted_dimensions[1])
    length_of_bow = length * width * height

    return length_of_ribbon + length_of_bow


def total_length_of_ribbon_in_feet(file_name):
    """
    It opens the file, reads each line, splits the line into three numbers, and
    then calls the function length_of_ribbon_in_feet to calculate the length of
    ribbon needed for each present. It then adds the length of ribbon needed for
    each present to the total length of ribbon needed for all the presents
    
    :param file_name: The name of the file that contains the dimensions of the
    boxes
    :return: The total length of ribbon in feet.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        total_length_ribbon = 0
        while True:
            line = file.readline()
            if not line:
                break
            length = int(line.split("x")[0])
            width = int(line.split("x")[1])
            height = int(line.split("x")[2])           
            total_length_ribbon += length_of_ribbon_in_feet(length, width, height)                

        return total_length_ribbon


def main():
    """
    It takes a file name as input, reads the file, and returns the total length of
    ribbon in feet needed to wrap all the presents in the file
    """
    os.system("cls || clear")

    file_name_test_file = "C:/source/repos/AdventOfCode/AOC_2015/Day_02/test_file.txt"
    file_name_puzzle_file = "C:/source/repos/AdventOfCode/AOC_2015/Day_02/puzzle_input_file.txt"
    test_file_answer = total_length_of_ribbon_in_feet(file_name_test_file)
    puzzle_file_answer = total_length_of_ribbon_in_feet(file_name_puzzle_file)
    print(f"test file: {test_file_answer}")
    print(f"puzzle file: {puzzle_file_answer}")

if __name__ == '__main__':
    main()
