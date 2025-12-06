from pathlib import Path


def reader(lines: list[str]):
    return [line.strip() for line in lines]


def part1(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())
        for line in data:
            x, y = 0, 0
            seen = set({(0, 0)})
            for d in line:
                match d:
                    case "^":
                        y += 1
                    case ">":
                        x += 1
                    case "<":
                        x -= 1
                    case "v":
                        y -= 1
                    case v:
                        raise ValueError(f"Unknown value {v}")
                seen.add((x, y))
            print(len(seen))


def part2(input_file):
    class Robot:
        def __init__(self):
            self.x = 0
            self.y = 0

        def up(self):
            self.y += 1

        def down(self):
            self.y -= 1

        def left(self):
            self.x -= 1

        def right(self):
            self.x += 1

        def location(self):
            return self.x, self.y

    with open(input_file, "r") as f:
        data = reader(f.readlines())
        for line in data:
            robot1 = Robot()
            robot2 = Robot()
            seen = set({(0, 0)})
            for i, d in enumerate(line):
                robot = robot1 if i % 2 else robot2
                match d:
                    case "^":
                        robot.up()
                    case ">":
                        robot.right()
                    case "<":
                        robot.left()
                    case "v":
                        robot.down()
                    case v:
                        raise ValueError(f"Unknown value {v}")
                seen.add(robot.location())
            print(len(seen))


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
