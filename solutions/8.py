# https://adventofcode.com/2023/day/8
from utils.utils import get_input_path


def part_1(file_path: str) -> int:
    """

    :param file_path: File path of input data
    :return:
    """
    path = None
    network = {}
    with open(file_path, "r") as f:
        for line in f:
            if not path:
                path = line.strip('\n')
                continue
            if line == '\n':
                continue
            nodes = line.strip('\n').split(' = ')
            node_key = nodes[0]
            node_left, node_right = nodes[1].strip('(').strip(')').split(', ')
            network[node_key] = (node_left, node_right)

    steps = 0
    node = 'AAA'
    while True:
        for move in path:
            steps += 1
            if move == 'L':
                node = network[node][0]
            if move == 'R':
                node = network[node][1]
            if node == 'ZZZ':
                return steps


def part_2(file_path: str) -> int:
    """

    :param file_path: File path of input data
    :return:
    """
    path = None
    network = {}
    with open(file_path, "r") as f:
        for line in f:
            if not path:
                path = line.strip('\n')
                continue
            if line == '\n':
                continue
            nodes = line.strip('\n').split(' = ')
            node_key = nodes[0]
            node_left, node_right = nodes[1].strip('(').strip(')').split(', ')
            network[node_key] = (node_left, node_right)

    steps = 0
    nodes = [node for node in list(network.keys()) if node.endswith('A')]
    while True:
        for move in path:
            if all(node.endswith('Z') for node in nodes):
                print(steps)
                return steps
            steps += 1
            new_nodes = []
            for node in nodes:
                if move == 'L':
                    node = network[node][0]
                if move == 'R':
                    node = network[node][1]
                new_nodes.append(node)
            if steps % 1000000 == 1:
                print(steps)
            nodes = new_nodes

def main():
    # Test input
    test_file_path = get_input_path("8.txt", test=True)

    # Real input
    file_path = get_input_path("8.txt")

    # Part 1
    test_first_answer = part_1(test_file_path)
    assert test_first_answer == 6
    first_answer = part_1(file_path)
    assert first_answer == 20221

    # Part 2
    test_file_path = get_input_path("8b.txt", test=True)
    test_second_answer = part_2(test_file_path)
    assert test_second_answer == 6
    # second_answer = part_2(file_path)
    # assert second_answer == 250757288


if __name__ == "__main__":
    main()
