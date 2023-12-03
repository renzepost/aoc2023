import math
from collections import defaultdict

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def get_max_per_game(lines):
    data = {}
    for line in lines:
        record = line.split(":")
        game = int(record[0].split(" ")[1])
        sets = record[1].split(";")
        counts_per_game = defaultdict(list)
        for st in sets:
            counts = [
                (cube.split(" ")[1], int(cube.split(" ")[0]))
                for cube in [s.strip() for s in st.split(",")]
            ]
            for k, v in counts:
                counts_per_game[k].append(v)
        data[game] = {cube: max(counts) for cube, counts in counts_per_game.items()}

    return data


def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    data = get_max_per_game(lines)
    exceeding_max = {
        game: any([v["red"] > MAX_RED, v["green"] > MAX_GREEN, v["blue"] > MAX_BLUE])
        for game, v in data.items()
    }

    # Answer part 1
    print(sum([game for game, exceeds_max in exceeding_max.items() if not exceeds_max]))

    # Answer part 2
    print(sum([math.prod([v["red"], v["green"], v["blue"]]) for v in data.values()]))


if __name__ == "__main__":
    main()
