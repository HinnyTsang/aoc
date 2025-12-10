from pathlib import Path


def parsed(line: str):
    items = line.split(" ")
    goal, joltage = items[0][1:-1], list(map(int, items[-1][1:-1].split(",")))
    steps = [list(map(int, item[1:-1].split(","))) for item in items[1:-1]]
    return goal, steps, joltage


def reader(lines: list[str]):
    lines = [line.strip() for line in lines]
    return [parsed(line) for line in lines]


def solve1(goal: str, steps: list[list[int]], joltage: list[int]) -> int:
    def apply_bitmask(n: int, bitmask: int, steps: list[list[int]]):
        i = 0
        test = [0] * n
        while 1 << i <= bitmask:
            mask = 1 << i
            if bitmask & mask:
                for item in steps[i]:
                    test[item] += 1
            i += 1
        return "".join(["." if v % 2 == 0 else "#" for v in test])

    n = len(steps)
    bitmasks = list(range((1 << n)))
    min_steps = len(steps) + 1
    for bitmask in bitmasks:
        result = apply_bitmask(len(goal), bitmask, steps)
        if result == goal:
            min_steps = min(min_steps, bitmask.bit_count())
    return min_steps


def part1(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())
        min_press = 0
        for goal, steps, joltage in data:
            min_press += solve1(goal, steps, joltage)
        print(min_press)


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
