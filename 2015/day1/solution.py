from pathlib import Path


def reader(lines: list[str]):
    return [line.strip() for line in lines]


def part1(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())
        for line in data:
            result = line.count("(") - line.count(")")
            print(result)


def part2(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())

        for line in data:
            v = 0
            for i, c in enumerate(line, 1):
                match c:
                    case ")":
                        v -= 1
                    case "(":
                        v += 1
                if v == -1:
                    print(i)
                    break



if __name__ == "__main__":
    print("Test Case")
    input_file = Path(__file__).parent / "input.test.txt"
    part1(input_file)
    print()
    part2(input_file)

    print("\n\nResult")
    input_file = Path(__file__).parent / "input.txt"
    part1(input_file)
    print()
    part2(input_file)
