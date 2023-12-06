# https://adventofcode.com/2023/day/5
from utils.utils import get_input_path


class Mapping:
    def __init__(self):
        self.seed_to_soil = {}
        self.soil_to_fertilizer = {}
        self.fertilizer_to_water = {}
        self.water_to_light = {}
        self.light_to_temperature = {}
        self.temperature_to_humidity = {}
        self.humidity_to_location = {}


class Seed:
    def __init__(self, id, mapping, used_mapping=None):
        self.id = id
        self.mapping = mapping
        self.used_mapping = used_mapping

    def map_source_target(self, source, the_map):
        target = source
        for k, v in the_map.items():
            if source == k or (source > k and source < k + v[1]):
                target = source + (v[0] - k)
        return target

    @property
    def soil(self):
        return self.map_source_target(self.id, self.mapping.seed_to_soil)

    @property
    def fertilizer(self):
        return self.map_source_target(self.soil, self.mapping.soil_to_fertilizer)

    @property
    def water(self):
        return self.map_source_target(self.fertilizer, self.mapping.fertilizer_to_water)

    @property
    def light(self):
        return self.map_source_target(self.water, self.mapping.water_to_light)

    @property
    def temperature(self):
        return self.map_source_target(self.light, self.mapping.light_to_temperature)

    @property
    def humidity(self):
        return self.map_source_target(
            self.temperature, self.mapping.temperature_to_humidity
        )

    @property
    def location(self):
        return self.map_source_target(self.humidity, self.mapping.humidity_to_location)


def create_seeds_and_mapping(file_path: str):
    seeds = []
    mapping = Mapping()
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip("\n")
            if line == "":
                continue
            if line.startswith("seeds:"):
                seeds += [int(seed) for seed in line.strip("seeds: ").split(" ")]
            elif line == "seed-to-soil map:":
                the_map = mapping.seed_to_soil
            elif line == "soil-to-fertilizer map:":
                the_map = mapping.soil_to_fertilizer
            elif line == "fertilizer-to-water map:":
                the_map = mapping.fertilizer_to_water
            elif line == "water-to-light map:":
                the_map = mapping.water_to_light
            elif line == "light-to-temperature map:":
                the_map = mapping.light_to_temperature
            elif line == "temperature-to-humidity map:":
                the_map = mapping.temperature_to_humidity
            elif line == "humidity-to-location map:":
                the_map = mapping.humidity_to_location
            else:
                target, source, rnge = line.split(" ")
                the_map[int(source)] = (int(target), int(rnge))
    return seeds, mapping


def part_1(file_path: str) -> int:
    """

    :param file_path: File path of input data
    :return: Total number of points
    """
    seeds, mapping = create_seeds_and_mapping(file_path)

    location = None
    for seed_nr in seeds:
        seed = Seed(seed_nr, mapping)
        if not location or location > seed.location:
            location = seed.location
    return location


def part_2(file_path: str) -> int:
    """

    :param file_path: File path of input data
    :return:
    """
    seeds, mapping = create_seeds_and_mapping(file_path)

    location = None
    seed_start = None
    for idx, nr in enumerate(seeds):
        print(idx)
        if idx % 2:
            seed_range = nr
            for x in range(seed_range):
                seed = Seed(seed_start + x, mapping)
                if not location or location > seed.location:
                    location = seed.location
        else:
            seed_start = nr
    return location


def main():
    # Test input
    test_file_path = get_input_path("5.txt", test=True)

    test_first_answer = part_1(test_file_path)
    assert test_first_answer == 35
    test_second_answer = part_2(test_file_path)
    assert test_second_answer == 46

    # Real input
    file_path = get_input_path("5.txt")

    first_answer = part_1(file_path)
    assert first_answer == 227653707
    second_answer = part_2(file_path)
    # I forgot
    assert second_answer == 0


if __name__ == "__main__":
    main()
