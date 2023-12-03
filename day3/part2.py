def get_number(pos, line):
    result = []
    while pos >= 0 and pos < len(line):
        if line[pos].isdigit():
            result.append(line[pos])

    return int("".join(result))


def main():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    gears = []
    y = 0
    for line in lines:
        x = 0
        while x < len(line):
            char = line[x]
            if char == "*":
                adj_numbers = []
                if x > 0:
                    if lines[y][x - 1].isdigit():
                        adj_numbers.append(get_number(lines[y][x - 1]))

                if x + i + 1 < len(line) - 1:
                    if lines[y][x + i + 1] != "." and not lines[y][x + i + 1].isdigit():
                        adjacent_parts = True
                for j in range(x - 1, x + i + 2):
                    if j < 0 or j >= len(line):
                        continue

                    if y > 0:
                        if lines[y - 1][j] != "." and not lines[y - 1][j].isdigit():
                            adjacent_parts = True
                    if y < len(lines) - 1:
                        if lines[y + 1][j] != "." and not lines[y + 1][j].isdigit():
                            adjacent_parts = True
                numbers.append(Number(int("".join(value)), adjacent_parts))
                x += i
            x += 1
        y += 1

    print(sum([number.value for number in numbers if number.adjacent_parts]))


if __name__ == "__main__":
    main()
