## advent of code 2023
## https://adventofcode.com/2023
## day 05

from dataclasses import dataclass
import concurrent.futures


@dataclass
class Mapping:
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

        mp.mappings.append(Mapping(range(src, src + delta), dest - src))

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


def seed_to_location(almanac, seed) -> int:
    soil = almanac["seed-to-soil"].map_src_to_dest(seed)
    fertilizer = almanac["soil-to-fertilizer"].map_src_to_dest(soil)
    water = almanac["fertilizer-to-water"].map_src_to_dest(fertilizer)
    light = almanac["water-to-light"].map_src_to_dest(water)
    temperature = almanac["light-to-temperature"].map_src_to_dest(light)
    humidity = almanac["temperature-to-humidity"].map_src_to_dest(temperature)
    return almanac["humidity-to-location"].map_src_to_dest(humidity)


def part2(almanac):
    lowest_location = None
    num_iters = 0

    total_iters = sum(r.stop - r.start for r in almanac.seed_ranges)
    print(f"part2: total_iters={total_iters}")

    with concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor:
        for seed_range in almanac.seed_ranges:
            # heat-death-of-universe algorithm (will require about 2 billion iterations :o)
            # TODO actually use the executor
            for seed in seed_range:
                num_iters += 1
                if num_iters % 1_000_000 == 0:
                    print(
                        f"{num_iters // 1_000_000} million iterations done out of {total_iters / 1_000_000} million"
                    )

                location = seed_to_location(almanac, seed)

                if lowest_location is None or location < lowest_location:
                    print(f"new lowest location={location}")
                    lowest_location = location

    return lowest_location
