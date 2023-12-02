# https://adventofcode.com/2023/day/2
from utils.utils import get_input_path
from typing import List, Dict


def find_valid_games(file_path: str, bag_content: Dict) -> int:
    """
    Find the sum of ids for valid games based on the records and given bag content
    :param file_path: File path of input data
    :param bag_content: Known bag content of red, green and blue cubes
    :return: Sum of ids of valid games
    """
    valid_games = 0
    game_id = 0

    with open(file_path, "r") as f:
        for line in f:
            game_id += 1
            records = line.strip('\n').split(':')[1].split(';')
            if not is_game_valid(records, bag_content):
                continue
            valid_games += game_id
    return valid_games


def find_fewest_cubes(file_path: str) -> int:
    """ Find the minimal number of cubes that should be in each bag per colour and multiply with each other.
    Return the total sum of multiplied values

    :param file_path: File path of input data
    :return: Sum of power of sets
    """
    sum_of_power = 0
    with open(file_path, "r") as f:
        for line in f:
            min_bag_content = {'red': 0, 'blue': 0, 'green': 0}
            records = line.strip('\n').split(':')[1].split(';')
            for record in records:
                number_colours = record.split(',')
                for number_colour in number_colours:
                    _, number, colour = number_colour.split(' ')
                    if int(number) > min_bag_content[colour]:
                        min_bag_content[colour] = int(number)
            powered_cubes = min_bag_content['red'] * min_bag_content['blue'] * min_bag_content['green']
            sum_of_power += powered_cubes
    return sum_of_power


def is_game_valid(records: List[str], bag_content: Dict) -> bool:
    """ Determine if the game is valid based on the bag content and return True or False

    :param records: List of recorded games
    :param bag_content: Bag content of red, green and blue cubes
    :return: Whether game is valid
    """
    for record in records:
        number_colours = record.split(',')
        for number_colour in number_colours:
            _, number, colour = number_colour.split(' ')
            if int(number) > bag_content[colour]:
                return False
    return True


def main():
    bag_content = {'red': 12, 'green': 13, 'blue': 14}

    # Test input
    test_file_path = get_input_path("2.txt", test=True)

    test_first_answer = find_valid_games(test_file_path, bag_content)
    assert test_first_answer == 8
    test_second_answer = find_fewest_cubes(test_file_path)
    assert test_second_answer == 2286

    # Real input
    file_path = get_input_path("2.txt")

    first_answer = find_valid_games(file_path, bag_content)
    assert first_answer == 2101
    second_answer = find_fewest_cubes(file_path)
    assert second_answer == 58269


if __name__ == "__main__":
    main()
