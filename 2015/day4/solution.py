from pathlib import Path
import hashlib


def reader(lines: list[str]):
    return [line.strip() for line in lines]


def part1(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())

        for line in data:
            value = 0
            while True:
                key = line + str(value)
                result = hashlib.md5(key.encode()).hexdigest()
                if result[:5] == "00000":
                    print(value)
                    break
                value += 1


def part2(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())

        for line in data:
            value = 0
            while True:
                key = line + str(value)
                result = hashlib.md5(key.encode()).hexdigest()
                if result[:6] == "000000":
                    print(value)
                    break
                value += 1


if __name__ == "__main__":
    print("Test Case")
    input_file = Path(__file__).parent / "input.test.txt"
    part1(input_file)
    part2(input_file)

    print("\n\nResult")
    input_file = Path(__file__).parent / "input.txt"
    part1(input_file)
    part2(input_file)
