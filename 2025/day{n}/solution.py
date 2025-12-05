from pathlib import Path


def reader(lines: list[str]):
    return [line.strip() for line in lines]


def part1(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())


def part2(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())


if __name__ == "__main__":
    print("Test Case")
    input_file = Path(__file__).parent / "input.test.txt"
    part1(input_file)
    # part2(input_file)

    print("\n\nResult")
    input_file = Path(__file__).parent / "input.txt"
    part1(input_file)
    # part2(input_file)
