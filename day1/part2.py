def main():
    spelled_out_numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    with open("input.txt", "r") as file:
        lines = file.readlines()

    result = []

    for line in lines:
        digits = []
        for i in range(len(line)):
            if line[i] in numbers:
                digits.append(line[i])
            else:
                for k, v in spelled_out_numbers.items():
                    if line[i : i + len(k)] == k:
                        digits.append(v)
        result.append(int(f"{digits[0]}{digits[-1]}"))

    print(sum(result))


if __name__ == "__main__":
    main()
