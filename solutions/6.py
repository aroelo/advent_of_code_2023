# https://adventofcode.com/2023/day/6

def part_1(races) -> int:
    """

    :param races:
    :return: Total number of points
    """
    ways_to_win = 1
    for race in races:
        ways_to_win_race = 0
        time, distance = race
        for ms in range(time):
            max_distance = ms * (time - ms)
            if max_distance > distance:
                ways_to_win_race += 1
        ways_to_win *= ways_to_win_race
    return ways_to_win


def part_2(race) -> int:
    """

    :param race:
    :return:
    """
    ways_to_win = 0
    time, distance = race
    for ms in range(time):
        max_distance = ms * (time - ms)
        if max_distance > distance:
            ways_to_win += 1
    return ways_to_win


def main():
    # Test input
    test_first_races = [(7, 9), (15, 40), (30, 200)]
    test_first_answer = part_1(test_first_races)
    assert test_first_answer == 288

    test_second_race = (71530, 940200)
    test_second_answer = part_2(test_second_race)
    assert test_second_answer == 71503

    # Real input
    first_races = [(49, 263), (97, 1532), (94, 1378), (94, 1851)]
    first_answer = part_1(first_races)
    assert first_answer == 4403592

    second_race = (49979494, 263153213781851)
    second_answer = part_2(second_race)
    assert second_answer == 38017587


if __name__ == "__main__":
    main()
