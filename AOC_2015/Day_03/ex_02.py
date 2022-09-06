#!/usr/bin/env python3
"""
Code used to solve Advent of Code 2015 Day 3 exercise 2
Advent of Code 2015, Day 03, Exercise 2
# https://adventofcode.com/2015
"""

import os


def deliver_more_than_once(file_name):
    """
    It reads the file character by character, and if the character is a direction,
    it moves the santa or robot in that direction.

    It then adds the new position to a set, which will only contain unique values.


    The length of the set is then returned.

    :param file_name: The name of the file that contains the directions
    :return: The number of houses that received at least one present.
    """
    santa_start_position = [0, 0]
    robot_start_position = [0, 0]
    more_than_once = {tuple(santa_start_position.copy())}
    postion_of_character = 0
    with open(file_name, "r", encoding="utf-8") as file:
        while True:
            character = file.read(1)
            if not character:
                break

            postion_of_character += 1
            if character == "^":
                if postion_of_character % 2 == 0:
                    robot_start_position[1] += 1
                else:
                    santa_start_position[1] += 1
            elif character == ">":
                if postion_of_character % 2 == 0:
                    robot_start_position[0] += 1
                else:
                    santa_start_position[0] += 1
            elif character == "v":
                if postion_of_character % 2 == 0:
                    robot_start_position[1] -= 1
                else:
                    santa_start_position[1] -= 1
            elif character == "<":
                if postion_of_character % 2 == 0:
                    robot_start_position[0] -= 1
                else:
                    santa_start_position[0] -= 1

            more_than_once.add(tuple(santa_start_position.copy()))
            more_than_once.add(tuple(robot_start_position.copy()))

    return len(more_than_once)


def main():
    """
    It reads the file, and then it uses a dictionary to keep track of the number of
    times each house has been visited.

    The dictionary is initialized with the starting house (0,0) having been visited
    once.

    Then, for each character in the file, it moves the current house in the
    direction indicated by the character, and increments the number of times that
    house has been visited.

    Finally, it returns the number of houses that have been visited more than once
    """
    os.system("cls || clear")

    file_name_test_file = "C:/source/repos/AdventOfCode/AOC_2015/Day_03/test_file.txt"
    file_name_puzzle_file = "C:/source/repos/AdventOfCode/AOC_2015/Day_03/puzzle_input_file.txt"
    test_file_answer = deliver_more_than_once(file_name_test_file)
    puzzle_file_answer = deliver_more_than_once(file_name_puzzle_file)
    print(f"test file: {test_file_answer}")
    print(f"puzzle file: {puzzle_file_answer}")

if __name__ == '__main__':
    main()
