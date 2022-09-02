#!/usr/bin/env python3
"""
Code used to solve Advent of Code 2015 Day 2 exercise 1
Advent of Code 2015, Day 02, Exercise 1
# https://adventofcode.com/2015
"""

import os


def total_surface_area_parcel_in_sq_feet(length, width, height):
    """
    > Given a parcel's length, width, and height, return the total surface area of
    the parcel in square feet
    
    :param length: The length of the parcel in inches
    :param width: the width of the box, in inches
    :param height: The height of the parcel in inches
    :return: The slack and the surface area
    """
    sorted_dimensions = [length, width, height]
    sorted_dimensions.sort()
    slack = sorted_dimensions[0] * sorted_dimensions[1]
    surface_area = (2 * length * width) + (2 * width * height) + (2 * length * height)

    return slack + surface_area


def total_wrapping_paper_in_sq_feet(file_name):
    """
    It reads the file line by line, splits the line into three parts, converts the
    three parts into integers, and then passes the three integers to the function
    total_surface_area_parcel_in_sq_feet.

    The function total_surface_area_parcel_in_sq_feet returns the total surface
    area of the parcel in square feet.

    The function total_wrapping_paper_in_sq_feet adds the total surface area of the
    parcel to the total wrapping paper.

    The function total_wrapping_paper_in_sq_feet returns the total wrapping paper
    in square feet

    :param file_name: The name of the file that contains the dimensions of the
    parcels
    :return: The total wrapping paper in square feet.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        total_wrapping_paper = 0
        while True:
            line = file.readline()
            if not line:
                break
            length = int(line.split("x")[0])
            width = int(line.split("x")[1])
            height = int(line.split("x")[2])           
            total_wrapping_paper += total_surface_area_parcel_in_sq_feet(length, width, height)                

        return total_wrapping_paper


def main():
    """
    It takes a file name as input, reads the file, and returns the total amount of
    wrapping paper needed to wrap all the presents in the file
    """
    os.system("cls || clear")

    file_name_test_file = "C:/source/repos/AdventOfCode/AOC_2015/Day_02/test_file.txt"
    file_name_puzzle_file = "C:/source/repos/AdventOfCode/AOC_2015/Day_02/puzzle_input_file.txt"
    test_file_answer = total_wrapping_paper_in_sq_feet(file_name_test_file)
    puzzle_file_answer = total_wrapping_paper_in_sq_feet(file_name_puzzle_file)
    print(f"test file: {test_file_answer}")
    print(f"puzzle file: {puzzle_file_answer}")

if __name__ == '__main__':
    main()
