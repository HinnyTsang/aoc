from pathlib import Path


def is_invalid_v2(v):
    """
    Brute force solution
    """
    s = str(v)
    l = len(s)
    if l == 1:
        return False
    if len(set(s)) == 1:
        return True

    for f in range(2, l // 2 + 1):
        """
        l = 4, f = 2 [:2], [2:]
        l = 5, f = 2, 3
        l = 6, f = 2, 3
            [:l // f] [l // f:],
            [0:l // f], [l // f:2 * l // f], [2 * l //f:-]
        l = 7, f = 2, 3
        l = 8, f = 2, 3, 4
        """
        if l % f != 0:
            continue

        splits = {s[i : i + l // f] for i in range(0, l, l // f)}
        if len(splits) == 1:
            return True

    return False


def is_invalid_v1(v):
    s = str(v)
    l = len(s)
    if len(s) % 2:
        return False

    return s[: l // 2] == s[l // 2 :]


def sum_invalid_id(first, last, *, validator):
    result = 0
    for v in range(int(first), int(last) + 1):
        if validator(v):
            result += v
    return result


def part1(input_file):
    with open(input_file, "r") as f:
        data = ("".join(line.strip() for line in f.readlines())).split(",")
        ranges = [item.split("-") for item in data]
        result = sum(
            sum_invalid_id(r[0], r[1], validator=is_invalid_v1) for r in ranges
        )
        print(result)


def part2(input_file):
    with open(input_file, "r") as f:
        data = ("".join(line.strip() for line in f.readlines())).split(",")
        ranges = [item.split("-") for item in data]
        result = sum(
            sum_invalid_id(r[0], r[1], validator=is_invalid_v2) for r in ranges
        )
        print(result)


if __name__ == "__main__":
    print("Test Case")
    input_file = Path(__file__).parent / "input.test.txt"
    part1(input_file)
    part2(input_file)

    input_file = Path(__file__).parent / "input.txt"
    print("Result")
    part1(input_file)
    part2(input_file)
