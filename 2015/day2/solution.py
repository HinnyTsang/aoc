from pathlib import Path


def reader(lines: list[str]):
    return [map(int, line.strip().split("x")) for line in lines]


def part1(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())
        result = 0
        for l, w, h in data:
            a = 2 * l * w
            b = 2 * w * h
            c = 2 * h * l
            sqft = a + b + c + min([a, b, c]) // 2
            result += sqft
        print(result)


def part2(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())
        result = 0
        for l, w, h in data:
            sqft = (l * w * h) + sum(sorted([l, w, h])[:2]) * 2
            result += sqft
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
