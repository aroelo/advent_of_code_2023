# https://adventofcode.com/2023/day/3
from utils.utils import get_input_path
import numpy as np


def create_array_and_lines(file_path: str):
    lines = []
    numbers = []
    with open(file_path, "r") as f:
        for line in f:
            lines.append(line.strip("\n"))
            numbers.append(list(line.strip("\n")))
    numbers = np.array(numbers)
    return lines, numbers


def find_part_numbers(lines, numbers):
    sum_numbers = 0
    i = 0
    for line in lines:
        j = -1
        number = ""
        next_to_symbol = False
        for char in line:
            j += 1
            if char.isdigit():
                number += char
                if next_to_symbol:
                    continue
                neighbours = find_neighbours(numbers, i, j)
                for symbol in neighbours:
                    if not symbol.isalnum() and symbol != ".":
                        next_to_symbol = True
            else:
                if next_to_symbol:
                    sum_numbers += int(number)
                number = ""
                next_to_symbol = False
        if next_to_symbol:
            sum_numbers += int(number)
        i += 1
    return sum_numbers


def find_gears(lines, numbers):
    gears = {}
    i = 0
    for line in lines:
        j = -1
        number = ""
        next_to_gear = False
        for char in line:
            j += 1
            if char.isdigit():
                number += char
                if next_to_gear:
                    continue
                neighbours = find_neighbours(numbers, i, j)
                for idx, symbol in enumerate(neighbours):
                    if symbol == "*":
                        next_to_gear = True
                        if i == 0:
                            idx += 3
                        if idx < 3:
                            x_gear = j + (idx - 1)
                            y_gear = i - 1
                        elif idx < 6:
                            x_gear = j + idx - 4
                            y_gear = i
                        else:
                            x_gear = j + idx - 7
                            y_gear = i + 1
            else:
                if next_to_gear:
                    try:
                        gears[(x_gear, y_gear)].append(int(number))
                    except KeyError:
                        gears[(x_gear, y_gear)] = [int(number)]
                number = ""
                next_to_gear = False
        if next_to_gear:
            try:
                gears[(x_gear, y_gear)].append(int(number))
            except KeyError:
                gears[(x_gear, y_gear)] = [int(number)]
        i += 1

    total = 0
    for numbers in gears.values():
        if len(numbers) == 2:
            total += numbers[0] * numbers[1]
    return total


# function to find the start row and column
def find_start(x):
    start = x - 1 if x - 1 >= 0 else 0
    return start


# function to find the end row and column
def find_end(x, shape):
    end = x + 1 if x + 1 <= shape else shape
    return end


def find_neighbours(a, i, j):
    neighbours = []
    row_start, row_end = find_start(i), find_end(i, a.shape[0])
    col_start, col_end = find_start(j), find_end(j, a.shape[1])

    for y in range(a.shape[0]):
        for z in range(a.shape[1]):
            if y >= row_start and y <= row_end:
                if z >= col_start and z <= col_end:
                    neighbours.append(a[y][z])
    return neighbours


def main():
    # Test input
    test_file_path = get_input_path("3.txt", test=True)
    lines, numbers = create_array_and_lines(test_file_path)

    # test_first_answer = find_part_numbers(lines, numbers)
    # assert test_first_answer == 4369
    test_second_answer = find_gears(lines, numbers)
    assert test_second_answer == 467835

    # Real input
    file_path = get_input_path("3.txt")
    lines, numbers = create_array_and_lines(file_path)

    first_answer = find_part_numbers(lines, numbers)
    assert first_answer == 537832
    second_answer = find_gears(lines, numbers)
    assert second_answer == 81939900


if __name__ == "__main__":
    main()
