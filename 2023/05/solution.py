## advent of code 2023
## https://adventofcode.com/2023
## day 05

from dataclasses import dataclass


@dataclass
class Mapping:
    dest_range: range
    src_range: range
    src_dest_delta: int


@dataclass
class Map:
    name: str
    mappings: [Mapping]

    def map_src_to_dest(self, src: int) -> int:
        for m in self.mappings:
            if src in m.src_range:
                return src + m.src_dest_delta

        # TODO deal with out of range srces?
        return src


@dataclass
class Almanac:
    seeds: [int]
    seed_ranges: [range]
    maps: dict[str, Map]

    def __getitem__(self, key):
        return self.maps[key]


def parse_input(lines):
    seeds = [int(s) for s in lines[0].split()[1:]]
    seed_ranges = [
        range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)
    ]

    maps = dict()

    mp = None
    almanac = Almanac(seeds, seed_ranges, dict())

    for line in lines[1:]:
        if not line:
            continue

        if not line[0].isdigit():
            if mp is not None:
                almanac.maps[mp.name] = mp

            mp = Map(line.split()[0], [])
            continue

        (dest, src, delta) = [int(n) for n in line.split()]

        mp.mappings.append(
            Mapping(range(dest, dest + delta), range(src, src + delta), dest - src)
        )

    almanac.maps[mp.name] = mp
    return almanac


def part1(almanac):
    lowest_location = None

    for seed in almanac.seeds:
        soil = almanac["seed-to-soil"].map_src_to_dest(seed)
        fertilizer = almanac["soil-to-fertilizer"].map_src_to_dest(soil)
        water = almanac["fertilizer-to-water"].map_src_to_dest(fertilizer)
        light = almanac["water-to-light"].map_src_to_dest(water)
        temperature = almanac["light-to-temperature"].map_src_to_dest(light)
        humidity = almanac["temperature-to-humidity"].map_src_to_dest(temperature)
        location = almanac["humidity-to-location"].map_src_to_dest(humidity)

        if lowest_location is None or location < lowest_location:
            lowest_location = location

    return lowest_location


def part2(almanac):
    lowest_location = None

    # num_seeds = sum(r.stop - r.start for r in almanac.seed_ranges)
    # print(f"part2: num_seeds={num_seeds}")

    # heat-death-of-universe algorithm (will require about 2 billion iterations :o)
    # for seed_range in almanac.seed_ranges:
    #     for seed in seed_range:
    #         soil = almanac["seed-to-soil"].map_src_to_dest(seed)
    #         fertilizer = almanac["soil-to-fertilizer"].map_src_to_dest(soil)
    #         water = almanac["fertilizer-to-water"].map_src_to_dest(fertilizer)
    #         light = almanac["water-to-light"].map_src_to_dest(water)
    #         temperature = almanac["light-to-temperature"].map_src_to_dest(light)
    #         humidity = almanac["temperature-to-humidity"].map_src_to_dest(temperature)
    #         location = almanac["humidity-to-location"].map_src_to_dest(humidity)

    #         if lowest_location is None or location < lowest_location:
    #             lowest_location = location

    return lowest_location
