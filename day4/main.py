def get_value(winning: set[int]) -> int:
    if len(winning) <= 1:
        return len(winning)
    else:
        return 2 ** len(list(winning)[1:])


def get_total_scratchcards(data: dict[int, tuple[set[int], set[int]]]) -> int:
    cards = {card: 1 for card in data.keys()}
    for card, numbers in data.items():
        winnings = len(numbers[0].intersection(numbers[1]))
        for i in range(card + 1, card + 1 + winnings):
            cards[i] += cards[card]

    return sum([counts for counts in cards.values()])


def main():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    data = {}
    for e, line in enumerate(lines):
        numbers = [l.strip() for l in line.split(":")[1].split("|")]
        winning = set(int(num) for num in numbers[0].split())
        have = set(int(num) for num in numbers[1].split())
        data[e] = (winning, have)

    total_winning = [winning.intersection(have) for winning, have in data.values()]
    # Answer part 1
    print(sum([get_value(winning) for winning in total_winning]))

    # Answer part 2
    print(get_total_scratchcards(data))


if __name__ == "__main__":
    main()
