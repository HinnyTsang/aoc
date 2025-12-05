from pathlib import Path


def merge_ranges(ranges):
    sranges = sorted(ranges)
    merged_ranges = sranges[:1]
    for l, r in sranges:
        if l <= merged_ranges[-1][1]:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], r)
        else:
            merged_ranges.append([l, r])
    return merged_ranges


def reader(lines: list[str]):
    lines = [line.strip() for line in lines]
    empty_line = lines.index("")
    ranges = [list(map(int, line.split("-"))) for line in lines[:empty_line]]
    ingradients = list(map(int, lines[empty_line + 1 :]))

    return merge_ranges(ranges), ingradients


def not_in_interval(intervals: list[list[int]], value: int):
    for l, r in intervals:
        if r < value:
            continue
        if l > value:
            continue
        if l <= value <= r:
            return True

    return False


def part1(input_file):
    with open(input_file, "r") as f:
        ranges, ingradients = reader(f.readlines())
        result = 0
        for value in ingradients:
            if not_in_interval(ranges, value):
                result += 1
        print(result)


def part2(input_file):
    with open(input_file, "r") as f:
        ranges, _ = reader(f.readlines())

        result = 0
        for l, r in ranges:
            result += r - l + 1
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
