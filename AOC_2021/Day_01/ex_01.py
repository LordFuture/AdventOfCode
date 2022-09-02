#!/usr/bin/env python3
import os


def get_depth_sum(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        depth_count = 0
        old_value = 0
        line_count = 0
        while True:
            line = f.readline()
            if not line:
                break
            line_count += 1
            if line_count != 1:
                new_value = int(line.strip())
                if new_value > old_value:
                    depth_count += 1

                old_value = new_value

    return depth_count


def main():
    os.system("cls || clear")

    FILE_NAME_TEST_FILE = "C:/source/repos/AdventOfCode/AOC_2015/Day_01/test_file.txt"
    FILE_NAME_PUZZLE_FILE = "C:/source/repos/AdventOfCode/AOC_2015/Day_01/puzzle_input_file.txt"
    depth_count_test_file = get_depth_sum(FILE_NAME_TEST_FILE)
    depth_count_puzzle_file = get_depth_sum(FILE_NAME_PUZZLE_FILE)
    print(f"test file: {depth_count_test_file}")
    print(f"puzzle file: {depth_count_puzzle_file}")


if __name__ == '__main__':
    main()
