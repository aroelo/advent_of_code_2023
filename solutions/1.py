# https://adventofcode.com/2023/day/1
from utils.utils import get_input_path


def find_calibration_value(file_path: str) -> int:
    """

    :param file_path: File path of input data
    :return: The number of times the depth increased
    """
    calibration_sum = 0
    with open(file_path, "r") as f:
        for line in f:
            numbers = []
            for char in line:
                if char.isdigit():
                    numbers += char
            calibration_sum += int(numbers[0] + numbers[-1])
    return calibration_sum


def find_calibration_value_letters(file_path: str) -> int:
    """

    :param file_path: File path of input data
    :return:
    """
    calibration_sum = 0
    with open(file_path, "r") as f:
        for line in f:
            numbers_left = {
                "one": -1,
                "two": -1,
                "three": -1,
                "four": -1,
                "five": -1,
                "six": -1,
                "seven": -1,
                "eight": -1,
                "nine": -1,
                "1": -1,
                "2": -1,
                "3": -1,
                "4": -1,
                "5": -1,
                "6": -1,
                "7": -1,
                "8": -1,
                "9": -1,
            }
            numbers_right = {
                "one": -1,
                "two": -1,
                "three": -1,
                "four": -1,
                "five": -1,
                "six": -1,
                "seven": -1,
                "eight": -1,
                "nine": -1,
                "1": -1,
                "2": -1,
                "3": -1,
                "4": -1,
                "5": -1,
                "6": -1,
                "7": -1,
                "8": -1,
                "9": -1,
            }
            for number in numbers_left.keys():
                # Find and set index
                numbers_left[number] = line.find(number)
                numbers_right[number] = line.rfind(number)

            # Sort numbers by index
            numbers_left = {key: val for key, val in numbers_left.items() if val != -1}
            numbers_right = {
                key: val for key, val in numbers_right.items() if val != -1
            }

            sorted_numbers_left = sorted(numbers_left.items(), key=lambda item: item[1])
            sorted_numbers_right = sorted(
                numbers_right.items(), key=lambda item: item[1]
            )

            calibration_sum += int(
                map_word_to_digit(sorted_numbers_left[0][0])
                + map_word_to_digit(sorted_numbers_right[-1][0])
            )
            print(calibration_sum)
    return calibration_sum


def map_word_to_digit(word: str) -> str:
    """

    :param word:
    :return:
    """
    return {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }[word]


def main():
    # Test input
    test_file_path = get_input_path("1.txt", test=True)
    test_first_answer = find_calibration_value(test_file_path)
    assert test_first_answer == 142

    test_file_path = get_input_path("1b.txt", test=True)
    test_second_answer = find_calibration_value_letters(test_file_path)
    assert test_second_answer == 281

    # # Real input
    file_path = get_input_path("1.txt")

    first_answer = find_calibration_value(file_path)
    assert first_answer == 54634
    second_answer = find_calibration_value_letters(file_path)
    assert second_answer == 53855


if __name__ == "__main__":
    main()
