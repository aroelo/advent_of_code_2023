# https://adventofcode.com/2023/day/7
from utils.utils import get_input_path


def part_1(file_path: str) -> int:
    """

    :param file_path: File path of input data
    :return: Total number of points
    """
    # ranking of hands, 5: 7, 4: 6, fullhouse: 5, 3: 4, 2x2: 3, 2: 1, 1: 0
    strength_map = {5: 7, 4: 6, "fh": 5, 3: 4, "2x2": 3, 2: 2, 1: 1}
    hands_map = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    bids_map = {}
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip("\n")
            hand, bid = line.split(" ")

            hand_count = {i: list(hand).count(i) for i in list(hand)}
            hand_count_sorted = sorted(list(hand_count.values()), reverse=True)
            strength = strength_map[hand_count_sorted[0]]

            # might be fh or 2x2
            strength = 5 if strength == 4 and hand_count_sorted[1] == 2 else strength
            strength = 3 if strength == 2 and hand_count_sorted[1] == 2 else strength

            hands_map[strength].append(hand)
            bids_map[hand] = bid

    cards_str = "AKQJT98765432"
    cards = {c: i for i, c in enumerate(cards_str)}
    total_winnings = 0
    rank = 1
    for hands in hands_map.values():
        if not hands:
            continue
        if len(hands) == 1:
            total_winnings += rank * int(bids_map[hands[0]])
            rank += 1
        else:
            hands = sorted(
                hands,
                key=lambda word: [cards.get(c, ord(c)) for c in word],
                reverse=True,
            )
            for hand in hands:
                total_winnings += rank * int(bids_map[hand])
                rank += 1

    return total_winnings


def part_2(file_path: str) -> int:
    """

    :param file_path: File path of input data
    :return:
    """
    # ranking of hands, 5: 7, 4: 6, fullhouse: 5, 3: 4, 2x2: 3, 2: 1, 1: 0
    strength_map = {5: 7, 4: 6, "fh": 5, 3: 4, "2x2": 3, 2: 2, 1: 1}
    hands_map = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    bids_map = {}
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip("\n")
            hand, bid = line.split(" ")

            hand_count = {i: list(hand).count(i) for i in list(hand)}
            hand_count_sorted = dict(
                sorted(hand_count.items(), key=lambda item: item[1], reverse=True)
            )
            jokers = hand_count.get("J", 0)
            if jokers == 5:
                strength = 7
            elif jokers:
                for card, counted in hand_count_sorted.items():
                    if card == "J":
                        continue
                    strength = strength_map[counted + jokers]
                    break

                # might be fh or 2x2
                strength = (
                    5
                    if strength == 4 and list(hand_count_sorted.values())[1] == 2
                    else strength
                )
            else:
                strength = strength_map[list(hand_count_sorted.values())[0]]

                # might be fh or 2x2
                strength = (
                    5
                    if strength == 4 and list(hand_count_sorted.values())[1] == 2
                    else strength
                )
                strength = (
                    3
                    if strength == 2 and list(hand_count_sorted.values())[1] == 2
                    else strength
                )

            hands_map[strength].append(hand)
            bids_map[hand] = bid

    cards_str = "AKQT98765432J"
    cards = {c: i for i, c in enumerate(cards_str)}
    total_winnings = 0
    rank = 1
    for hands in hands_map.values():
        if not hands:
            continue
        if len(hands) == 1:
            total_winnings += rank * int(bids_map[hands[0]])
            rank += 1
        else:
            hands = sorted(
                hands,
                key=lambda word: [cards.get(c, ord(c)) for c in word],
                reverse=True,
            )
            for hand in hands:
                total_winnings += rank * int(bids_map[hand])
                rank += 1

    return total_winnings


def main():
    """
    extra test cases
    JJJJJ 123
    J7777 740
    7777J 100
    JJJ55 123
    J5522 123
    J5512 123
    J552J 123
    2345J 123
    """
    # Test input
    test_file_path = get_input_path("7.txt", test=True)

    test_first_answer = part_1(test_file_path)
    assert test_first_answer == 6440
    test_second_answer = part_2(test_file_path)
    assert test_second_answer == 5905

    # Real input
    file_path = get_input_path("7.txt")

    first_answer = part_1(file_path)
    assert first_answer == 251287184
    second_answer = part_2(file_path)
    assert second_answer == 250757288


if __name__ == "__main__":
    main()
