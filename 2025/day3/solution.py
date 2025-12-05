from pathlib import Path


def reader(lines: list[str]):
    return [line.strip() for line in lines]


def largest_joltage(x: str):
    fst = 0

    largest_joltage = 0

    for c in x:
        v = int(c)
        if fst != 0:
            largest_joltage = max(largest_joltage, fst * 10 + v)
        fst = max(fst, v)
    return largest_joltage


def largest_joltage_n_size(x: str, n=12):
    class Handler:
        def __init__(self, n: int):
            self.n = n
            self.elements = []

        def add(self, v):
            self.elements.append(v)
            if len(self.elements) > n:
                self.pop_least()

        def pop_least(self):
            for i in range(1, n + 1):
                if self.elements[i - 1] < self.elements[i]:
                    self.elements = self.elements[: i - 1] + self.elements[i:]
                    return
            self.elements.pop()

        def get_value(self):
            v = 0
            for i in self.elements:
                v = v * 10 + i
            return v

    handler = Handler(n)
    for c in x:
        handler.add(int(c))

    result = handler.get_value()
    return result


def part1(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())
        print(sum(largest_joltage(x) for x in data))


def part2(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())
        print(sum(largest_joltage_n_size(x, n=12) for x in data))


if __name__ == "__main__":
    print("Test Case")
    input_file = Path(__file__).parent / "input.test.txt"
    part1(input_file)
    part2(input_file)

    print("\n\nResult")
    input_file = Path(__file__).parent / "input.txt"
    part1(input_file)
    part2(input_file)
