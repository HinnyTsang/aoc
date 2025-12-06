from functools import reduce
import operator
from pathlib import Path


def reader(lines: list[str]):
    return [line.strip().split() for line in lines]


def part1(input_file):
    ops = {"+": operator.add, "*": operator.mul}
    with open(input_file, "r") as f:
        lines = reader(f.readlines())
        print(len(lines))
        result = 0
        for line in zip(*lines):
            op = ops[line[-1]]
            value = reduce(op, map(int, line[:-1]))
            result += value
        print(result)


def reader_v2(lines: list[str]):
    collector = []
    for line in zip(*lines):
        if line[-1] != " ":
            collector.append(list(line))
        else:
            for i in range(4):
                collector[-1][i] += line[i]
    return collector


def decode_values(line: list[str]) -> list[int]:
    cols = ["".join(item).strip() for item in zip(*line)]
    cols = [int(c) for c in cols if c]
    return cols


def part2(input_file):
    ops = {"+": operator.add, "*": operator.mul}
    with open(input_file, "r") as f:
        lines = reader_v2(f.readlines())
        result = 0
        for line in lines:
            op = ops[line[-1][0]]
            result += reduce(op, decode_values(line[:-1]))
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
