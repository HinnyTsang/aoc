from pathlib import Path


def reader(lines: list[str]):
    return [line.strip() for line in lines]


def is_rubbable(i, j, data: list[str], max_surrounding_rolls: int):
    dis = [-1, -1, -1, 0, 0, 1, 1, 1]
    djs = [-1, 0, 1, -1, 1, -1, 0, 1]

    rolls = 0

    if data[i][j] != "@":
        return False

    for di, dj in zip(dis, djs):
        ni = i + di
        nj = j + dj

        if not 0 <= ni < len(data):
            continue
        if not 0 <= nj < len(data[0]):
            continue

        rolls += data[ni][nj] == "@"

    rubbable = rolls < max_surrounding_rolls

    return rubbable


def part1(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())
        n = len(data)
        m = len(data[0])
        result = 0

        for i in range(n):
            for j in range(m):
                result += is_rubbable(i, j, data, 4)

        print(result)


def is_rubbable_v2(i, j, data: list[list[str]], max_surrounding_rolls: int):
    dis = [-1, -1, -1, 0, 0, 1, 1, 1]
    djs = [-1, 0, 1, -1, 1, -1, 0, 1]

    rolls = 0

    if data[i][j] != "@":
        return False

    for di, dj in zip(dis, djs):
        ni = i + di
        nj = j + dj

        if not 0 <= ni < len(data):
            continue
        if not 0 <= nj < len(data[0]):
            continue

        rolls += data[ni][nj] == "@"

    rubbable = rolls < max_surrounding_rolls

    return rubbable


def part2(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())
        data = [list(i) for i in data]

        n = len(data)
        m = len(data[0])

        bfs = []

        for i in range(n):
            for j in range(m):
                if is_rubbable_v2(i, j, data, 4):
                    bfs.append((i, j))

        dis = [-1, -1, -1, 0, 0, 1, 1, 1]
        djs = [-1, 0, 1, -1, 1, -1, 0, 1]

        for i, j in bfs:
            data[i][j] = "x"

        while bfs:
            nfs = set()
            for i, j in bfs:
                for di, dj in zip(dis, djs):
                    ni = i + di
                    nj = j + dj
                    if not 0 <= ni < len(data):
                        continue
                    if not 0 <= nj < len(data[0]):
                        continue
                    if data[ni][nj] != "@":
                        continue
                    if is_rubbable_v2(ni, nj, data, 4):
                        nfs.add((ni, nj))
            bfs = nfs
            for i, j in bfs:
                data[i][j] = "x"

        result = [line.count("x") for line in data]

        print(sum(result))


if __name__ == "__main__":
    print("Test Case")
    input_file = Path(__file__).parent / "input.test.txt"
    part1(input_file)
    part2(input_file)

    print("\n\nResult")
    input_file = Path(__file__).parent / "input.txt"
    part1(input_file)
    part2(input_file)
