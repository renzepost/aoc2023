import math
from dataclasses import dataclass


@dataclass
class Number:
    value: int
    adjacent_parts: bool
    adjacent_gear: tuple[int]


def main():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    numbers = []
    y = 0
    for line in lines:
        x = 0
        while x < len(line):
            char = line[x]
            if char.isdigit():
                value = [char]
                try:
                    i = 0
                    while line[x + i + 1].isdigit():
                        value.append(line[x + i + 1])
                        i += 1
                except IndexError:
                    pass
                finally:
                    adjacent_parts = False
                    adjacent_gear = (-1, -1)
                    if x > 0:
                        if lines[y][x - 1] != "." and not lines[y][x - 1].isdigit():
                            adjacent_parts = True
                            if lines[y][x - 1] == "*":
                                adjacent_gear = (y, x - 1)
                    if x + i + 1 < len(line) - 1:
                        if (
                            lines[y][x + i + 1] != "."
                            and not lines[y][x + i + 1].isdigit()
                        ):
                            adjacent_parts = True
                            if lines[y][x + i + 1] == "*":
                                adjacent_gear = (y, x + i + 1)
                    for j in range(x - 1, x + i + 2):
                        if j < 0 or j >= len(line):
                            continue

                        if y > 0:
                            if lines[y - 1][j] != "." and not lines[y - 1][j].isdigit():
                                adjacent_parts = True
                                if lines[y - 1][j] == "*":
                                    adjacent_gear = (y - 1, j)
                        if y < len(lines) - 1:
                            if lines[y + 1][j] != "." and not lines[y + 1][j].isdigit():
                                adjacent_parts = True
                                if lines[y + 1][j] == "*":
                                    adjacent_gear = (y + 1, j)
                    numbers.append(
                        Number(int("".join(value)), adjacent_parts, adjacent_gear)
                    )
                    x += i
            x += 1
        y += 1

    # Answer part 1
    print(sum([number.value for number in numbers if number.adjacent_parts]))

    gears_dict = {}
    for num in numbers:
        if num.adjacent_gear == (-1, -1):
            continue
        gear = num.adjacent_gear
        if gear not in gears_dict:
            gears_dict[gear] = []
        gears_dict[gear].append(num.value)

    ratios = {
        gear: math.prod(numbers)
        for gear, numbers in gears_dict.items()
        if len(numbers) > 1
    }
    # Answer part 2
    print(sum([r for r in ratios.values()]))


if __name__ == "__main__":
    main()
