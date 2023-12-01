import re


def to_digits(line: str) -> int:
    digits = re.findall(r"\d", line)
    return int(f"{digits[0]}{digits[-1]}")


def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    print(sum([to_digits(line) for line in lines]))


if __name__ == "__main__":
    main()
