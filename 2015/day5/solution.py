from collections import Counter
from itertools import product
from pathlib import Path
from string import ascii_lowercase


def reader(lines: list[str]):
    return [line.strip() for line in lines]


def is_nice(line: str) -> bool:
    wc = Counter(line)

    for bad in ["ab", "cd", "pq", "xy"]:
        if bad in line:
            return False

    if sum(v for k, v in wc.items() if k in "aeiou") < 3:
        return False

    for a, b in zip(line, line[1:]):
        if a == b:
            return True

    return False


def part1(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())
        result = 0
        for line in data:
            result += is_nice(line)
        print(result)


def is_nice_v2(line: str) -> bool:
    possible = False
    possible_pairs = list("".join(i) for i in product(ascii_lowercase, ascii_lowercase))

    for pairs in possible_pairs:
        if line.count(pairs) >= 2:
            possible = True

    if not possible:
        return False

    for a, _, c in zip(line, line[1:], line[2:]):
        if a == c:
            return True

    return False


def part2(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())
        result = 0
        for line in data:
            result += is_nice_v2(line)
        print(result)


if __name__ == "__main__":
    print("Test Case")
    input_file = Path(__file__).parent / "input.test.txt"
    part1(input_file)
    part2(input_file)

    print("\n\nResult")
    input_file = Path(__file__).parent / "input.txt"
    part1(input_file)
    part2(input_file)
