#!/usr/bin/env python3
"""
Code used to solve Advent of Code 2015 Day 4 exercise 2
Advent of Code 2015, Day 04, Exercise 2
# https://adventofcode.com/2015
"""

import os
import hashlib
import timeit

def read_secret_key(file_name):
    """
    It opens the file, reads the first line, and returns it

    :param file_name: The name of the file that contains the secret key
    :return: The line read from the file.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        while True:
            if line := file.readline():
                return line
            break



def get_hash(file_name):
    """
    It takes a file name as input, reads the secret key from the file, and then
    iterates through a million numbers, calculating the MD5 hash of the secret key
    concatenated with the number. If the first 6 characters of the hash are
    zeroes, it returns the number. If it doesn't find a number that works, it
    returns zero

    :param file_name: The name of the file that contains the secret key
    :return: The number of iterations it took to find the hash.
    """
    secret_key = read_secret_key(file_name)
    for i in range(10000000):
        calculated_hash = hashlib.md5((secret_key + str(i)).encode()).hexdigest()
        if calculated_hash[:6] == '000000':
            return i

    return 0



def main():
    """
    It takes a file name as input, reads the file, and returns the lowest number
    that can be appended to the file's contents to produce a hash that starts with
    five zeros
    """
    start = timeit.default_timer()

    os.system("cls || clear")

    file_name_test_file = "C:/source/repos/AdventOfCode/AOC_2015/Day_04/test_file.txt"
    file_name_puzzle_file = "C:/source/repos/AdventOfCode/AOC_2015/Day_04/puzzle_input_file.txt"
    test_file_answer = get_hash(file_name_test_file)
    puzzle_file_answer = get_hash(file_name_puzzle_file)
    print(f"test file: {test_file_answer}")
    print(f"puzzle file: {puzzle_file_answer}")

    stop = timeit.default_timer()
    total_time = stop - start

    # output running time in a nice format.
    mins, secs = divmod(total_time, 60)
    hours, mins = divmod(mins, 60)
    print(f"Total running time: {hours}:{mins}:{secs}")


if __name__ == '__main__':
    main()
