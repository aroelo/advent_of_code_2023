# https://adventofcode.com/2023/day/4
from utils.utils import get_input_path


def part_1(file_path: str) -> int:
    """

    :param file_path: File path of input data
    :return: Total number of points
    """
    total_points = 0
    with open(file_path, "r") as f:
        for line in f:
            winning, mine = line.strip("\n").split(":")[1].split("|")
            winning = set(winning.split(" "))
            mine = set(mine.split(" "))
            winning.remove(""), mine.remove("")
            overlap = winning & mine
            if overlap:
                points = 2 ** (len(overlap) - 1)
                total_points += points
    return total_points


def part_2(file_path: str) -> int:
    """

    :param file_path: File path of input data
    :return: Total number of scratch cards
    """
    cards = []
    with open(file_path, "r") as f:
        for line in f:
            winning, mine = line.strip("\n").split(":")[1].split("|")
            winning = set(winning.split(" "))
            mine = set(mine.split(" "))
            winning.remove("")
            mine.remove("")
            overlap = winning & mine
            cards.append([1, len(overlap)])

    all_cards = cards
    total_cards = 0
    for idx, (copies, points) in enumerate(cards):
        total_cards += copies
        for card in all_cards[idx + 1 : idx + points + 1]:
            card[0] += copies
    return total_cards


def main():
    # Test input
    test_file_path = get_input_path("4.txt", test=True)

    test_first_answer = part_1(test_file_path)
    assert test_first_answer == 13
    test_second_answer = part_2(test_file_path)
    assert test_second_answer == 30

    # Real input
    file_path = get_input_path("4.txt")

    first_answer = part_1(file_path)
    assert first_answer == 24175
    second_answer = part_2(file_path)
    assert second_answer == 18846301


if __name__ == "__main__":
    main()
