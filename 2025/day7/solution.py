from functools import cache
from pathlib import Path


def reader(lines: list[str]):
    return [list(line.strip().replace("S", "|")) for line in lines]


def part1(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())
        m = len(data)
        n = len(data[0])

        splitted = 0

        for t in range(1, m):
            for i in range(n):
                match data[t][i]:
                    case ".":
                        if data[t - 1][i] == "|":
                            data[t][i] = "|"
                            continue
                        if data[t - 1][i] == "^":
                            continue
                        continue
                    case "^":
                        if data[t - 1][i] != "|":
                            continue
                        splitted += 1
                        l, r = i - 1, i + 1
                        if l >= 0:
                            data[t][l] = "|"
                        if r < n:
                            data[t][r] = "|"
                        continue
                    case "|":
                        continue
                    case x:
                        raise ValueError(f"Unknown symbol {x}")
        print(splitted)


def part2(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())
        m = len(data)
        n = len(data[0])

    @cache
    def get_time_lines(i, t):
        if t == m:
            return 1
        match data[t][i]:
            case ".":
                return get_time_lines(i, t + 1)
            case "^":
                l, r = i - 1, i + 1
                result = 0
                if l >= 0:
                    result += get_time_lines(l, t + 1)
                if r < n:
                    result += get_time_lines(r, t + 1)
            case x:
                raise ValueError(x)
        return result

    print(get_time_lines(data[0].index("|"), 1))


if __name__ == "__main__":
    print("Test Case")
    input_file = Path(__file__).parent / "input.test.txt"
    part1(input_file)
    part2(input_file)

    print("\n\nResult")
    input_file = Path(__file__).parent / "input.txt"
    part1(input_file)
    part2(input_file)
