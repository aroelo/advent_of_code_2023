# https://adventofcode.com/2023/day/9
from utils.utils import get_input_path
from typing import List


def part_1(file_path: str) -> int:
    """

    :param file_path: File path of input data
    :return:
    """
    total_next_value = 0
    with open(file_path, "r") as f:
        for line in f:
            values = [int(val) for val in line.strip("\n").split(" ")]
            next_value = values[-1]
            while not values.count(values[0]) == len(values):
                values = predict_next(values)
                next_value += values[-1]
            total_next_value += next_value
    return total_next_value


def part_2(file_path: str) -> int:
    """

    :param file_path: File path of input data
    :return:
    """
    with open(file_path, "r") as f:
        start_values_lines = []
        for line in f:
            values = [int(val) for val in line.strip("\n").split(" ")]
            start_values = [values[0]]
            while not values.count(values[0]) == len(values):
                values = predict_next(values)
                start_values.append(values[0])
            start_values_lines.append(start_values)

    total_value = 0
    for start_values in start_values_lines:
        start_value = 0
        for value in start_values[::-1]:
            start_value = value - start_value
        total_value += start_value
    return total_value


def predict_next(values: List[int]) -> List[int]:
    diffs = []
    for x in range(len(values) - 1):
        diff = -1 * (values[x] - values[x + 1])
        diffs.append(diff)
    return diffs


def main():
    # Test input
    test_file_path = get_input_path("9.txt", test=True)

    # Real input
    file_path = get_input_path("9.txt")

    # Part 1
    test_first_answer = part_1(test_file_path)
    assert test_first_answer == 114
    first_answer = part_1(file_path)
    assert first_answer == 1953784198

    # Part 2
    test_second_answer = part_2(test_file_path)
    assert test_second_answer == 2
    second_answer = part_2(file_path)
    assert second_answer == 957


if __name__ == "__main__":
    main()
